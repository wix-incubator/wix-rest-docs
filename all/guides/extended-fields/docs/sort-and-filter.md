SortOrder: 2
# Extended Fields: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the extended field object:

| Field         | Supported Filters                          | Sortable |
| ------------- | ------------------------------------------ | -------- |
| `key`         | `$eq`, `$ne`, `$in`                        |          |
| `displayName` | `$eq`, `$ne`, `$in`, `$startsWith`         | Sortable |
| `createdDate` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `updatedDate` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `namespace`   | `$eq`, `$ne`                               |          |
| `fieldType`   | `$eq`                                      |          |
| `dataType`    | `$eq`, `$ne`                               |          |

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Extended Fields](https://dev.wix.com/api/rest/contacts/extended-fields/query-extended-fields)
