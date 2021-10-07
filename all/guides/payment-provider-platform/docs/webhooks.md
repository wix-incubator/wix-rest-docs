SortOrder: 5
# Webhooks

## Introduction

A *Payment Plugin* should use a `SubmitEvent` webhook to inform Wix about any changes to payment state such as approval, decline, or refund.

Each time payment state changes the *Payment Plugin* should send a [POST](https://en.wikipedia.org/wiki/POST_(HTTP)) HTTP request to `https://www.wixapis.com/payments/v1/provider-platform-events` with a `Content-Type` header containing `application/json`, meaning a request body should have *JSON* format.

The response [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) will be `200 OK`, the `Content-Type` header will contain `application/json`, and the response body will be an empty [JSON object](http://json-schema.org/understanding-json-schema/reference/object.html#object). Any other response indicates failure to deliver an event, so the *Payment Plugin* should [retry](https://en.wikipedia.org/wiki/Exponential_backoff) sending the event later.

Money amounts in `SubmitEvent` requests should be provided in *currency minor units* described in *Currencies* table.

In order to be able to call `SubmitEvent` the *Payment Plugin* should have a `CASHIER.GET_ACCESS` permission, which can be configured in the [Dev Center](https://dev.wix.com/dc3/my-apps/).

A `SubmitEvent` HTTP request should have an `Authorization` HTTP header with an *Access Token*. The token should be [obtained](https://dev.wix.com/api/rest/authorization/oauth-2/request-an-access-token) each time before sending an event. When requesting the *Access Token* please pass `grant_type`=`client_credentials`, `scope`=`CASHIER.GET_ACCESS`, `client_id`, and `client_secret`. The latter two can be [found](https://devforum.wix.com/kb/en/article/find-your-apps-secret-key) in the Dev Center as *App ID* and *App Secret Key*.

> **Note**
> * An *Access Token* obtained this way is only applicable for the `SubmitEvent` endpoint.
> * Do not cache an *Access Token*, obtain a new one for each call.
> * There is no *Refresh Token* for a `client_credentials` grant type.
> * The `SubmitEvent` endpoint does not support tokens acquired using other grant types.


## Example
Given a *Payment Plugin* has its *App ID*=`00000000-0000-0000-000000000000` and *App Secret Key*=`11111111-1111-1111-111111111111` it should make the following call to obtain an access token:
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
After that the *Payment Plugin* can send an event:
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
