SortOrder: 1
# About the Locations API



With Locations, site owners can define multiple physical locations for their business. This allows them to set individual opening hours for each location.

The Locations API allows your app to:

* List existing locations
* Create, update, and archive locations
* Set a default location that is reflected in the site properties

Read more about how site owners can manage their [location specific bookings](https://support.wix.com/en/article/wix-bookings-offering-services-at-multiple-locations). You can also read more about how to retrieve the [site properties](https://dev.wix.com/api/rest/business-info/site-properties/properties/get-site-properties).


## Terminology


+ **Default location:** Location reflected in the [site properties](https://dev.wix.com/api/rest/business-info/site-properties/introduction). This location is used on invoices.
+ **Type:** Describes whether a location is an office, reception, branch or the headquarters.
+ **Status:** Indicates whether a location is `ACTIVE` or `INACTIVE`.
+ **Business Schedule:** Describes the location's regular and exceptional opening hours.
    - **Period:** Regular, weekly recurring opening hours of the location.
    - **Special Hour Period:** Exception to the location's regular hours. The location can be either open or closed during the **Special Hour Period**.


## Limitations

+ The [Wix Bookings API](https://dev.wix.com/api/rest/wix-bookings/about-wix-bookings) doesn't support the `businessSchedule` object.
+ You can't delete a location. Instead, you can archive a location using the [Archive Location](https://dev.wix.com/api/rest/business-info/locations/archive-location) endpoint.
+ You can't archive the default location.
+ Archived locations can't be unarchived.
+ The [Update Location](https://dev.wix.com/api/rest/business-info/locations/update-location) endpoint replaces a location. Currently, you can't partially update a location.
+ Currently, the location type is just informational and doesn't affect a location's functionality.
+ The status `INACTIVE` isn't currently supported.

