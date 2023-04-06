SortOrder: 1
# Sample Flow

This article presents a sample flow your app can support. You aren't limited to this exact flow, but it can be a helpful jumping off point as you plan your Additional Fees integration.

## Configuration flow

1. A site owner installs and authorizes your 3rd-party app to provide additional fee calculations based on various factors (line items, shipping info, and buyer details). The app collects the JSON Web Token (JWT), decodes it, and stores the resulting instance ID.
    
    For example, the token in this request:
    
    ```bash
    $ curl -X POST https://ext-server.com/wix-spi/account-ids
    -H 'Content-Type: plain/text'
    -d 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbnN0YW5jZUlkIjoiMDQ0NjY3ZjQtYzEzZi00NmMyLTg1MDYtZGU5ZTQyMjkzODk2In0.fxedHrnHUFi6V-S5OH8gL-pY4STxFWZHjj-xo9QUwQY'
    ```
    
    Decodes into:
    
    ```json
    { "instanceId": "044667f4-c13f-46c2-8506-de9e42293896" }
    ```

## Display additional fees calculated for eCommerce orders

1. A customer logs on to the merchant’s Wix site and adds a product to the cart or checkout.

2. Wix sends a Calculate Additional Fees SPI request to your app. The payload will include some or all of the fields described in the Body Params and example sections of [Calculate Additional Fees](https://dev.wix.com/api/rest/wix-ecommerce/additional-fees-integration-spi/calculate-additional-fees). The payload will also include the `currency` in a `context` parameter in the [request envelope](https://dev.wix.com/api/rest/getting-started/service-provider-interface#getting-started_service-provider-interface_request-envelope).

3. Your Additional Fees integration triggers the required flow on its platform and processes the request.

    Wix expects an object containing the additional fees calculated, the currency of those fees, and either a 4xx HTTP status code or a 200 HTTP status code.
    
    Example of a successful response from your app:
    
    ```json
    {
      "currency": "USD",
      "additionalFees": [
        {
          "code": "fragile-fee",
          "name": "Fragile Packaging Fee",
          "price": "3",
          "taxDetails": {
            "taxable": true
          }
        }
      ]
    }
    ```

4. The Wix site displays the additional fees on the cart or checkout page (depending on which page triggered the SPI request). The customer can confirm the additional fees before proceeding to payment.
