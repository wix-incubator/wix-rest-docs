# Release Notes

## New Release: [Wix Blog Post Stats API](https://dev.wix.com/api/rest/wix-blog/blog/post-stats/get-total-posts)

The [Wix Blog Post Stats API](https://dev.wix.com/api/rest/wix-blog/blog/post-stats/get-total-posts) provides the ability to get the total number of posts published to a blog, and to filter for number of posts published per month. (October 28, 2021)

## New Release: [Wix Restaurants Orders API](https://dev.wix.com/api/rest/wix-restaurants/orders)

The [Wix Restaurants Orders API](https://dev.wix.com/api/rest/wix-restaurants/orders) provides the ability to retrieve orders and update their statuses.
(October 26, 2021)

## New Release: [Marketing Tags API](https://dev.wix.com/api/rest/marketing/marketing-tags)

The [Marketing Tags API](https://dev.wix.com/api/rest/marketing/marketing-tags) provides the ability to manage embedded marketing tags.
(October 26, 2021)

## New Release: [Query Service Catalog](https://dev.wix.com/api/rest/wix-bookings/service-catalog/services/query-service-catalog)

The Query Service Catalog endpoint replaces
[List services](https://dev.wix.com/api/rest/wix-bookings/service-catalog/services/list-services),
which has been deprecated.
(October 13, 2021)

## New Webhooks: [Contacts v4](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-object)

The Contacts v4 API introduces the
[Contact Created](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-created-webhook),
[Contact Updated](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-updated-webhook),
and [Contact Deleted](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-deleted-webhook)
webhooks.  
This deprecates the
[Contacts v1](https://dev.wix.com/api/rest/contacts/contacts/contacts-v1-(deprecated)/contact-object)
webhooks.
(September 13, 2021)

## New Release: [Query Bookings Resources](https://dev.wix.com/api/rest/wix-bookings/resources/query-resources)

The Query Resources endpoint replaces
[List Resources](https://dev.wix.com/api/rest/wix-bookings/resources/list-resources),
which has been deprecated.
(September 13, 2021)

## New Data: [Bookings Resources](https://dev.wix.com/api/rest/wix-bookings/resources)

`location.businessLocation` field added to [Resource](https://dev.wix.com/api/rest/wix-bookings/resources/resource-object) object.  
Note that the `location.businessLocation.businessSchedule` object is not supported by Wix Bookings.
(September 13, 2021)

## New Release: [FAQ API](https://dev.wix.com/api/rest/site-content/faq)

The [FAQ API](https://dev.wix.com/api/rest/site-content/faq) provides the ability to view and manage the questions and answers in the FAQ app.
(August 24, 2021)

## New Data: [App Instance API](https://dev.wix.com/api/rest/app-management/apps/app-instance)

`ownerEmail` field added to [Get App Instance](https://dev.wix.com/api/rest/app-management/apps/app-instance/get-app-instance) endpoint response.
(August 8, 2021)

## New Data: [Stores Orders API](https://dev.wix.com/api/rest/wix-stores/orders)

`order.shippingInfo.code` field added to [Wix Stores Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object) object.  
The `code` field can be used by carrier services / fulfillers to see orders shipped by them.
(July 25, 2021)
