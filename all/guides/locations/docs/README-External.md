SortOrder: 1

# Locations

## About Locations

With Wix Locations, site owners can define multiple physical locations for their business, so they can set individual opening hours, menus or pricing options for each location. 

The Multi Location APIs allow your app to:

* List existing locations
* Create, update, and archive locations
* Set a default location reflected in the site properties

Read more on how site owners can manage their [location specific bookings](https://support.wix.com/en/article/wix-bookings-offering-services-at-multiple-locations)
and [site properties](https://dev.wix.com/api/rest/business-info/site-properties)

## Terminology

* The default location is the main business location, which is reflected in and synced with the site properties. 
* The location type describes the functionality of a location, showing whether it is  an office, reception, branch or the headquarters.
* The location status reflects whether the location is active or inactive.
* Locations cannot be deleted, but they can be archived. Note, once a location has been archived, it can not be restored. A default location can not be archived. 

## Sample use cases & flows: Locations

This article shares some possible use cases for your app, as well as an example flow that could support each one. <br/>
You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.

### Set Up a new main location for a fitness chain

Imagine, the owner of a fitness chain is opening a new bigger studio to host all their new customers. 
The owner will also extend the opening hours to better accommodate the needs of the members. 
Your app will set up the new main studio location, update the existing location and change the default location. 
Later, your app may also support location specific bookings via the [Wix Bookings app](https://dev.wix.com/api/rest/wix-bookings/bookings/introduction).

#### Create Location
First, you will call the **Create Location** endpoint. The call needs to include a name, timezone and address. 

```curl
curl -X POST \
   'https://www.wixapis.com/locations/v1/locations' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>' \
   --data-binary '{
     "location": {
         "name":"South Figueroa Street",
         "default":false,
         "status":"ACTIVE",
         "locationType":"UNKNOWN",
         "timeZone":"America/Los_Angeles",
         "address":{
            "country":"US",
            "subdivision":"CA",
            "city":"Los Angeles",
            "postalCode":"90015",
            "streetAddress":{
               "number":"1111",
               "name":"South Figueroa Street",
               "apt":""
            },
            "formattedAddress":"STAPLES Center, South Figueroa Street, Los Angeles, CA, USA",
            "geocode":{
               "latitude":34.0430175,
               "longitude":-118.2672541
            }
         }
     }
   }'

Response:

{
  "location": {
     "id":"ea50573e-35fa-47ca-bba7-3e45a935d9bc",
     "name":"South Figueroa Street",
     "default":false,
     "status":"ACTIVE",
     "locationType":"UNKNOWN",
     "timeZone":"America/Los_Angeles",
     "address":{
        "country":"US",
        "subdivision":"CA",
        "city":"Los Angeles",
        "postalCode":"90015",
        "streetAddress":{
           "number":"1111",
           "name":"South Figueroa Street",
           "apt":""
        },
        "formattedAddress":"STAPLES Center, South Figueroa Street, Los Angeles, CA, USA",
        "geocode":{
           "latitude":34.0430175,
           "longitude":-118.2672541
        }
     },
     "revision":"1",
     "archived":false
  }
}
```

Remember to extract the new location’s id from the response for future calls.

#### Set Default Location
There can be only one default location, that is synced with the site properties. 
You will reflect this change via the **Set Default Location** endpoint. 
You'll need to pass the id of the new location, that you have collected in the previous example call.

```
curl -X POST \
  'https://www.wixapis.com/locations/v1/locations/ea50573e-35fa-47ca-bba7-3e45a935d9bc/set-default' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>' \
  --data-binary '{}'
```

#### List Locations
In order to update an existing location, your app will need to pass its id. 
Therefore, you will call the **List locations** endpoint. 
Later, your app may also use this information to support displaying the available locations within the Wix Bookings app. 
Then site visitors can select one or more locations in the create service form. 

```curl
curl -X GET \ 'https://www.wixapis.com/locations/v1/locations/' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

#### Update Location
Finally, your app will update the name of the location. 
You’ll do that by calling the **Update Location** endpoint.
 
```
curl -X PUT \
  'https://www.wixapis.com/locations/v1/locations/ea50573e-35fa-47ca-bba7-3e45a935d9bc' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>' \
  --data-binary '{
    "location": {
         "id":"ea50573e-35fa-47ca-bba7-3e45a935d9bc",
         "name":"South Figueroa Street",
         "default":false,
         "status":"ACTIVE",
         "locationType":"UNKNOWN",
         "timeZone":"America/Los_Angeles",
         "address":{
            "country":"US",
            "subdivision":"CA",
            "city":"Los Angeles",
            "postalCode":"90015",
            "streetAddress":{
               "number":"1111",
               "name":"South Figueroa Street",
               "apt":""
            },
            "formattedAddress":"STAPLES Center, South Figueroa Street, Los Angeles, CA, USA",
            "geocode":{
               "latitude":34.0430175,
               "longitude":-118.2672541
            }
         },
         "revision":"4",
         "archived":false
      }
  }'
```

