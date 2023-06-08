SortOrder: 1
# Order Fulfillments: Sample Use Cases & Flows

This article shares a possible use case your app could support, as well as
a sample flow that could support the use case. This can be a helpful jumping
off point as you plan your app's implementation.

## Create a fulfillment for a new order

You can use webhooks to listen for when an order is placed, and then create a fulfillment for the new order.

1. Use the [Order Approved Webhook](https://dev.wix.com/api/rest/wix-ecommerce/orders/order-approved-webhook) to listen for incoming approved orders.
2. When a new order comes in, save the order ID. This can be found as the value of the `entityId` or `actionEvent.body.order.id` fields in the [Order Approved Webhook's](https://dev.wix.com/api/rest/wix-ecommerce/orders/order-approved-webhook) payload.

3. Pass the new order ID and the new fulfillment info to the [Create Fulfillment](https://dev.wix.com/api/rest/wix-ecommerce/order-fulfillments/create-fulfillment) endpoint.
The response holds information about the newly created fulfillment and the ID of its associated order.
