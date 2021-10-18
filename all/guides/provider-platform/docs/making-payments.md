SortOrder: 4
# Making Payments

## Introduction

To comply with payment processing requirements, a *Payment Plugin* must:
* accept [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) requests from Wix
* notify Wix about all changes to a *Transaction* state by calling [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event)

When processing card payments, Wix collects card details and sends them in a [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request within a `card` property of a `paymentMethodData` field. So the *Payment Plugin* must be compliant with [PCI DSS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard).

When a *Payment Plugin* receives a call to the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) endpoint, it must initiate a payment. Both cards and redirection-based payment methods can be supported.

This endpoint includes a `Digest` header used for [validation](https://dev.wix.com/api/rest/payment-provider/provider-platform/payment-plugins#payment-provider_provider-platform_payment-plugins_request-validation).

If the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) endpoint receives `wixTransactionId`, which has already been processed or is being processed, it must never initiate a new payment but respond with the latest payment state. If the state has not changed, send the previous response for  `wixTransactionId`.

Most fields in the request are optional and may be missing. Some fields can be configured as required. All required fields are described in the [Required Fields](https://dev.wix.com/api/rest/payment-provider/provider-platform/required-fields) section.

For each *Transaction* state, except for states that require *buyer* interaction, a *Payment Plugin* must call [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with `reasonCode` which can be used to determine that state, or without `reasonCode` which indicates success. When the buyer abandons a redirection-based payment, the plugin must send a failure event with a `3030` `reasonCode`, which means payment cancellation.

Depending on the flow, one or two events can be sent per `wixTransactionId` during the payment process. If a payment cannot be completed fast enough a first event sent should have `reasonCode` with a reason for the pending state. In any case when the payment comes to its final state an event should be fired with a `reasonCode` indicating a failure reason or without `reasonCode` to indicate success. The event should be sent even when a [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) response contains final payment state.

For each `wixTransactionId` a *Payment Plugin* can only send duplicate events or a final state event after an event designating a pending state. Do not send controversial events:
* Success events after failure events
* Failure events after success events
* Pending events after success or failure events

## Card payment examples

If a payment requires *3D Secure* verification, a *Payment Plugin* must respond with a redirection URL to a web page where a *buyer* can proceed with the payment. If a card does not have 3DS enabled, or the 3DS verification is not required, or the payment fails instantly, the *Payment Plugin* should respond with a final payment state.

The following *JWT* values are fake and used for example purposes. An `installments` field is applicable for card payments only.

Fields `errorCode` and `errorMessage` in the following examples are fake. *Payment Plugin* can send their own specific values for these fields.

Examples are applicable for both `live` and `sandbox` modes.

In the following example, Wix initiates a `$10 US` payment by sending a request:

```bash
curl -X POST https://psp.example.com/sale \
 -H 'Content-Type: application/json' \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "wixMerchantId": "333333-3333-3333-3333-333333333333",
  "wixTransactionId": "000000-0000-0000-0000-000000000000",
  "paymentMethod": "creditCard",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "order": {
    "id": "11111111-1111-1111-1111-111111111111",
    "description": {
      "totalAmount": 1000,
      "currency": "USD",
      "items": [
        {
          "id": "it_1",
          "name": "Digital camera",
          "quantity": 1,
          "price": 1000,
          "description": "Portable digital camera",
          "category": "physical"
        }
      ],
      "buyerInfo": {
        "buyerId": "ffc0a971-60cb-4c63-8016-39b1bce41e8d",
        "buyerLanguage": "en"
      }
    },
    "returnUrls": {
      "successUrl": "https://merchant.com/success",
      "errorUrl": "https://merchant.com/error",
      "cancelUrl": "https://merchant.com/cancel",
      "pendingUrl": "https://merchant.com/pending"
    }
  },
  "installments": 1,
  "mode": "live",
  "paymentMethodData": {
    "card": {
      "number": "4111111111111111",
      "year": 2030,
      "month": 12,
      "cvv": "777",
      "holderName": "John Smith"
    }
  }
}'
```

### Instant card payment approval

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment becomes approved with no additional verifications or *buyer* actions needed. The plugin responds with a `200` HTTP status code, and a *JSON object*:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665"
}
```

2. *Payment Plugin* then calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}'
```

3. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```

3. Transaction is successfully approved on Wix side.

### Instant card payment decline

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The card does not have enough money available to cover the payment. The plugin responds with a `200` HTTP status code, and a *JSON object* with a `3012` `reasonCode`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "reasonCode": 3012,
  "errorCode": "INSUFFICIENT_FUNDS",
  "errorDescription": "Insufficient funds"
}
```

2. *Payment Plugin* calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3012,
      "errorCode": "INSUFFICIENT_FUNDS",
      "errorDescription": "Insufficient funds"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```

4. Transaction becomes declined on Wix side.

### A payment is in a pending state and moves to a final state

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires fraud verification. The plugin responds with a `200` HTTP status code and a *JSON object* with a `5005` `reasonCode`:
```json
{
  "wixTransactionId": "000000-0000-0000-0000-000000000000",
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "reasonCode": 5005
}
```

2. *Payment Plugin* calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5005
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. Transaction becomes pending on Wix side. This intermediate state serves to prevent double charges and shipping unpaid goods.

5. If later on fraud verification is passes successfully, *Payment Plugin* sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}'
```
6. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

7. Transaction becomes approved on Wix side.

8. However, if fraud verification fails to pass successfully, *Payment Plugin* sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5001,
      "errorCode": "RISK_MANAGEMENT_DECLINED",
      "errorDescription": "Risk management declined"
    }
  }
}'
```
9. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

10. Transaction becomes declined on Wix side.

### Approval when 3D Secure verification is successfully completed

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires *3D Secure* verification. The plugin responds with a `200` HTTP status code, and a *JSON object* with `redirectUrl`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window. A *buyer* approves the payment on that web page. *Payment Plugin* redirects the browser to `successUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. Only after receiving the event, transaction becomes approved on Wix side.

