SortOrder: 2
# Ratings: Supported Filters and Sorting

The following table shows field support for filters and sorting for rating properties:


| Fields      | Supported Filters | Sortable |
| ----------- | ------------ | ------------- |
| `id` | `$eq`, `$ne`, `$in` | Sortable |
| `group` | `$eq`, `$ne`, `$in` |  |          |
| `entityId` | `$eq`, `$ne`, `$in` |          |
| `attributeId` | `$eq`, `$ne`, `$in` |          |
| `value` | `$eq`, `$ne`, `$in`, `$lt`, `$lte`, `$gt`, `$gte` | Sortable |
| `owner.contactId` | `$eq`, `$ne`, `$in` |          |
| `owner.anonymousVisitorId` | `$eq`, `$ne`, `$in` |          |
| `owner.memberId` | `$eq`, `$ne`, `$in` |          |
| `relatedEntityIds` | `$hasSome`, `$hasAll` |          |
| `createdDate` | `$eq`, `$ne`, `$in`, `$lt`, `$lte`, `$gt`, `$gte` | Sortable |
