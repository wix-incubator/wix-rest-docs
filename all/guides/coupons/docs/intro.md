SortOrder: 0
# Coupons

## About This API
Wix site owners can create coupons to provide their customers with discounts on the products, bookings, or events on their site.
With the Coupons API you can integrate with the Wix site owner's coupon management to create, delete, get, check and query the site owner's coupons.

## Checking for Installed Apps

To use the Coupons API, the user's site must have a valid app installed.
In the response to the [Get App Instance](https://dev.wix.com/api/rest/app-management/apps/app-instance/get-app-instance) endpoint, check the `site.installedWixApps` array for the following values:
+ `stores`
+ `bookings`
+ `events`

## Coupon Types
Wix supports the following types of coupons:
* *$ discount* - a.k.a. moneyOff, a fixed discount amount
* *% discount* - a.k.a. percentOff, a discount as a % (e.g., 20% off)
* *Free Shipping* - free shipping
* *Sale Price* - a.k.a. fixedPrice, a fixed sale price
* *Buy X Get Y* - get a certain number/kind of product for free (Y) when a customer buys a minimum number/kind of items (X). Both X and Y items must be in the customer's cart at time of purchase

## Usage Limits
Coupons can be limited to:

- 1 item per order
- Minimum subtotal
- X number of uses in total (all purchases by all customers, including repeat uses by the same customer)
