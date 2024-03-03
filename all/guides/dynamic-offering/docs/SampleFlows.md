SortOrder: 1
# Sample Flows


This article shares possible use cases your implementation could support, as 
well as sample flows. You're certainly not limited to these use cases, but it 
can be a helpful jumping off point for your planing.


## Setup flow


You can follow this flow to integrate your business proposition with the 
Premium Product Catalog. This allows your customers to later purchase your 
products. Alternatively, you can use the 
[Premium Platform Backoffice](https://dev.wix.com/docs/rest/internal-only/premium/premium-product-catalog-v2/backoffice-tutorial) 
to set up your product type, families, products, and features. Then, you could 
set up your Package Picker and checkout page.

1. Call the 
   [Create Product Type](https://dev.wix.com/docs/rest/internal-only/premium/premium-product-catalog-v2/product-types/create-product-type) 
   endpoint of the Premium Product Catalog V2 API. It's required to create the 
   type first, before you can create your product, because every product must 
   belong to a type.
1. Optional: In case you want to group your products into families, call the 
   [Create Product Family](https://dev.wix.com/docs/rest/internal-only/premium/premium-product-catalog-v2/product-families/create-product-family) 
   endpoint of the Premium Product Catalog V2 API.
1. Use the 
   [Create Feature](https://dev.wix.com/docs/rest/internal-only/premium/premium-feature-catalog/create-feature) 
   endpoint of the Premium Feature Catalog V2 API to set up your features. You 
   need to call the endpoint once for every feature.
1. Call the [Create Product](https://dev.wix.com/docs/rest/internal-only/premium/premium-product-catalog-v2/products/create-product) 
   endpoint of the Premium Product Catalog V2 API. You need to call the 
   endpoint once for every product.
1. Set up display attributes for all your entities, by calling the 
   [Create Display Attributes](https://dev.wix.com/docs/rest/internal-only/premium/premium-display-manager/translatable-content/attributes-v2/create-display-attributes) 
   endpoint of the Premium Display Manager API. You need to call this endpoint 
   once for every feature, product, product type, and user offering. 
   Currently, you can't create display attributes in the Premium Platform 
   Backoffice. 
1. Set up the translations for your display attributes. To do so, call the 
   [Create Bulk Translatable Content](https://dev.wix.com/docs/rest/internal-only/premium/premium-display-manager/translatable-content/translatable-content-v2/create-bulk-translatable-content) 
   endpoint of the Premium Display Manager API. You only need to call the 
   endpoint once, to set up all translations.
1. Set up your Package Picker page.
1. Set up your checkout page. To do so, 
   [configure the page's components](https://github.com/wix-private/checkout-components/tree/master/packages/checkout-components)
   and [configure the page itself](https://github.com/wix-private/premium-purchase/tree/master/packages/dynamic-offering-checkout-page). 


## Display flow


This flow lets you display your offerings to site owners. You need to 
[set up your products](https://dev.wix.com/docs/rest/internal-only/premium/dynamic-offering/sample-flows#setup-flow) 
first before your customers can purchase them.

1. Optional: If you need, call 
   [Get Product Info](https://dev.wix.com/docs/rest/internal-only/premium/dynamic-offering/dynamic-offering/get-product-info) 
   to check your product’s configuration.  
   > __Note:__ The response of __Get Product Info__ includes details about the 
   > pricing. In contrast 
   > [Get Product](https://dev.wix.com/docs/rest/internal-only/premium/premium-product-catalog-v2/products/get-product) 
   > doesn’t return pricing details but instead information about coupons and 
   > vouchers associated with the product. Both endpoints return the features 
   > included in the product.
1. Call the [Get User Offering](https://dev.wix.com/docs/rest/internal-only/premium/dynamic-offering/dynamic-offering/get-user-offering) 
   endpoint. This returns all `active` products of your product type that the 
   given user can purchase. Including enriched information about supported 
   currencies, tax settings, features, and more.
   > __Note__: In case you haven’t integrated with the 
   > [dealer](https://wix-marketing.wixanswers.com/en/article/dealer-faqs), the 
   > endpoint returns all `PUBLISHED` products of the given product type. Then, 
   > you’ll need to add your own filtering before populating the package picker. 
   > This is especially important, if you add new products to a specific product 
   > type. You can reach out to the Dealer team on 
   > [Slack](https://wix.slack.com/archives/C9FFLTB63) to get more info.
1. Use the [Create Order Page](https://dev.wix.com/docs/rest/internal-only/premium/dynamic-offering/dynamic-offering/create-order-page) 
   endpoint to generate the `orderSessionId` and `riskIframeUrl` for your order 
   page.
1. Generate and display a post purchase success page to the customer.
