SortOrder: 2
# Flows

This article presents some sample flows your app can support. You aren't limited to these exact flows, but they can be a helpful jumping off point as you plan your Local Delivery integration.

* [Configuration Flow](#Configuration-Flow)
* [Delivery Flow](#Delivery-Flow)

## Configuration Flow

1. A site owner installs and authorizes an app for a local delivery service provider on a merchant’s Wix site. The app collects the JSON Web Token (JWT), decodes it, and stores the resulting instance ID.

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

1. When the site owner loads the Delivery Area dashboard page, Wix sends a [List Account IDs](https://dev.wix.com/api/rest/wix-restaurants/local-delivery-integration-spi/local-delivery/list-account-ids) request to the local delivery service provider with the instance ID of the merchant's store, restaurant, or business.
    
    Wix expects an array of the IDs of all the accounts belonging to this instance ID (regardless of their operational status) and a 200 HTTP status code. The instance ID is sent as a query parameter in the request to the third-party. For example:
    
    ```json
    {
    "accountIds" :[
        "03cabfd0-e8aa-496d-a411-baf4275811d5",
        "04b5b58a-a803-477b-81a5-cced1534dd1e",
        "0d79528d-46e7-4b29-bdb1-145876c4ef9d"
      ]
    }
    ```

1. Wix sends a [Get Account Status](https://dev.wix.com/api/rest/wix-restaurants/local-delivery-integration-spi/local-delivery/get-account-status) request to your app per account ID to get the status of each location. After decoding the returned JWT, you’ll get an object like this:
    
    ```json
    {
     "instanceId": "044667f4-c13f-46c2-8506-de9e42293896",
     "accountId": "03cabfd0-e8aa-496d-a411-baf4275811d5"
    }
    ```

1. Wix expects a string containing the operational status for each account and a 200 HTTP status code. For example:
    ```json
    { "status": "ACTIVE" }
    ```
    
    The possible values for the status property are:
    
    + `CREATED`. The account is created.
    + `ACTIVE`. The account is active.
    + `INACTIVE`. The account is inactive.
    
    If an account’s status is “ACTIVE,” delivery operations can be processed for that location. Otherwise, deliveries cannot be requested for that location.

1. The Wix site displays the updated information for all accounts on the Delivery Area dashboard page. The information from this page is displayed on a site page so the customer can select an active location from a list.

## Delivery Flow

1. Customer logs on to the merchant’s Wix site, chooses an active location, and starts placing an order.

1. To present the customer with how much the delivery will cost on the checkout page, Wix requests an estimate of the delivery fee and availability when the customer enters their delivery address.

1. Wix sends a [Get Delivery Estimate](https://dev.wix.com/api/rest/wix-restaurants/local-delivery-integration-spi/local-delivery/get-delivery-estimate) request to the local delivery service provider with the account ID for the location.

    After decoding, you get an object like this:
    
    ```json
    {
      "instanceId": "044667f4-c13f-46c2-8506-de9e42293896",
      "accountId": "03cabfd0-e8aa-496d-a411-baf4275811d5",
      "pickupAddress": {
        "country": "US",
        "subdivision": "FL",
        "city": "Fort Lauderdale",
        "postalCode": "33301",
        "streetAddress": {
          "number": "300",
          "name": "SE 2nd St"
        },
        "formattedAddress": "300 SE 2rd St, Fort Lauderdale, FL, USA"
      },
      "dropoffAddress": {
        "country": "US",
        "subdivision": "FL",
        "city": "Fort Lauderdale",
        "postalCode": "33301",
        "streetAddress": {
          "number": "500",
          "name": "SE 3rd St"
        },
      "formattedAddress": "500 SE 3rd St, Fort Lauderdale, FL, USA"
      },
      "metaSiteId": "6c2384aa-f02f-455d-935e-3a16991d958f",
      "pickupTime": "2022-03-24T01:45:00.000000Z",
      "dropoffTime": "2022-03-24T02:00:26.000000Z",
      "orderTotal": {
        "value": 500,
        "currency": "USD"
      }
    }
    ```

1. The Local Delivery integration triggers the required flow on its platform and processes the request.

    Wix expects an object containing the estimate, and either a 4xx HTTP status code (and some errors) or a 200 HTTP status code.
    
    Example of an error:
    
    ```json
    {
      "errors": [
        {
          "code": "SYSTEM_ERROR"
          "message": "Account not ready"
        }
      ]
    }
    ```
    
    Example of a successful response:
    
    ```json
    {
      "id": "01940e92-cefd-4d39-b582-6047f38291c7",
      "fee": {
        "value": 690,
         "currency": "USD"
      },
      "promisedPickupTime": "2022-03-24T01:45:00.000000Z",
      "promisedDropoffTime": "2022-03-24T02:00:26.000000Z"
     }
    ```

1. Customer accepts the fee and orders the delivery during checkout.  

1. The site owner sees the order in the Dashboard and decides whether to accept the order. Accepting the order triggers the [Order Accepted](https://dev.wix.com/api/rest/wix-restaurants/orders/order-accepted-webhook) webhook.

1. When the order is accepted by the site owner, Wix sends a [Create Delivery](https://dev.wix.com/api/rest/wix-restaurants/local-delivery-integration-spi/local-delivery/create-delivery) request to the local delivery service provider with all details needed to create the order and process the delivery. Wix sends another [Get Delivery Estimate](https://dev.wix.com/api/rest/wix-restaurants/local-delivery-integration-spi/local-delivery/get-delivery-estimate) request to the local delivery service provider to confirm availability. The app then requests delivery on the third-party's platform.
    
    After decoding, you get an object like this:
    
    ```json
    {
      "instanceId": "044667f4-c13f-46c2-8506-de9e42293896",
      "accountId": "03cabfd0-e8aa-496d-a411-baf4275811d5",
      "estimateId": "01940e92-cefd-4d39-b582-6047f38291c7",
      "orderId": "123123123123123",
      "pickupBusinessName": "The restaurant",
      "pickupAddress": {
        "country": "US",
        "subdivision": "FL",
        "city": "Fort Lauderdale",
        "postalCode": "33301",
        "streetAddress": {
          "number": "300",
          "name": "SE 2nd St"
        },
        "formattedAddress": "300 SE 2rd St, Fort Lauderdale, FL, USA"
      },
      "pickupPhoneNumber": "305-123-4532",
      "customer": {
        "email": "the-customer@gmail.com",
        "firstName": "John",
        "lastName": "Doe",
        "phoneNumber": "305-654-211"
      },
      "pickupInstructions": "Knock on the door",
      "dropoffAddress": {
        "country": "US",
        "subdivision": "FL",
        "city": "Fort Lauderdale",
        "postalCode": "33301",
        "streetAddress": {
          "number": "500",
          "name": "SE 3rd St"
        },
        "dropoffInstructions": "Ring the bell",
        "formattedAddress": "500 SE 3rd St, Fort Lauderdale, FL, USA"
      },
      "metaSiteId": "6c2384aa-f02f-455d-935e-3a16991d958f",
      "pickupTime": "2022-03-24T01:45:00.000000Z",
      "dropoffTime": "2022-03-24T02:00:27.000000Z",
      "orderTotal": {
        "value": 500,
        "currency": "USD"
      },
      "orderTip": {
        "value": 50,
        "currency": "USD"
      },
      "contactlessDelivery": false
    }
    ```

1. The Local Delivery integration triggers the required flow on its platform, processes the request. Wix expects an object containing the delivery information and a 200 HTTP status code. For example:
    
    ```json
    {
      "id": "00bdf1e1-da4b-45dc-adf2-40c76467822a",
      "pickupWindowStartTime": "2022-03-24T01:45:00.000000Z",
      "pickupWindowEndTime": "2022-03-24T02:00:00.000000Z",
      "dropoffWindowStartTime": "2022-03-24T02:00:00.000000Z",
      "dropoffWindowEndTime": "2022-03-24T02:15:00.000000Z",
      "fee": {
        "value": 50,
        "currency": "USD"
      }
    }
    ```