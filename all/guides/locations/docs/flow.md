SortOrder: 2
# Sample use cases & flows: Locations


This article shares a possible use case for your app, as well as an example flow that supports it.
You're certainly not limited to this use case, but it can be a helpful jumping off point as you plan your app's implementation.


## Set Up a New Main Business Location


Your app can help the site owners create a new business location, set it as default, and update the opening hours for a location.


1. Call the [Create Location](https://dev.wix.com/api/rest/business-info/locations/create-location) endpoint.

2. Set the new location as **default** via the [Set Default Location](https://dev.wix.com/api/rest/business-info/locations/set-default-location) endpoint.

3. List all existing locations by calling the [List Locations](https://dev.wix.com/api/rest/business-info/locations/list-locations) endpoint.

   > **Note:** Make sure to extract the relevant locations’ IDs from the response and save it for future calls.


4. Update a location's opening hours via the [Update Location](https://dev.wix.com/api/rest/business-info/locations/update-location) endpoint.

   > **Note:** Currently, it isn't possible to partially update a location. Therefore, you'll need to pass the full location object in the body of the call.