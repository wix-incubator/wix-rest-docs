SortOrder: 2
# Marketing Consent: Supported Filters and Sorting

The table below shows field support for filters and sorting for the base set of marketing consent properties.

| Field                        | Supported Filters                             | Sortable | 
| ---------------------------- | --------------------------------------------- | -------- |
| `id`                         | `$eq`, `$ne`, `$in`, `$exists`                |          |
| `createdDate`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `updatedDate`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `details.email`              | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |
| `details.phone`              | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |
| `state`                      | `$eq`, `$ne`, `$in`                           |          |
