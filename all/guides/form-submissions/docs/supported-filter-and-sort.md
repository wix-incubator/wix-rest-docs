SortOrder: 2
# Form Submissions: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the form submission object:

| Field           | Supported Filters                             | Sortable |
| --------------- | --------------------------------------------- | -------- |
| `id`            | `$eq`, `$ne`, `$in`, `$nin`                   | Sortable |
| `createdDate`   | `$eq`, `$gt`, `$gte`, `$in`, `$lt`, `$lte`, `$ne`, `$nin` | Sortable |
| `updatedDate`   | `$eq`, `$gt`, `$gte`, `$in`, `$lt`, `$lte`, `$ne`, `$nin` | Sortable |
| `formId`        | `$eq`, `$ne`, `$in`, `$nin`                   | Sortable |
| `namespace`     | `$eq`, `$ne`, `$in`, `$nin`                   | Sortable |
| `properties`    | `$eq`, `$ne`                                  | Sortable | 
| `status`        | `$eq`, `$ne`, `$in`, `$nin`                   | Sortable |



__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Submissions](https://dev.wix.com/api/rest/drafts/form-submissions/query-submission)
