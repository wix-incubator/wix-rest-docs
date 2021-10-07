SortOrder: 8
# Making Payments
## Introduction
To comply with payment processing requirements, a *Payment Plugin* must:
* accept `CreateTransaction` requests from Wix
* notify Wix about all changes to a *Transaction* state by calling `SubmitEvent`

When a *Payment Plugin* receives a call to the `CreateTransaction` endpoint, it must initiate a payment. Both cards and redirection-based payment methods can be supported.

This endpoint includes a `Digest` header used for [request validation](https://devforum.wix.com/kb/en/article/validating-requests-received-from-wix).

If the `CreateTransaction` endpoint receives `wixTransactionId`, which has already been processed or is being processed, it must never initiate a new payment but respond with the latest payment state. If the state has not changed, send the previous response for  `wixTransactionId`.

Most fields in the request are optional and can be missing. Some fields can be configured as required. All required fields are described in the *Required Fields* section.

For each *Transaction* state, except for states that require *buyer* interaction, a *Payment Plugin* must call `SubmitEvent` with `reasonCode` which can be used to determine that state, or without `reasonCode` which indicates success.

Depending on the flow, one or two events can be sent per `wixTransactionId` during the payment process. If a payment cannot be completed fast enough a first event sent should have `reasonCode` with a reason for the pending state. In any case when the payment comes to its final state an event should be fired with a `reasonCode` indicating a failure reason or without `reasonCode` to indicate success. The event should be sent even when a `CreateTransaction` response contains final payment state.

For each `wixTransactionId` a *Payment Plugin* can only send duplicate events or a final state event after an event designating a pending state. Do not send controversial events:
* Success events after failure events
* Failure events after success events
* Pending events after success or failure events

## Card payment examples
In case if transaction requires *3D Secure* check user should be redirected to third party page to proceed with challenges.
In case if __3D Secure__ authorization is not supported for specified card, is not required or transaction is instantly failed there are will not be any redirection to any page.

> **Note**
> * In all following examples `contry` will be `US`, as well amount will be always `10 USD`.
> * `DIGEST` header value in all following examples are faked and are not actually correct *JWT*, and always equals to `JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup`
> * In all following examples `mode` is set to `live`. All the use cases applicable to `sandbox` mode as well
> * WIX transaction id and order id will be `000000-0000-0000-0000-000000000000` and `11111111-1111-1111-1111-111111111111` respectively
> * Merchant credentials will be like the following:
>```json
>{
>  "client_id": "MerchantClientId",
>  "client_secret": "MerchantClientSecret"
>}
>```
> * There will be only one order item like the following:
>```json
>{
>  "id": "it_1",
>  "name": "Digital camera",
>  "quantity": 1,
>  "price": 1000,
>  "description": "Portable digital camera",
>  "weightInKg": 0.3,
>  "category": "physical"
>}
>```
> * Wix merchant id will be `333333-3333-3333-3333-333333333333`
> * Return URLs will be like the following:
>```json
>{
>  "successUrl": "https://merchant.com/successful",
>  "errorUrl": "https://merchant.com/error",
>  "cancelUrl": "https://merchant.com/cancelled",
>  "pendingUrl": "https://merchant.com/pending"
>}
>```
> * Installments will be equal to `1`. For now *installments* are applicable only for card payments.
> * Parameters `errorCode` and `errorMessage` are internal *Payment Provider*'s data, and can be different for different *Payment Providers*. In all examples they are placed as an example. Use your own `errorCode` and `errorMessage` in the implementation.

All credit card information will be collected by WIX and will be passed in `card` parameter of `paymentMethodData` field of the request.
So to process cards the backend servers should be PCI compliant.
This endpoint supports *3D Secure* as well as non 3D Secure payments.

> __Note__
> In all examples for card payments, the card information is:
> - number  =  `4111111111111111`,
> - expiration year = `2030`
> - expiration month = `12`
> - cvv = `777`
> - holder name = `John Biggins`
>
> Given the card information, the request example is the following:
>```bash
>curl -X POST \
> https://url.provider.com/sale \
> -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
> -d '{
>  "wixMerchantId": "333333-3333-3333-3333-333333333333",
>  "wixTransactionId": "000000-0000-0000-0000-000000000000",
>  "paymentMethod": "creditCard",
>  "merchantCredentials": {
>    "client_id": "MerchantClientId",
>    "client_secret": "MerchantClientSecret"
>  },
>  "order": {
>    "id": "11111111-1111-1111-1111-111111111111",
>    "description": {
>      "totalAmount": 1000,
>      "currency": "USD",
>      "items": [
>        {
>          "id": "it_1",
>          "name": "Digital camera",
>          "quantity": 1,
>          "price": 1000,
>          "description": "Portable digital camera",
>          "weightInKg": 0.3,
>          "category": "physical"
>        }
>      ],
>      "buyerInfo": {
>        "buyerId": "ffc0a971-60cb-4c63-8016-39b1bce41e8d",
>        "buyerLanguage": "en"
>      }
>    },
>    "returnUrls": {
>      "successUrl": "https://merchant.com/successful",
>      "errorUrl": "https://merchant.com/error",
>      "cancelUrl": "https://merchant.com/cancelled",
>      "pendingUrl": "https://merchant.com/pending"
>    }
>  },
>  "installments": 1,
>  "mode": "live",
>  "paymentMethodData": {
>    "card": {
>      "number": 4111111111111111,
>      "year": 2030,
>      "month": 12,
>      "cvv": "777",
>      "holderName": "John Biggins"
>    }
>  }
>}'
>```
>
> In all responses plugin transaction ID will be `e89b-12d3-a456-42665`.

### Instant approval
If the *buyer*'s card was charged in favour of *merchant* and there no additional checks and actions are needed. Then response on the call should be with __HTTP__ status code `200` and body like following:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665"
}
```

As a result, transaction will be successful on Wix side.
In addition, to respond, the *Payment Plugin* must fire an event, using `SubmitEvent` to notify Wix about the status of the transaction with the following body:

```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665"
    }
  }
}
```

### Instant decline
For example, the transaction is declined because of insufficient fund, with *Payment Provider*'s `error code`  as `INSUFFICIENT_FUNDS` and `error message` as `Insufficient funds`. In this case, the response on the call must be with __HTTP__ status code `200` and the following body:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "reasonCode": 3012,
  "errorCode": "INSUFFICIENT_FUNDS",
  "errorDescription": "Insufficient funds"
}
```

