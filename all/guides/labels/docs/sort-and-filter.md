SortOrder: 2
# Contact Labels: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the label object:

| Field         | Supported Filters                          | Sortable |
| ------------- | ------------------------------------------ | -------- |
| `key`         | `$eq`, `$ne`, `$in`                        |          |
| `displayName` | `$eq`, `$ne`, `$in`, `$startsWith`         | Sortable |
| `createdDate` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `updatedDate` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `namespace`   | `$eq`, `$ne`                               |          |
| `labelType`   | `$eq`                                      |          |

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Labels](https://dev.wix.com/api/rest/contacts/labels/query-labels)
