SortOrder: 5
# Filter and Sort

## Guidelines

Read [these guidelines](https://dev.wix.com/api/rest/getting-started/api-query-language) to get more information on how to construct a correct query request with filtering and sorting.

## List & Query Events


| Field                          | Query Filter Operators                          | Sorting |
|--------------------------------|-------------------------------------------------|---------|
| created                        | $eq,$ne,$lt,$lte,$gt,$gte,$in                   | Allowed |
| modified                       | $eq,$ne,$lt,$lte,$gt,$gte,$in                   | Allowed |
| id                             | $eq,$ne,$in                                     |   N/A   |
| title                          | $eq,$ne,$lt,$lte,$gt,$gte,$in                   | Allowed |
| slug                           | $eq,$ne,$lt,$lte,$gt,$gte,$in                   |   N/A   |
| status                         | $eq,$ne,$in                                     | Allowed |
| userId                         | $eq,$ne,$in                                     |   N/A   |

