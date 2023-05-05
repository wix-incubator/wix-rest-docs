SortOrder: 6
# Payment Plugins

## Introduction
*Payment Plugin* is a [web application](https://en.wikipedia.org/wiki/Web_application) that provides a payment service to Wix site owners and implements the following HTTP endpoints:
* [Connect Account](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/account/connect-account) to prepare for future payments.
* [Create Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/create-transaction) to make a payment.
* [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) to refund a payment.

Wix calls these endpoints exclusively with the [POST](https://en.wikipedia.org/wiki/POST_(HTTP)) HTTP request method and `application/json` as a value for the `Content-Type` header. A request body always has a *JSON* format. The *Payment Plugin* should ignore unknown *JSON* properties in the request.

The *Payment Plugin* must always respond with an [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) `200 OK` and *JSON* in the response body. The `Content-Type` header must contain `application/json`. Any other responses indicate failures.


## Request validation

*Payment Plugin* must [validate](https://devforum.wix.com/kb/en/article/validating-requests-received-from-wix) each incoming request to make sure it comes from Wix and has not been tampered with.

To validate a request, *Payment Plugin* must:
1. Obtain a *JSON Web Token* by taking the value of a `Digest` header and strip the prefix `JWT=` from it.
2. Validate the *JWT* signature by using their public key from the [Developer Center](https://dev.wix.com/dc3/my-apps/).
3. Validate an [`exp` claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4) of the *JWT* for expiration.
4. Check that the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) message digest of the request body matches the one from the `data` claim of the *JWT*.

Header names are case-insensitive, therefore, the `Digest` header can also be called `DIGEST` or `digest`.

The `exp` *JWT* claim represents seconds past 1970-01-01 00:00:00Z.

The `data` claim value is a [JSON object](http://json-schema.org/understanding-json-schema/reference/object.html#object) with a property `SHA256`. The value of this property is a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) message digest of the request body.

> **Note**
> Use raw bytes of the request body to calculate the message digest. Do not parse the request body before calculating the message digest. JSON parsing or even converting bytes into text can lead to a different message digest and validation failure.

> Wix recommends using [jwt.io](https://jwt.io) for debugging purposes.

## Validation example

*Payment Plugin* receives a request with the following body:
```json
{
  "credentials": {
    "clientId": "my_client",
    "clientSecret": "my_client_secret"
  },
  "country": "US",
  "currency": "USD",
  "mode": "sandbox",
  "wixMerchantId": "000000-0000-0000-0000-000000000000"
}
```
*Payment Plugin* takes *JWT* from the `Digest` header, successfully verifies it using its public key and decodes it.  The *JWT* payload is:
```json
{
  "data": {
    "SHA256": "5f4b44d33fae46e015494ebcce11456c74ba4bdae0412016a89b03844e9a7361"
  },
  "iat": 1625836375,
  "exp": 1625836475
}
```
The *JWT* token expiration time is `09 Jul 2021 13:14:35 GMT`, 2 minutes after the current time `09 Jul 2021 13:12:35 GMT`, therefore, the token has not expired yet. Token expiration time is 2 minutes.

An SHA-256 message digest of the request body matches with corresponding value from the *JWT* payload. The request body has not been modified in transit.
