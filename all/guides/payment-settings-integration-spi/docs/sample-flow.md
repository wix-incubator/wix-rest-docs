SortOrder: 1
# Payment Settings: Sample Flow

This article presents sample flows your app can support. You aren't limited to this exact flow, but it can be a helpful jumping off point as you plan your Payment Settings integration.

## Retrieve Payment Settings

1. A site visitor clicks on the "Place Order" button in their Wix checkout, and an online payment is required.

2. Wix sends a [Get Payment Settings SPI](https://dev.wix.com/api/rest/wix-ecommerce/payment-settings-integration-spi/get-payment-settings) request to your app. 

3. Your server handles the request and returns the payment settings.
    
    Example of a payment settings response from your app:
    
    ```json
    {
      "paymentSettings": {
        "requires3dSecure": true
      }
    } 
    ```

4. Wix passes the payment settings to the payment provider to continue the payment process.
