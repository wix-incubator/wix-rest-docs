SortOrder: 1
# CRM Tasks: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the task object:

| Field         | Supported Filters                          | Sortable |
| ------------- | ------------------------------------------ | -------- |
| `id`          | `$eq`, `$ne`, `$in`                        | Sortable |
| `createdDate` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `updatedDate` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `dueDate`     | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `status`      | `$eq`, `$ne`, `$in`, `$nin`                |          |
| `contact.id`  | `$eq`, `$ne`, `$in`, `$exists`             |          |

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Tasks](https://dev.wix.com/docs/rest/api-reference/crm/tasks/task-v2/query-tasks)
