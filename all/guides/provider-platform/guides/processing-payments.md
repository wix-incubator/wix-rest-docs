SortOrder: 7
# Processing Payments

When a buyer submits a payment for a Payment Service Provider (PSP) on a Wix site, Wix sends a request to the PSP's [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint. The PSP must then process the payment and send a response to Wix. This article includes general information about implementing the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint. To learn more about specific payment flows, see [Sample Payment Flows](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/sample-payment-flows).

## About the Create Transaction endpoint

In general, an implementation of the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint must do 2 things:
1. Accept requests in the format indicated in the SPI reference, process payments accordingly, and respond with the appropriate HTTP status code and response body.
1. Send webhooks to Wix to confirm payment events and to notify Wix about any changes to a payment status. Webhooks are sent using the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API.

Here are some important things to keep in mind when implementing the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint:
* Wix uses reason codes to indicate the statuses of payments. Your `Create Transaction` endpoint should respond with the appropriate reason code for each payment status. For a list of reason codes, see [Reason Codes](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/reason-codes).
* When processing credit card and [digital wallet](/guides/./sample-payment-flows.md/#digital-wallet-payments) payments, Wix collects card details and sends them as part of the SPI request. Card data is sent in the `paymentMethodData` field. Because requests include sensitive card data, the PSP must be compliant with [PCI DSS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard).
* Requests made to the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint include a `Digest` header whose value is a [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token). The PSP should use this value to validate all requests to the endpoint. Learn more about [JWT validation](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/validate-endpoint-requests).
* Most fields in the request body are optional. Your endpoint should not rely on these fields being present. You can configure certain fields as required so that they are included with every request. This configuration is done in your app's payment gateway component in the [Wix Developers Center](https://dev.wix.com).

## Idempotency
When Wix sends a request to the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint, it includes a `wixTransactionId` field. This field is a unique identifier for the payment. When the PSP receives this request, it must create an internal ID for the payment and include it in the response in the `pluginTransactionId` field. Each `wixTransactionId` must be idempotent. This means that if the PSP receives a request with a `wixTransactionId` that it has already processed, it must not initiate a new payment. Instead, it must respond with the latest payment status. If the status hasn't changed, the PSP should send the previous response for that `wixTransactionId`.

## Send webhooks
In addition to responding to requests to the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint, the PSP must send webhooks to Wix to confirm payment events and to notify Wix about any changes to a payment status. Webhooks are sent using the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API. 

Webhook requests must use 0Auth 2.0 authentication. To learn more, see [Webhooks](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/webhooks).

### Confirm a final payment event
When confirming a payment event, such as an instantly approved card payment, the webhook request body is the same as the response body for the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint with the `wixTransactionId` added. This webhook is sent immediately after the PSP responds to the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) request.

For example, the response body for a declined card payment looks like this:
```json
{
  "pluginTransactionId": "0dd8c114-b70e-493f-90b7-bf106b445ccd",
  "reasonCode": 3019,
  "errorCode": "CARD_LIMIT_EXCEEDED",
  "errorMessage": "Not enough funds left in the card limit for this transaction."
}
```

The webhook request body for the same payment looks like this:
```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
      "pluginTransactionId": "0dd8c114-b70e-493f-90b7-bf106b445ccd",
      "reasonCode": 3019,
      "errorCode": "CARD_LIMIT_EXCEEDED",
      "errorMessage": "Not enough funds left in the card limit for this transaction."
    }
  }
}
```
### Update payment status

When a payment request is not finalized immediately, such as when a payment requires fraud verification or 3D Secure verification, the PSP must send multiple webhooks to Wix. The first request is sent immediately after the PSP responds to the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) request. This request indicates that the payment is in a pending state. The PSP must include a `reasonCode` field with a value of `5005` to indicate that the payment is pending.

For example, the webhook request body for a pending payment looks like this:
```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
      "pluginTransactionId": "0dd8c114-b70e-493f-90b7-bf106b445ccd",
      "reasonCode": 5005
    }
  }
}
```
When the payment is finalized, the PSP must send another webhook to Wix. This webhook indicates the final payment status. If the payment is rejected, the PSP must include a `reasonCode` field with the appropriate value. If the payment is approved, the PSP must not include a `reasonCode` field.

For example, the webhook request body for an approved payment looks like this:
```json
{
  "event": {
    "transaction": {
      "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
      "pluginTransactionId": "0dd8c114-b70e-493f-90b7-bf106b445ccd"
    }
  }
}
```
> **Note:** If a buyer abandons a [redirection-based payment](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/sample-payment-flows#redirection-based-payments), the update webhook must use the `3030` reason code. This indicates that the payment was canceled by the buyer.

A PSP must not send contradictory webhooks. For example, you must not send a webhook indicating that a payment is approved after you have sent a webhook indicating that the payment is declined. You should also not send a webhook indicating that a payment is pending after you have sent a webhook indicating that the payment is approved or declined.