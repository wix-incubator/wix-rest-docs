SortOrder: 1
# Sample Use Case & Flow: Wix Restaurants Orders

This article shares a possible use case your app could support, as well as an example flow. 
You're certainly not limited to this use case, but it can be a helpful jumping off point 
as you plan your app's implementation.

## Sync Orders Placed on Wix Restaurants with an External POS

In order to enable site owners to sync their external POS with Wix Restaurants Orders 
data, your app will need to retrieve each new order that is placed in Wix Restaurants. 
Then you can create a mapping to keep the order statuses synced.  


1. Sign up for the [Order Created Domain Event](https://dev.wix.com/api/rest/wix-restaurants/orders/order-created-domain-event).
2. Create a mapping between Wix Restaurants and the external POS. Store the mapping on your servers.
3. Get notified when a new order has been placed on Wix Restaurants and add it to the mapping.
4. Add the order to the external POS.

    > **Note:** Make sure to include both Wix Restaurants `orderId` and external order ID in the mapping.
5. Change the order status on Wix Restaurants according to events in the external POS. Use the [Accept Order](https://dev.wix.com/api/rest/wix-restaurants/orders/accept-order), [Fulfill Order](https://dev.wix.com/api/rest/wix-restaurants/orders/fulfill-order), and [Cancel Order](https://dev.wix.com/api/rest/wix-restaurants/orders/cancel-order) endpoints.