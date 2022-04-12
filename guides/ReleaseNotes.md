# Release Notes

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
APIs exposed include Sites, Site Folders and Resellers. (February 24, 2022)  

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
