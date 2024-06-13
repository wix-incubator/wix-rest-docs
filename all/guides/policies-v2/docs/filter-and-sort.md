SortOrder: 3
# Policies v2: Supported Filters and Sorting

The following table shows field support for filters and sorting for the Policy object:

| Field              | Query Filter Operators                                                            | Sortable |
|--------------------|-----------------------------------------------------------------------------------|----------|
| `id`               | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$hasSome`, `$exists`  | Sortable |
| `eventId`          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$hasSome`, `$exists`  | Sortable |
| `name`             | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$hasSome`, `$exists`  | Sortable |
| `body`             | `$eq`, `$ne`, `$lt`, `$lte,` `$gt`, `$gte`, `$in`, `$nin`, `$hasSome`, `$exists`  | Sortable |
| `revision`         | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$hasSome`, `$exists`  | Sortable |      
| `updatedDate`      | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$hasSome`, `$exists`  | Sortable |
| `createdDate`      | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$hasSome`, `$exists`  | Sortable |

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Policy Query endpoint](https://dev.wix.com/api/rest/wix-events/policy-v2/query-policies)