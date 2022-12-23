SortOrder: 1
# Posts: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the Post object:

| Field               | Supported Filters                                                                     | Sortable |
| ------------------- | ------------------------------------------------------------------------------------- | -------- |
| `id`                | `$eq`, `$ne`, `$hasSome`                                                              | Sortable |
| `title`             | `$eq`, `$ne`, `$contains`, `$startsWith`, `$endsWith`, `$hasSome`, `$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in`    | Sortable |
| `firstPublishedDate`| `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`                                     | Sortable |
| `lastPublishedDate` | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`                                     | Sortable |
| `slug`              | `$hasSome`, `$hasAll`                                                                 |          |
| `featured`          | `$eq`, `$ne`                                                                          | Sortable |
| `pinned`            | `$eq`, `$ne`                                                                          | Sortable |
| `categoryIds`       | `$hasSome`, `$hasAll`                                                                 |          |
| `memberId`          | `$eq`, `$ne`, `$hasSome`                                                              |          |
| `hashtags`          | `$hasSome`, `$hasAll`                                                                 |          |
| `commentingEnabled` | `$eq`, `$ne`                                                                          | Sortable |
| `minutesToRead`     | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`                                     |          |
| `tagIds`            | `$hasSome`, `$hasAll`                                                                 |          |
| `pricingPlanIds`    | `$hasSome`, `$hasAll`                                                                 |          |
| `language`          | `$eq`, `$ne`, `$hasSome`, `$exists`, `$in`                                            |          |
| `translationId`     | `$eq`, `$ne`, `$exists`, `$in`                                                        |          |
| `metrics.views`     | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`, `$in`                                     | Sortable |
| `metrics.comments`  | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`, `$in`                                     | Sortable |
| `metrics.likes`     | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`, `$in`                                     | Sortable |


__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Posts](https://dev.wix.com/api/rest/wix-blog/blog/posts/query-posts)
