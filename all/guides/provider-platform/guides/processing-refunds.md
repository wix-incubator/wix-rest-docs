SortOrder: 9
# Processing Refunds

The Payment Provider Platform supports refunds initiated by Wix and by the Payment Service Provider (PSP). Wix-initiated refunds happen when a merchant requests a refund using the Wix dashboard. When this happens, Wix sends a request to the PSP's [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction) endpoint. This article includes general information about implementing the `Refund Transaction` endpoint and supporting PSP-initiated refunds. To learn more about specific refund flows, see [Sample Refund Flows](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/sample-refund-flows).

## About the Refund Transaction endpoint

In general, an implementation of the `Refund Transaction` endpoint must do 2 things:
1. Accept requests in the format indicated in the SPI reference, process refunds accordingly, and respond with the appropriate HTTP status code and response body.
1. Send webhooks to Wix to confirm refund events and to notify Wix about any changes to a payment status. Webhooks are sent using the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API.  

Here are some important things to keep in mind when implementing the `Refund Transaction` endpoint:
* Wix uses reason codes to indicate the reason why a refund request was declined. Your `Refund Transaction` endpoint should respond with the appropriate reason code for each case. For a list of reason codes, see [Reason Codes](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/reason-codes).
* Currently, the platform only support synchronous refunds. This means that all refunds must be processed immediately. The `Refund Transaction` endpoint must respond with an HTTP status code of `200` and the appropriate response body. Any response body that includes a `reasonCode` indicates that the refund attempt has failed. Otherwise, it has succeeded.
* Merchants can request partial refunds including multiple partial refunds for the same payment. The total amount of all partial refunds requested by Wix never exceeds the amount of the original payment.
* Requests made to the `Refund Transaction` endpoint include a `Digest` header whose value is a [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token). The PSP should use this value to validate all requests to the endpoint. Learn more about [JWT validation](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/validate-endpoint-requests).

## Idempotency
When Wix sends a request to the `Refund Transaction` endpoint, it includes a `wixRefundId` field. This field is a unique identifier for the refund. When the PSP receives this request, it must create an internal ID for the payment and include it in the response in the `pluginRefundId` field. Each `wixRefundId` must be idempotent. This means that if the PSP receives a request with a `wixRefundId` that it already processed, it must not initiate a new refund. Instead, it must respond with the latest refund state. In the case of partial refunds, Wix sends a different `wixRefundId` for each partial refund request.

When a PSP initiates a refund using the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API, it must provide a `pluginRefundId` identifier in the request. Wix treats this ID as idempotent. This means only the first request with a particular `pluginRefundId` creates a corresponding refund entity on the Wix side. All subsequent requests can only update the details of that refund.

## Send webhooks
In addition to responding to requests to the `Refund Transaction` endpoint, the PSP must send webhooks to Wix to confirm refund events. For PSP-initiated refunds, the PSP must send a webhook to notify Wix about the refund. Webhooks are sent using the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API. 

> **Notes:** 
> * When sending webhooks in response to Wix-initiated refunds, the PSP must include the `wixRefundId` from the request and the `pluginRefundId` from the response. For PSP-initiated refunds, include only the `pluginRefundId`.
> * Calling [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) several times with the same `pluginRefundId` is allowed as long as the payload remains the same, especially `reasonCode`.

Here are some sample webhooks:

### Confirm a refund event
When confirming a refund event, the webhook request body is the same as the response body for the `Refund Transaction` endpoint with the `wixRefundId` added. This webhook is sent immediately after the PSP responds to the `Refund Transaction` request.

Here is an example webhook:

```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
      "event": {
        "refund": {
          "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
          "pluginRefundId": "212b7c92-a7db-4dca-94f4-2f7d2dbb5a51",
          "amount": "1000",
          "wixRefundId": "ce590272-87bf-428f-943a-0ff594059712"
        }
      }
    }'
```

### PSP-initiated refund
When a PSP initiates a refund, it sends a webhook with the following format:

```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
      "event": {
        "refund": {
          "wixTransactionId": "fcd2655f-e261-4c5b-8129-72a241461a27",
          "pluginRefundId": "212b7c92-a7db-4dca-94f4-2f7d2dbb5a51",
          "amount": "1000"
        }
      }
    }'
```

