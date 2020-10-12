SortOrder: 0
# Orders Service

## About This API

Stores Orders allows third party apps to manage orders for Wix store owners.

Use this API to:
1. Query the orders in the store
2. Get a specific order
3. Get notifications (via webhook) about new orders

*Note: Write operations are not supported at this time*

## Permissions

The API requires `WIX_STORES.READ_ORDERS`

## Order Types

**Shipping orders**: Order and shipment of any selection of products from the store's catalog.  
**Pickup orders**: Order of any selection of products from the store's catalog for user pickup.  
**Point of Sale (POS) orders**: Sale consisting only of price and partial billing information, of products not included in the store's catalog.


## Error handling
| Status code | Description |
| --- | --- |
| 200 |Success|
| 400 |Invalid input|
| 401 |Invalid authorization token, or Wix stores is not installed|
| 404 |Requested order is not found|
| 500 |Unexpected error|
