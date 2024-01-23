SortOrder: 0
# Localization

## About Localization
The core of every Wix site comprised mostly out of it's content, written by the site owner.
With Localization, site owners can adapt (localized) it's user generated content (AKA UGC) for every language and locale their site includes.
The content can be represented with a variety of types such as: text, rich text, images, video and more.
The service consists of two sub-domains: Content and Content-Schema.
The Content-Schema helps to model the TPA's domain entities, while the Content domain is designed to hold the localized entities themselves.

The Localization Content-Schema API allows your app to:
- Change the model of your data by performing CRUD operations on your Content-Schema
- Validate your content by adding restrictions to it like: min length, max length, format, etc

The Localization Content API allows your app to:
- Localize the content of your site by performing CRUD operations on your Content
- Manage the life-cycle of your translations from initial proposal state to approved and published
- Track the history of your content changes, and revert to any previous revision at any time

This service is part of [Wix Multilingual solution](https://support.wix.com/en/article/about-wix-multilingual).

## Terminology
- Language Tag: Language unique identifier in [IETF BCP 47 tag format](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers).
This format allows separate also between different tongues of the same language such as traditional Chinese and spoken Chinese.
- Content-Schema: Defines the metadata of the TPA's domain entities. Every entity may have a different schema.
The schema can be specific for each site, or can be global. It is not possible to upload localized content for entity without setting the entity schema first.
- Schema Key: A compound key that acts as a unique representation of a schema. It contains the following fields:
 1. App id - id of the TPA
 2. Entity type - defines which entity of the TPA this schema represents (like product, ribbon, event, etc)
 3. Scope - whether this schema represents the entity for all sites or for a specific site
- Localized Content: Holds all the "translations" of all the fields of a specific entity for every language of the site.
- Content Key: A compound key that acts as a unique representation of a content. It contains the following fields:
 1. Schema Key - key of the schema this entity belongs to
 2. Entity Id - unique id that represents the given entity

## Limitations
- Since the service requires static modeling of the TPA entities, Localization cannot support schema-free entities.
 However, it is possible to create a schema which includes all fields variations, and adding partial entity.
- Localization does not handle currency conversions
- Localization does not in charge of managing site languages, only storing the actual localized data
- The published content that resides in the live site, and that is shown to the site end users, cannot be fetched via this service.
This specific purpose is covered by an extension of this service called Localization Public. 

## Use Cases
Listed here below are few exemplary use cases your app might need to support, and the relevant flows in this service that could cover them.
You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.
<br>
`Initial Setup`
<br>
As a first step, your TPA must integrate with Localization, by uploading the metadata of all your entities. 
Entity can be any object in your domain, such as product for Stores, or form for Booking.
In order to do that, use the *CreateOrUpdateContentSchemaByKey* API. Here you define the fields of every entity and their constraints.
It is advised to mark schemas as hidden at this stage, since generally there is no reason to show schemas until they have contents linked to them.
For changes in existing schema, you can use the *UpdateContentSchema* API if more convenient.
<br> 
`Import Content In Primary Language/Translate Content To Secondary Language`
<br>
Once schemas are ready, you can upload the content of your entities' fields in any of your site supported languages. It is
preferred to start with the primary language, and then add the translations on subsequent calls.
To do so, use the *CreateOrUpdateContentsByKey* API. This is a bulk API, so you could upload multiple entities in one request.
Every upload is limited to one language.
For changes in existing contents, you can use the *UpdateContents* API if more convenient.
Once you are done uploading your contents, don't forget to remove the "hidden" mark from your schemas.
If you wish to expose your translations to UoU, make sure they are marked as "published" when you upload.
<br> 
`Export Site Content`
<br>
Site owner might wish to export content in a given language to a professional translator.
To fetch existing contents from your site, use the *ListContents* API. You may filter the results by specifying specific
ids, app id, entity, language, or any combination of them.
<br> 
`Revert Translation To A Previous Version In History`
<br>
If you are unhappy with the current translation of your entity, and you want to revert it back to previous value, you may 
do the following:
 1. Get all content revisions by calling *GetContentHistory* or *GetContentHistoryByKey* API.
 2. Choose the desired revision and upload it. It will replace the current version.
 3. You may need to repeat step 2 for every language you want to make this change.
<br> 
`Track Changes In Your Entities`
<br>
When you create a new content, it triggers a *Content Created Event*, which expose the created content, as well as the id associated with
this content. Some API require using id as identification - this id can be retrieved from this event.
If you want to synchronize your system with Localization service, you may listen to the changes in your contents using these events:
 1. Content Created Event
 2. Content Updated Event
 3. Content Deleted Event