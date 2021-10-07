SortOrder: 9
# Refunds

## Introduction

For any transaction initiated by Wix a *Payment Plugin* should
* accept `RefundTransaction` requests from Wix
* notify Wix about all refunds including but not limited to those initiated by Wix by calling `SubmitEvent`

When a *Payment Plugin* receives a call to the `RefundTransaction` endpoint it should initiate a refund. For now, this endpoint only supports synchronous refunds. If it responds with `reasonCode` it means a refund attempt has failed otherwise it has succeeded.

This endpoint has a `Digest` header which should be used for [request validation](https://devforum.wix.com/kb/en/article/validating-requests-received-from-wix).

If the `RefundTransaction` endpoint receives `wixRefundId` which has already been processed or is being processed it should never initiate a new refund but should respond with the latest refund state. Usually it means sending the previous response for that `wixRefundId`.

For any refund initiated by Wix a *Payment Plugin* should call `SubmitEvent` webhook passing payload consistent with `RefundTransaction` request and response. Specifically, the payload should contain `wixRefundId` from the request and `pluginRefundId` from the response. For refunds not initiated by Wix the payload does not contain `wixRefundId`.

Calling `SubmitEvent` several times for same `pluginRefundId` is ok as long as payload stays the same, especially `reasonCode`.

> **NOTE**
> All *JWT* in the following examples are not actual JWT and always equal to `ai0zIQqt71bmnkgEJ1CRJchjKJup`.

## Refund examples

### Successful full refund initiated by Wix

Wix initiates a full refund for a `10 USD` transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "1000",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "1000",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes fully refunded.

### Unsuccessful full refund initiated by Wix

Wix initiates a full refund for a `10 USD` transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "1000",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object* containing `reasonCode: 3025` which indicates that the refund attempt has failed because of insufficient funds. Fields `errorCode` and `errorMessage` contain data specific for each provider.
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222",
  "reasonCode": "3025",
  "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
  "errorMessage": "Insufficient funds for refund"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "1000",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333",
                    "reasonCode": "3025",
                    "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
                    "errorMessage": "Insufficient funds for refund"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction does not change.

### Successful partial refund initiated by Wix

Wix initiates a `5 USD` refund for a `10 USD` transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "500",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "500",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes partially refunded. Amount left is `5 USD`.

### Unsuccessful partial refund initiated by Wix

Wix initiates a `5 USD` refund for a `10 USD` transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "500",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object* containing `reasonCode: 3025` which indicates that the refund attempt has failed because of insufficient funds. Fields `errorCode` and `errorMessage` contain provider specific data.
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222",
  "reasonCode": "3025",
  "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
  "errorMessage": "Insufficient funds for refund"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "500",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333",
                    "reasonCode": "3025",
                    "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
                    "errorMessage": "Insufficient funds for refund"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction does not change.

### Multiple successful partial refunds initiated by Wix with total amount less than amount of a transaction

Wix initiates a first `5 USD` refund for a `10 USD` transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "500",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "500",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes partially refunded. Amount left is `5 USD`.

Wix initiates a second `4 USD` refund for the transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "400",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "400",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction stays partially refunded. Amount left is `1 USD`.

#### Multiple successful partial refunds initiated by Wix which become a full refund

Wix initiates a first `6 USD` refund for a `10 USD` transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "600",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "600",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes partially refunded. Amount left is `4 USD`.

Wix initiates a second `4 USD` refund for the transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "400",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "400",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes fully refunded.

### Successful full refund initiated on the side of a *Payment Provider*

A merchant successfully refunds a `10 USD` transaction within a UI of the *Payment Provider*.
The plugin calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "1000"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes fully refunded.

### Successful partial refund initiated on the side of a *Payment Provider*

A merchant successfully refunds `6 USD` out of a `10 USD` transaction within a UI of the *Payment Provider*.
The plugin calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "600"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes partially refunded. Amount left is `4 USD`.

### Multiple successful partial refunds initiated on the side of a *Payment Provider* with total amount less than amount of a transaction

First, a merchant successfully refunds `6 USD` out of a `10 USD` transaction within a UI of the *Payment Provider*.
The plugin calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "600"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes partially refunded. Amount left is `4 USD`.

Second, a merchant again successfully refunds `2 USD` within a UI of the *Payment Provider*.
The plugin calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "200"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction stays partially refunded. Amount left is `2 USD`.

### Multiple successful partial refunds initiated on the side of a *Payment Provider* which become a full refund

First, a merchant successfully refunds `6 USD` out of a `10 USD` transaction within a UI of the *Payment Provider*.
The plugin calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "600"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes partially refunded. Amount left is `4 USD`.

Second, a merchant again successfully refunds `4 USD` within a UI of the *Payment Provider*.
The plugin calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "400"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes fully refunded.

### One successful partial refund initiated by Wix and another one initiated on the side of a *Payment Provider* with total amount less than amount of a transaction

First, Wix initiates a `6 USD` refund for a `10 USD` transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "600",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "600",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes partially refunded. Amount left is `4 USD`.

Second, a merchant successfully refunds `2 USD` within a UI of the *Payment Provider*.
The plugin calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "200"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction stays partially refunded. Amount left is `2 USD`.

### One successful partial refund initiated by Wix and another one initiated on the side of a *Payment Provider* which becomes a full refund

First, Wix initiates a `6 USD` refund for a `10 USD` transaction by calling `RefundTransaction`:
```bash
curl -X POST \
 https://url.provider.com/refund \
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
  "refundAmount": "600",
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
  }
}'
```
The plugin responds with `200` __HTTP__ status code, and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
The plugin also calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "600",
                    "wixRefundId": "33333333-3333-3333-3333-333333333333"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes partially refunded. Amount left is `4 USD`.

Second, a merchant successfully refunds `4 USD` within a UI of the *Payment Provider*.
The plugin calls `SubmitEvent`:
```bash
curl -v -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
    -H 'Content-Type: application/json' \
    -d '{
            "event" : {
                "refund": {
                    "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                    "pluginRefundId" : "22222222-2222-2222-2222-222222222222",
                    "amount": "400"
                }
            }
        }'
```
Wix responds with `200` __HTTP__ status code, and an empty *JSON object*:
```json
{}
```
The transaction becomes fully refunded.