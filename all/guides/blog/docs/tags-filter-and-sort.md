SortOrder: 4
# Tags: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the Tag object:

| Field                | Supported Filters                                                              | Sortable |
| -------------------- | ------------------------------------------------------------------------------ | -------- |
| `id`                 | `$eq`, `$ne`, `$hasSome`                                                       |          |
| `label`              | `$eq`, `$ne`, `$contains`, `$startsWith`, `$hasSome`, `$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in` | Sortable |
| `slug`               | `$eq`, `$ne`, `$startsWith`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`,`$hasSome`    | Sortable |
| `postCount`          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`                              | Sortable |
| `publishedPostCount` | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`                              | Sortable |
| `translationId`      | `$eq`, `$ne`, `$exists`, `$in`                                                 |          |
| `language`           | `$eq`, `$ne`, `$exists`, `$in`                                                 | Sortable |


__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query endpoint 1](https://dev.wix.com/api/rest/wix-blog/blog/tags/query-tags)
