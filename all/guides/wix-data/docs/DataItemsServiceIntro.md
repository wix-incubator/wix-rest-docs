SortOrder: 1
# About the Data Items API

The Data Items API allows you to access and manage items in a Wix site's data collections.

With the Data Items API, you can:

+ Create and manage data items in a site's collections.
+ Retrieve data items from a collection individually or with filtering and sorting queries.
+ Create and manage reference fields.
+ Perform aggregations and calculations on data in collections.
+ Truncate a data collection, removing all its contents.

The Data Items API only works with existing collections. To create and manage data collections, use the [Data Collections API](/docs/wix-data/data-collections).

## Before you begin

It's important to note the following points before starting to code:

+ The maximum size of an item you can save to a collection is 500 kb.
+ We don't recommend updating a data item more than once per second.
+ When using data retrieval endpoints such as [Query Data Items](/docs/wix-data/data-items/query-data-items) or [Get Data Item](/docs/wix-data/data-items/get-data-item) following an update to a collection's data, the data retrieved may not yet contain the most recent changes. See [Wix Data and Eventual Consistency](/docs/wix-data/eventual-consistency) for more information and instructions for overriding this.
+ When querying Wix App Collections, check which fields can be filtered in the relevant collection field article.
+ Updating a data item replaces the existing item entirely. If the existing item had fields with values and those fields aren't included in the updated item, the values in those properties are lost.
+ Aggregations can't be performed on Wix App collections.
+ After connecting external database collections to a Wix site using the [External Database Connections API](/docs/wix-data/external-database-connections), you can use the Data Items API to manage and retrieve data from those collections as if they were Wix Data collections.
