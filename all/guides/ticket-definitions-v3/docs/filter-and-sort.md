SortOrder: 1
# Ticket Definitions v3: Supported Filters and Sorting

The following table shows field support for filters and sorting for the Ticket Definition object:

| Field                                  | Query Filter Operators                                                | Sortable |
|----------------------------------------|-----------------------------------------------------------------------|----------|
| `id`                                   | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `eventId`                              | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `name`                                 | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `description`                          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `limit`                                | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `pricing_method.pricing_type`          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `feeType`                              | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `saleStatus`                           | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |     
| `updatedDate`                          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `createdDate`                          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`  | Sortable |
| `hidden`                               | `$eq`, `$ne`, `$in`, `$nin`, `$exists`                                | Sortable |
| `pricing_method.free`                  | `$eq`, `$ne`, `$in`, `$nin`, `$exists`                                | Sortable |

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Ticket Definitions Query endpoint](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/query-ticket-definitions)