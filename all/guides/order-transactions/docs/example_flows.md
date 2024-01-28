SortOrder: 1
# Sample Use Case & Flow: Order Transactions

This article shares a possible use case your app could support, as well as an example flow. You're certainly not limited to this use case, but it can be a helpful jumping off point as you plan your app's implementation.

## Retrieve transactions related eCommerce orders

Your app can retrieve details about payments and refunds associated with an order. For example, you can check for payments that were made by credit-card, payments made by gift card, or orders that were not successfully refunded.

To retrieve info about an order's transactions:

1. Call [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) with an [eCommerce order ID](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/introduction).
    * To retrieve transaction details about more than 1 order, call [List Transactions For Multiple Orders](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-multiple-orders) with an array of [eCommerce order IDs](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/introduction).
2. You can use the returned info to check payment and refund details in the relevant provider or gateway systems, pass the details on to your accounting or invoice apps, and more.

## Add payment records to imported orders

If you are importing orders from other systems, you may want to add payment records to those orders. To add a payment record to an order that is already in the eCommerce system:

1. Once you have the order ID, pass it to the [Add Payments](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/add-payments) endpoint.
2. In the body params, pass payment details like the `createdDate`, `amount`, `paymentMethod`, and any other payment details.
3. When using [Add Payments](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/add-payments) you can add up to 50 payment records to a single order with 1 API call.