SortOrder: 1
# Checkout Settings: Sample Use Cases & Flows

This article presents possible use cases and corresponding sample flows that your app can support. It provides a useful starting point as you plan your app's implementation. 

## Update checkout settings across all sites

If you have several Wix eCommerce sites that use your app you might need to sync checkout settings across those sites. For example, if the return policies change on 1 site, and now the policies guarantee a 100-day item return, this change also needs to be reflected on other sites.

To update the checkout policy settings across all sites:

1. Call [Get Checkout Settings](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/settings/checkout-settings/get-checkout-settings) on the site where you updated the policy.
1. Extract the `checkoutPolicies.returnPolicy.content` field value.
1. Call [Update Checkout Settings](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/settings/checkout-settings/update-checkout-settings) for your other sites and pass the new policy to each.