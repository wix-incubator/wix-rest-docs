SortOrder: 0
# About Custom Discount Triggers SPI

The eCommerce Custom Discount Triggers SPI allows you to provide custom triggers that specify when an item can be discounted.

Custom triggers play a part in the definition of discount rules - sets of triggers and scopes that together define the necessary conditions for a discount to apply to items in the cart/checkout.

## Before you begin

To use a custom trigger, first [create an automatic discount using the dashboard](https://support.wix.com/en/article/wix-stores-creating-automatic-discounts), or by using the [Discount Rules API](https://dev.wix.com/api/rest/wix-ecommerce/discount-rules/create-discount-rule).

The integration is done via an app in the Wix App Market (created in the [Wix Developers Center](https://dev.wix.com/)) and the Wix Custom Discount Triggers Rates SPI.

Learn more about [implementing an SPI with Wix](https://dev.wix.com/api/rest/getting-started/service-provider-interface).

## Terminology

+ **Custom triggers:** Triggers that can meet any condition you want. For example, a trigger that only fires between 8pm-10pm on Mondays and Thursdays, and only on a rainy day.

## Prerequisites

Complete the following steps to adapt Wix system's integration to make your custom triggers available to merchants and their customers.

1. Create an [app](https://dev.wix.com/dc3/my-apps/) and retrieve its app ID either from the URL or as displayed in the My Apps dashboard in the [Wix Developers Center](https://dev.wix.com/).

    ![Sample App ID](https://s3.amazonaws.com/wixplorer-readme-images/custom-triggers-integration-spi%2Fappid.png "Sample App ID")

1. Go to the [Components](https://devforum.wix.com/kb/en/article/about-app-components) tab in the Wix Developers Center.
1. Click **Add Component**, select **Integration Component** from the dropdown menu, select **Ecom Custom Discount Triggers** and click **Add Component**.
1. Use the JSON editor to create the integration component’s configuration file. Take care to include the required fields noted in the table below. Click **Save**.

    | Name                 | Type                     | Description       |
    | ---------------------|--------------------------|-------------------|
    | `deploymentUri`      | string                   | Required. Base URI which Wix eCommerce will call to retrieve the custom triggers. For example, `https://my-discount-app.com/v1/getEligibleTriggers`.|

1. Click [**Test Your App**](https://devforum.wix.com/kb/en/article/how-to-test-your-app-on-a-free-premium-development-site).