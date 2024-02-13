SortOrder: 1
# Handle Item Variants

This article explains how to handle item customization and variants when implementing the Catalog SPI.

## The `catalogReference` object

When Wix calls the Get Catalog Items endpoint, it includes a `catalogReference` object containing the reference details for each item to retrieve from your catalog. This object includes the following properties:

+ `catalogItemId`: The ID of the item in the catalog it belongs to. You can use any system you like for generating and storing unique item IDs. You may wish to expose an API so your app can query and retrieve item IDs.
+ `appId`: ID of the app providing the catalog. You can get your app's ID from its page in the [Wix Dev Center](https://dev.wix.com/apps).
+ `options`: Additional item details in key:value pairs. Use this optional field to specify a variant of the item or add custom details. See below for more information.

## The `options` field

In some cases, your catalog might need more than just the item ID and app ID in order to return all of the correct item details. On a site's item page, visitors can often choose variants of the item or add custom details. For example:

+ T-shirt size
+ Recipient information for a gift
+ Time and date of an appointment
+ Donation or gift card amount
+ Custom text for a necklace

There are several ways you can use the `options` object for handling item variants. Here are two different approaches to implementing it. Decide which approach to take based on your technical requirements, existing system architecture, and business needs.

### Approach 1 | Pass variant details in `options`

You can pass specific information about the item in the `options` object as key:value pairs. You can choose how to structure the information and what keys and values to support.

For example, you can specify item variant details in any of the following ways:

+ T-shirt size and color: `"options": {"Size": "M", "Color": "Red"}`
+ Custom text for a necklace: `"options": {"customText": "Natalie"}`
+ Recipient information: `"options": {"recipientName": "Omar", "message": "Happy anniversary!"}`

If you take this approach, make sure that:

+ Your Catalog SPI implementation handles the expected `options` properties, processes them, and returns the correct item details.
+ When your app adds an item to a cart, checkout, or order, the `options` property of the item's `catalogReference` only includes key:value pairs that your catalog supports.

Use this approach if:

+ You prefer not to store details for every variant a client selects, unless they result in a purchase.
+ You don't mind handling validation of the `options` object's properties in your implementation of Get Catalog Items.

### Approach 2 | Pass a variant ID in `options`

You can create a separate API that processes item variants and returns a unique variant ID. Then your app can pass an `options` object containing only the item variant ID. When Wix calls Get Catalog Items, your Catalog SPI retrieves the correct details for the item variant on the basis of this ID and returns them.

For example, suppose you are creating an app for processing donations that can be added to a customer's transaction. You could implement this as follows:

1. Create an API called Create Donation for generating the specific details for a given donation. The request body might include properties that vary between donations, such as `organizationId`, `campaignId` and `amount`. It returns a unique `donationId`.
1. Create an API called Get Donation for retrieving the details of a donation based on its unique `donationId`.
1. When a site visitor makes a donation, they specify their preferred organization, campaign, and donation amount. The app then sends these details to the Create Donation API, which creates a donation entry and stores the details in your catalog's database. It then returns a unique `donationId`.
1. When your app adds a donation to a [cart](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/cart/introduction), [checkout](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/checkout/introduction), or [order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/introduction), include the unique donation ID in the `catalogReference` object's `options` property. For example: `"options": { "donationId": "bf3b953d-d0b7-4755-a54e-13c167fc4484"}`.
1. When Wix calls your Get Catalog Items endpoint to retrieve current information on the donation, it provides the `catalogReference` for the item, including the unique `donationId`. On the basis of this ID, the endpoint returns the full details for the specific donation, which can then be added to the cart, checkout, or order.

If you take this approach, make sure that:

+ You implement an API for creating item variants. Your API must receive the required variant details, store them, and generate a unique ID for each item variant.
+ When your app adds an item to a cart, checkout, or order, the `options` property of the item's `catalogReference` contains a field with the item variant ID your API generated.
+ Your Catalog SPI implementation expects and handles the unique item variant IDs it receives in the `options` object, and returns the correct item details.

Use this approach if:

+ You don't mind storing details for every variant a client selects, including those that don't result in a purchase.
+ You prefer to implement a formal API that enforces structure and validates all variants before they are included in a request to the catalog.