SortOrder: 0
# About Translation Schemas

The core of every Wix site comprised mostly out of its content, written by the site owner.
With the Translation services, site owners can adapt (translate) their user generated content (AKA UGC) for every language and locale their site includes.
The content can be represented with a variety of types such as: text, rich text, images, video and more.
This service manages the Translation Schemas, which helps to model the TPA's domain entities.

The Translation Schema API allows your app to:
- Change the model of your data by performing CRUD operations on your Schema
- Validate your content by adding restrictions to it like: min length, max length, format, etc

In order to manage Translated Content, see [Translation Content Service]() <!--- TODO: Add link after Translation Content is generated -->

This service is part of [Wix Multilingual solution](https://support.wix.com/en/article/about-wix-multilingual).

## Use cases

REST:

- As an app (TPA) owner, you can create, update, and delete Schemas that represent your App's entities.
- As a Translation Manager, you can query the Schemas with different filters, in order to show your users what entities they can translate.


## Terminology

- Schema Key: A compound key that acts as a unique representation of a schema. It contains the following fields:
  1. App ID - the ID of the TPA
  2. Entity type - defines which entity of the TPA this schema represents (like product, ribbon, event, etc)
  3. Scope - whether this schema represents the entity for all sites or for a specific site
- SchemaField: The description of a unique field on your app's entity. It contains metadata such as: FieldType, display name and more. The schema object contains a map of SchemaField Ids to SchemaField objects.