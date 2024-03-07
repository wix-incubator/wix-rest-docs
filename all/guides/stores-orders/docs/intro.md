SortOrder: 0
# Orders Service

<blockquote class='warning'>

__Deprecation Notice:__

Stores Orders API has been replaced with
[eCommerce Orders API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/introduction)
and will be removed on September 4, 2024.

Learn more about [migrating from Wix Stores to Wix eCommerce](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-object-conversion).

</blockquote>

## About This API

Stores Orders API allows third party apps to create and manage orders for Wix store owners.

Use this API to:
1. Query the orders in the store
2. Get a specific order
3. Get notifications (via webhook) about new orders
4. Create and update orders

## Order Types

- **Shipping orders**: Order and shipment of any selection of products from the store's catalog.

- **Pickup orders**: Order of any selection of products from the store's catalog for user pickup.

- **Point of Sale (POS) orders**: Sale consisting only of price and partial billing information, of products not included in the store's catalog.
