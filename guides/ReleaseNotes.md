# Release Notes


## New Release: [Bookings Services](wix-bookings/services-v2)

The [Bookings Services V2](wix-bookings/services-v2) API provides third parties the ability to retrieve information about services using the [Get Service](wix-bookings/services-v2/get-service) and 
[Query Services](wix-bookings/services-v2/query-services) APIs.

(February 27, 2023)


## New Release: [Wix Blog](wix-blog/blog)

The [Blog](wix-blog/blog) API introduces new write functionality:
+ The new [Draft Posts](wix-blog/blog/draft-posts) APIs enable you to create, delete, and manage blog draft posts.
+ You can now manage blog categories using the Categories APIs, such as [Create Category](wix-blog/blog/categories/create-category), [Update Category](wix-blog/blog/categories/update-category), and [Delete Category](wix-blog/blog/categories/delete-category).
+ You can now manage blog tags using the Tags APIs, such as [Create Tag](wix-blog/blog/tags/create-tag) and [Delete Tag](wix-blog/blog/tags/create-tag).  

Some Blog API parameters and properties have been renamed. The existing parameters and properties are deprecated and will be removed on June 30, 2023. 

(Dec 20, 2022)

## New Fields: [Restaurants Orders API](wix-restaurants/orders)

The [Order object](wix-restaurants/orders/order-object) has new fields:
+ The new `discounts.catalogDiscountDescription` field is the discount description as defined in the catalog.
+ The new `lineItems.dishOptions.name` field is the line item option name.
+ The new `loyaltyInfo.estimatedAccountBalance` field is the Wix Loyalty estimated account balance.
+ The new `loyaltyInfo.estimatedPointsEarned` field is the Wix Loyalty estimated total earned points.
+ The new `loyaltyInfo.rewardRevision` field is the Wix Loyalty reward revision number.

(December 13, 2022)

## New Data: [App Instance API](app-management/apps/app-instance)
+ The `copiedFromTemplate` parameter replaces the deprecated `isOriginSiteTemplate` parameter.
+ The `siteId` parameter is Wix's internal unique site identifier.

(November 6, 2022)

## New Endpoints: [Coupons API](coupons/coupons/coupon)
The [Coupons API](coupons/coupons/coupon) now includes two new endpoints:
+ [Bulk Create Coupons](coupons/coupons/coupon/bulk-create-coupons) allows for creating multiple coupons with one API call.
+ [Bulk Delete Coupons](coupons/coupons/coupon/bulk-delete-coupons) allows for deleting multiple coupons with one API call.

(October 26, 2022)

## New Webhook: [Email Marketing API](marketing/email-marketing)
The [Email Activity Updated Webhook](marketing/email-marketing/campaign/email-activity-updated-webhook) is triggered each time an email campaign has a new recipient activity.

(October 19, 2022)

## New Webhooks: [Members API](members/badges)
The [Members Badges API](members/badges) now includes these new webhooks:
+ [Badge Created](members/badges/badge-created-webhook) is triggered when a badge is created.
+ [Badge Updated](members/badges/badge-updated-webhook) is triggered when a badge is updated.
+ [Badge Assigned](members/badges/badge-assigned-webhook) and [Badge Unassigned](members/badges/badge-unassigned-webhook) are triggered when a badge is assigned to, or unassigned from, a member.
+ [Badge Deleted](members/badges/badge-deleted-webhook) is triggered when a badge is deleted.

(September 22, 2022)

