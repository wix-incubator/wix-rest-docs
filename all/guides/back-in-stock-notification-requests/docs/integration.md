SortOrder: 1
#Integrating with BackInStock

Read this if you want to integrate a new vertical into using back in stock. 
Integration with BackInStock has 2 major steps: 

1) Create an instance of `BackInStockVerticalConfig` class, which will hold all your vertical - specific 
configurations.
2) Create an adapter service which will notify platformized BackInStockNotificationRequestService that
products of your vertical are back in stock.  

#Creating an instance of BackInStockVerticalConfig
[BackInStockVerticalConfig](https://github.com/wix-private/ecom/blob/master/server/wix-ecommerce-server/wix-ecommerce-back-in-stock/back-in-stock-service/src/com/wixpress/ecom/back/in/stock/config/BackInStockVerticalConfigs.scala) declares fields and methods that each vertical must provide.
It lets you to customize notifications sent both to UoUs and Site Owners. 
```scala
abstract class BackInStockVerticalConfig(
  // Your catalog app id. All BackInStockNotificationRequests created by your vertical should have same CatalogReference.appId.  
  val appDefId: String,  
  
  // Is used to trigger automatic notifications to UoU about product being back in stock.
  val automationTriggerName: String,
  
  // Is used to notify Site Owner about newly created and resolved BackInStockNotificationRequests.
  val pingTemplateId: String
) {

  // All notifications to Site Owner (i.e about `New Request`, and `Resolved Request`) contain links to base BackInStock TPA page 
  // (with list of all BackInStockNotificationRequests) and link to particular BackInStockNotificationRequest.
 
  // Creates link to base back in stock page in your UI (list with all BackInStockNotificationRequests)  
  def buildBackInStockHomeUrl(metaSiteId: String): String
  
  // Creates link to particular back in stock request page in your UI
  def buildBackInStockRequestUrl(metaSiteId: String, requestId: String): String

}
```

Example of BackInStockVerticalConfig for Stores TPA
```scala
class BackInStockStoresConfig extends BackInStockVerticalConfig(
  appDefId = TpaKeys.wixStoresAppId,
  automationTriggerName = "e_commerce/back_in_stock_stores",
  pingTemplateId = "ecom.product_back_in_stock_request"
) {

  def buildBackInStockHomeUrl(metaSiteId: String): String =
    s"https://manage.wix.com/dashboard/$metaSiteId/store/back-in-stock"

  def buildBackInStockRequestUrl(metaSiteId: String, requestId: String): String =
    s"https://manage.wix.com/dashboard/$metaSiteId/store/back-in-stock/request/$requestId"

}
```

Once created, your configuration instance should be added to the `BackInStockVerticalConfigs` class which contains all registered vertical configs. 
- Add your instance to class constructor 
- Add it to `configs` Set in `BackInStockVerticalConfigs`. 
```scala
case class BackInStockVerticalConfigs(
  stores: BackInStockVerticalConfig = new BackInStockStoresConfig(), // predefined configuration
  integratedVertical: BackInStockVerticalConfig = new BackInStockIntegratedVerticalConfig() // add your new config as collaborator
) {

  val configs = Set(stores, integratedVertical) // and put it here
  
  // ....  
}
```
##Providing value for BackInStockVerticalConfig.appDefId
Your verticals' TPA app def id.

##Providing value for BackInStockVerticalConfig.automationTriggerName
Automation Service is responsible for automatic notifications to UoU with configured trigger-action recipe.

###Preconditions for this step: 
You have a ShoutOut email template provided by designers. 
As an example you may visit [shoutout](https://bo.wix.com/shoutout/templates#/) and perform search by tag = `back_in_stock-stores`.
You'll find email template designed for Stores TPA.

After you get ShoutOut email template for your vertical, you should add a tag for it. 
(No special naming requirements here. Stores use `back_in_stock-stores`) 

###Create automation trigger configuration.
Trigger configuration will bundle unique trigger name with your ShoutOut email template. 
Configuration will describe email template placeholders, trigger preconditions (if any), default action. 

<blockquote class='warning'>
  <p>Note: Default trigger action should be `Send email to contacts`</p>
  <p>Even though it's possible to assign other action than `Send email to contacts`, only this action should be bound to your trigger!</p>
</blockquote>

Use [create-trigger-configuration](https://bo.wix.com/wix-docs/rest/communications-&-marketing/automations-by-ascend/triggers-configuration/create-trigger-configuration)
endpoint to create your trigger configuration. 

<details>
<summary>Example of trigger configuration created for Stores TPA</summary>
<p>

```json
{
    "source": {
        "sourceId": "16be6c71-d061-4f56-8cda-c6aa911d1832",
        "sourceType": "WIX_APP"
    },
    "name": "e_commerce/back_in_stock_stores",
    "displayName": "Product is back in stock",
    "description": "With Wix Stores",
    "categories": [
        "1380b703-ce81-ff05-f115-39571d94dfcd"
    ],
    "schemaConfiguration": {
        "fields": [
            {
                "key": "product.name",
                "displayName": "Product Name",
                "fieldType": "TEXT",
                "sampleValues": [
                    "Shirt"
                ],
                "exposure": "EXPOSED",
                "allowNegativeOffset": false,
                "conditionOptions": {},
                "isArray": false
            },
            {
                "key": "product.price",
                "displayName": "Product Price",
                "fieldType": "TEXT",
                "sampleValues": [
                    "$10.00"
                ],
                "exposure": "EXPOSED",
                "allowNegativeOffset": false,
                "conditionOptions": {},
                "isArray": false
            },
            {
                "key": "product.imageUrl",
                "displayName": "Product Image",
                "fieldType": "TEXT",
                "sampleValues": [],
                "exposure": "EXPOSED",
                "allowNegativeOffset": false,
                "conditionOptions": {},
                "isArray": false
            },
            {
                "key": "product.buyNowUrl",
                "displayName": "Link to product page",
                "fieldType": "TEXT",
                "sampleValues": [
                    "https://www.mywebsite.com/product-page/shirt"
                ],
                "exposure": "EXPOSED",
                "allowNegativeOffset": false,
                "conditionOptions": {},
                "isArray": false
            }
        ]
    },
    "preconditions": [
        {
            "preconditionType": "PETRI",
            "key": "specs.stores.BackInStockAutomation",
            "value": "true"
        },
        {
            "preconditionType": "APP_DEPENDENCY",
            "key": "16be6c71-d061-4f56-8cda-c6aa911d1832",
            "value": "true"
        }
    ],
    "actionRecommendation": [
        {
            "actionName": "triggered-emails",
            "actionVisibilityOverride": "SHOW",
            "propertySuggestions": {
                "actionConfig": {
                    "templateTag": "back_in_stock-stores"
                }
            }
        }
    ],
    "enrichments": [],
    "eventTopic": "",
    "eventSlug": "",
    "eventType": "LEGACY"
}
```

A few notes about Stores trigger configuration example. 
- `source.sourceId` and `preconditions[1].key` value is `16be6c71-d061-4f56-8cda-c6aa911d1832`, which is BackInStock TPA app def id. 
You'll most likely want to use same value in your config. 
- `schemaConfiguration.fields[_].key`. all field names like `product.name` should be the same as the keys you'll send in 
`BackInStockNotificationRequestService.ReportItemsBackInStockRequest.automation_template_parameters` see [Creating an Adapter](#Creating an Adapter) section
- `actionRecommendation[0].propertySuggestions.actionConfig.templateTag` must have the same value as the tag of your ShoutOut email template.
</p>
</details>


After you create your trigger configuration, put its name to your verticals' `BackInStockStoresConfig.automationTriggerName` 
(in Stores example name is `e_commerce/back_in_stock_stores`)

##Providing value for BackInStockVerticalConfig.pingTemplateId
Ping template determines which notifications Store owner receives when someone creates new BackInStockNotificationRequest.
It defines multiple notification channels like (`web`, `mobile`, `email`)
`email` channel requires its own module and template configuration [Email template docs](https://github.com/wix-private/wixos/blob/master/ping/templates/templates-data/PingTemplates.md#email)
Terminology warning! email template != ping template. email template is part of Ping template which describes `email` notification channel.

1) Define your configuration template in templates data project [according to docs](https://github.com/wix-private/wixos/tree/master/ping/templates/templates-data)
   You must use predefined `back_in_stock.request` as your template settings group (defined [here](https://github.com/wix-private/wixos/blob/master/ping/ping-settings/ping-settings-static-data/src/main/resources/setting-groups.json))

2) If your Ping template defines `email` as one of your notification channels: 

Ping email template is less configurable than Automation email template.
You are not in control of parameters, and their names which are passed to Ping.
BackInStockNotificationService will pass predefined set of fields to Ping.  
You should define your template using all (or some) of those fields.

Translation parameters: 
```js
[
`email`, 
`productName`
]
```
Data parameters: 

```js
[
`email`, 
`productName`,
`formattedPrice`,
`mediaUrl`, // product image url
`isAutomationEnabled`, // whether automatic notifications are enabled for this products' catalog
`viewRequestsUrl`, // link to base back-in-stock requests table
`automationManagementUrl` // link to the page with request collection management
]
```  

Full example of Ping template for Stores vertical can be found [here](https://github.com/wix-private/wixos/blob/master/ping/templates/templates-data/src/main/resources/templates/ecom-notifications.json)
Under `ecom.product_back_in_stock_request` property. 

After you create your verticals' Ping configuration [here](https://github.com/wix-private/wixos/blob/master/ping/templates/templates-data/src/main/resources/templates/ecom-notifications.json)
Provide a property name which holds your configuration to `BackInStockVerticalConfig.pingTemplateId`. <br>
For example: Stores provide `ecom.product_back_in_stock_request`. 

For more questions refer to general [Ping integration guide](https://bo.wix.com/wix-docs/rest/drafts/ping-notifications-hub/integration-guide/overview)

##Implementing BackInStockVerticalConfig.buildBackInStockHomeUrl and BackInStockVerticalConfig.buildBackInStockRequestUrl
All notifications to Site Owner (i.e about `New Request`, and `Resolved Request`) contain links to base BackInStock TPA page (with list of
all BackInStockNotificationRequests) and link to particular BackInStockNotificationRequest.
Based on routing configured by your implementation of BackInStock UI, implement methods in your `BackInStockVerticalConfig` todo link:
```scala
def buildBackInStockHomeUrl(metaSiteId: String): String
def buildBackInStockRequestUrl(metaSiteId: String, requestId: String): String
```
buildBackInStockHomeUrl - given metaSiteId creates a URL to base BackInStock page (with the list of all BackInStockNotificationRequests) in BM
buildBackInStockRequestUrl - given metaSiteId and BackInStockNotificationRequest.id creates a URL to particular BackInStockNotificationRequest in BM
<blockquote class='warning'>
  <p>Note: Stores did not actually implement a page for particular requests. Both `buildBackInStockHomeUrl` and `buildBackInStockRequestUrl`
  currently generate the same link. (You can do the same.)</p>
</blockquote>


#Creating an Adapter
BackInStockNotificationRequestService does not detect that particular product goes back in stock.
This is vertical-specific logic that should be implemented inside an Adapter. 
Adapters' responsibility is to detect, that some product changed it status from `out of stock` to `in stock` and notify
BackInStockNotificationRequestService, using `reportItemsBackInStock` endpoint. BackInStockNotificationRequestService will search
for all BackInStockNotificationRequests referencing that product, and resolve them.   
For example check out [BackInStockStoresNotificationsAdapter implementation](https://github.com/wix-private/ecom/tree/master/server/wix-ecommerce-server/wix-ecommerce-back-in-stock/back-in-stock-stores-adapter/proto/docs#readme)

<blockquote class='warning'>
  <p>Note: `reportItemsBackInStock` accepts 2 mutually exclusive parameters: `request_ids` and `catalog_reference`</p>
</blockquote>

- `catalog_reference`: adapter calls `reportItemsBackInStock` providing CatalogReference, and service will resolve all 
BackInStockNotificationRequests that have exactly the same CatalogReference (deep equality). This is a simpler approach compared to `by requestIds`
and you should strive to use it whenever possible. 

- `request_ids`: When strict equality for CatalogReferences doesn't work. E.g. when business logic involves range comparisons or comparing complex sets of options
Consider an example:
Some UoU books a room from 1PM to 5PM.
Another UoU wants to book the same room from 1PM to 2PM. As room is already taken the only thing second user can do is to leave a 
BackInStockNotificationRequest providing:  
```
CatalogReference(
    appId: {catalogId},
    catalogItemId: {roomId},
    options: {start: 1619517600, end: 1619521200} // start: Tue Apr 27 2021 13:00:00 GMT+0300, end: Tue Apr 27 2021 14:00:00 GMT+0300  
)
```
First UoU cancels his booking. 
If Adapter for this vertical would send a CatalogReference of cancelled room, it would send a different one: 
```
CatalogReference(
    appId: {catalogId},
    catalogItemId: {roomId},
    options: {start: 1619517600, end: 1619532000} // start: Tue Apr 27 2021 13:00:00 GMT+0300, end: Tue Apr 27 2021 17:00:00 GMT+0300
                                 ^^^ this is different    
)
```
And we wouldn't match original BackInStockNotificationRequest because catalog references have different `options.end` values.
One of possible solutions here would be to use interval comparison for `start` and `end` fields: 
BackInStockNotificationRequestService exposes QueryBackInStockNotificationRequests endpoint, which lets you to use [QueryV2 API](https://github.com/wix-private/server-infra/blob/master/iptf/simple-data-layer/README.md#examples-for-queries)
in order to retrieve BackInStockNotificationRequests by richer (than simple full equality) set of predicates. 

After filtering BackInStockNotificationRequests according to your verticals' business logic, you can send the list with 
found BackInStockNotificationRequest.id to `reportItemsBackInStock` endpoint.