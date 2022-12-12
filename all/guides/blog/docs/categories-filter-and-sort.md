SortOrder: 4
# Categories: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the Category object:

| Field             | Supported Filters                                                                        | Sortable |
| ----------------- | ---------------------------------------------------------------------------------------- | -------- |
| `id`              | `$eq`, `$ne`, `$hasSome`                                                                 |          |
| `title`           | `$eq`, `$ne`, `$contains`, `$startsWith`, `$endsWith`, `$hasSome`,`$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in` | Sortable |
| `label`           | `$eq`, `$ne`, `$contains`, `$startsWith`, `$endsWith`, `$hasSome`,`$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in` | Sortable |
| `postCount`       | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`                                        | Sortable |
| `displayPosition` | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`                                        | Sortable |
| `translationId`   | `$eq`, `$ne`, `$exists`, `$in`                                                           |          |
| `language`        | `$eq`, `$ne`, `$exists`, `$in`                                                           | Sortable |
| `slug`            | `$hasSome`, `$hasAll`                                                                    | Sortable |


__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query endpoint 1](https://dev.wix.com/api/rest/wix-blog/blog/categories/query-categories)