As a result, transaction will fail on Wix side.
In addition, to respond, the *Payment Plugin* must fire an event using `SubmitEvent` to notify Wix about the status of the transaction with the following body:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3012,
      "errorCode": "INSUFFICIENT_FUNDS",
      "errorDescription": "Insufficient funds"
    }
  }
}
```

### Payment stuck in pending state then was moved to the final state
For example, transaction will most likely be successfully charged but requires some additional fraud checks. Then response on the call should be with __HTTP__ status code `200` and the following body:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5005
    }
  }
}
```
In addition, to respond, the *Payment Plugin* must fire an event using `SubmitEvent` to notify Wix about the status of the transaction with the following body:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5005
    }
  }
}
```

As a result, the transaction on Wix side will wait for the event with the final transaction status. This intermediate state is needed to avoid double charges and shipping unpaved goods.

If as a result, transaction will successfully pass fraud check and be successfully charged, then the *Payment Plugin* should fire an event using `SubmitEvent` to notify Wix about successful charge of the transaction with the following body:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}
```

If transaction fails to pass the fraud check, *Payment Plugin* must fire an event using `SubmitEvent` to notify Wix about charge failure.
For example, with error code `Risk management declined`.

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5001,
      "errorCode": "RISK_MANAGEMENT_DECLINED",
      "errorDescription": "Risk management declined"
    }
  }
}
```

### Approval after 3D Secure completes successfully
For example, *3D Secure* page is on `https://example.com/redirect-sale-form`.
Response on call must be with __HTTP__ status code `200` and the following body:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

__Wix__ will open a modal on the `redirectUrl` when user should proceed with *3D Secure*.
Once *buyer* successfully approves the payment, *Payment Plugin* must redirect user to `successUrl` which is `https://merchant.com/successful` in the example.
It will display success result to user, on __Wix__ side but will not actually approve the transaction cause __Wix__ will await for and event to be fired using `SubmitEvent` with the body like follows:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}
```

Only after this event, transaction on __Wix__ side will be actually approved.

### Decline after 3D Secure completes unsuccessfully
Assume that *3D Secure* page is on `https://example.com/redirect-sale-form`.
Response on call should be with __HTTP__ status code `200` and body like following:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

