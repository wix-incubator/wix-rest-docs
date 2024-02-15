SortOrder: 1
# eCommerce Orders: Sample Use Cases and Flows

This article shares some possible use cases your app could support, as well as
a sample flow that could support each use case. This can be a helpful jumping
off point as you plan your app's implementation.

## Using an order ID across different eCommerce APIs

Some eCommerce functionality is accessible by using an order's ID and passing it to other eCommerce APIs. Here are a few examples:

+ To retrieve transaction details for one or more orders, pass the order IDs to [List Transactions For Multiple Orders](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-multiple-orders).
+ To add a record of payment, pass the order ID and payment details to [Add Payments](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/add-payments).
+ To modify an order's payment status, pass its ID along with the relevant payment's ID to [Update Payment Status](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/update-payment-status). To modify up to 300 orders at once, pass their IDs along with the relevant payment IDs to [Bulk Update Payment Statuses](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/bulk-update-payment-statuses).
+ To retrieve fulfillment details of up to 100 orders at once, pass the order IDs to [List Fulfillments For Multiple Orders](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-fulfillments/list-fulfillments-for-multiple-orders).

## Record an external order

When an order is made on an external system, you may want to record it and its payment details on your app.

To record an external order:

1. Call [Create Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/create-order) and pass all the details of the external order.
2. Save the order `id` from the Create Order API's response.
3. Pass the order `id`, along with the external order's payments details, to [Add Payments](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/add-payments). This will add a record of the payment associated with the order.


