SortOrder: 0
# About the Wix eCommerce Validations SPI

As a validation service provider, you can integrate your service with Wix's cart and checkout to allow merchants to request and use your services on their Wix sites. By integrating your service with Wix, the validations are performed on the site visitor's cart and checkout.

The integration is done via an app in the Wix App Market (created in the [Wix Developers Center](https://dev.wix.com/)) and the Wix Validations SPI.  

Future functionality includes validating products and orders.

Learn more about [implementing an SPI with Wix](https://dev.wix.com/api/rest/getting-started/service-provider-interface).

## Before you begin

By default, the Validations SPI only validates a site visitor's checkout. If you want to also validate a site visitor's cart, set the `validateInCart` parameter to `true` in the integration component’s configuration file in the Wix Developers Center.

## Use Cases

Using the SPI, you can design your app to validate a cart and checkout for your merchant's customers, including:
+ Minimum cart value.
+ Age of a customer before they proceed to checkout.
+ [Line item quantity limit](https://dev.wix.com/api/rest/wix-ecommerce/validations-integration-spi/sample-flow#wix-ecommerce_validations-integration-spi_sample-flow_validate-a-line-item's-quantity).
+ [Valid coupon code](https://dev.wix.com/api/rest/wix-ecommerce/validations-integration-spi/sample-flow#wix-ecommerce_validations-integration-spi_sample-flow_validate-a-coupon-code-for-a-wix-checkout).
+ Specific items to ship only to specific regions.
+ Restrict purchases to site members only.
+ Close the checkout on certain days. 

## Configuration

To enable Wix to communicate with your app,
[create an integration component](https://dev.wix.com/api/rest/getting-started/service-provider-interface#getting-started_service-provider-interface_configure-an-integration-component-in-the-development-center)
in the Wix Developers Center.
Select the **Ecom Validations** component and provide the following configuration:

| Name | Type | Description |
| --- | --- | --- |
| `baseUri`|object|Required. Base URI which Wix eCommerce will call to retrieve the validation violations.<br/> For example, `"baseUri": { "baseUri": "https://my-validations.com" }` |
| `componentName`|string|A unique name for this component. This is an internal name that will only appear in the Dev Center. |
| `validateInCart`|boolean|Whether to validate the cart page in addition to the checkout page. Default: `false` |

## Terminology

| Term | Definition |
| --- | --- |
| Merchant |Business that offers products on their Wix site to customers. |  
| Severity |How severe the violation is. The violations are shown on the cart and checkout pages. A warning is displayed as yellow, and allows a site visitor to proceed with caution. An error is displayed as red, and doesn't allow a site visitor to proceed with the eCommerce flow. | 
| Subscription Option |A store owner can create [subscriptions]((https://support.wix.com/en/article/wix-stores-selling-product-subscriptions)) to sell their products on a recurring basis. A line item can be a subscription. |  
| Target |Target location on a checkout or cart page where the violation will be displayed. The target violation can either be in a particular `lineItem`, or in an `other` area of the cart or checkout page. |
| Validation Service Provider |A 3rd-party app that implements custom logic to validate the site's cart or checkout.|  
| Violations |A list of any validation violations in a site visitor's cart or checkout. |  
| Wix site owner |The person managing the merchant's Wix site. | 