SortOrder: 0
# About the eCommerce Orders API

The eCommerce Orders API allows apps or site owners to customize management of the order lifecycle, including viewing, updating, and canceling. In the dashboard, business staff can create new orders, view and edit existing orders, track fulfillment, and manage the payments cycle.

An order holds information about purchased items, price and tax summaries, shipping and billing information, any applied discounts, and the status of payment and fulfillment.

With the eCommerce Orders API you can:

* [Get](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/get-order) and [search](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/search-orders) for orders.
* [Update](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/update-order) and [cancel](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/cancel-order) an order.
* [Create](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/create-order) an order for your records.
* Listen to events when an order is [approved](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-approved), [updated](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-updated), or [canceled](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-canceled).
* Listen to events when an order's [transactions are updated](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/order-transactions-updated). This event is part of the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).


## Before you begin

If you are migrating from the Stores Orders API, please refer to the following conversion tables:
+ Stores to eCommerce [Order Object Conversion Table](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-object-conversion).
+ Stores to eCommerce [Webhook Conversion Table](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-object-conversion#webhook-conversion-table).
