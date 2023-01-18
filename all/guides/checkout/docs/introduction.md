SortOrder: 0
# About the eCommerce Checkout API

A checkout is created directly, or when a site visitor completes the cart phase of a purchase. Checkouts can also be created, as well as managed via the Checkout API.

A checkout holds information about items to be purchased, price and tax summaries, shipping and billing info, any applied discounts, and more.

To assist in moving from the Stores Cart API to the new eCommerce Checkout API, please refer to the [conversion table](https://dev.wix.com/api/rest/ecommerce/cart/old-cart-to-new-checkout-object-conversion).

## Permissions
A checkout can be created by the following:

### Logged-in Site Member
- `checkout.buyerInfo.memberId` will be set automatically.
- Same logged in site member can access it without permissions check.
- Anonymous visitors and different members will receive NOT_FOUND
- For other identities permissions will be checked (specific permissions depends on endpoint)

### Anonymous Visitor (Not Logged-in)
`checkout.buyerInfo.visitorId` will be set automatically.
- Any anonymous visitor can access it
- Any member can access it which means that after login buyer still can access his checkout.
After checkout first time accessed by member `checkout.buyerInfo.memberId` will be set and "Site member" rules will be applied.
- For other identities permissions will be checked (specific permissions depends on endpoint)

### User/Service/TPA with ECOM.MODIFY_CHECKOUTS permission
Access to checkout will be defined by the identity provided in `checkout.buyerInfo` upon creation.
- If `checkout.buyerInfo.memberId` is set - see [Site member](#site-member)
- If `checkout.buyerInfo.openAccess: true`, checkout can be accessed by everyone. After checkout is first accessed by visitor or member, `checkout.buyerInfo` will be updated and permissions will be applied according to [Site member](#site-member) or [Anonymous visitor](#anonymous-visitor) rules.
- If `checkout.buyerInfo.openAccess: false`, checkout can be accessed only after permissions check. This means that visitors/members cannot access checkout. This is the default behavior when `checkout.buyerInfo` is not set.


## Validations

### Addresses
Relating to `billingInfo` and `shippingInfo.shippingDestination`:
- Either `address.addressLine` or `address.streetAddress` can be provided but not both
- `contactDetails.vatId` is optional but if it is provided,
then `contactDetails.vatId.type` is required.
- In order to be compliant with GDPR we don't save PII data if we don't have clear way to identify owner of it.
It means that addresses can be saved only if:
    - checkout created/update by member (then we will save `buyerInfo.memberId`)
    OR
    - `buyerInfo.email` provided
    OR
    - `buyerInfo.contactId` provided

### Subscription
If `checkout.lineItems.subscriptionOptionInfo` is defined:
- Checkout should have only one line item
- Gift card cannot be applied
- Total price must be greater than 0 (see `checkout.priceSummary.total.amount` property)