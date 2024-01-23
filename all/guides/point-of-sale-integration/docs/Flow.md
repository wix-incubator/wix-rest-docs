SortOrder: 2
# Flows

This article presents some sample flows your app can support. You aren't limited to these exact flows, but they can be a helpful jumping off point as you plan your POS integration.

+ [Location connection and synchronization flow](#location-connection-and-synchronization-flow)
+ [Order creation flow](#order-creation-flow)

## Location connection and synchronization flow
This flow demonstrates a possible flow for checking the connection between Wix location configurations and the corresponding locations in the POS system, and for synchronizing the Wix catalogs with the POS menus. 

+ [Initial setup](#initial-setup)
+ [Listing accounts](#listing-accounts)
+ [Listing configurations for locations](#listing-configurations-for-locations)
+ [Checking configuration status](#checking-configuration-status)
+ [Starting catalog (menu) synchronization](#starting-catalog-menu-synchronization)
+ [Checking synchronization status](#checking-synchronization-status)

### Initial setup

A site owner installs and authorizes your app for you, the POS service provider, on a merchant’s Wix site. The app collects the JSON Web Token (JWT), decodes it, and stores the resulting instance ID.

For example, the token in this request: (???)

```bash
$ curl -X POST https://ext-server.com/wix-spi/account-ids
-H 'Content-Type: plain/text'
-d 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbnN0YW5jZUlkIjoiMDQ0NjY3ZjQtYzEzZi00NmMyLTg1MDYtZGU5ZTQyMjkzODk2In0.fxedHrnHUFi6V-S5OH8gL-pY4STxFWZHjj-xo9QUwQY'
```

Decodes into:

```json
{ "instanceId": "044667f4-c13f-46c2-8506-de9e42293896" }
```

### Listing accounts

The first step is to retrieve a list of accounts that the merchant has with the POS system. Wix sends a [List Account IDs](https://dev.wix.com/api/rest/wix-restaurants/point-of-sale-integration/pos-integration-spi/list-account-ids) SPI call to the POS service provider.

Wix expects an array of the IDs for  all valid, active accounts between the merchant and the POS system and a 200 HTTP status code. For example:

```json
{
"accountIds" :[
    "03cabfd0-e8aa-496d-a411-baf4275811d5",
    "04b5b58a-a803-477b-81a5-cced1534dd1e",
    "0d79528d-46e7-4b29-bdb1-145876c4ef9d"
  ]
}
``` 

### Listing configurations for locations

When your POS Integration dashboard page is loaded, the Wix site displays the updated information for all locations with the [List Configurations](https://dev.wix.com/api/rest/wix-restaurants/point-of-sale-integration/pos-connectivity-api/list-configurations) API. The configuration information can be used later, such as:

+ When checking the status of a specific location.
+ On a site page, so a customer can select an active location when creating an order.

Wix retrieves an array of the location configurations defined for the merchant (regardless of their operational status with the POS system) and a 200 HTTP status code. For example:

```json
{
"configurations": [
    "id": "04b5b58a-a803-477b-81a5-cced1534dd1e",
    "location": [
        (???)
    ]
    "catalogId": "06c5c7sa-a803-477b-81a5-cced1534dd1e",
    "archived": false,
    "enabled": true,
    "integrationSettingsUrl": "https://(???)"
  ]
  [
    "id": "1212c11ea-a803-477b-81a5-cced1534dd1e",
    "location": [
        (???)
    ]
    "catalogId": "06c5c7sa-a803-477b-81a5-cced1534dd1e",
    "archived": false,
    "enabled": true,
    "integrationSettingsUrl": "https://(???)"
  ]
}
```

### Checking configuration status

To check the location configuration’s status with the POS system, Wix sends a [Get Configuration Status](https://dev.wix.com/api/rest/wix-restaurants/point-of-sale-integration/pos-connectivity-api/get-configuration-status) SPI call to your app to get the status of a specific configuration location with an object like this:

```json
{
  "accountId": "03cabfd0-e8aa-496d-a411-baf4275811d5", 
  "configurationId": "04b5b58a-a803-477b-81a5-cced1534dd1e"
}
```

Wix expects a string containing the operational status for the configuration and a 200 HTTP status code. For example:

```json
{ "status": "READY"  }
```

The possible values for the status property are:

+ `NOT_STARTED`. Your app is installed but not yet authenticated. 
+ `PENDING`. The app is authenticated but the location is not yet ready. For example, the Wix configuration location might not yet be connected to the POS location.
+ `READY`. The location is ready. POS integration can be activated for this location and ordering is possible.
+ `ERROR`. An error occurred.

If a configuration’s status is `READY`, POS operations can be processed for that location. Otherwise, the business cannot activate the POS integration for this location.

The Wix site displays the updated information for all locations on the Configurations  (???) dashboard page. The information from this page is displayed on a site page so the customer can select an active location from a list.

### Starting catalog (menu) synchronization

Wix sends a [Sync Catalog](https://dev.wix.com/api/rest/wix-restaurants/point-of-sale-integration/pos-integration-spi/sync-catalog) SPI call to your app to start synchronizing the Wix catalogs and the POS system’s menus. This is an asynchronous operation that returns an empty object. 

Synchronization is triggered when (???).

### Checking synchronization status

Wix sends a [Get Catalog Sync Status](https://dev.wix.com/api/rest/wix-restaurants/point-of-sale-integration/pos-integration-spi/get-catalog-sync-status) SPI call to your app to get the status of a synchronization between a Wix catalog and a POS system’s menu for a specific location.

Wix expects a `status` object (containing additional details) and a 200 HTTP status code. For example:

```json
{
    "status": "IN_PROGRESS",
    "inProgress": [
      "elapsedSeconds": 145
    ]
}
```

## Order Creation Flow

To create an order, the customer logs on to the merchant’s Wix site and chooses a location configuration at which to place the order. The order is validated and created on the POS system.

+ [Connecting and synchronizing configurations](#connecting-and-synchronizing-configurations)
+ [Validating the order](#validating-the-order)
+ [Placing the order](#placing-the-order)
+ [Updating inventory](#updating-inventory)

### Connecting and synchronizing configurations

On a regular basis, and also when a customer starts to place an order, make sure that: 

+ The account between the merchant and the POS system is active. 
+ Wix configurations are connected to their corresponding POS locations. 
+ Menus are synchronized. 

See [Location connection and synchronization](#location-connection-and-synchronization-flow) flow for a sample flow.

### Validating the order 

Before letting the customer place an order on a POS system, Wix sends the account ID, configuration ID, and the order for validation to your app with a [Validate Order](https://dev.wix.com/api/rest/wix-restaurants/point-of-sale-integration/pos-integration-spi/validate-order) SPI call. 

```json
{
    "accountId": "70a8b23f-c977-443f-9030-cf8add9ddbf3",
    "configurationId": "1caf5d2f-df70-43eb-8779-39200d32b117",
    "order": { ??? }
}
```

Wix expects in response a `posOrderStatus` string and a 200 HTTP status code. The statuses that can be returned vary for each POS system. Make sure you let the site owner know which statuses indicate success.

### Placing the order

To enable the customer to place an order on a POS system, Wix sends the order when the customer checks out with the [Create Order](https://dev.wix.com/api/rest/wix-restaurants/point-of-sale-integration/pos-integration-spi/create-order) SPI call, after first validating the order for errors with the [Validate Order](https://dev.wix.com/api/rest/wix-restaurants/point-of-sale-integration/pos-integration-spi/validate-order) SPI call. 

Wix expects to receive a POS order status and a 200 HTTP status code.

```json
{
   "posOrderStatus": "valid"
}
```

### Updating inventory

When the customer places an order, the app can update inventory counts using webhooks. This can prevent customers ordering on the Wix site from placing orders for out-of-stock items.