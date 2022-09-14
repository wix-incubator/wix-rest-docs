SortOrder: 4
# Making Payments

## Introduction

To comply with payment processing requirements, a Payment Plugin must:

- accept [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) requests from Wix
- notify Wix about all changes to a _Transaction_ state by calling [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event)

When processing card payments, Wix collects card details and sends them in a [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request within a `card` property of a `paymentMethodData` field. So the _Payment Plugin_ must be compliant with [PCI DSS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard).

When a _Payment Plugin_ receives a call to the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) endpoint, it must initiate a payment. Both cards and redirection-based payment methods can be supported.

This endpoint includes a `Digest` header used for [validation](https://dev.wix.com/api/rest/payment-provider/provider-platform/payment-plugins#payment-provider_provider-platform_payment-plugins_request-validation).

If the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) endpoint receives `wixTransactionId`, which has already been processed or is being processed, it must never initiate a new payment but respond with the latest payment state. If the state has not changed, send the previous response for `wixTransactionId`.

Most fields in the request are optional and may be missing. Some fields can be configured as required. All required fields are described in the [Required Fields](https://dev.wix.com/api/rest/payment-provider/provider-platform/required-fields) section.

For each _Transaction_ state, except for states that require _buyer_ interaction, a _Payment Plugin_ must call [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with `reasonCode` which can be used to determine that state, or without `reasonCode` which indicates success. When the buyer abandons a redirection-based payment, the plugin must send a failure event with a `3030` `reasonCode`, which means payment cancellation.

Depending on the flow, one or two events can be sent per `wixTransactionId` during the payment process. If a payment cannot be completed fast enough a first event sent should have `reasonCode` with a reason for the pending state. In any case when the payment comes to its final state an event should be fired with a `reasonCode` indicating a failure reason or without `reasonCode` to indicate success. The event should be sent even when a [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) response contains final payment state.

For each `wixTransactionId` a _Payment Plugin_ can only send duplicate events or a final state event after an event designating a pending state. Do not send controversial events:

- Success events after failure events
- Failure events after success events
- Pending events after success or failure events

## Card payment examples

If a payment requires _3D Secure_ verification, a _Payment Plugin_ must respond with a redirection URL to a web page where a _buyer_ can proceed with the payment. If a card does not have 3DS enabled, or the 3DS verification is not required, or flag `moto` is true, or the payment fails instantly, the _Payment Plugin_ must respond with a final payment state.

The following _JWT_ values are fake and used for example purposes. An `installments` field is applicable for card payments only.

Fields `errorCode` and `errorMessage` in the following examples are fake. _Payment Plugin_ can send their own specific values for these fields.

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

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment is then approved with no additional verifications or _buyer_ actions needed. _Payment Plugin_ responds with a `200` HTTP status code, and a _JSON object_:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665"
}
```

2. Payment Plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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

3. Wix responds with a `200` HTTP status code and an empty JSON object:

```json
{}
```

3. Transaction is successfully approved on Wix side.

### Instant card payment decline

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The card does not have enough money available to cover the payment. _Payment Plugin_ responds with a `200` HTTP status code, and a _JSON object_ with a `3012` `reasonCode`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "reasonCode": 3012,
  "errorCode": "INSUFFICIENT_FUNDS",
  "errorMessage": "Insufficient funds"
}
```

2. Payment Plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "Insufficient funds"
    }
  }
}'
```

3. Wix responds with a `200` HTTP status code and an empty JSON object:

```json
{}
```

4. Transaction is declined on Wix side.

### Payment is in a pending state and moves to the final state

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires fraud verification. The plugin responds with a `200` HTTP status code and a _JSON object_ with a `5005` `reasonCode`:

```json
{
  "wixTransactionId": "000000-0000-0000-0000-000000000000",
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "reasonCode": 5005
}
```

2. Payment Plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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

3. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

4. Transaction becomes pending on Wix side. This intermediate state serves to prevent double charges and shipping of unpaid goods.

5. If later on fraud verification is passes successfully, Payment Plugin sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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

6. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

7. Transaction is approved on Wix side.

8. However, if fraud verification fails to pass successfully, _Payment Plugin_ sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "Risk management declined"
    }
  }
}'
```

9. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

10. Transaction is declined on Wix side.

### Approval when 3D Secure verification is successfully completed

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires 3D Secure verification. 

2. Payment Plugin responds with a `200` HTTP status code, and a JSON object with `redirectUrl`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

3. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window. A _buyer_ approves the payment on that web page. _Payment Plugin_ redirects the browser to `successUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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

4. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

4. Only after receiving the event, transaction is approved on Wix side.

### Decline when 3D Secure verification fails

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires 3D Secure verification. 
2. Payment Plugin responds with a `200` HTTP status code, and a JSON object with `redirectUrl`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

3. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window. A _buyer_ fails to complete the verification on that web page. _Payment Plugin_ redirects the browser to `errorUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "3D Secure failed"
    }
  }
}'
```

4. Wix responds with a `200` HTTP status code, and an empty _JSON object_:

```json
{}
```

5. Only after receiving the event, transaction is declined on Wix side.

### Cancellation of 3D Secure verification

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires 3D Secure verification. 
2. Payment Plugin responds with a `200` HTTP status code, and a JSON object with `redirectUrl`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

3. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window. A _buyer_ cancels the verification on that web page. 
4. Payment Plugin redirects the browser to `cancelUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "Buyer canceled"
    }
  }
}'
```

3.  Wix responds with a `200` HTTP status code, and an empty _JSON object_:

```json
{}
```

5. Only after receiving the event, transaction is canceled on Wix side.

### Payment is in a pending state after 3D Secure verification and moves to the final state

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). The payment requires 3D Secure verification. 
2. Payment Plugin responds with a `200` HTTP status code, and a JSON object with `redirectUrl`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window. A _buyer_ approves the payment on that web page, but the payment requires fraud verification. 
3. Payment Plugin redirects the browser to `pendingUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request, and calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with a `5005` `reasonCode`:

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

3. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

4. If later on the fraud verification passes successfully, Payment Plugin sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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

5. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

6. Transaction becomes approved on Wix side.

7. When fraud verification fails to pass successfully, Payment Plugin sends the following details with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "Risk management declined"
    }
  }
}'
```

8. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

9. Transaction is declined on Wix side.

## Redirection-based payment examples

Payment Plugin can support alternative [payment methods](https://dev.wix.com/api/rest/payment-provider/provider-platform/payment-methods) that redirect a buyer to a specific web page to proceed with a payment. If Wix does not support some payment method directly, Payment Plugin can support a Hosted Page where the buyer can select an actual payment method. In this case, [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) requests from Wix do not have a `paymentMethod` field.

Wix initiates a `$10 US` payment and sends a request:

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

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). 
2. Payment Plugin responds with a `200` HTTP status code, and a JSON object with `redirectUrl`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

3. Wix opens the `redirectUrl` and buyer approves the payment on that web page. 
4. Payment Plugin redirects the browser to `successUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request.
5. Payment Plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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

6. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

7. Transaction is approved on Wix side only after the [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) is received by Wix.

### Decline when a buyer cannot proceed with a payment

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). 
2. Payment Plugin responds with a `200` HTTP status code, and a JSON object with `redirectUrl`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

3. Wix opens the `redirectUrl`, but buyer fails to approve the payment on that web page because there's no money available to cover the payment. 
4. Payment Plugin redirects the browser to `errorUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request.
5. Payment Plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "Insufficient funds"
    }
  }
}'
```

6. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

6. Only after receiving the event, transaction becomes declined on Wix side.

### Cancellation of a payment

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction).
2. Payment Plugin responds with a `200` HTTP status code, and a JSON object with `redirectUrl`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

3. Wix opens the `redirectUrl`, but buyer cancels the payment on that web page. 
4. Payment Plugin redirects the browser to `cancelUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request.
5.  calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "Buyer canceled"
    }
  }
}'
```

6. Wix responds with a `200` HTTP status code, and an empty _JSON object_:

```json
{}
```

7. Only after receiving the event, transaction becomes canceled on Wix side.

### Payment is in pending state and moves to final state

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). 
2. Payment Plugin responds with a `200` HTTP status code, and a JSON object with `redirectUrl`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens the `redirectUrl` and buyer approves the payment on that web page, but the payment requires fraud verification. 
3. Payment Plugin redirects the browser to `pendingUrl`, sent in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) request.
4. Payment Plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with a `5005` `reasonCode`:

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

5. Wix responds with a `200` HTTP status code, and an empty _JSON object_:

```json
{}
```

6. If the fraud verification passes successfully, Payment Plugin sends the following with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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

7. Wix responds with a `200` HTTP status code, and an empty _JSON object_:

```json
{}
```

8. Transaction becomes approved on Wix side.

9. When fraud verification fails to pass successfully, the Payment Plugin sends the following details with [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "Risk management declined"
    }
  }
}'
```

10. Wix responds with a `200` HTTP status code, and an empty _JSON object_:

```json
{}
```

11. Transaction becomes declined on Wix side.

### Instant payment decline

1. Wix calls [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction). 
2. Payment Plugin does not support currency of the payment. 
3. Payment Plugin responds with a `200` HTTP status code, and a JSON object with a `3003` `reasonCode`:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "reasonCode": 3003,
  "errorCode": "CURRENCY_IS_NOT_SUPPORTED",
  "errorMessage": "Currency USD is not supported"
}
```

