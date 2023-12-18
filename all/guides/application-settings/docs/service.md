SortOrder: 1

# app-settings-service

  

A service that stores and retrieves client-side configurations and multilingual data for third party applications (aka TPAs), such as Stores and Booking. It exposes an API both for client (HTTP) and server (RPC). The API definitions can be found [here](/docs/proto/service.proto).

## Basic Concepts

The service handles the settings of an instance of an application in a given container (e.g. Editor, Viewer, Business Manager) and therefore gets and sets settings according to the following key

1. Application Id
2. Instance Id
3. One of two options, based on the preference of the client; (a) A unique identifier passed by the user or (b) The state of the object displayed (Saved / Published).

Data can be stored at a level of a specific component in the app, or for the app globally.

### External ID option 
The service support passing a unique identifier which is a reference settings stored. In this option the settings are immutable, and each write operation on an existing set of settings, produces a new copy of the updated settings with new external id which is returned in the response of the set operation.  

This helps the service to support revisions of settings in revision based interfaces such as the editor. The external id is saved on the site document (in the case of the editor/viewer), and therefore is updated across revisions, and therefore could be reverted when reverting the site.

#### App v. Component level
**In the get flow**: Passing the external id depends on the level onto which the settings apply, for global settings of the app, the externalAppId member should be passed, and for a specific component, the externalComponentId should be passed (in REST, it's external_app_id and external_component_id as query params).
- If both are passed, both are returned, in fields named appData and componentData respectively). 
- If a field mask is passed, it's applied to both.

**In the set flow**: The scope is passed explicitly, and the external id is part of the URL
e.g. settings/app/<external_id>/

Endpoints are: Get, Set and Update.

****Currently Multilingual data  is not supported in this option***
### State based option 
The service supports passing a collection of states of the component/app onto which the settings apply. State options could be either "SAVED" or "PUBLISHED". In this relatively simple case, the settings support only two revisions, one for the published object, and one for the saved one. Also, the host is passed as part of the key (e.g. Viewer, OneApp etc.).

When using this option, publishing the site, automatically creates a clone of the "saved" settings, with a "published" state under the hood.   

#### App v. Component
The service has different endpoints for component and app level settings:
- getComponentSettings
- setComponentSettings
- getGlobalSettings
- setGlobalSettings

## Data format

### Settings 
The settings are saved in a straight-forward manner as a plain JS object. New settings are merged with old ones 

### Multilingual data
The multilingual data is passed as an array of objects, representing a collection of languages and their translations (more data about the structure can be found [here](/docs/proto/service.proto)). 

Upon Get, only the translations of the requested language are returned. The selected language is inferred from the aspects (x-wix-linguist), or can be overridden explicitly as documented in the API.