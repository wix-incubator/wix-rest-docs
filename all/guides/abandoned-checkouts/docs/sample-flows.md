SortOrder: 1
# Abandoned Checkouts: Sample Use Case & Flow 

This article shares some possible use cases your app could support, as well as an example flow that could support each
use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your
app's implementation.

## Redirect a site visitor with an abandoned checkout back to their checkout page

If a site visitor starts a checkout but doesn't complete it, you can redirect them to their checkout page. You can also check whether the site visitor has recovered their abandoned checkout and completed the purchase. 

To redirect the site visitor to their checkout page:

1. Using the [Abandoned Checkout Created Webhook](https://dev.wix.com/api/rest/wix-ecommerce/abandoned-checkouts/abandoned-checkout-created-webhook), listen for an event when an abandoned checkout is created (a checkout was not completed).

2. Save the newly created abandoned checkout's ID (`entityId` field) and `checkoutUrl` from the above webhook's payload. Then send a marketing campaign with the `checkoutURL` to your site visitor, redirecting them to their checkout page.

3. After the marketing campaign, call [Get Abandoned Checkout](https://dev.wix.com/api/rest/wix-ecommerce/abandoned-checkouts/get-abandoned-checkout) with the abandoned checkout's ID. Then check the `status` field in the response to see if the abandoned checkout has been recovered.

