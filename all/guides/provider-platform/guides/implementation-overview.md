SortOrder: 1
# Implementation Overview

In order to integrate with Wix, a Payment Service Provider (PSP) needs to implement several endpoints and support sending webhooks to Wix. This article provides an overview of the integration process.

## Implementing Endpoints

In order to integrate with Wix, a Payment Service Provider (PSP) needs to implement 3 endpoints. Wix calls these endpoints at different points when merchants and buyers interact with Wix sites. 

The endpoints are:
* [**`Connect Account`**](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/accounts/connect-account): This endpoint is called when a merchant connects their PSP account to a Wix site. Learn more about [Connecting Accounts](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/connecting-accounts).
* [**`Create Transaction`**](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction): This endpoint is called when a buyer initiates a payment on a Wix site. Learn more about [Processing Payments](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/processing-payments).
* [**`Refund Transaction`**](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction): This endpoint is called when a merchant initiates a payment on the Wix platform. Learn more about [Processing Refunds](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/processing-refunds).

Wix calls these endpoints using `POST` HTTP requests. The requests always have a `"Content-Type"` header with the value `"application/json; charset=utf-8"`. The request body is always in JSON format. The PSP must respond to valid requests with an HTTP status code of `200` and a JSON response body with [UTF-8](https://en.wikipedia.org/wiki/UTF-8) character encoding. Wix interprets any other response as a failure.

You can use any URL for your endpoints. Let Wix know which URLs to call by configuring them in the [Wix Developers Center](https://dev.wix.com/).

For general information about implementing endpoints, see [Validate Endpoint Requests](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/validate-endpoint-requests) and [Idempotency](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/idempotency).

## Implementing Webhooks

In addition to the endpoints, PSPs must send webhooks to Wix. These webhooks are used to:

+ Confirm payment events.
+ Confirm refund events. 
+ Notify Wix about any changes to a payment or refund status. 

Webhooks are sent using the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API. Learn more about [sending webhooks](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/webhooks).

## Sample Implementation Flows

This reference includes detailed sample flows for a number of common use cases. The samples also explain when and how to send webhooks. 

To learn more see:
* [Account connection flows](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/connecting-accounts#sample-flows)
* [Payment flows](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/sample-payment-flows)
* [Refund flows](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/sample-refund-flows)

If you need assistance with your integration, feel free to contact the Wix team.