### Decline when 3D Secure verification fails

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires *3D Secure* verification. The plugin responds with a `200` HTTP status code, and a *JSON object* with `redirectUrl`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window. A *buyer* fails to complete the verification on that web page. *Payment Plugin* redirects the browser to `errorUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3004,
      "errorCode": "THREE_D_SECURE_FAILED",
      "errorDescription": "3D Secure failed"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. Only after receiving the event, transaction is declined on Wix side.

### Cancellation of 3D Secure verification

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires *3D Secure* verification. The plugin responds with a `200` HTTP status code, and a *JSON object* with `redirectUrl`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window. A *buyer* cancels the verification on that web page. *Payment Plugin* redirects the browser to `cancelUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3030,
      "errorCode": "BUYER_CANCELED",
      "errorDescription": "Buyer canceled"
    }
  }
}'
```
3.  Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. Only after receiving the event, transaction is canceled on Wix side.

### A payment is in a pending state after 3D Secure verification and moves to a final state

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires *3D Secure* verification. The plugin responds with a `200` HTTP status code, and a *JSON object* with `redirectUrl`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window. A *buyer* approves the payment on that web page, but the payment requires fraud verification. *Payment Plugin* redirects the browser to `pendingUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with a `5005` `reasonCode`:
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5005
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. If later on the fraud verification passes successfully, *Payment Plugin* sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}'
```
5. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

6. Transaction becomes approved on Wix side.

7. However, if fraud verification fails to pass successfully, *Payment Plugin* sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5001,
      "errorCode": "RISK_MANAGEMENT_DECLINED",
      "errorDescription": "Risk management declined"
    }
  }
}'
```
8. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

9. Transaction is declined on Wix side.

## Redirection-based payment examples

