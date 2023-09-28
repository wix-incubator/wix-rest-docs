SortOrder: 3
# Connecting Account

## Introduction
When a merchant connects their [PSP](https://en.wikipedia.org/wiki/Payment_service_provider) account to a Wix site, a [Connect Account](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/account/connect-account) request (as implemented by a *Payment Plugin*) will be triggered. The *Payment Plugin* must:
* verify the passed credentials as those provided by the merchant.
* ensure the merchant has an operational account with the *Payment Service Provider*.
* ensure merchant's country and currency are appropriate for further payments.

The country and currency fields may be omitted from a [Connect Account](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/account/connect-account) request, or they may be changed later without notifying a *Payment Plugin* about it. Validate currency on each payment request.

This endpoint has a `Digest` header. Use it for [validation](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/payment-plugins#payment-provider_provider-platform_payment-plugins_request-validation).

In response, *Payment Plugin* must return the following:
* `accountId` - must be unique for each merchant but same when a merchant connects an account multiple times
* `accountName` - can be displayed on Wix side
* `credentials` - passed back to the *Payment Plugin* in [Create Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/create-transaction) and [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) calls

*Payment Plugin* must use `credentials` from a request and add new properties if needed. No properties can be removed or renamed. The `credentials` can only hold string values. Therefore, booleans, numbers, or dates must be represented as strings.

## Connect examples

The following *JWT* values are fake and used for example purposes. Examples are applicable for both `live` and `sandbox` modes.

### Connecting without enriching credentials
1. Wix calls [Connect Account](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/account/connect-account) with some credentials provided by a merchant:

```bash
curl -X POST https://psp.example.com/connect \
 -H 'Content-Type: application/json' \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "country": "US",
  "currency": "USD",
  "mode": "live",
  "wixMerchantId": "000000-0000-0000-0000-000000000000"
}'
```

2. *Payment Plugin* responds with a `200` HTTP status code and a *JSON object*:

```json
{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "accountId": "999999-9999-9999-9999-999999999999",
  "accountName": "jane.brown@example.com"
}
```

### Connecting with numeric and boolean credentials

1. Wix calls [Connect Account](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/account/connect-account) with credentials of different types:

```bash
curl -X POST https://psp.example.com/connect \
 -H 'Content-Type: application/json' \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret",
    "price_includes_tax": "true",
    "tax_percentage": "20"
  },
  "country": "US",
  "currency": "USD",
  "mode": "live",
  "wixMerchantId": "000000-0000-0000-0000-000000000000"
}'
```

2. *Payment Plugin* responds with a `200` HTTP status code and a *JSON object*:

```json
{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret",
    "price_includes_tax": "true",
    "tax_percentage": "20"
  },
  "accountId": "999999-9999-9999-9999-999999999999",
  "accountName": "jane.brown@example.com"
}
```

### Connecting with enriching credentials

1. Wix calls [Connect Account](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/account/connect-account):

```bash
curl -X POST https://psp.example.com/connect \
 -H 'Content-Type: application/json' \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "country": "US",
  "currency": "USD",
  "mode": "live",
  "wixMerchantId": "000000-0000-0000-0000-000000000000"
}'
```

2. *Payment Plugin* responds with a `200` HTTP status code and a *JSON object*. The response contains `credentials` with an additional property `caller_token` used to avoid payment failures if `client_secret` is changed on the provider's side.

```json
{
  "credentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret",
    "caller_token": "6mW9GHIsmhjSqGE7DBkD"
  },
  "accountId": "999999-9999-9999-9999-999999999999",
  "accountName": "jane.brown@example.com"
}
```

### Connecting fails because a currency is unsupported

1. Wix calls [Connect Account](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/account/connect-account):

```bash
curl -X POST https://psp.example.com/connect \
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

2. *Payment Plugin* responds with a `200` HTTP status code and a *JSON object*. The response contains a `2009` `reasonCode`, which means the currency is not supported. Values of `errorCode` and `errorMessage` properties can be different for each provider.

```json
{
  "reasonCode": 2009,
  "errorCode": "CURRENCY_IS_NOT_SUPPORTED",
  "errorMessage": "Currency USD is not supported"
}
```
