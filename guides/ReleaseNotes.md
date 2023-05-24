# Release Notes


## New Webhooks: [Wix Bookings V2](wix-bookings/bookings-v2)

The Bookings V2 API now includes new webhooks:

+ [Booking Created](/wix-bookings/bookings-v2/booking-created-webhook)
+ [Booking Rescheduled](/wix-bookings/bookings-v2/booking-rescheduled-webhook)
+ [Booking Confirmed](/wix-bookings/bookings-v2/booking-confirmed-webhook)
+ [Booking Declined](/wix-bookings/bookings-v2/booking-declined-webhook)
+ [Booking Canceled](/wix-bookings/bookings-v2/booking-canceled-webhook)
+ [Number Of Participants Updated](/wix-bookings/bookings-v2/number-of-participants-updated -webhook)


(May 24, 2023)


## New Release: [Bookings Service Options and Variants](wix-bookings/service-options-and-variants)

The [Bookings Service Options and Variants](wix-bookings/service-options-and-variants) API enables you to retrieve and manage options and variants for a particular bookings service. The new API includes:

+ [Get Service Options And Variants](/wix-bookings/service-options-and-variants/get-service-options-and-variants)  
+ [Get Service Options And Variants By Service ID](/wix-bookings/service-options-and-variants/get-service-options-and-variants-by-service-id)
+ [Query Service Options And Variants](/wix-bookings/service-options-and-variants/query-service-options-and-variants)
+ [Create Service Options And Variants](/wix-bookings/service-options-and-variants/create-service-options-and-variants)
+ [Clone Service Options And Variants](/wix-bookings/service-options-and-variants/clone-service-options-and-variants)
+ [Update Service Options And Variants](/wix-bookings/service-options-and-variants/update-service-options-and-variants)
+ [Delete Service Options And Variants](/wix-bookings/service-options-and-variants/delete-service-options-and-variants)
+ Webhooks: 
    + [Service Options And Variants Created](/wix-bookings/service-options-and-variants/service-options-and-variants-created-webhook)
    + [Service Options And Variants Updated](/wix-bookings/service-options-and-variants/service-options-and-variants-updated-webhook)
    + [Service Options And Variants Deleted](/wix-bookings/service-options-and-variants/service-options-and-variants-deleted-webhook)

(May 22, 2023)

