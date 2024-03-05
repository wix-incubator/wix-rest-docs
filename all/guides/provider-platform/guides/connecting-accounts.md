SortOrder: 6

# Connecting Accounts

When a merchant requests to connect their Wix site to a Payment Service Provider (PSP), Wix sends a request to the PSP's [`Connect Account`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/accounts/connect-account) endpoint. The PSP must verify the request and respond to Wix with any extra credentials needed for the merchant's account. This article includes general information about implementing the `Connect Account` endpoint as well as some sample flows.

## Implement the Connect Account endpoint
Every request sent by Wix to the `Connect Account` endpoint includes these fields:
* `credentials`: An object containing credentials provided by the merchant when they make the connection request. A PSP can configure the `credentials` fields that are requested in the [Wix Developers Center](https://dev.wix.com).
* `wixMerchantId`: The merchant's Wix merchant ID. This is a unique identifier for the merchant.

Requests can also include these optional fields:
* `country`: The country where the merchant is located.
* `currency`: The currency used by the merchant.

After receiving a request, the PSP must take the following steps:
* Verify the credentials provided by the merchant.
* Ensure the merchant has an operational account with the PSP.
* If possible, ensure the site's country and currency are appropriate for further payments.  
  > **Note:** The site's country and currency can change after the merchant connects their account. The PSP must validate the currency on each payment request.

The `Connect Account` endpoint's response must include the following fields:
* `accountId`: A unique identifier for the merchant's account. This value must be the same if the merchant connects their account multiple times from the same site.
* `accountName`: The name of the merchant's PSP account. This value is displayed partially in the Wix dashboard.  
  ![account name display](https://s3.amazonaws.com/wixplorer-readme-images/provider-platform%2Faccount-name-display.png)
* `credentials`: The credentials received in the request plus any other credentials the merchant needs to make payment and refund requests. This object is included by Wix in all [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) and [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction) requests. This object can only contain string values, so booleans, numbers, or dates must be represented as strings.

Wix uses reason codes to indicate the statuses of account connection requests. A PSP's Create Account endpoint should respond with the appropriate reason code for each status. For a list of reason codes, see [Reason Codes](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/reason-codes).

Requests made to the `Connect Account` endpoint include a `Digest` header whose value is a [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token). The PSP should use this value to validate all requests to the endpoint. Learn more about [JWT validation](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/validate-endpoint-requests).

## Sample flows

Here are some examples of how to implement the `Connect Account` endpoint. The examples are applicable for both `live` and `sandbox` modes.

### Basic account connection
1. Wix calls [`Connect Account`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/accounts/connect-account) with the following request body:
    ```json
    {
      "credentials": {
        "client_id": "john@example.com",
        "client_secret": "asdjdj44-asdd-3445566fdss"
      },
      "country": "US",
      "currency": "USD",
      "mode": "live",
      "wixMerchantId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1"
    }
    ```
1. The PSP responds with an HTTP status code of `200` and this JSON object:
    ```json
    {
      "credentials": {
        "client_id": "john@example.com",
        "client_secret": "asdjdj44-asdd-3445566fdss"
      },
      "accountId": "e89b-12d3-a456-42665",
      "accountName": "jane.brown@example.com"
    }
    ```

### Adding numeric and boolean credentials when connecting
1. Wix calls [`Connect Account`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/accounts/connect-account) with the following request body:
    ```json
    {
      "credentials": {
        "client_id": "john@example.com",
        "client_secret": "asdjdj44-asdd-3445566fdss"
      },
      "country": "US",
      "currency": "USD",
      "mode": "live",
      "wixMerchantId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1"
    }
    ```

2. The PSP responds with an HTTP status code of `200` and a JSON object that adds boolean and numeric values to the `credentials` object:
    ```json
    {
      "credentials": {
        "client_id": "john@example.com",
        "client_secret": "asdjdj44-asdd-3445566fdss"
        "price_includes_tax": "true",
        "tax_percentage": "20"
      },
      "accountId": "e89b-12d3-a456-42665",
      "accountName": "jane.brown@example.com"
    }
    ```

### Failed account connection
1. Wix calls [`Connect Account`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/accounts/connect-account) with the following request body:
    ```json
    {
      "credentials": {
        "client_id": "john@example.com",
        "client_secret": "asdjdj44-asdd-3445566fdss"
      },
      "country": "US",
      "currency": "USD",
      "mode" : "live",
      "wixMerchantId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1"
    }
    ```
1. The PSP responds with a `200` HTTP status code and the following JSON object. The response contains a `2009` reason code, which indicates that the PSP doesn't support the site's currency. The values of the `errorCode` and `errorMessage` fields can be customized by the PSP. To find reason codes for other cases, see [Reason Codes](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/reason-codes).
    ```json
    {
      "reasonCode": 2009,
      "errorCode": "CURRENCY_NOT_SUPPORTED",
      "errorMessage": "USD is not supported"
    }
    ```
