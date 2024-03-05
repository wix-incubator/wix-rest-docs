SortOrder: 10
# Sample Refund Flows

This article shows how to handle refund flows when implementing a [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction) endpoint. For general information about this endpoint, see [Processing Refunds](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/processing-refunds).

The Payment Provider Platform supports these refunds flows:
* [Wix-initiated refunds](#wix-initiated-refunds)
* [Payment Service Provider (PSP)-initiated refunds](#psp-initiated-refunds)

Refunds can be full or partial but cannot exceed the original payment amount. 

The following sections include examples of each refund flow. These examples are based on the [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction) request body and the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) request body. The values in these examples are fake. Examples are applicable for both `live` and `sandbox` modes.

## Wix-initiated refunds

Here are some examples of Wix-initiated refunds flows:

### Successful full refund

1. Wix calls [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction) to initiate a full refund for 10 USD. The request body looks like this:
    ```json
    {
      "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
      "wixRefundId": "ce590272-87bf-428f-943a-0ff594059712",
      "pluginTransactionId": "212b7c92-a7db-4dca-94f4-2f7d2dbb5a51",
      "merchantCredentials": {
        "client_id": "john@example.com",
        "client_secret": "asdjdj44-asdd-3445566fdss"
      },
      "refundAmount": 1000,
      "mode": "live"
    }
    ```
1. The PSP responds with an HTTP status code of `200` and this JSON object:
    ```json
    {
      "pluginRefundId": "7178df7c-8b58-42a9-86ed-9dbc143f5ac5"
    }
    ```
1. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event). Note that the `amount` field is a string:
    ```bash
    curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
          "event": {
            "refund": {
              "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
              "pluginRefundId": "7178df7c-8b58-42a9-86ed-9dbc143f5ac5",
              "amount": "1000",
              "wixRefundId": "ce590272-87bf-428f-943a-0ff594059712"
            }
          }
        }'
    ```
1. Wix marks the payment as refunded and responds with an HTTP status code of `200` and an empty JSON object.


### Successful partial refund
Requests for partial refunds are handled the same way as requests for full refunds. If Wix initiates a partial refund, the PSP can [initiate](#successful-partial-refund-1) another partial refund for the same payment.

1. Wix calls [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction) to initiate a partial refund for 5 USD. The request body looks like this:
    ```json
    {
      "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
      "wixRefundId": "ce590272-87bf-428f-943a-0ff594059712",
      "pluginTransactionId": "212b7c92-a7db-4dca-94f4-2f7d2dbb5a51",
      "merchantCredentials": {
        "client_id": "john@example.com",
        "client_secret": "asdjdj44-asdd-3445566fdss"
      },
      "refundAmount": 500,
      "mode": "live"
    }
    ```
1. The PSP responds with a HTTP status code of `200` and this JSON object:
    ```json
    {
      "pluginRefundId": "7178df7c-8b58-42a9-86ed-9dbc143f5ac5"
    }
    ```
1. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event). Note that the `amount` field is a string:
    ```bash
    curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
          "event": {
            "refund": {
              "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
              "pluginRefundId": "7178df7c-8b58-42a9-86ed-9dbc143f5ac5",
              "amount": "500",
              "wixRefundId": "ce590272-87bf-428f-943a-0ff594059712"
            }
          }
        }'
    ```
1. Wix marks the payment as partially refunded and responds with an HTTP status code of `200` and an empty JSON object.  
   At a later point, the merchant can request another partial refund.

### Failed refund
When a refund attempt fails, the PSP must respond with the appropriate reason code. For a list of reason codes, see [Reason Codes](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/reason-codes). The following example is relevant for both full and partial refunds.

1. Wix calls [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction) to initiate a full refund for 10 USD. The request body looks like this:
    ```json
    {
      "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
      "wixRefundId": "ce590272-87bf-428f-943a-0ff594059712",
      "pluginTransactionId": "212b7c92-a7db-4dca-94f4-2f7d2dbb5a51",
      "merchantCredentials": {
        "client_id": "john@example.com",
        "client_secret": "asdjdj44-asdd-3445566fdss"
      },
      "refundAmount": 1000,
      "mode": "live"
    }
    ```
2. The PSP responds with an HTTP status code of `200` and a JSON object that includes `"reasonCode": 3025`. This reason code indicates that the refund failed because of insufficient funds. The `errorCode` and `errorMessage` fields include PSP-specific data.
    ```json
    {
      "pluginRefundId": "7178df7c-8b58-42a9-86ed-9dbc143f5ac5",
      "reasonCode": 3025,
      "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
      "errorMessage": "Insufficient funds for refund"
    }
    ```
1. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event). Note that the `amount` field is a string:
    ```bash
    curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
          "event": {
            "refund": {
              "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
              "pluginRefundId": "7178df7c-8b58-42a9-86ed-9dbc143f5ac5",
              "amount": "1000",
              "wixRefundId": "ce590272-87bf-428f-943a-0ff594059712",
              "reasonCode": "3025",
              "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
              "errorMessage": "Insufficient funds for refund"
            }
          }
        }'
    ```
4. Wix does not update the payment status and responds with an HTTP status code of `200` and an empty JSON object.

## PSP-initiated refunds
PSP-initiated refunds don't involve the `Refund Transaction` endpoint. Instead, the PSP sends a webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) to notify Wix about the refund. The following examples show how to handle PSP-initiated refunds.


### Successful full refund
1. A merchant successfully refunds a 10 USD payment through the PSP's platform. 
1. The PSP sends the following webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):
    ```bash
    curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
          "event": {
            "refund": {
              "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
              "pluginRefundId": "7178df7c-8b58-42a9-86ed-9dbc143f5ac5",
              "amount": "1000"
            }
          }
        }'
    ```
1. Wix marks the payment as refunded and responds with an HTTP status code of `200` and an empty JSON object.

### Successful partial refund
Requests for partial refunds are handled the same way as requests for full refunds. When a PSP initiates a partial refund, Wix can [initiate](#successful-partial-refund) another partial refund for the same payment. 

1. A merchant successfully refunds 6 USD out of a 10 USD payment through the PSP's platform.
1. The PSP sends the following webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):
    ```bash
    curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
          "event": {
            "refund": {
              "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
              "pluginRefundId": "7178df7c-8b58-42a9-86ed-9dbc143f5ac5",
              "amount": "600"
            }
          }
        }'
    ```
1. Wix marks the payment as partially refunded and responds with an HTTP status code of `200` and an empty JSON object.