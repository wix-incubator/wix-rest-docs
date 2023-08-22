SortOrder: 2
# Reviews: Supported Filters and Sorting

The following table shows field support for filters and sorting for review properties:

| Fields      | Supported Filters | Sortable |
| ----------- | ----------- | ----------- |
| `id` | `$eq`, `$ne`, `$in` |          |
| `namespace` | `$eq`, `$ne`, `$in` |          |
| `entityId` | `$eq`, `$ne`, `$in` |          |
| `content.rating` | `$eq`, `$ne`, `$in`, `$lt`, `$lte`, `$gt`, `$gte` | Sortable |
| `content.media` | `$isEmpty` |          |
| `helpfulness` | `$eq`, `$ne`, `$in`, `$lt`, `$lte`, `$gt`, `$gte` | Sortable |
| `moderation.moderationStatus` | `$eq`, `$ne`, `$in` |          |
| `createdDate` | `$eq`, `$ne`, `$in`, `$lt`, `$lte`, `$gt`, `$gte` | Sortable |