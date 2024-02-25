SortOrder: 1
# Orders Settings: Sample Use Cases and Flows

This article presents possible use cases and corresponding sample flows that your app can support. It provides a useful starting point as you plan your app's implementation. 

## Update orders settings across all sites

If you have several Wix eCommerce sites that use your app you might need to apply the same orders settings to those sites. For example, if now the store inventory is updated only after an order is paid, this change also needs to be reflected on other sites.

To update the orders settings across all sites:

1. Call [Get Orders Settings](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/settings/orders-settings/get-orders-settings) on the site where you updated the settings.
1. Extract the `inventoryUpdateTrigger` field value.
1. Call [Update Orders Settings](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/settings/orders-settings/update-orders-settings) for your other sites and pass the new settings to each.

