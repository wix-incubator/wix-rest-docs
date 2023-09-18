SortOrder: 0

# Site Properties

Site Properties is a service that holds all the public information about the site/business in one single place, such as its name, address, contact info and more.
It’s a single source of truth of the data across all the verticals, so the user have only one place to update its details, no vertical/horizontal should need to manage its own data about a site/business, and all the apps will always be synced.

For discussions, bug reports, announcements and other bits please use the 
[#site-management](https://wix.slack.com/messages/site-management/) channel on Slack.

## Domain - All the data in Site Properties

|Basic Info|Contact Info|Location|Regional|Opening Hours|
|---|---|---|---|---|
|Business Name|Email|Address (Country, State, City, Street, <br> Apartment, Zip, Description, Has physical address)|Locale|Business Schedule [Example](https://gist.github.com/orgar28/5b6285f175507e408898e7aae4727bdc)|
|Site Display Name|Phone||Language||
|Logo|Fax||Multilingual||
|Description|||Payment Currency||
|Category (+subcat) [Possible Values](https://github.com/wix-private/wix-templates-cms-translations/blob/6389f89757fffdef3801f0f6196f2c00c27152ed/categories/categories_en.json)|||Timezone [Possible Values](https://github.com/wix-private/wix-locale-data/blob/master/app/scripts/locale/wix-locale-data/localeData_en.json#L240:L488)||


## User Interface

Coupled with Site Properties, is the General Info tab under Settings in the Business Manager

![General Info](https://s3.amazonaws.com/wixplorer-readme-images/site-properties%2Fgeneral_info1.png)
![General Info](https://s3.amazonaws.com/wixplorer-readme-images/site-properties%2Fgeneral_info2.png)

## Common use cases

* “We have a language settings in our app. How do we sync it?”
    * Start listening to the Greyhound message, and update your app’s data accordingly.
    * Don’t update only your own app - you should direct users to use General Info.
* “We have a business name field in our app. How do we sync it?”
    * Start listening to the Greyhound message, and update your app’s data accordingly.
    * One of the two options:
        * Update Site Properties on every update in your app
        * Remove the update option in your product, and direct the users to update in the General Info
* “We don’t support a specific language. How can we inform the user?”
    * We have [specific API in the Business Manager](https://github.com/wix-private/business-settings-api#api) to warn the user in the General Info before saving a change in certain fields such as language and currency: 
       ![Regional Settings](https://s3.amazonaws.com/wixplorer-readme-images/site-properties%2Fgeneral_info3.png)

## Common Questions

### Q: What’s the difference between language and locale?

* Language (e.g. “en”) determines the site language that will be displayed to the user of user on the site. It’s a list of (currently) 29 languages Wix’s verticals supports. It also used in the html of the site for SEO and browsers support purposes.
* Locale (e,g, “en-US”) determines the formats that will be used across the site: date and time, currency, units and measurements, and first day of the week.

### Q: Why do we have both? Locale already holds a language in it

* We don’t support all languages, but we can support all locales.
* We can allow special combinations, such as a site in hebrew for users in the US.


## About The API

### Concepts

Site Properties are a set of business-related values associated with a particular MetaSite. This is modelled as a
stream of versioned _events_ (as in an event-sourced system), which can be accessed as-is or materialized
into _snapshots_; a snapshot is essentially a key-value container that represents site properties at a given point in
time (or _version_). Versions are monotonously increasing and represent a logical _clock_ for a particular event stream.

### Data

We have an API over protobuf that allows you to get and set data.

### Notifications

In many cases you have the data in your app's storage, but still want to be synced with Site Properties. 
For that we have a messaging solution called Greyhound (based on Kafka), that allows you get a message for every change made to the data.


## API

The Site Properties functionality is exposed via the 
[com.wixpress.siteproperties.api.v4](https://github.com/wix-private/wixos/tree/master/site-properties/site-properties-api-proto/src/main/proto/com/wixpress/siteproperties/api/v4) package, 
which includes the following components:

* [Properties](http://wixplorer.wixpress.com/site-properties/reference/properties) provides the
  actual property types available;
* [Notifications](https://github.com/wix-private/wixos/blob/master/site-properties/site-properties-api-proto/src/main/proto/com/wixpress/siteproperties/api/v4/notifications.proto) consist the data that is sent on greyhound topic on each update;
    
[SitePropertiesV4](https://github.com/wix-private/wixos/blob/master/site-properties/site-properties-api-proto/src/main/proto/com/wixpress/siteproperties/api/v4/service.proto#L43) is the primary API, which can be consumed by RPC & REST.
It provides a read & update capabilities.

* [Read](http://wixplorer.wixpress.com/site-properties/reference/properties/.com.wixpress.siteproperties.api.v4.-site-properties-v4.-read) gets fields which is a sequence of wanted properties. 
If the endpoint got no fields to return, it will return all the properties exist for the site.

* [Update](http://wixplorer.wixpress.com/site-properties/reference/properties/.com.wixpress.siteproperties.api.v4.-site-properties-v4.-update) gets fields which is a sequence of wanted properties, and their values in properties object. 
For each field that was specified, there need to be a value in the properties object.

### Authentication
The entities that we serve on Api Gateway are authorized User and Service - Therefore the request has to include user session or server signing. Moreover, when performing a request, it also needs to include [Authorization header or server signing](https://github.com/wix-private/platformization-guidelines/blob/master/guides/auth.md) in order to resolve the designated site.

 

### Setup

You'll first need to depend on `site-properties-api` in your POM:

```
@wixos//site-properties/site-properties-api-proto/src/main/proto:proto_scala
```

The service URL can be configured via the usual .erb macro:
```ruby
<%= rpc_service_url("com.wixpress.siteproperties.site-properties-service") %>
```
 
### RPC
 
```scala
import com.wixpress.siteproperties.api.v4._
import com.wixpress.siteproperties.api.v4.SitePropertiesV4Grpc.SitePropertiesV4
import scala.concurrent.Await
import scala.concurrent.duration.Duration
import com.google.protobuf.field_mask.FieldMask


val storage: SitePropertiesV4 = ... // An RPC proxy declared normally

// Reading a snapshot;
val fields = Some(FieldMask(Seq("email", "siteDisplayName"))) //the properties requested - Defaults to all properties
val request: PropertiesReadRequest = PropertiesReadRequest(fields)
val response: PropertiesReadResponse = Await.result(sitePropertiesV4.read(request), 50 millis)  
val email = response.properties.get.email
val siteDisplayName = response.properties.get.siteDisplayName

// Writing properties:
val fields: FieldMask = Some(FieldMask(Seq("email", "siteDisplayName"))) //the properties that are upadted
val properties: Properties = Some(Properties(email = Some("newEmail@wix.com"), siteDisplayName = Some("newSiteName"))) // the values of the properties
val request = PropertiesUpdateRequest(fields = fields, properties = properties)
val response: PropertiesUpdateResponse = Await.result(sitePropertiesV4.update(request), 50 millis)
```

### REST

```javascript
const properties = {
  siteDisplayName:'newSiteName',
  email: 'newEmail@wix.com'
};
const query = Object.keys(properties).map(fieldKey => `fields.paths=${fieldKey}`).join('&');
const url = `/_api/site-properties-service/properties?${query}`;
//url = `/_api/site-properties-service/properties?$fields.paths=siteDisplayName&fields.paths=email`;
const headers = {Authorization: 'MSID.464f9eab-f621-4e7e-b534-d1775e36e379'};

// Reading a snapshot;
axios.get(url, {headers}).then(res => console.log(res.data.properties));

//email: "amitle@wix.com"
//siteDisplayName: "My site 31"


// Writing properties:
axios.patch(url, {properties}, {headers}).then(res => console.log(res.data));
```

### Notifications on Greyhound

Site Properties issues notifications to interested consumers over a single 
[Greyhound](https://github.com/wix-private/wix-iptf/tree/master/greyhound/) topic. Each message is a single event
associated with a particular MetaSite, and translation map is made available on each message for embedded services
to resolve their particular IDs.
The translation map also states if the embedded service was migrated to SiteProperties

[Notifications](https://github.com/wix-private/wixos/blob/master/site-properties/site-properties-api-proto/src/main/proto/com/wixpress/siteproperties/api/v4/notifications.proto) object
provides the necessary information and DTOs to consume these notifications. 

#### Consuming Notifications

The Site Properties service emits a notification for each change event via a Greyhound topic named `site-properties.changes.v4`. The message on this queue are serialized messages of type `SitePropertiesNotification`; fundamentally, every event is composed of three parts:

* Metadata (site ID, the site version for this update etc.);
* One or more changed properties (represented by a `Properties` message and a field mask);
* A "translation map", detailing the embedded services comprising the site and their respective types, `appDefId`s if applicable, instance IDs (details of vertical migration to Site Properties are outside the scope of this document). 

#### Common Scenarios

* Maintaining a local view (or "read-only replica")
* Responding to property changes


### Testkit

Site Properties provides a testkit to ease integration. <br>
The testkit is a managed service and needs ApiGatewayFullTestkit. <br>
Also if the greyhound notifications are enabled, KafkaManagedService is required in the collaborators. <br>
 
#### Setup

```
@wixos//site-properties/site-properties-testkit
```  

#### Use

##### Environment Setup

```scala
val sitePropertiesTestkit = new SitePropertiesFullTestkit(
  port = 9904, // doesn't have to be 9904 but to be equal to the port you register the service 
  apiGatewayFullTestkit = apiGatewayTestkit, // needs ApiGatewayFullTestkit to get the context and identities
  enableNotifications = true // if greyhound notifications on changes needed
)
```
Raise sitePropertiesTestkit as ManagedService - `withCollaborators`

##### Test

```scala
val metaSiteId = randomGuid[_]
val properties = Some(v4.Properties(email = Some("test@wix.com")))
val fieldMask = Some(FieldMask(Seq("email")))
val updateRequest = PropertiesUpdateRequest(properties, fieldMask)

sitePropertiesTestkit.givenProperties(updateRequest, metaSiteId)  //updating testkit

// check update in production code 
val readRequest = new PropertiesReadRequest(fields = fieldMask)
Await.result(sitePropertiesV4.read(readRequest), 50 millis).properties 
```

##### Tips of Context Use

###### Setting Permissions To Users

Read Permissions
```scala
sitePropertiesTestkit.givenReadPermissionsForUser(userId: UserGuid, metaSiteId: Guid[_])
```
Update Permissions
```scala
sitePropertiesTestkit.givenUpdatePermissionsForUser(userId: UserGuid, metaSiteId: Guid[_])
```

###### Server Signing Use

If you use server signing in your production code. <br>
For the token to pass to the testkit, you need to first register your app in ApiGatewayFullTestkit with your app secret key.
```scala
apiGatewayTestkit.givenApp(appDefId,appSecretKey)
```

###### Signed Instance Use

If you pass the signed instance as part of the aspects. <br>
Trigger the flow that calls Site Properties with signed instance in the aspects.

```scala
ProtobufIdlRpcProxyFactoryTestBuilder(ApiGatewayFullTestkit.withIdentificationHeaderPair(signedInstance))
  .builderFor...
```

