SortOrder: 5
# About the Orders API

With Orders, you can manage orders and create offline orders. You can also change access to content on Wix or external apps upon plan purchase or cancellation.

The Orders API allows your app to:
- Create an offline order.
- Preview an order to show price, tax, and other details.
- Extend an order's duration or cancel an order.
- Pause and resume an order.


## Terminology
- **Order:** A purchase of a subscription to a Pricing Plan. The order details include price, duration, and billing schedule information. Orders can be free. Orders can also be partially free using free trial days.
- **Offline Order:** A purchase of a subscription to a Pricing Plan where the payment isn't handled via Wix. This type of order can be created via API.
- **Online Order:** A purchase of a subscription to a Pricing Plan where the payment is handled via Wix. This type of order can't be created via API.
- **Buyer:** A customer.

## Limitations
- This API supports creating offline orders only. Pricing plan orders created via API can't be paid for using the Wix Payment system.
- The application of tax to orders is defined at the site level, and isn't accessible via API. If site owners need to collect tax, they must [set up tax collection manually](https://support.wix.com/en/article/pricing-plans-setting-up-tax-collection).