## New Webhooks: [Pricing Plans API](wix-pricing-plans/pricing-plans/orders)
The [Pricing Plans Orders API](wix-pricing-plans/pricing-plans/orders/) now includes these new webhooks:
+ [Order Created](wix-pricing-plans/pricing-plans/orders/order-created-webhook) and [Order Purchased](wix-pricing-plans/pricing-plans/orders/order-purchased-webhook) are triggered when an order is created or purchased.
+ [Order Started](wix-pricing-plans/pricing-plans/orders/order-started-webhook) and [Order Cycle Started](wix-pricing-plans/pricing-plans/orders/order-cycle-started-webhook) are triggered at the start of a new order or a new order cycle.
+ [Order Marked As Paid](wix-pricing-plans/pricing-plans/orders/order-marked-as-paid-webhook) is triggered when an offline order is marked as paid.
+ [Order End Date Postponed](wix-pricing-plans/pricing-plans/orders/order-end-date-postponed-webhook), [Order Paused](wix-pricing-plans/pricing-plans/orders/order-paused-webhook) and [Order Resumed](wix-pricing-plans/pricing-plans/orders/order-resumed-webhook) are triggered when an order is postponed, paused, or resumed.
+ [Order Canceled](wix-pricing-plans/pricing-plans/orders/order-canceled-webhook) and [Order Auto Renew Canceled](wix-pricing-plans/pricing-plans/orders/order-auto-renew-canceled-webhook) are triggered when an order is canceled.
+ [Order Ended](wix-pricing-plans/pricing-plans/orders/order-ended-webhook) is triggered when an order ends.
+ [Order Updated](wix-pricing-plans/pricing-plans/orders/order-updated-webhook) is triggered when an order is updated.

(September 6, 2022)

## New Endpoints: [Email Marketing API](marketing/email-marketing)
The [Email Marketing API](marketing/email-marketing) now includes two new endpoints:
+ [List Recipients](marketing/email-marketing/campaign/list-recipients) retrieves a list of recipients for a selected campaign based on a specific recipient activity.
+ [List Statistics](marketing/email-marketing/campaign/list-statistics) retrieves a list of detailed statistics for selected campaigns.

(September 5, 2022)

## New Webhooks: [Members API](members/members)
The [Members API](members/members) now includes three new webhooks:
+ [Member Created](members/members/member-created-webhook) is triggered when a member is created.
+ [Member Deleted](members/members/member-deleted-webhook) is triggered when a member is deleted.
+ [Member Updated](members/members/member-updated-webhook) is triggered when a member is updated.