*Payment Plugin* can support alternative [payment methods](https://dev.wix.com/api/rest/payment-provider/provider-platform/payment-methods) that redirect a *buyer* to a specific web page to proceed with a payment. If Wix does not support some payment method directly, *Payment Plugin* can support a *Hosted Page* where the *buyer* can select an actual payment method. In this case, [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) requests from Wix do not have a `paymentMethod` field.

In the following example, Wix initiates a `$10 US` payment by sending a request:
```bash
curl -X POST https://psp.example.com/sale \
 -H 'Content-Type: application/json' \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "wixMerchantId": "333333-3333-3333-3333-333333333333",
  "wixTransactionId": "000000-0000-0000-0000-000000000000",
  "paymentMethod": "sofort",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "order": {
    "id": "11111111-1111-1111-1111-111111111111",
    "description": {
      "totalAmount": 1000,
      "currency": "USD",
      "items": [
        {
          "id": "it_1",
          "name": "Digital camera",
          "quantity": 1,
          "price": 1000,
          "description": "Portable digital camera",
          "category": "physical"
        }
      ],
      "buyerInfo": {
        "buyerId": "ffc0a971-60cb-4c63-8016-39b1bce41e8d",
        "buyerLanguage": "en"
      }
    },
    "returnUrls": {
      "successUrl": "https://merchant.com/success",
      "errorUrl": "https://merchant.com/error",
      "cancelUrl": "https://merchant.com/cancel",
      "pendingUrl": "https://merchant.com/pending"
    }
  },
  "installments": 1,
  "mode": "live",
}'
```

### Approval when a buyer confirms a payment

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). *Payment Plugin* responds with a `200` HTTP status code, and a *JSON object* with `redirectUrl`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl` and a *buyer* approves the payment on that web page. The *Payment Plugin* redirects the browser to `successUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. Transaction is approved on Wix side only after the [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) is received by Wix.

### Decline when a buyer cannot proceed with a payment

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The plugin responds with a `200` HTTP status code, and a *JSON object* with `redirectUrl`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl`, but a *buyer* fails to approve the payment on that web page because there's no money available to cover the payment. The *Payment Plugin* redirects the browser to `errorUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3012,
      "errorCode": "INSUFFICIENT_FUNDS",
      "errorDescription": "Insufficient funds"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. Only after receiving the event, transaction becomes declined on Wix side.

### Cancellation of a payment

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The plugin responds with a `200` HTTP status code, and a *JSON object* with `redirectUrl`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl`, but a *buyer* cancels the payment on that web page. The *Payment Plugin* redirects the browser to `cancelUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3030,
      "errorCode": "BUYER_CANCELED",
      "errorDescription": "Buyer canceled"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. Only after receiving the event, transaction becomes canceled on Wix side.

### Payment is in pending state and moves to final state

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). *Payment Plugin* responds with a `200` HTTP status code, and a *JSON object* with `redirectUrl`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl` and a *buyer* approves the payment on that web page, but the payment requires fraud verification. *Payment Plugin* redirects the browser to `pendingUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with a `5005` `reasonCode`:
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5005
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. If later on the fraud verification passes successfully, *Payment Plugin* sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}'
```
5. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

6. Transaction becomes approved on Wix side.

7. However, if fraud verification fails to pass successfully, the plugin sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5001,
      "errorCode": "RISK_MANAGEMENT_DECLINED",
      "errorDescription": "Risk management declined"
    }
  }
}'
```
8. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

9. Transaction becomes declined on Wix side.

### Instant payment decline

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). A *Payment Plugin* does not support currency of the payment. The plugin responds with a `200` HTTP status code, and a *JSON object* with a `3003` `reasonCode`:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "reasonCode": 3003,
  "errorCode": "CURRENCY_IS_NOT_SUPPORTED",
  "errorDescription": "Currency USD is not supported"
}
```

2. *Payment Plugin* calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3003,
      "errorCode": "CURRENCY_IS_NOT_SUPPORTED",
      "errorDescription": "Currency USD is not supported"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```

4. Transaction becomes declined on Wix side.