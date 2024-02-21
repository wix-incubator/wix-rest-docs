SortOrder: 0
# About Subscription Options

Wix site owners can create subscriptions to sell their products on a recurring basis. With the Subscription Options API, you can integrate with the store owner's subscriptions in their Wix store to create, delete, get, check and query the site owner's subscriptions.

<blockquote class='warning'>

__Deprecation Notice:__

Subscription Options API has been deprecated and will be removed on January 29, 2024.

</blockquote>

## Subscription frequency and duration

Wix supports the following frequencies and durations of subscriptions:
- Every day for X days
- Every week for X weeks
- Every month for X months
- Every year for X years

## Subscription Settings

- `frequency` - How often the payment will be made/product will be provided as part of the subscription. Supported frequencies: daily, weekly, monthly, yearly.
- `billingCycle` - Number of billing cycles before subscription ends.
- `autoRenewal` - Allow for automatic renewal of a subscription at the end of its specified period. Can only be used if billingCycle is empty.

## Subscription Pricing

Each subscription option has a separate price that is set through a discount on the product’s price.
For example, a coffee bag can be sold for $20 as a regular one-time purchase.
However, with a monthly subscription (1 coffee bag per month) for 3 months the price of the coffee bag could be $18 per bag/month, and with a longer subscription of 12 months sold for $15 per bag/month.

## Current Limitations

The following list contains currently unavailable functionality:

- Providing/delivering a product X times per week/month/year (for example, 3 times a month).
- Suspending a subscription.
- Skipping a cycle.
- Applying the same subscriptions to multiple different products in bulk.
- Extending subscriptions (adding more billing cycles to an active subscription).
- Creating a subscription from the whole cart.
- Coupons on X first payments of a subscription.
- Adding a subscription to a cart. Currently the subscription goes straight to checkout, similar to using ‘buy now’.