__Wix__ will open a modal on the `redirectUrl` when user should proceed with *3D Secure*.
Once *buyer* will fail the payment, *Payment Plugin* should redirect user to `errorUrl` which is `https://merchant.com/error` in the example.
It will display error result to user with ability to retry the payment, but will not actually decline the transaction cause __Wix__ will await for and event to be fired using `SubmitEvent` with the body like follows:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3004,
      "errorCode": "THREE_D_SECURE_FAILED",
      "errorDescription": "3D Secure failed"
    }
  }
}
```

Only after this event, transaction on __Wix__ side will be actually declined.

### Cancel 3D Secure card authentication on user action

Assume that *3D Secure* page is on `https://example.com/redirect-sale-form`.
Response on call should be with __HTTP__ status code `200` and body like following:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

__Wix__ will open a modal on the `redirectUrl` when user should proceed with *3D Secure*.
Once *buyer* will press cancel button, if such exists, *Payment Plugin* should redirect user to `cancelUrl` which is `https://merchant.com/cancelled` in the example.
It will display cancel result to user with ability to retry the payment, but will not actually cancel the transaction cause __Wix__ will await for and event to be fired using `SubmitEvent` with the body like follows:

```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665",
      "reasonCode": 3030,
      "errorCode": "BUYER_CANCELLED",
      "errorDescription": "Buyer cancelled"
    }
  }
}
```

Only after this event, transaction on __Wix__ side will be actually cancelled.

### Payment stuck in pending state after 3D Secure completes successfully and then moved to final state
Assume that *3D Secure* page is on `https://example.com/redirect-sale-form`.
Response on call should be with __HTTP__ status code `200` and body like following:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

__Wix__ will open a modal on the `redirectUrl` when user should proceed with *3D Secure*.
Once *buyer* will successfully approve the payment, but payment is not instantly approved cause requires some additional checks like fraud check, *Payment Plugin* should redirect user to `pendingUrl` which is `https://merchant.com/pending` in the example.
In addition to redirect *Payment Plugin* should fire an event using `SubmitEvent` to notify __Wix__ about status of the transaction with the following body:
```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665",
      "reasonCode": 5005
    }
  }
}
```

If as a result, transaction will successfully pass fraud check and will be successfully charged then *Payment Plugin* should fire an event using `SubmitEvent` to notify __Wix__ about success charge of the transaction with the following body:

```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665"
    }
  }
}
```

In case if transaction will fail to pass fraud check transaction *Payment Plugin* should fire an event using `SubmitEvent` to notify __Wix__ about charge failure.
As and example because of `Risk management declined`.

```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665",
      "reasonCode": 5001,
      "errorCode": "RISK_MANAGEMENT_DECLINED",
      "errorDescription": "Risk management declined"
    }
  }
}
```

Only after this event, transaction on __Wix__ side will be actually approved or declined.


## Redirection-based payment examples
A *Payment Plugin* can support alternative payment methods that involve redirecting a *buyer* to a specific web page to proceed with a payment. If Wix does not support a some payment method directly the *Payment Plugin* can own *Hosted Page* where *buyers* can select actual payment method. If that case `CreateTransaction` requests from Wix do not have a `paymentMethod` field.

> __Note__
> Request in all examples will be like following:
>```bash
>curl -X POST \
> https://url.provider.com/connect \
> -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
> -d '{
>  "wixMerchantId": "333333-3333-3333-3333-333333333333",
>  "wixTransactionId": "000000-0000-0000-0000-000000000000",
>  "paymentMethod": "sofort",
>  "merchantCredentials": {
>    "client_id": "MerchantClientId",
>    "client_secret": "MerchantClientSecret"
>  },
>  "order": {
>    "id": "11111111-1111-1111-1111-111111111111",
>    "description": {
>      "totalAmount": 1000,
>      "currency": "USD",
>      "items": [
>        {
>          "id": "it_1",
>          "name": "Digital camera",
>          "quantity": 1,
>          "price": 1000,
>          "description": "Portable digital camera",
>          "weightInKg": 0.3,
>          "category": "physical"
>        }
>      ],
>      "buyerInfo": {
>        "buyerId": "ffc0a971-60cb-4c63-8016-39b1bce41e8d",
>        "buyerLanguage": "en"
>      }
>    },
>    "returnUrls": {
>      "successUrl": "https://merchant.com/successful",
>      "errorUrl": "https://merchant.com/error",
>      "cancelUrl": "https://merchant.com/cancelled",
>      "pendingUrl": "https://merchant.com/pending"
>    }
>  },
>  "installments": 1,
>  "mode": "live",
>}'
>```
>
> In all responses plugin transaction id will be `e89b-12d3-a456-42665`.

