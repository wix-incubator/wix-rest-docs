SortOrder: 0

# Locations

Locations service is the multi location platform which enables users to manage their business in multiple locations. <br/>
For discussions, bug reports, announcements and other bits please use the 
[#multi-location-dev](https://wix.slack.com/messages/multi-location-dev/) channel on Slack.

## Background 
The motivation for Locations service came originally from our top verticals (Restaurants, Bookings & Stores) which could not provide a solution for growing users or new users that already have more than a single business location.

For example: A chain restaurants that has 3 different branches. Each branch requires flexibility to define it's own Work hours, Contact Information, Menu's, Reservation/Order settings and more...

## User Interface
Currently there are 3 different interfaces where locations can be set:

1. Dashboard Settings - Business Info
Each user can enter the Dashboard Settings Business Info page and create or manage his business locations

2. Biz Mgr - Locations Modal
The Biz Mgr Locations Modal is a platformized solution which allows any Biz Mgr application to load a "Add New Location" modal on top of their application. <br/>
For example: A Bookings user is creating a new service and he would like to assign it to a new location which is not created. <br/>
Bookings will show an option to select "New Location" within the service creation flow that will trigger the Location modal.

3. Location Platform
Our platformised API which supports all CRUD functions.

## Common Questions

### Default Location 

Default location exists if there is an address in SiteProperties and then it remains synced with the Properties.
The user can also change the default location and then its Site Properties will be also changed accordingly.
Also, site can have only one default location

Default locations allows Biz Mgr applications to use a specific location details in cases where a specific location is not defined. <br/>
This scenario can happen especially in use cases where products do not support multi location

Default location exists if there is an address in SiteProperties and then it remains synced with the Properties. <br/>
The user can also change the default location and then its Site Properties will be also changed accordingly. Also, a site can have only one default location.

### Archive Location
Location cannot be deleted, but it can be archived. 
Fetching only non-archived locations can be done via [ListLocations](https://github.com/wix-private/wixos/blob/master/locations/proto/com/wixpress/locations/locations-service.proto#L40). 
This API can be provided with a flag to include archived locations in the response.

### Location Name

The location name is automatically derived from the Street name from the formatted address. <br/>
In case the street name is not available, the location name will be Location 1,2,3... based on its position.
From competitors research, we've noticed many business present their branch/location name based on the street name. <br/>
As we understand that the location name is a critical input (as it's used across verticals presenting the list of available locations), <br/>
we want to assure that the user a good starting point entering a valid location name that will be easily consumed both by himself within different product usages across Wix and by his site visitors.

## API
￿
Locations service funcionality is exposed via 
[com.wixpress.locations](https://github.com/wix-private/wixos/blob/master/locations/proto/com/wixpress/locations/locations-service.proto) package, 
which includes the following components:

* [￿Location](https://github.com/wix-private/wixos/blob/master/locations/proto/com/wixpress/locations/locations-service.proto#L131-L146) provides the location entity.
    
* [LocationService](https://github.com/wix-private/wixos/blob/master/locations/proto/com/wixpress/locations/locations-service.proto) is the primary API, which can be consumed by RPC & REST.
It provides CRUD capabilities and SetDefaultLocation endpoint.


#### Request headers

All API calls should be with metaSiteId in context. <br/> 
This should be done by sending signed instance from client or with server signing with metaSiteId

#### Required Permissions

Read flows: Query, Get - LOCATIONS.READ <br/>
Write flows: Create, Update, Delete, SetDefault - LOCATIONS.MANAGE

#### Default Location Use

* Default location can be only set through SetDefaultLocation endpoint.
* Can't be updated through the Create & Update methods and can't be deleted through Delete.


### Setup

Bazel Target
```
@wixos//locations:proto_scala
```

Service Url
```ruby
<%= rpc_service_url("com.wixpress.wixos.locations-web") %>
```
 
### Code Examples

#### RPC
 
```scala

// Locations Grpc client 
val locationsService: LocationsServiceWithCallScope = ...

// Querying site locations
val query = wix.common.Query() // common query object
val locations = locationsApi.queryLocations(QueryLocationsRequest(query)).locations

// Create location
val data = Some(Location(name = "New Location", address = ...)) // location data
val locationCreated = locationsApi.createLocation(CreateLocationRequest(data)).location

// Set default location
val newDefaultLocationId = ...
val defaultLocation = locationsApi.setDefaultLocation(SetDefaultLocationRequest(newDefaultLocationId)).location
```

#### REST

```javascript
const baseUrl = `/_api/locations-web/v1/locations/`;
const headers = { authorization: ${ signedInstance } };

// Querying site locations
await axios.get(url, { headers });

// Create location
const location = {
  name: 'New Location',
  timeZone: 'ASIA/JERUSALEM'
  address: ...
  .
  .
};
await axios.post(url, { location }, { headers });

// Set default location
const newDefaultLocationId = ...
await axios.post(url + newDefaultLocationId +'/set-default', { id: ${newDefaultLocationId } }, { headers });
```

### Notifications on Greyhound

Locations notifications are the the standard domain events notifications and are based on [DomainEvents](https://github.com/wix-private/p13n/blob/master/protos/domain-events/src/main/proto/wix/common/domainevents/domainevents.proto) 
[Guide](https://github.com/wix-private/server-infra/tree/master/iptf/domain-events#where-can-i-find-domain-event-for-a-given-entity) to consume our platformized Domain Events.
* Topic: domain_events_com.wixpress.locations.Location
* Each change in Create, Update, Delete endpoints will trigger its corresponding message in Domain Events.
* When setting default location, update message on both location (previous and current default) will be sent, also with a [SetDefaultLocation](https://github.com/wix-private/wixos/blob/master/locations/proto/com/wixpress/locations/locations-service.proto#L125-L129) message

### Testkit

#### Setup

```
@wixos//locations/testkit/com/wixpress/locations:locations
```  

#### Use

##### Environment Setup

```scala
val locationsTestkit = new LocationsTestkit()
val embeddedGrpcServer = new GrpcManagedService(port = grpcPort, locationsTestkit.locationsTestkit) 
```

Use embeddedGrpcServer as a collaborator
##### Test

```scala
val locationData: Location = Location(name = "New Location", address = ...)
val createdLocation: CreateLocationResponse = locationsTestkit.givenLocation(locationData) // given a location exists
val locationServiceClient = ... // locations service grpc client

locationServiceClient.getLocation(createdLocation.getId).location must beSome(createdLocation)
```