4. Payment Plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event):

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
      "errorMessage": "Currency USD is not supported"
    }
  }
}'
```

5. Wix responds with a `200` HTTP status code, and an empty JSON object:

```json
{}
```

6. Transaction becomes declined on Wix side.

## Recurring payment examples

Recurring payments (also known as subscription payments, automatic payments, or recurring billing) occur when customers authorize a merchant to charge them repeatedly for goods or services on a prearranged schedule (monthly, weekly, daily, or annually).

Wix handles each charge of a recurring subscription and supports the following payments use cases:

With a token:

- Instant payment
- Payment with 3D Secure
- Subsiquent payment

With network reference:

- Instant payment
- Payment with 3D Secure
- Subsiquent payment

## Example of a configured payment request

1. Wix initiates a `$10 US` payment and sends a request. The request is the same as the original credit card request except for one thing: it includes field `setupCredentialsOnFile` which represents the object with an `offSession` boolean field:

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
  },
  "setupCredentialsOnFile": {
    "offSession": true
  }
}'
```

### Set up with card reference without 3D Secure

1. Wix responds with a `200` HTTP status code, and a JSON object:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "credentialsOnFile": {
    "paymentMethodReference": {
      "token": "PMR-e89b-12d3-a456-42665"
    }
  }
}
```

2. [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with a confirmation:

```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "credentialsOnFile": {
        "paymentMethodReference": {
          "token": "PMR-e89b-12d3-a456-42665"
        }
      }
    }
  }
}'
```

### Set up with network reference without 3D Secure

1. Wix responds with a `200` HTTP status code, and a JSON object:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "credentialsOnFile": {
    "cardReference": {
      "networkTransactionId": "NTI-e89b-12d3-a456-42665"
    }
  }
}
```

2. [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with confirmation:

```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "credentialsOnFile": {
        "cardReference": {
          "networkTransactionId": "NTI-e89b-12d3-a456-42665"
        }
      }
    }
  }
}'
```

### Set up with 3D Secure with card reference

1. Wix responds with `200` HTTP status code, and a JSON object:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens a page with `redirectUrl` link. 
3. After a buyer confirms the payment, [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with a confirmation:

```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "credentialsOnFile": {
        "cardReference": {
          "networkTransactionId": "NTI-e89b-12d3-a456-42665"
        }
      }
    }
  }
}'
```

### Set up with 3D Secure with network reference

1. Wix responds with `200` HTTP status code, and a JSON object:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

2. Wix opens a page with `redirectUrl` link. 
3. After a buyer confirms the payment, [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with a confirmation:

```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "credentialsOnFile": {
        "paymentMethodReference": {
          "networkTransactionId": "NTI-e89b-12d3-a456-42665",
          "dsTransactionId": "DTI-e89b-12d3-a456-42665"
        }
      }
    }
  }
}'
```

### Payment with network reference

1. Wix initiates a `$10 US` payment and sends a request:

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
    "reference": {
      "token": "PMR-e89b-12d3-a456-42665"
    }
  },
  "offSession": true
}'
```

2. Wix responds with `200` HTTP status code, and a JSON object:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665"
}
```

3. [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with confirmation:

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

### Payment with card reference

1. Wix initiates a `$10 US` payment and sends a request. 
2. `dsTransactionId` may not be present if you did not submit it in [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) in the initial transaction.

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
      "networkTransactionId": "NTI-e89b-12d3-a456-42665",
      "dsTransactionId": "DTI-e89b-12d3-a456-42665",
      "holderName": "John Smith"
    }
  },
  "offSession": true
}'
```

3. Wix responds with `200` HTTP status code, and a *JSON object*:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665"
}
```

4. [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with confirmation:

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

## Mail Order/Telephone Order (MOTO) payment example

Mail order / telephone order payment (MOTO) is a card-not-present transaction where a buyer provides a merchant with their order and payment details by regular mail (not email), fax, or telephone. For a MOTO payment, the request is the same as the original credit card request, except it includes the boolean field `"moto": true`. For a non-MOTO transaction, the MOTO field is absent or equals `false`.

1. Wix initiates a `$10 US` payment and sends a request.

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
  "moto": true,
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

2. Wix responds with a `200` HTTP status code and a JSON object similar to the following:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665"
}
```

3. Payment provider must [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) with a confirmation:

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

