SortOrder: 5
# Comments: Supported Filters and Sorting

The following table shows field support for filters and sorting for the comment object:

| Field              | Supported Filters                             | Sortable |
| ------------------ | --------------------------------------------- | -------- |
| `id`               | `$eq`, `$ne`, `$in`                           |          |
| `contextId`        | `$eq`, `$ne`, `$in`                           |          |
| `resourceId`       | `$eq`, `$ne`, `$in`                           |          |
| `author.userId`    | `$eq`, `$ne`, `$in`                           |          |
| `author.memberId`  | `$eq`, `$ne`, `$in`                           |          |
| `author.visitorId` | `$eq`, `$ne`, `$in`                           |          |
| `parentComment.id` | `$eq`, `$ne`, `$in`                           |          |
| `parentIdsInThread`| `$hasAll`, `$hasSome`, `$isEmpty`             |          |
| `replyCount`       | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `status`           | `$eq`, `$ne`, `$in`                           |          |
| `voteSummary.netVoteCount` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `rating`       | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`        | Sortable |
| `reactionSummary.total` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `marked`       | `$eq`, `$ne`                                      | Sortable |
