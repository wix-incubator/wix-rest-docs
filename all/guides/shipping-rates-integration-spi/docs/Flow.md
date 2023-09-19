SortOrder: 1
# Sample Flow

This article presents a sample flow your app can support. You aren't limited to this exact flow, but it can be a helpful jumping off point as you plan your Shipping Rates integration.

## Configuration flow

1. A site owner installs and authorizes your 3rd-party app to provide shipping rates based on various factors (region, product weight, taxes, and so on). The app collects the JSON Web Token (JWT), decodes it, and stores the resulting instance ID.
    
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

## Display custom shipping rates for eCommerce orders

1. A customer logs on to the merchant’s Wix site and starts adds a product to the cart or checkout.

2. Wix sends a Get Shipping Rates SPI request to your app. The payload will include some or all of the fields described in the Body Params and example sections of the [Get Shipping Rates reference](https://dev.wix.com/api/rest/wix-ecommerce/shipping-rates-integration-spi/get-shipping-rates).

3. Your Shipping Rates integration triggers the required flow on its platform and processes the request.

    Wix expects an object containing the shipping rates, and either a 4xx HTTP status code (and some errors) or a 200 HTTP status code.
    
    Example of a successful response from your app:
    
    ```json
    {
      "shippingRates": [
        {
          "code": "usps_international",
          "title": "USPS - International",
          "logistics": {
            "deliveryTime": "2-5 days"
          },
          "cost": {
            "price": "15",
            "currency": "USD",
            "additionalCharges": [
              {
                "price": "10",
                "type": "HANDLING_FEE",
                "details": "Handling fee of $5 applied for fragile items."
              }
            ]
          }
        }
      ]
    }
    ```

    Example of an error:
    
    ```json
    {
      "errors": [
        {
          "code": "MISSING_POSTAL_CODE",
          "message": "Postal Code was missing from request"
        }
      ]
    }
    ```

4. The Wix site displays the shipping rate/s on the cart or checkout page (depending on where the customer is selecting the shipping option). The customer can confirm the shipping rate before proceeding to payment.
