SortOrder: 2
# Abandoned Checkouts: Supported Filters and Sorting

The table below shows field support for filters and sorting for the base set of abandoned checkout properties.

| Field                        | Supported Filters                             | Sortable | 
| ---------------------------- | --------------------------------------------- | -------- |
| `id`                         | `$eq`, `$ne`, `$in`, `$exists`                |          |
| `createdDate`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `updatedDate`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `status`                     | `$eq`                                         | Sortable |
| `buyerInfo.email`            | `$eq`                                         |          |
| `totalPrice.amount`          | `$eq`, `$gt`, `$lt`, `$gte`, `$lte`           | Sortable |
| `totalPrice.convertedAmount` | `$eq`, `$gt`, `$lt`, `$gte`, `$lte`           | Sortable |