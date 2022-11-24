# About Wix Coupons  
Wix site owners can [create and manage coupons](https://support.wix.com/en/wix-stores/managing-coupons) to provide their customers with discounts on the products on their site.  

With the Coupons API, you can integrate with the site owner's coupon management in their Wix site to manage the site's coupons.  

## Before you begin
- Each coupon must include a scope, including a namespace. To get a list of relevant namespaces for a specific site, [check for installed apps](https://dev.wix.com/api/rest/coupons/coupons/introduction#coupons_coupons_introduction_checking-for-installed-apps).
- At the current time, there is no way to receive notifications about  site owner actions that affect the viability of the coupons you create (e.g., deleting a product for which your platform has an active coupon).  
- Get familiar with the [Wix coupons functionality](https://dev.wix.com/api/rest/coupons/coupons/functionality).


## Terminology

- **Scope**: Details about [what the coupon should be applied to](https://dev.wix.com/api/rest/coupons/coupons/valid-scope-values).
   - **Namespace**: The Wix app that the coupon should be applied to.
   - **Group**: The type of product/service/event, within the Wix app, that the coupon should be applied to.
   - **Entity ID**: The specific product, service, or event ID that the coupon should be applied to.
