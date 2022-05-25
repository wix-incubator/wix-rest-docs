SortOrder: 7
# Working With Webhooks

## Introduction

A *Payment Plugin* must send a [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) webhook to inform Wix about any changes to payment state such as approval, decline, or refund.

Every time the payment state changes, *Payment Plugin* must send a [POST](https://en.wikipedia.org/wiki/POST_(HTTP)) HTTP request to `https://www.wixapis.com/payments/v1/provider-platform-events` with a `Content-Type` header including `application/json`. Request body must be *JSON* format.

Response [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) will be `200 OK`, the `Content-Type` header will contain `application/json`, and the response body will be an empty [JSON object](http://json-schema.org/understanding-json-schema/reference/object.html#object). Any other response indicates failure to deliver an event. *Payment Plugin* must [retry](https://en.wikipedia.org/wiki/Exponential_backoff) sending the event later.

Provide amounts in [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) requests in *minor currency units* described in the [Currencies](https://dev.wix.com/api/rest/payment-provider/provider-platform/currencies) table.

To call [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event), *Payment Plugin* must have a `CASHIER.GET_ACCESS` permission.

[Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) HTTP request must have an `Authorization` HTTP header with an *Access Token*. [Obtain](https://dev.wix.com/api/rest/authorization/oauth-2/request-an-access-token) a new token each time before sending an event.

When requesting an *Access Token*, pass `grant_type`=`client_credentials`, `scope`=`CASHIER.GET_ACCESS`, `client_id`, and `client_secret`. The latter two can be found in the [Wix Developers Center](https://devforum.wix.com/kb/en/article/find-your-apps-secret-key) as **App ID** and **App Secret Key**.

> **Note**
> * An *Access Token* obtained this way is *only* applicable for the [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) endpoint.
> * Do not cache an *Access Token*. Obtain a new one for each call.
> * There is no *Refresh Token* for a `client_credentials` grant type.
> * The [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) endpoint does not support tokens acquired using other grant types.


## Example
Given the *Payment Plugin*'s *App ID*=`00000000-0000-0000-000000000000` and *App Secret Key*=`11111111-1111-1111-111111111111`. Make the following call to obtain an access token:
```bash
curl -v -X POST \
  'https://www.wix.com/oauth/access' \
  -H 'Content-Type: application/json' \
  -d '{
    "grant_type": "client_credentials",
    "scope": "CASHIER.GET_ACCESS",
    "client_id": "00000000-0000-0000-000000000000",
    "client_secret": "11111111-1111-1111-111111111111"
  }'
```
The response body would be the following:
```json
{
  "refresh_token": null,
  "access_token": "ai0zIQqt71bmnkgEJ1CRJchjKJup"
}
```
Then *Payment Plugin* can send an event:
```bash
curl -v -X POST \
  'https://www.wixapis.com/payments/v1/provider-platform-events' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: ai0zIQqt71bmnkgEJ1CRJchjKJup' \
  -d '{
    "event" : {
      "transaction": {
        "wixTransactionId": "22222222-2222-2222-2222-222222222222",
        "pluginTransactionId" : "33333333-3333-3333-3333-333333333333"
      }
    }
  }'
```
