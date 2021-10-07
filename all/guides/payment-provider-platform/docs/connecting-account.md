SortOrder: 7
# Connecting Account

## Introduction
When a merchant connects their payment provider account to a Wix site, Wix calls `ConnectAccount` endpoint implemented by a *Payment Plugin*. The *Payment Plugin* must:
* verify credentials provided by the merchant
* ensure the merchant has an operational account on a *Payment Provider*
* ensure merchant's country and currency are appropriate for further payments

The country and currency fields can be omitted from a `ConnectAccount` request, or they can be changed later without notifying a *Payment Plugin* about it. Validate currency on each payment request.

This endpoint has a `Digest` header. Use it for [request validation](https://devforum.wix.com/kb/en/article/validating-requests-received-from-wix).

In response a *Payment Plugin* must return the following:
* `accountId` - must be different for each merchant but same when a merchant connects an account multiple times
* `accountName` - can be displayed on Wix side
* `credentials` - passed back to the *Payment Plugin* in `CreateTransaction` and `RefundTransaction` calls

The *Payment Plugin* must use `credentials` from a request and add new properties if needed. No properties can be removed or renamed. The `credentials` can only hold string values. Therefore, booleans, numbers, or dates must be represented as strings.

## Connect examples

> **Note**
> In all following examples:
> - `currency` and `contry` are `USD` and `US`.
> - All *JWT* values are fake. JWT always equals to `ai0zIQqt71bmnkgEJ1CRJchjKJup`.
> - `mode` is set to `live`. All the use cases are applicable to `sandbox` mode as well.
> - Wix merchant ID is `000000-0000-0000-0000-000000000000`

### Connect account without enriching credentials
For example, credentials keys are `client_id` and `client_secret` with values `MerchantClientId` and `MerchantClientSecret`, respectively.
On the provider's side, `account_id` is `ABON1` and representative account name is `Funny Pony's shop`.

Example of the request:

```bash
curl -X POST \
 https://url.provider.com/connect \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
    "credentials": {
        "client_id": "MerchantClientId",
        "client_secret": "MerchantClientSecret"
    },
    "country": "US",
    "currency": "USD",
    "mode" : "live",
    "wixMerchantId": "000000-0000-0000-0000-000000000000"
 }'
```

Response body:

```json
{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "accountId": "ABON1",
  "accountName": "Funny Pony's shop"
}
```

with __HTTP__ status code equal to `200`

### Connect account with numeric and boolean credential properties
For example, credentials keys are `client_id` and `client_secret`, `price_includes_tax`, `tax_percentage` with values `MerchantClientId`, `MerchantClientSecret`, `true` and `20`, respectively.
On the provider's side, `account_id` is `ABON1` and representative account name is `Funny Pony's shop`.

Example of the request:

```bash
curl -X POST \
 https://url.provider.com/connect \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
    "credentials": {
        "client_id": "MerchantClientId",
        "client_secret": "MerchantClientSecret"
        "price_includes_tax": "true",
        "tax_percentage": "20"
    },
    "country": "US",
    "currency": "USD",
    "mode" : "live",
    "wixMerchantId": "000000-0000-0000-0000-000000000000"
 }'
```

Response body:

```json
{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret",
    "price_includes_tax": "true",
    "tax_percentage": "20"
  },
  "accountId": "ABON1",
  "accountName": "Funny Pony's shop"
}
```

with __HTTP__ status code equal to `200`

### Connect account with enriching credentials
For example, credentials keys are `client_id` and `client_secret` with values `MerchantClientId` and `MerchantClientSecret`, respectively.
On the provider's side, `account_id` is `ABON1` and representative account name is `Funny Pony's shop`.
Provider needs to add `caller_token` property to the credentials with value `6mW9GHIsmhjSqGE7DBkD` to avoid transaction failures when `client_secret` is changed on the provider's side.

Example of the request:

```bash
curl -X POST \
 https://url.provider.com/connect \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
    "credentials": {
        "client_id": "MerchantClientId",
        "client_secret": "MerchantClientSecret"
    },
    "country": "US",
    "currency": "USD",
    "mode" : "live",
    "wixMerchantId": "000000-0000-0000-0000-000000000000"
 }'
```

Response body:

```json
{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret",
    "caller_token": "6mW9GHIsmhjSqGE7DBkD"
  },
  "accountId": "ABON1",
  "accountName": "Funny Pony's shop"
}
```

with __HTTP__ status code equal to `200`

### Connect account failed because merchant does not support currency
For example, credentials keys are `client_id` and `client_secret` with values `MerchantClientId` and `MerchantClientSecret`, respectively.
Provider's error code for not supported currency is `CURRENCY_IS_NOT_SUPPORTED` and error message is `Currency USD is not supported`.

Example of the request:

```bash
curl -X POST \
 https://url.provider.com/connect \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
    "credentials": {
        "client_id": "MerchantClientId",
        "client_secret": "MerchantClientSecret"
    },
    "country": "US",
    "currency": "USD",
    "mode" : "live",
    "wixMerchantId": "000000-0000-0000-0000-000000000000"
 }'
```

Response body:

```json
{
  "reasonCode": "2009",
  "errorCode": "CURRENCY_IS_NOT_SUPPORTED",
  "errorMessage": "Currency USD is not supported"
}
```

with __HTTP__ status code equal to `200`