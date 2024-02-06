SortOrder: 0
# About the Wix eCommerce Additional Fees SPI

As an additional fees calculation service provider, you can integrate your service with Wix to allow merchants to request and use your services on their Wix sites.
By integrating your service with Wix, the additional fees are then included on the site's cart and checkout pages.  

The integration is done via an app in the Wix App Market (created in the [Wix Developers Center](https://dev.wix.com/)) and the Wix Additional Fees SPI.  

Using the SPI, you can design your app to calculate various additional fees for your merchant's customers, including:
+ Fragile packaging fees
+ Shipping insurance fees
+ Item warranty fees
+ Gift wrapping fees
+ Carbon offset fees

Learn more about [implementing an SPI with Wix](https://dev.wix.com/api/rest/getting-started/service-provider-interface).


## Before you begin

It's important to note that when Wix calls your implementation of the [Calculate Additional Fees](https://dev.wix.com/api/rest/wix-ecommerce/additional-fees-integration-spi/calculate-additional-fees) SPI endpoint, the app must return fees in the same currency as the Wix site. Extract the `currency` for a site from the [request envelope](https://dev.wix.com/api/rest/getting-started/service-provider-interface#getting-started_service-provider-interface_request-envelope) to ensure the correct currency is used in your calculation.


## Terminology

+ __Calculate additional fees__: Wix calls [this SPI endpoint](https://dev.wix.com/api/rest/wix-ecommerce/additional-fees-integration-spi/calculate-additional-fees) to retrieve the various additional fees you calculate.
+ __Line items__: Line items to calculate additional fees for. For more information, see [eCommerce Integration in Wix Stores Catalog](https://dev.wix.com/api/rest/wix-stores/catalog/ecommerce-integration).
+ __Site owner__: The person managing the merchant's Wix site.


## Prerequisites

Follow these steps to customize Wix system's integration and enable merchants and their customers to access your additional fees calculations.

1. Create an [app](https://dev.wix.com/dc3/my-apps/) and retrieve its app ID either from the URL or as displayed in the My Apps dashboard in the [Wix Developers Center](https://dev.wix.com/).

    ![Sample App ID](https://s3.amazonaws.com/wixplorer-readme-images/additional-fees-integration-spi%2FAddFeesAppId.png "Sample App ID")

1. Go to the [Extensions](https://dev.wix.com/docs/build-apps/developer-tools/extensions/about-extensions) tab in the Wix Developers Center.
1. Click **Create Extension** in the top right.
1. Filter by **eCommerce** in the left menu, then find **Ecom Additional Fees** and click **Create**.
1. Use the JSON editor to create the extension's configuration file. Take care to include the required fields noted in the table below. Click **Save**.

    | Name | Type | Description |
    | --- | --- | --- |
    | `deploymentUri`|string|Required. Base URI where the endpoints are called. Wix eCommerce appends the endpoint path to the base URI. For example, to call the Calculate Additional Fees endpoint at `https://my-additional-fees.com/v1/calculateAdditionalFees`, the base URI you provide here is `https://my-additional-fees.com/`. |
    | `componentName`|string|A unique name for this component. This is an internal name that will only appear in the Dev Center. |

1. Click [**Test Your App**](https://devforum.wix.com/kb/en/article/how-to-test-your-app-on-a-free-premium-development-site).
