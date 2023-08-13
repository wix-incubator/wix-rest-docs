SortOrder: 0
# About the Items Selection SPI

The Items Selection SPI allows you to make your items available for selection in the Wix Dashboard. For example, if you offer products for sale, you can expose your product list to site owners and admins in the Wix eCommerce edit order page, and they can add your products to an existing order. This can be done even if site visitors don't have access to your product list on the live site. 

![eCommerce order page 1](images/order-pg-1.png)


The integration is done via an app in the Wix App Market (created in the [Wix Developers Center](https://dev.wix.com/)) and the Wix Items Selection SPI.  

Learn more about [implementing an SPI with Wix](https://dev.wix.com/api/rest/getting-started/service-provider-interface).


## Integrations

Currently you can only use this SPI in conjunction with the following verticals:

+ Wix eCommerce Order page
+ Wix Automations

## Use Cases

Using the SPI, you can design your app to provide items for selection in the Wix Dashboard, including:
+ Luxurious jewelry for upscale clientele to add to an eCommerce order page. 
+ *Insert automations use case here* 

## Configuration

To enable Wix to communicate with your app,
[create an integration extension](https://dev.wix.com/api/rest/getting-started/service-provider-interface#getting-started_service-provider-interface_configure-an-integration-component-in-the-development-center)
in the Wix Developers Center.
Select the **Items Selection** extension and provide the following configuration:

| Name | Type | Description |
| --- | --- | --- |
| `deploymentUri`|string|Required. Base URI which Wix eCommerce will call to retrieve a list of items for selection.<br/> For example, `"deploymentUri": "https://my-list-of-items.com"`. |
| `key`|string| Required. A unique identifier for the provider. |
| `searchParams`|object|Supported search parameters. |
| `searchParams.fields`|Array<object>|Supported fields to search by. |
| `contentData`|object| Display data such as provider name and icon. |
| `contentData.iconKey`|string| Provider icon. |
| `contentData.providerName`|string| Provider name. |
| `contentData.title`|string| Item title. |
| `contentData.button`|string| Button label. |
| `contentData.subtitle`|string| Item description. |
| `supportedTags`|Array<string>| Tags representing a vertical. List the tags you want to integrate with. If no tags are listed, the Items Selection extension integrates with all supported verticals. Supported values: "UNKNOWN_TAG", "EMBEDDABLE", "ECOM_EDIT_ORDER" |
| `componentName`|string|A unique name for this component. This is an internal name that will only appear in the Dev Center. |

![eCommerce order page markup 1](images/order-pg-2-edit.png)

![eCommerce order page markup 2](images/order-pg-3-edit.png)
