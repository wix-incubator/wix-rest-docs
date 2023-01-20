SortOrder: 0
# About the eCommerce Orders API

An order is the last stage of the eCommerce purchase flow: cart; checkout; order.

The order holds information about purchased items, price and tax summaries, shipping and billing info, any applied
discounts, payment and fulfillment statuses, and more.

The eCommerce Orders API currently provides functionality for [retrieving](https://dev.wix.com/api/rest/ecommerce/orders/get-order) orders and listening to events when an order is [approved](https://dev.wix.com/api/rest/ecommerce/orders/order-approved-webhook), [updated](https://dev.wix.com/api/rest/ecommerce/orders/order-updated-webhook), [canceled](https://dev.wix.com/api/rest/ecommerce/orders/order-canceled-webhook), and more.

To assist in migration from the Stores to eCommerce APIs, please refer to the [Stores to eCommerce Order Object Conversion Table](https://dev.wix.com/api/rest/ecommerce/orders/order-object-conversion).

Future functionality includes creating and managing orders, managing orders' fulfillments, and retrieving orders' transactions.