These webhooks complement the existing [Members](https://dev.wix.com/api/rest/members/members) endpoints.
(September 1, 2022)


## New Endpoints: [Site Properties API](business-info/site-properties)
The [Site Properties API](business-info/site-properties) now includes three new endpoints:
+ [Update Business Contact](business-info/site-properties/properties/update-business-contact) updates a site's business contact information.
+ [Update Business Profile](business-info/site-properties/properties/update-business-profile) updates a site's business profile.
+ [Update Business Schedule](business-info/site-properties/properties/update-business-schedule) updates a site's business schedule.

These endpoints complement the existing [Update Consent Policy](business-info/site-properties/properties/update-consent-policy) endpoint.

(August 17, 2022)

## New Release: [Pricing Plans Orders API](wix-pricing-plans/pricing-plans/orders)
The [Pricing Plans Orders API](wix-pricing-plans/pricing-plans/orders/) provides third parties the ability to manage a site's pricing plan orders, as well as create offline orders.

(July 20, 2022)

## New Release: [Wix Loyalty Program](wix-loyalty-program/)
The [Wix Loyalty Program API](wix-loyalty-program/) provides third parties the ability to activate and manage a site's loyalty program. This includes creating and adjusting customer loyalty accounts.

(July 14, 2022)
## New Releases: [Stores Catalog API](wix-stores/catalog)
#### New and Updated APIs
+ The new [Bulk Update Products](wix-stores/catalog/products/bulk-update-products) introduces bulk functionality for updating/setting a certain field for up to 100 products at a time.
+ The new [Bulk Adjust Product Properties](wix-stores/catalog/products/bulk-adjust-product-properties) allows for bulk adjusting a certain numerical property (price, cost, or weight) for up to 100 products at a time.
+ The new [Remove Brand](wix-stores/catalog/products/remove-brand) introduces functionality for deleting a [product's brand](https://support.wix.com/en/article/adding-brand-names-to-boost-product-page-seo-in-wix-stores).
+ The new [Remove Ribbon](wix-stores/catalog/products/remove-ribbon) introduces functionality for deleting a product's ribbon. Ribbons can be used to draw attention to products you want to promote.

#### New Data
+ A new query param was added to the [Get Product](wix-stores/catalog/products/get-product) API - `includeMerchantSpecificData`. This boolean determines whether merchant specific data, such as cost and profit data, is included in the response.
+ A new query param was added to the [Get Collection](wix-stores/catalog/collections/get-collection) API - `includeNumberOfProducts`. This boolean determines whether a field named `numberOfProducts` is included in the response.
+ The new `product.costAndProfitData` field holds information about a product's cost of goods, profit, and margin. Learn more about [calculating the cost of goods for a product](https://support.wix.com/en/article/wix-stores-calculating-cost-of-goods).
+ The new `product.costRange`, `product.weightRange`, and `product.priceRange` fields hold information about the minimum and maximum values of each. For example, the lightest and heaviest products/variants in a store's catalog.

(July 14, 2022)

## New Release: [Restaurants Local Delivery Integration SPI](wix-restaurants/local-delivery-integration-spi)
The new Restaurants [Local Delivery SPI](wix-restaurants/local-delivery-integration-spi/local-delivery) introduces the ability to integrate third-party local delivery services with a Wix site. Local delivery services include estimating and creating deliveries.

New to working with Wix SPIs? [Learn more](https://dev.wix.com/api/rest/getting-started/service-provider-interface)

(June 30, 2022)

## New Release: [Wix Blog Tags](wix-blog/blog/tags/tag-object/)
The new Blog [Tags API](wix-blog/blog/tags/tag-object/) introduces read functionality for blog tags.

(April 25, 2022)

## New Webhook: [Restaurants Orders API](wix-restaurants/orders)

The new [New Order Webhook](wix-restaurants/orders/new-order-webhook)
is triggered when an order is created. This means
the order has been validated and the payment has cleared,
and now the site owner can accept or cancel the order.

This replaces the [Order Created](wix-restaurants/orders/order-created-webhook) webhook, 
which has been deprecated and will be removed on 
September 30, 2022.

(April 18, 2022)

## New Fields: [Wix Groups API](wix-groups/)

The Wix Groups API has renamed some fields,
resulting in deprecating some existing fields.
The deprecated fields will be removed on June 30, 2022.
In addition, the `memberIds` parameter in
[Approve Join Group Requests](wix-groups/wix-groups/join-requests/approve-join-group-requests)
will be required after June 30, 2022.

For more information, see [End-of-Life Notices](./Deprecations.md#end-of-life-june-30-2022).  
(March 23, 2022)

## New Release: [Inbox API](inbox/)

The new Inbox API introduces functionality
for managing [conversations](inbox/conversations) and [messages](inbox/messages)
between the site and its visitors, contacts, and members.

This deprecates the [Wix Chat API](wix-chat/wix-chat).
(March 1, 2022)

## New Release: [Account Level APIs](account-level-apis/)

The Account Level APIs are accessible only using API keys, which are currently available to selected beta users only.
APIs exposed include Sites, Site Folders, Resellers, B2B Site Management, Domain Search and Domain Connections. (February 24, 2022)  

## New Release: [Editor Deep Link API](app-management/about-the-editor-deep-link-api)

The [Editor Deep Link API](app-management/about-the-editor-deep-link-api) generates a URL for an app that navigates to a user's Editor and places the app's components on a page. (January 30, 2022)

## New Webhooks and Endpoints: [Contacts API](contacts/)

The new [Contact Merged Webhook](contacts/contacts/contacts-v4/contact-merged-webhook)
is triggered when source contacts are merged to a target contact.
The new `originatedFrom` property is sent as `merge` when
[Contact Updated Webhook](contacts/contacts/contacts-v4/contact-updated-webhook)
or [Contact Deleted Webhook](contacts/contacts/contacts-v4/contact-deleted-webhook)
are triggered as the result of merging, allowing you to ignore redundant events.

The [Query Labels](contacts/labels/query-labels)
and [Query Extended Fields](contacts/extended-fields/query-extended-fields)
endpoints are also now available.

(January 25, 2022)

## New Release: [Wix Members Badges API](members/badges)

The [Wix Members Badges API](members/badges) provides third parties with the ability to read existing site members’ badges used on Wix apps, and create and assign badges to site members from their own apps. (December 14, 2021)

## New Release: [Wix Forums API](wix-forum/)

The [Wix Forums API](wix-forum/) provides third parties with the ability to read a site’s Wix Forums and members’ posts, and receive updates on new Wix Forum activities via webhooks from their own apps. (December 14, 2021)

## New Release: [Wix Members Activity Counters API](members/activity-counters)

The [Wix Members Activity Counters API](members/activity-counters) provides third parties with the ability to read public counts of member activities from Wix apps, and read and set public and private counts of member activities from their own apps. (November 24, 2021)

## New Release: [Wix Blog Post Stats API](wix-blog/blog/post-stats/get-total-posts)

The [Wix Blog Post Stats API](wix-blog/blog/post-stats/get-total-posts) provides the ability to get the total number of posts published to a blog, and to filter for number of posts published per month. (October 28, 2021)

## New Release: [Wix Restaurants Orders API](wix-restaurants/orders)

The [Wix Restaurants Orders API](wix-restaurants/orders) provides the ability to retrieve orders and update their statuses.
(October 26, 2021)

## New Release: [Marketing Tags API](marketing/marketing-tags)

The [Marketing Tags API](marketing/marketing-tags) provides the ability to manage embedded marketing tags.
(October 26, 2021)

## New Release: [Query Service Catalog](wix-bookings/service-catalog/services/query-service-catalog)

The Query Service Catalog endpoint replaces
[List services](wix-bookings/service-catalog/services/list-services),
which has been deprecated.
(October 13, 2021)

## New Webhooks: [Contacts v4](contacts/contacts/contacts-v4/contact-object)

The Contacts v4 API introduces the
[Contact Created](contacts/contacts/contacts-v4/contact-created-webhook),
[Contact Updated](contacts/contacts/contacts-v4/contact-updated-webhook),
and [Contact Deleted](contacts/contacts/contacts-v4/contact-deleted-webhook)
webhooks.  
This deprecates the
[Contacts v1](contacts/contacts/contacts-v1-(deprecated)/contact-object)
webhooks.
(September 13, 2021)

## New Release: [Query Bookings Resources](wix-bookings/resources/query-resources)

The Query Resources endpoint replaces
[List Resources](wix-bookings/resources/list-resources),
which has been deprecated.
(September 13, 2021)

## New Data: [Bookings Resources](wix-bookings/resources)

`location.businessLocation` field added to [Resource](wix-bookings/resources/resource-object) object.  
Note that the `location.businessLocation.businessSchedule` object is not supported by Wix Bookings.
(September 13, 2021)

## New Release: [FAQ API](site-content/faq)

The [FAQ API](site-content/faq) provides the ability to view and manage the questions and answers in the FAQ app.
(August 24, 2021)

## New Data: [App Instance API](app-management/apps/app-instance)

`ownerEmail` field added to [Get App Instance](app-management/apps/app-instance/get-app-instance) endpoint response.
(August 8, 2021)

## New Data: [Stores Orders API](wix-stores/orders)

`order.shippingInfo.code` field added to [Wix Stores Orders](wix-stores/orders/order-object) object.  
The `code` field can be used by carrier services / fulfillers to see orders shipped by them.
(July 25, 2021)
