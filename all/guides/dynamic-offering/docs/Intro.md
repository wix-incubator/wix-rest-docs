SortOrder: 0
# About the Dynamic Offering API


The Dynamic Offering API allows you to offer your Premium products to customers.

With the Dynamic Offering API you can:
+ retrieve only the relevant Premium products and their display properties
+ display Package Picker and checkout pages to customers

Learn more about setting up Premium products and features with the 
[Premium Product Catalog V2 API](https://dev.wix.com/docs/rest/internal-only/premium/premium-product-catalog-v2/introduction) 
and the [Premium Features Catalog API](https://dev.wix.com/docs/rest/internal-only/premium/premium-feature-catalog/introduction). 
You can use the [Premium Display Manager API](https://dev.wix.com/docs/rest/internal-only/premium/premium-display-manager/introduction) 
to localize text that's shown to customers in the Pakage Picker and checkout pages. 
See the [Features Manager API](https://dev.wix.com/docs/rest/internal-only/premium/premium-features-manager/introduction) 
for more information about enforcing access restrictions for features that you 
want to monetize.


## Terminology


+ __Feature__: Most granular capability or benefit that comes with a product. 
   You can’t sell a feature on its own, it has to be included in a product. 
   Features can be included in multiple different products at the same time.
+ __Product__: Sellable entity, usually consisting of multiple features. Keep 
   in mind that products can also include only a single or even no feature at 
   all. For example, products for features from external (non-Wix) partner 
   programs have no features in the database. Externally, product instances may 
   be called __paid service__ or __Premium Plan__.
+ __Customer__: Wix account or site owner who is purchasing a product.
+ __Purchase Funnel__: Flow that customers navigate to add, upgrade, or change 
   a product. Usually consisting of 3 pages, but you can customize the funnel.
+ __Package Picker__: First page of the purchase funnel. Displays an offering 
   to the customer.
+ __Checkout Page__: Last page of the purchase funnel. Displays the checkout
   to the customer.
+ __Product Type__: Business proposition that you want to monetize. For example, 
   __Premium Plan__, __Ascend__, or __Facebook Ads__.
+ __Product Family__: Different products within the same type are ranked by the 
   amount of benefits they include. For example, __Business Plans__ have the 
   following ranks: __Unlimited__, __VIP__, and __Basic__. A family includes 
   all products of the same rank. This lets you offer localized versions of 
   your product such as __Unlimited (United States)__, __Unlimited (Canada)__, 
   and __Unlimited (UK)__ to your customers. 
+ __Coupon__: With [coupons](https://dev.wix.com/docs/rest/internal-only/premium/coupons-core-service/coupon/coupon-object), 
   you can offer discounts for your customers.
+ __Voucher__: Customers may receive [vouchers](https://dev.wix.com/docs/rest/internal-only/premium/vouchers/introduction) 
   when purchasing a specific Premium product. Vouchers allow customers to get 
   time limited free access to another Wix Premium service or product like purchasing a 
   domain, or an external service such as Google Ads. 
+ __User Offering__: 1 or more products belonging to the same type, that can 
   be displayed together in the package picker.
+ __Quota__: There are 2 usage quotas:
  + The feature’s default free quota specifies how often customers can use the 
      feature free of charge during a specific timeframe.
  + When you include a feature in a product, you’ll be able to set a higher 
      usage quota for customers who have purchased the relevant product.
+ __Display attributes__: Text that's displayed to customers 
   purchasing your product in the Package Picker and checkout pages. This includes product name, 
   description, and other custom attributes. It also sets which attributes are 
   translated and which ones are always displayed in the original language. See the 
   [Premium Display Manager API](https://dev.wix.com/docs/rest/internal-only/premium/premium-display-manager/introduction) 
   for more information.
+ __Display properties__: The actual text values that are displayed to a 
   specific customer in a Package Picker or checkout page. The text is shown 
   as translation based on the customer's location.
+ __Dealer__: Wix Personalization Engine that lets you customize the user 
   experience with personalized suggestions and content. Learn more about the 
   [Dealer](https://wix-marketing.wixanswers.com/en/article/dealer-faqs).
+ __Placement__: Real estate across Wix pages displayed to customers that 
   suggests to purchase a product from your product type.


## Before you begin


+ We strongly recommend that you integrate with the 
   [Dealer](https://wix-marketing.wixanswers.com/en/article/dealer-faqs) before 
   starting to offer your products to customers. This guarantees, that 
   you’ll show only relevant products in the package picker, without having to 
   add your own filtering functionality to your code. You can read more about the 
   [Defining Products in the Dealer](https://bo.wix.com/wix-docs/rest/internal-tools/dealer-offers-serving/introduction).
+ Currently, the [Get User Coupons Type Eligibility endpoint](https://dev.wix.com/docs/rest/internal-only/premium/dynamic-offering/dynamic-offering/get-user-coupons-type-eligibility) 
   only retrieves 1-year vouchers for domains, in case the customer purchases a 
   Premium Plan. You can't use it to retrieve other vouchers yet.


## Best practice for the initial setup


1. Integrate with the [Dealer](https://wix-marketing.wixanswers.com/en/article/dealer-faqs)
1. Ask the funnel team to duplicate one of your placements in 
   [Premium Offerings Location](https://bo.wix.com/dealer/placements?location=Premium%20Offerings). 
   Choose your product type as name.
1. Contact the Premium Services Operations mangers at 
   [#premium-services](https://wix.slack.com/archives/C0E7B6VC7/p1658063197730769) 
   to link the new placement to your product type.
1. In your new placement: Create an offering with all relevant product IDs 
   that will be displayed in the Package Picker.
1. Optional, but highly recommended when you want to offer sales or discounts:  
   Create another placement for special offerings such as discounts under 
   __Premium Sales Location__. It is easier to duplicate the relevant existing 
   placement and then rename it according to your product type.