### Approval after the payment was approved on payment provider's page
Assume that page to proceed the payment is `https://example.com/redirect-sale-form`.
Response on call should be with __HTTP__ status code `200` and body like following:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

__Wix__ will open a modal on the `redirectUrl` when user should proceed with the payment.
Once *buyer* will successfully approve the payment, *Payment Plugin* should redirect user to `successUrl` which is `https://merchant.com/successful` in the example.
It will display success result to user, on __Wix__ side but will not actually approve the transaction cause __Wix__ will await for and event to be fired using `SubmitEvent` with the body like follows:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}
```

Only after this event, transaction on __Wix__ side will be actually approved.

### Decline after the payment was declined on payment provider's page
Assume that page to proceed the payment is `https://example.com/redirect-sale-form`.
Response on call should be with __HTTP__ status code `200` and body like following:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

__Wix__ will open a modal on the `redirectUrl` when user should proceed with the payment.
Once *buyer* will fail the payment eg: because of insufficient funds, *Payment Plugin* should redirect user to `errorUrl` which is `https://merchant.com/error` in the example.
It will display error result to user with ability to retry the payment, but will not actually decline the transaction cause __Wix__ will await for and event to be fired using `SubmitEvent` with the body like follows:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3012,
      "errorCode": "INSUFFICIENT_FUNDS",
      "errorDescription": "Insufficient funds"
    }
  }
}
```

Only after this event, transaction on __Wix__ side will be actually declined.

### Cancel payment on user action

Assume that page to proceed the payment is `https://example.com/redirect-sale-form`.
Response on call should be with __HTTP__ status code `200` and body like following:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

__Wix__ will open a modal on the `redirectUrl` when user should proceed with the payment.
Once *buyer* will press cancel button, if such exists, a *Payment Plugin* should redirect user to `cancelUrl` which is `https://merchant.com/cancelled` in the example.
It will display cancel result to user with ability to retry the payment, but will not actually cancel the transaction cause __Wix__ will await for and event to be fired using `SubmitEvent` with the body like follows:

```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665",
      "reasonCode": 3030,
      "errorCode": "BUYER_CANCELLED",
      "errorDescription": "Buyer cancelled"
    }
  }
}
```

Only after this event, transaction on __Wix__ side will be actually cancelled.

### Payment stuck in pending state after payment completes on the payment provider's page successfully and then moved to final state
Assume that page to proceed the payment is `https://example.com/redirect-sale-form`.
Response on call should be with __HTTP__ status code `200` and body like following:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

__Wix__ will open a modal on the `redirectUrl` when user should proceed with the payment.
Once *buyer* will successfully approve the payment, but payment is not instantly approved cause requires some additional checks like fraud check, *Payment Plugin* should redirect user to `pendingUrl` which is `https://merchant.com/pending` in the example. As a result *buyer* will see success page on __Wix__ side.
In addition to redirect *Payment Plugin* should fire an event using `SubmitEvent` to notify __Wix__ about status of the transaction with the following body:
```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665",
      "reasonCode": 5005
    }
  }
}
```

If as a result, transaction will successfully pass fraud check and will be successfully charged then *Payment Plugin* should fire an event using `SubmitEvent` to notify __Wix__ about success charge of the transaction with the following body:

```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665"
    }
  }
}
```

In case if transaction will fail to pass fraud check transaction *Payment Plugin* should fire an event using `SubmitEvent` to notify __Wix__ about charge failure.
As and example because of `Risk management declined`.

```json
{
  "event" : {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId" : "e89b-12d3-a456-42665",
      "reasonCode": 5001,
      "errorCode": "RISK_MANAGEMENT_DECLINED",
      "errorDescription": "Risk management declined"
    }
  }
}
```

Only after this event, transaction on __Wix__ side will be actually approved or declined.

### Instant decline
Assume that transaction is declined because currency, with *Payment Provider*'s `error code`  like `CURRENCY_IS_NOT_SUPPORTED` and `error message` like `Currency USD is not supported` then response on the call should be with __HTTP__ status code `200` and body:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "reasonCode": 3003,
  "errorCode": "CURRENCY_IS_NOT_SUPPORTED",
  "errorDescription": "Currency USD is not supported"
}
```

As a result transaction will fail on the __Wix__ side.
In addition to response *Payment Plugin* should fire an event using `SubmitEvent` to notify __Wix__ about status of the transaction with the following body:

```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3003,
      "errorCode": "CURRENCY_IS_NOT_SUPPORTED",
      "errorDescription": "Currency USD is not supported"
    }
  }
}
```