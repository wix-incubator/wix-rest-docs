SortOrder: 1
# Checkout Templates: Sample Use Case & Flow
This article shares some possible use cases your app could support, as well as an sample flow that could support each
use case. This can be a helpful jumping off point as you plan your app's implementation.

## Run a flash sale through social media
Offer a sale to customers through social media channels that runs for a limited time only. Create the checkout template and pull the URL to automatically redirect anyone that clicks on the link to a checkout page with the offer. When the period for the sale is complete, update the checkout template's `status` to `INACTIVE` to turn it off.

To create and share the offer:

1. Use [Create Checkout Template](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/checkout-templates/create-checkout-template) with the product and coupon information for offer.
2. Use the `checkoutTemplateId` to build the URL to share with customers. Build the URL in this format: `https://www.wixapis.com/ecom/v1/checkout-templates/{checkoutTemplateId}/create-and-redirect-to-checkout?siteId={siteId}`.
3. Post and share the URL to customers.

To turn off the offer at the end of the sale:

1. Use [Update Checkout Template](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/checkout-templates/update-checkout-template) to update `checkoutTemplate.status` to `INACTIVE`.

## Limit the number of checkouts for a specific coupon
Offer a sale to the first 100 customers that click on an offer. Create a checkout template, then share your own custom link that will run custom logic before creating a new checkout for the customer.

Create a checkout template and add your own custom logic:

1. Use [Create Checkout Template](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/checkout-templates/create-checkout-template) with the product and coupon information for offer.
2. Create a bank of all new checkouts for this sale by collecting the `checkoutId`s of checkouts created from this `checkoutTemplateId`.
3. Before a new checkout is created with the `checkoutTemplateId`, check the bank and count the number of `checkoutId`s being stored.
4. Once the count hits `100` checkouts, use [Update Checkout Template](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/checkout-templates/update-checkout-template) to update `checkoutTemplate.status` to `INACTIVE`.
