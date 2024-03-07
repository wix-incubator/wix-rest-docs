SortOrder: 1
# Events v3: Supported Filters and Sorting

The following table shows field support for filters and sorting for the Events object:

| Field                                  | Query Filter Operators                                                | Sortable |
|----------------------------------------|-----------------------------------------------------------------------|----------|
| `id`                                   | `$eq`, `$ne`, `$in`, `$hasSome`  | Sortable |
| `title`                                | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$hasSome`  | Sortable |
| `slug`                                 | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$hasSome`  | Sortable |   
| `updatedDate`                          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$hasSome`  | Sortable |
| `createdDate`                          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$hasSome`  | Sortable |
| `status`                               | `$eq`, `$ne`, `$in`, `$hasSome`                                | Sortable |
| `userId`                               | `$eq`, `$ne`, `$in`, `$hasSome`                                | Sortable |
| `registration.initialType`             | `$eq`                               | Not sortable |
| `dateAndTimeSettings.startDate`        | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$hasSome`  | Sortable |
| `dateAndTimeSettings.endDate`          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$hasSome`  | Sortable |


__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Events Query endpoint](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/query-ticket-definitions)