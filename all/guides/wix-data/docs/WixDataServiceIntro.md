SortOrder: 0
# About the Wix Data API

The Wix Data API provides a complete solution for accessing, organizing, configuring, and managing data stored in a Wix project or site's database.

With the Wix Data API, you can:

+ Create, modify, and delete [data collections](https://dev.wix.com/api/rest/wix-data/wix-data/data-collections).
+ Access, manage, and perform aggregations on [data items](https://dev.wix.com/api/rest/wix-data/wix-data/data-items) stored in a site's existing data collections.
+ Create [indexes](https://dev.wix.com/api/rest/wix-data/wix-data/indexes) for data collections, to speed up data queries.
+ Connect [external databases](https://dev.wix.com/api/rest/wix-data/wix-data/external-database-connections) to a Wix site.

## Before you begin

It's important to note the following points before starting to code:

+ A Wix project or site's database can store up to 10 GB of data.
+ A Wix project or site's database can hold up to 1000 data collections.
+ The maximum size of an item you can save to a collection is 500 kb.
+ When naming fields in data collections, we recommend avoiding special characters. You can do this by using field names that match this regex pattern: `[a-zA-Z_][a-zA-Z0-9_-]{0,63}`.
+ Each data collection defines a schema of fields for the items it contains. However, this schema isn't enforced. This means that if you add or update an item containing a field or data type that doesn't match the collection's schema specification, your data is stored anyway.
+ When using data retrieval endpoints such as [Query Data Items](https://dev.wix.com/api/rest/wix-data/wix-data/data-items/query-data-items) or [Get Data Item](https://dev.wix.com/api/rest/wix-data/wix-data/data-items/get-data-item) following an update to a collection's data, the data retrieved may not yet contain the most recent changes. See [Wix Data and Eventual Consistency](https://dev.wix.com/api/rest/wix-data/wix-data/eventual-consistency) for more information and instructions for overriding this.
+ After connecting external database collections to a Wix site using the [External Database Connections API](https://dev.wix.com/api/rest/wix-data/wix-data/external-database-connections), you can use the Data Items API to manage and retrieve data from those collections as if they were Wix Data collections.

## Permissions

Access to a [data collection](https://dev.wix.com/api/rest/wix-data/wix-data/data-collections) is controlled by its permissions. These permissions are defined in the collection object and they specify which types of user can perform actions on the data contained in the collection.

Wix Data recognizes 4 roles: 
* `ADMIN`: The site owner.
* `SITE_MEMBER_AUTHOR`: A signed-in user who has added content to the collection.
* `SITE MEMBER`: Any signed-in user.
* `ANYONE`: Any site visitor.

For each of the 4 basic actions (inserting, updating, removing, and reading content) the minimal role required must be set. For example, if you want to allow only site members to view data, and only the site owner to insert, update, and remove data, declare your permissions as follows:
* `insert`: `ADMIN`
* `update`: `ADMIN`
* `remove`: `ADMIN`
* `read`: `SITE_MEMBER`

## Terminology

+ **Data collection:** A schema determining the structure of data items to be stored, defining the fields each item should contain and the data type of each field.
+ **Data item:** A single data entry in a collection, in JSON format.
+ **Index:** A map of a collection's data, organized according to selected fields. An index is used to increase query speed, and in some cases, to enforce unique values.
+ **External database connection:** An adaptor that translates Wix data requests from a Wix site or app into an external database's protocol, and translates the response back into a format that Wix APIs can read. This enables Wix APIs, apps, and sites to treat the external database exactly as if it was an internal data collection.