## New Functionality: [Wix Blocks](https://support.wix.com/en/wix-blocks)
3rd party apps can now be written partially or completely using Wix Blocks, powered by [Velo by Wix](https://www.wix.com/velo/reference).
See [Publishing your Blocks app to the App Market](https://support.wix.com/en/article/wix-blocks-publishing-your-app-to-the-app-market) for details.

(May 22, 2023)

## New Release: [Redirect Session](redirect-session/redirect-session)

The [Redirect Session](redirect-session/redirect-session) API enables you to manage redirection of site visitors between external Wix Headless client sites and Wix-managed pages for processes such as authentication and checkout. The new API includes:

- [Create Redirect Session](redirect-session/redirect-session/create-redirect-session)

(April 30, 2023)

## New Release: [Event Guests](wix-events/event-guests)

The [Event Guests](wix-events/event-guests) API enables you to manage guests for a particular event. The new API includes:

- [Query Event Guests](wix-events/event-guests/query-event-guests)

(April 25, 2023)

## New Release: Wix eCommerce [Additional Fees Integration SPI](wix-ecommerce/additional-fees-integration-spi)

The new [Calculate Additional Fees](wix-ecommerce/additional-fees-integration-spi/calculate-additional-fees) endpoint provides third parties the ability to calculate various additional fees for items in a cart, checkout, or order.

(April 13, 2023)

## New Release: [Wix Data API](wix-data)

The [Wix Data API](wix-data/wix-data) provides a complete solution for accessing, organizing, configuring, and managing data stored in a Wix project or site's database. It includes the following APIs:

+ [Data Items](wix-data/wix-data/data-items): Access and manage items in a Wix site's data collections.
+ [Data Collections](wix-data/wix-data/data-collections): Create data collections and manage their structure.
+ [Indexes](wix-data/wix-data/indexes): Create indexes for data collections, to make querying data faster.
+ [External Database Connections](wix-data/wix-data/external-database-connections): Connect an external database and manage it with Wix Data APIs.

(April 13, 2023)

## New Release: [OAuth Apps API](auth-management/oauth-apps)

The [OAuth Apps API](auth-management/oauth-apps) API enables you to create and manage OAuth apps which authorize external apps or sites to access a Wix project or site's data. It includes the following endpoints:

+ [Create OAuth App](auth-management/oauth-apps/create-oauth-app)
+ [Delete OAuth App](auth-management/oauth-apps/delete-oauth-app)
+ [Get OAuth App](auth-management/oauth-apps/get-oauth-app)
+ [Query OAuth Apps](auth-management/oauth-apps/query-oauth-apps)
+ [Update OAuth App](auth-management/oauth-apps/update-oauth-app)

(April 02, 2023)

## New Endpoints: [Wix Media](media/media-manager)

The Media API now includes new endpoints and webhooks:

+ [Update File Descriptor](media/media-manager/files/update-file-descriptor) updates a file. This replaces [Update File](media/media-manager/files/update-file) which has been deprecated and will be removed on March 31, 2023.
+ [List Files](media/media-manager/files/list-files) retrieves a list of files in the Media Manager.
+ [List Deleted Files](media/media-manager/files/list-deleted-files) retrieves a list of files in the Media Manager's trash bin.
+ [List Folders](media/media-manager/folders/list-folders) retrieves a list of folders in the Media Manager's trash bin.
+ [List Deleted Folders](media/media-manager/folders/list-deleted-folders) retrieves a list of folders in the Media Manager's trash bin.
+ [File Ready Webhook](media/media-manager/files/file-ready-webhook) triggered when a file is ready to be used, after any post-upload processing.
+ [File Failed Webhook](media/media-manager/files/file-failed-webhook) triggered when a file fails during essential post-upload processing.
+ [File Descriptor Updated Webhook](media/media-manager/files/file-descriptor-updated-webhook) triggered when a file is updated, including when a file is moved to a different folder.
+ [File Descriptor Deleted Webhook](media/media-manager/files/file-descriptor-deleted-webhook) triggered when a file is deleted.
+ [Folder Created Webhook](media/media-manager/folders/folder-created-webhook) triggered when a folder is created.
+ [Folder Updated Webhook](media/media-manager/folders/folder-updated-webhook) triggered when a folder is updated.
+ [Folder Deleted Webhook](media/media-manager/folders/folder-deleted-webhook) triggered when a folder is deleted.

(March 30, 2023)

## New Releases: Wix Bookings [Pricing API](wix-bookings/pricing) and [Pricing Integration SPI](wix-bookings/pricing-integration-spi)

The new [Wix Bookings Pricing APIs](wix-bookings/pricing) and [Pricing Integration SPI](wix-bookings/pricing-integration-spi) provide third parties the ability to preview, calculate, and customize pricing for bookings:

+ [Preview](wix-bookings/pricing/preview-price) how much a booking will cost based on its line items.
+ [Calculate](wix-bookings/pricing/calculate-price) how much a booking will cost based on either: 
    + Standard pricing logic supplied with Wix Bookings.
    + Custom pricing, that you implement.
+ [Integrate](wix-bookings/pricing-integration-spi) your own custom pricing logic, such as varied pricing, into Wix Bookings with the [Pricing Integration SPI](wix-bookings/pricing-integration-spi).

(March 28, 2023)


## New Release: [eCommerce Order Fulfillments](wix-ecommerce/order-fulfillments)

The [eCommerce Order Fulfillments](wix-ecommerce/order-fulfillments) API provides third parties the ability to manage eCommerce order fulfillments. The new API includes:
- [Create Fulfillment](wix-ecommerce/order-fulfillments/create-fulfillment)
- [Bulk Create Fulfillments](wix-ecommerce/order-fulfillments/bulk-create-fulfillments)
- [Update Fulfillment](wix-ecommerce/order-fulfillments/update-fulfillment)
- [List Fulfillments For Single Order](wix-ecommerce/order-fulfillments/list-fulfillments-for-single-order)
- [List Fulfillments For Multiple Orders](wix-ecommerce/order-fulfillments/list-fulfillments-for-multiple-orders)
- [Delete Fulfillment](wix-ecommerce/order-fulfillments/delete-fulfillment)

(March 13, 2023)


## New Release: [External Calendars V2](wix-bookings/external-calendars-v2)

The [External Calendars V2](wix-bookings/external-calendars-v2) API enables you to connect and sync a Wix site with external calendars. The new API includes the following endpoints:
- [Connect By Credentials](wix-bookings/external-calendars-v2/connect-by-credentials)
- [Connect By OAuth](wix-bookings/external-calendars-v2/connect-by-o-auth)
- [Disconnect](wix-bookings/external-calendars-v2/disconnect)
- [Get Connection](wix-bookings/external-calendars-v2/get-connection)
- [List Calendars](wix-bookings/external-calendars-v2/list-calendars)
- [List Connections](wix-bookings/external-calendars-v2/list-connections)
- [List Events](wix-bookings/external-calendars-v2/list-events)
- [List Providers](wix-bookings/external-calendars-v2/list-providers)
- [Update Sync Config](wix-bookings/external-calendars-v2/update-sync-config)

(March 02, 2023)


## New Release: [Policies v2](wix-events/policies-v2)

The [Policies v2](wix-events/policies-v2) API enables you to manage the policies for a particular event. The new API includes:

- [Create Policy](wix-events/policies-v2/create-policy)
- [Delete Policy](wix-events/policies-v2/delete-policy)
- [Get Policy](wix-events/policies-v2/get-policy)
- [Query Policies](wix-events/policies-v2/query-policies)
- [Reorder Event Policies](wix-events/policies-v2/reorder-event-policies)
- [Update Policy](wix-events/policies-v2/update-policy)

(March 01, 2023)


## New Release: [Bookings Services](wix-bookings/services-v2)

The [Bookings Services V2](wix-bookings/services-v2) API provides third parties the ability to retrieve information about services using the [Get Service](wix-bookings/services-v2/get-service) and 
[Query Services](wix-bookings/services-v2/query-services) APIs.

(February 27, 2023)


## New Endpoints: [Wix eCommerce](wix-ecommerce)

The Wix eCommerce [Cart API](wix-ecommerce/cart) now includes 8 new endpoints:
+ [Create Checkout From Cart](wix-ecommerce/cart/create-checkout-from-cart).
+ [Estimate Totals](wix-ecommerce/cart/estimate-totals).
+ [Add To Cart](wix-ecommerce/cart/add-to-cart).
+ [Update Cart](wix-ecommerce/cart/update-cart).
+ [Update Line Items](wix-ecommerce/cart/update-line-items).
+ [Remove Coupon](wix-ecommerce/cart/remove-coupon).
+ [Remove Line Items](wix-ecommerce/cart/remove-line-items).
+ [Delete Cart](wix-ecommerce/cart/delete-cart).

(February 27, 2023)

## New Endpoints: [Contacts API](contacts/contacts/contacts-v4)

The Contacts API now includes two new endpoints:

- [Merge Contacts](contacts/contacts/contacts-v4/merge-contacts)
  allows you to merge one or more source contacts into a target contact.
  Note that a successful merge deletes the source contacts
  and updates the target contact.
- [Preview Merge Contacts](contacts/contacts/contacts-v4/preview-merge-contacts)
  allows you to perform a dry run of a merge
  without deleting or updating contacts.

## New Release: [Wix Notifications](wix-notifications)

The new [Wix Notifications API](wix-notifications) enables you to trigger the sending of predefined notifications to Wix site owners and contributors. [Create a notification](wix-notifications/notifications/creating-a-notification-template) in the Wix Dev Center, then call the [Notify](wix-notifications/notifications/notify) endpoint to send notifications.

(February 26, 2023)

## New Endpoint: [Bookings Calendar API](wix-bookings/calendar)

The Wix Bookings [Calendar API](wix-bookings/calendar) now includes a new endpoint:

+ [Query Sessions](wix-bookings/calendar/sessions/query-sessions) retrieves a list of sessions, given provided time range, filtering, and paging. This replaces [List Sessions](wix-bookings/calendar/sessions/list-sessions) which has been deprecated and will be removed on June 30, 2023.

(February 23, 2023)

## New Release: [Site Actions](site-actions)

[Account Level APIs](account-level-apis/) has a new Site Actions API that enables you to manage sites. The new API introduces the [Bulk Delete Site](site-actions/bulk-delete-site) endpoint.

As with other Account Level APIs, Site Actions APIs are accessible only using API keys.

(January 25, 2023)

## New Release: [Wix eCommerce](wix-ecommerce)

Wix eCommerce introduces new APIs functionality that enables you to read eCommerce cart, checkout, and order information, as well as listen to webhooks. The new APIs includes:
+ [Cart API](wix-ecommerce/cart).
+ [Checkout API](wix-ecommerce/checkout).
+ [Order API](wix-ecommerce/orders).

(January 22, 2023)

## New Release: [Pro Gallery](site-content/pro-gallery)

Site Content has a new Pro Gallery API.

The Pro Gallery API enables 3rd-parties to view and manage pro galleries on a Wix site's backend. The new API includes:
+ [Creating a gallery](site-content/pro-gallery/create-gallery-item).
+ [Creating a gallery item](site-content/pro-gallery/create-gallery).
+ [List Galleries](site-content/pro-gallery/list-galleries).
+ [List Gallery items](site-content/pro-gallery/list-gallery-items).

(January 17, 2023)

## New Release: [Media](media)

The new Media API
enables 3rd-parties to view and manage content in the [Media Manager](media/media-manager) such as:
+ [Importing a file](media/media-manager/files/import-file) to the Media Manager.
+ [Generating a video streaming URL](media/media-manager/files/generate-video-streaming-url).
+ [Searching for a file](media/media-manager/files/search-files) in the Media Manager.
+ [Creating a new folder](media/media-manager/folders/create-folder) in the Media Manager. 
+ [Getting a folder](media/media-manager/folders/get-folder) from the Media Manager. 

(January 17, 2023)

## New Release: [Wix Automations](wix-automations)

The new Wix Automations API
introduces configuration options for you to become a
[trigger provider](wix-automations/introduction#how-to-become-a-trigger-provider).
As a trigger provider,
your custom triggers and trigger payloads
are installed with your app,
allowing site collaborators to create automations
triggered by events you report and control.

(January 15, 2023)

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
