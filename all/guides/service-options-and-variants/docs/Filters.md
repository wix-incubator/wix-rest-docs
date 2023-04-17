SortOrder: 2
# Service Variants and Options: Supported Filters and Sorting

Query endpoints allow you to filter and sort results based on service variant and
options properties. This article covers field support for filtering and sorting.

## Filtering

Specify the [Query Service Options and Variants](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants/query-service-options-and-variants) `filter` object in the following format: 

```json
"filter" : 
  { 
    "fieldName": "value",
  }
```


The following table shows field support for filters and sorting
for the `serviceOptionsAndVariants` object:

| Field           | Supported Filters                             | Sortable |
| --------------- | --------------------------------------------- | --------------- |
| `id` | `eq`, `ne`, `in` | Sortable |
| `serviceId` | `eq`, `ne`, `in` |   |
| `options.values` | `exists` |   | 
| `options.values.id` | `hasSome`, `hasAll` |   | 
| `options.values.type` | `hasSome`, `hasAll` |   | 
| `options.values.optionSpecificData.customData.name` | `hasSome`, `hasAll` |   | 
| `variants.values` | `exists` |   | 
| `variants.values.choices.choice.custom.value` | `hasSome`, `hasAll` |   | 
| `variants.values.price` | `hasSome`, `hasAll` |   |
| `variants.values.choices.optionId` | `hasSome`, `hasAll` |   |



## Sorting 

[Query Service Options and Variants](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants/query-service-options-and-variants) 
runs with this default:

- sorted by `id` in `ASC` order


Specify the `sort` object in the following format:

```json
"sort" : [ 
  { 
    "fieldName":"sortField1",
    "order":"ASC"
  },
  { 
    "fieldName":"sortField2",
    "order":"ASC"
  },
]
```


## Paging 

By default `pagingMetadata.cursors` are returned, unless you specifically pass 
`query.paging`.

The maximum for `cursorPaging.limit` is `100`.

If you pass a cursor token that you have received in a previous query response, 
passing additional sort or filter information results in an invalid cursor 
error. This is because the received cursor token already holds all the needed information 
for sort and filter. Changing the sort and filter properties during the span of 
a cursor query isn't supported. You may provide a different limit though.

__Related content:__
+ [API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language)
+ [Sorting and Paging](https://dev.wix.com/api/rest/getting-started/sorting-and-paging)
+ [Field Projection](https://dev.wix.com/api/rest/getting-started/field-projection)
+ [Query Service Options and Variants endpoint](https://dev.wix.com/api/rest/wix-bookings/services/query-service-options-and-variants)
