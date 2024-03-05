SortOrder: 4
# Webhooks

Payment Service Providers (PSPs) must send webhooks to Wix to confirm payment and refund events and to notify Wix about any changes to a payment or refund status. Webhooks are sent using the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API. This article includes general information about sending webhooks. For details about when in the payment and refund flows to send webhooks, see [Processing Payments](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/processing-payments) and [Processing Refunds](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/processing-refunds).

We created a [code example](https://github.com/wix-incubator/payment-spi-sample/blob/master/submit-event.mjs) using Node.js that demonstrates how to send webhooks. You can use this code as a reference when you implement your own validation logic.

## Authorization
Every call to the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API must include an `Authorization` header with an access token as its value. 

Before you can obtain an access token, your Wix Developers Center app must have the appropriate permissions. To get these permissions, contact the Wix Payments team and confirm that your app has the `CASHIER.GET_ACCESS` permission.

To obtain an access token, send a `POST` request to this endpoint:
```bash
https://www.wixapis.com/oauth/access
```
Include this header:
```bash
Content-Type: application/json,
```
The body of the request must be a JSON object with following format:
```json
{
  "grant_type" : "client_credentials",
  "scope" : "CASHIER.GET_ACCESS",
  "client_id" : <APP_ID>,
  "client_secret" : <APP_SECRET_KEY>
}
```
You can [find your app's ID and secret key](https://devforum.wix.com/kb/en/article/find-your-apps-secret-key) in the Wix Developers Center.

The response to the request has a body with the following format:
```json
{
  "refresh_token": null,
  "access_token" : <ACCESS_TOKEN>
}
```
Use the value for `access_token` as the value for the `Authorization` header in your [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) requests.

> **Notes:**
> * Don't cache access tokens. Obtain a new one for each webhook you send.
> * These access tokens are only valid for the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API. You can't use them for other Wix APIs.
> * Access tokens retrieved using different `"grant_type"` values can't be used to send webhooks.

## Sending webhooks

To send a webhook, send a request to the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) API with the following format:
```bash
curl -v -X POST \
  'https://www.wixapis.com/payments/v1/provider-platform-events' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <ACCESS_TOKEN>' \
  -d '{
    "event" : { <EVENT_OBJECT> }
  }'
``` 
If the webhook is received successfully, the response has a status code of `200`, the `Content-Type` header's value is `application/json`, and the response body is an empty JSON object. Any other response indicates that the webhook wasn't received. In this case, retry sending the webhook later.

> **Note:** When you send currency values in your webhook data, use the minor currency units described in the [currencies table](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/currencies).
