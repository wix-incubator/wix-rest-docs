SortOrder: 5
# Refunding Payments

## Introduction

For any transaction initiated by Wix, a *Payment Plugin* must
* accept [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) requests from Wix
* notify Wix about all refunds, including but not limited to those initiated by Wix, by calling the [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) webhook

When a *Payment Plugin* receives a call to the [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) endpoint, it must initiate a refund. If it responds with `reasonCode`, a refund attempt has failed. Otherwise, it has succeeded. For now, this endpoint only supports synchronous refunds.

This endpoint has a `Digest` header used for [validation](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/payment-plugins#payment-provider_provider-platform_payment-plugins_request-validation).

If the [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) endpoint receives `wixRefundId`, which has already been processed or is being processed, it must never initiate a new refund but respond with the latest refund state. Usually, it means sending the previous response for `wixRefundId`.

For any refund initiated by Wix, *Payment Plugin* must call [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) webhook passing payload consistent with [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) request and response. Specifically, the payload must contain `wixRefundId` from the request and `pluginRefundId` from the response. For refunds not initiated by Wix, the payload does not contain `wixRefundId`.

Calling [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) several times for the same `pluginRefundId` is ok as long as the payload remains the same, especially `reasonCode`.

## Refund examples

The following *JWT* values are fake and used for example purposes.

### Successful full refund initiated by Wix

1. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a full refund for `$10 US`:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'Content-Type: application/json' \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 1000,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
}'
```
2. Payment plugin responds with a `200` HTTP status code and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
3. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "1000",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
4. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
5. The transaction is fully refunded.

### Unsuccessful full refund initiated by Wix

1. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a full refund for `$10 US`:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'Content-Type: application/json' \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 1000,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
}'
```
2. Payment plugin responds with a `200` HTTP status code and a *JSON object* that includes `reasonCode: 3025`. Reason code indicates that the refund attempt has failed because of insufficient funds. Fields `errorCode` and `errorMessage` provider-specific data.
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222",
  "reasonCode": 3025,
  "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
  "errorMessage": "Insufficient funds for refund"
}
```
3. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "1000",
      "wixRefundId": "33333333-3333-3333-3333-333333333333",
      "reasonCode": "3025",
      "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
      "errorMessage": "Insufficient funds for refund"
    }
  }
}'
```
4. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
5. The transaction status does not change.

### Successful partial refund initiated by Wix

1. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a partial `$5 US` refund for a `$10 US` transaction:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -H 'Content-Type: application/json' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 500,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
2. Payment plugin responds with a `200` HTTP status code and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
3. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "500",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
4. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
5. Transaction becomes partially refunded. Remaining amount is `$5 US`.

### Unsuccessful partial refund initiated by Wix

1. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a partial `$5 US` refund for a `$10 US` transaction:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -H 'Content-Type: application/json' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 500,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
2. Payment plugin responds with a `200` HTTP status code and a *JSON object* with `reasonCode: 3025`. Reason code indicates that the refund attempt has failed because of insufficient funds. Fields `errorCode` and `errorMessage` contain provider-specific data.
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222",
  "reasonCode": 3025,
  "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
  "errorMessage": "Insufficient funds for refund"
}
```
3. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "500",
      "wixRefundId": "33333333-3333-3333-3333-333333333333",
      "reasonCode": 3025,
      "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
      "errorMessage": "Insufficient funds for refund"
    }
  }
}'
```
4. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
5. Transaction does not change.

### Multiple successful partial refunds initiated by Wix with total amount less than amount of the payment

1. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a partial `$5 US` refund for a `$10 US` transaction:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -H 'Content-Type: application/json' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 500,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
2. Payment plugin responds with a `200` HTTP status code and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
3. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "500",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
4. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
5. Transaction becomes partially refunded. Remaining amount is `$5 US`.

6. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a second partial `$4 US` refund:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -H 'Content-Type: application/json' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 400,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
Payment plugin responds with a `200` HTTP status code and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
7. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash 
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "400",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
8. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
9. Transaction is partially refunded. Remaining amount is `$1 US`.

#### Multiple successful partial refunds initiated by Wix which become a full refund

1. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a partial `$6 US` refund for a `$10 US` transaction:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -H 'Content-Type: application/json' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 600,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
2. Payment plugin responds with a `200` HTTP status code and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
3. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "600",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
4. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
5. Transaction becomes partially refunded. Remaining amount is `$4 US`.

6. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a a second partial `$4 US` refund:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -H 'Content-Type: application/json' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 400,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
7. Payment plugin responds with a `200` HTTP status code and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
8. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "400",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
9. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
10. Transaction becomes fully refunded.

### Successful full refund initiated not by Wix

Merchant successfully refunds a `$10 US` transaction through the  *Payment Service Provider* UI.
Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event):
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "1000"
    }
  }
}'
```
Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
Transaction becomes fully refunded.

### Successful partial refund initiated not by Wix

1. Merchant successfully refunds `$6 US` out of a `$10 US` transaction through the  *Payment Service Provider* UI.
2. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event):
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "600"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
4. Transaction becomes partially refunded. Remaining amount is `$4 US`.

### Multiple successful partial refunds initiated not by Wix with a total amount less than the amount of payment

1. Merchant successfully refunds `$6 US` out of a `$10 US` transaction through the  *Payment Service Provider* UI.
Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event):
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "600"
    }
  }
}'
```
2. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
3. Transaction becomes partially refunded. Remaining amount is `$4 US`.

4. Merchant successfully refunds another `$2 US` through the *Payment Service Provider* UI.
5. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event):
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "200"
    }
  }
}'
```
6. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
7. Transaction stays partially refunded. Remaining amount is `$2 US`.

### Multiple successful partial refunds that become a full refund initiated not by Wix

1. Merchant successfully refunds `$6 US` out of a `$10 US` transaction through the *Payment Service Provider* UI.
2. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event):
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "600"
    }
  }
}'
```
3. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
4. Transaction becomes partially refunded. Remaining amount is `$4 US`.

5. Merchant successfully refunds another `$4 US` through the *Payment Service Provider* UI.
6. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event):
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "400"
    }
  }
}'
```
7. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
8. Transaction becomes fully refunded.

### One successful partial refund initiated by Wix and another one initiated not by Wix with a total amount less than the amount of a payment

1. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a partial `$6 US` refund for a `$10 US` transaction:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -H 'Content-Type: application/json' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 600,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
2. Payment plugin responds with a `200` HTTP status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
3. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "600",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
4. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
5. Transaction becomes partially refunded. Amount left is `$4 US`.

6. Merchant successfully refunds `$2 US` through the *Payment Service Provider* UI.
7. The plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event):
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "200"
    }
  }
}'
```
8. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
9. Transaction stays partially refunded. Remaining amount is `$2 US`.

### One successful partial refund initiated by Wix and another one initiated not by Wix which become a full refund

1. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to initiate a partial `$6 US` refund for a `$10 US` transaction:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -H 'Content-Type: application/json' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 600,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
2. Payment plugin responds with a `200` HTTP status code and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
3. Payment plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "600",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
4. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
5. Transaction becomes partially refunded. Remaining amount is `$4 US`.

6. Merchant successfully refunds `$4 US` through the *Payment Service Provider* UI.

7. The plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event):
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "400"
    }
  }
}'
```
8. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
9. Transaction becomes fully refunded.
