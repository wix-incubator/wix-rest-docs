SortOrder: 0
# About the Wix eCommerce Shipping Rates SPI

As a shipping provider, you can integrate your shipping rates service with Wix to allow a merchants' stores or businesses to request and use your shipping services on their Wix sites.
The shipping rates are then displayed on the site's cart and checkout pages.

The integration is done via an app in the Wix App Market (created in the [Wix Developers Center](https://dev.wix.com/)) and the Wix Shipping Rates SPI.

Using the SPI, you can design your app to:
+ Provide shipping estimates, including fees and times.
+ Provide shipping rates using your own custom logic.
+ Provide services for delivery and pickup.

Learn more about [implementing an SPI with Wix](https://dev.wix.com/api/rest/getting-started/service-provider-interface).

## Terminology


+ __Get Shipping Rates__: Wix calls [this SPI endpoint](https://dev.wix.com/api/rest/wix-ecommerce/shipping-rates-integration-spi/get-shipping-rates) to retrieve the shipping rates you provide.
+ __Merchant__: Business that offers products on their Wix site to customers.
+ __Wix site owner__: The person managing the merchant's Wix site.
+ __Shipping Rates Provider__: A 3rd-party app that implements custom logic to calculate shipping rates. 

## Prerequisites

Complete the following steps to adapt Wix system's integration to make your shipping rates available to merchants and their customers.

1. Create an [app](https://dev.wix.com/dc3/my-apps/) and retrieve its app ID either from the URL or as displayed in the My Apps dashboard in the [Wix Developers Center](https://dev.wix.com/).

    ![Sample App ID](https://s3.amazonaws.com/wixplorer-readme-images/shipping-rates-integration-spi%2Fappid.png "Sample App ID")

1. Go to the [Components](https://devforum.wix.com/kb/en/article/about-app-components) tab in the Wix Developers Center.
1. Click **Add Component**, select **Integration Component** from the dropdown menu, select **Ecom Shipping Rates** and click **Add Component**.
1. Use the JSON editor to create the integration component’s configuration file. Take care to include the required fields noted in the table below. Click **Save**.

    | Name                 | Type                     | Description       |
    | ---------------------|--------------------------|-------------------|
    | `deploymentUri`      | string                   | Required. Base URI which Wix eCommerce will call to retrieve the shipping rates. For example, `https://my-shipping-provider.com/v1/getRates`.|
    | `name`               | string                   | Required. Human-readable name of the shipping provider. Max characters: 64.|
    | `description`        | string                   | Description of the shipping provider. Max characters: 200.|
    | `learnMoreUrl`       | string                   | URL to more info about the shipping provider.|
    | `dashboardUrl`       | string                   | URL to reach the shipping provider app's dashboard.|
    | `fallbackDefinitionMandatory`      | boolean    | Whether to require the site owner to define a fallback/default rate. Set to `true` if you do not provide rates as part of the integration.|

1. Click [**Test Your App**](https://devforum.wix.com/kb/en/article/how-to-test-your-app-on-a-free-premium-development-site).