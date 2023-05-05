SortOrder: 1
# Sample Flows

This article presents a sample flow your app can support. You aren't limited to this exact flow, but they can be a helpful jumping off point as you plan your pricing integration.

## Price Calculation Flow

1. A site owner installs and authorizes your 3rd-party app to calculate prices for their services based on various factors (region, age, taxes, and so on). The app collects the JSON Web Token (JWT), decodes it, and stores the resulting instance ID.
    
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
    
1. Once the site owner installs the app, Wix ignores the built-in pricing logic for pricing Bookings services and instead uses the pricing logic provided by your app. 

1. A customer logs on to the merchant’s Wix site and starts placing an order for a booking.

1. When the customer books on the Wix site, the checkout process (such as Wix eCommerce, coming soon!) sends a [Calculate Price](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi/calculate-price) SPI request, including the [`booking` object]((https://dev.wix.com/api/rest/wix-bookings/bookings-v2/booking-object)), to your app. 

1. Your app triggers the required flow on its platform to process the request.
    
    Wix expects an object containing the price, and either a 4xx HTTP status code (and some errors) or a 200 HTTP status code.

1. Wix expects an array of line items for the booking and either a calculated price
   or a textual price description.

    When returning a price description, the app formats the response like this: 

    ```json 
    {
        "priceDescription": "50.00 BRL"
    }
    ```
  
    When returning a calculated price, the app formats the response like this: 
  
    ```json 
    {
        "calculatedPrice": 16.0
    }
    ```
    
1. The Wix site displays the updated pricing on a site page. The customer can
   confirm the price before proceeding to payment.