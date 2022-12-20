SortOrder: 3
# Draft Posts: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the Draft Post object:

| Field                   | Supported Filters                                                                  | Sortable |
| ----------------------- | ---------------------------------------------------------------------------------- | -------- |
| `id`                    | `$eq`, `$ne`, `$hasSome`, `$not`                                                   | Sortable |
| `title`                 | `$eq`, `$ne`, `$contains`, `$startsWith`, `$endsWith`, `$hasSome`, `$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in` | Sortable |
| `excerpt`               | `$eq`, `$ne`, `$contains`, `$startsWith`, `$endsWith`, `$hasSome`, `$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in` | Sortable |
| `featured`              | `$eq`, `$ne`                                                                       | Sortable |
| `categoryIds`           | `$hasSome`, `$hasAll`                                                              |          |
| `memberId`              | `$eq`, `$ne`, `$hasSome`                                                           |          |
| `hashtags`              | `$hasSome`, `$hasAll`                                                              |          |
| `commentingEnabled`     | `$eq`, `$ne`                                                                       | Sortable |
| `minutesToRead`         | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`                                  |          |
| `tagIds`                | `$hasSome`, `$hasAll`                                                              |          |
| `pricingPlanIds`        | `$hasSome`, `$hasAll`                                                              |          |
| `translationId`         | `$eq`, `$ne`, `$contains`, `$startsWith`, `$endsWith`, `$hasSome`, `$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in` |          |
| `language`              | `$eq`, `$ne`, `$contains`, `$startsWith`, `$endsWith`, `$hasSome`, `$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in` |          |
| `status`                | `$eq`, `$ne`, `$contains`, `$startsWith`, `$endsWith`, `$hasSome`, `$lt`, `$lte`, `$gt`, `$gte`, `$exists`, `$in` |          |
| `hasUnpublishedChanges` | `$eq`, `$ne`                                                                       |          |
| `editedDate`            | `$lt`, `$lte`, `$gt`, `$gte`                                                       | Sortable |
| `scheduledPublishDate`  | `$lt`, `$lte`, `$gt`, `$gte`                                                       | Sortable |


__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query endpoint 1](https://dev.wix.com/api/rest/wix-blog/blog/draft-posts/query-draft-posts)
