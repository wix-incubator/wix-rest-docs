SortOrder: 0
# About the Coupons API

Wix site owners can create coupons to offer their customers discounts for products on their site.  

With the Coupons API, you can manage a site's coupons.  

## Checking for Installed Apps

To use the Coupons API, the user's site must have a valid app installed.
In the response to the [Get App Instance](https://dev.wix.com/api/rest/app-management/apps/app-instance/get-app-instance) endpoint, check the `site.installedWixApps` array for the following values:
+ `stores`
+ `bookings`
+ `events`
+ `pricingPlans`

## Coupon Types
Wix supports the following types of coupons:
* *$ discount* - a.k.a. `moneyOffAmount`, a fixed discount amount
* *% discount* - a.k.a. `percentOffAmount`, a discount as a % (e.g., 20% off)
* *Free Shipping* - free shipping
* *Sale Price* - a.k.a. `fixedPrice`, a fixed sale price
* *Buy X Get Y* - purchase one or more of a specified product (X), and get one or more additional products (Y) for free. Both X and Y can be defined either as specified products or as a specified collection of products. All items must be in the customer's cart at time of purchase.


## Usage Limits
Coupons can be limited to:

- 1 item per order
- Minimum subtotal
- X number of uses in total (all purchases by all customers, including repeat uses by the same customer)
