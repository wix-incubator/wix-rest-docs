SortOrder: 4
# Payment Plugin

## Introduction
A *Payment Plugin* is a [web application](https://en.wikipedia.org/wiki/Web_application) that implements the following HTTP endpoints:
* `ConnectAccount` to prepare for further payments
* `CreateTransaction` to make a payment
* `RefundTransaction` to refund a payment

Wix calls those endpoints exclusively with the [POST](https://en.wikipedia.org/wiki/POST_(HTTP)) HTTP request method and `application/json` as a value for the `Content-Type` header, so a request body always have *JSON* format.

A *Payment Plugin* should always respond with an [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) `200 OK` and *JSON* in a response body, so the `Content-Type` header should contain `application/json`. Any other responses indicate failures.

## Request validation

A *Payment Plugin* has to [validate](https://devforum.wix.com/kb/en/article/validating-requests-received-from-wix) each incoming request to make sure it comes from Wix and has not been tampered with.

In order to do so, the *Payment Plugin* has to
* Obtain a *JSON Web Token* by taking the value of a `Digest` header and stripping a prefix `JWT=` from it.
* Validate a signature of the *JWT* using own public key from a [Dev Center](https://dev.wix.com/dc3/my-apps/).
* Validate an [`exp` claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4) of the *JWT* for expiration.
* Check that an [SHA-256](https://en.wikipedia.org/wiki/SHA-2) message digest of a request body matches one from a `data` claim of the *JWT*.

Header names are case-insensitive, so the `Digest` header can also be called `DIGEST`, `digest`, etc.

The `exp` *JWT* claim represents seconds past 1970-01-01 00:00:00Z.

The `data` claim value is a [JSON object](http://json-schema.org/understanding-json-schema/reference/object.html#object) with a property `SHA256`. The value of this property is a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) message digest of a request body.

> **Note**
> Use raw bytes of the request body to calculate the message digest. Do not parse request body before calculating calculate the message digest. JSON parsing or even converting bytes to text can lead to a different message digest and validation fail.

Use [jwt.io](https://jwt.io) for debugging purposes. A JWT must not contain any sensitive information.

## Validation example

A *Payment Plugin* receives a request with the following body
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
It takes a *JWT* from the `Digest` header, successfully verifies it using own public key, and decodes it, so the *JWT* payload is
```json
{
  "data": {
    "SHA256": "5f4b44d33fae46e015494ebcce11456c74ba4bdae0412016a89b03844e9a7361"
  },
  "iat": 1625836375,
  "exp": 1625836475
}
```
The *JWT* token expiration time is `09 Jul 2021 13:14:35 GMT` which is 2 minutes after current time `09 Jul 2021 13:12:35 GMT`, so the token has not expired yet.

An SHA-256 message digest of a request body matches a corresponding value taken from the *JWT* payload, so the request body has not been modified in transit.