SortOrder: 2
# Filter and Sort

Select endpoints allow sorting results by field. Use `field:asc` to sort results in **ascending** order, and `field:desc` to sort in **descending** order.

For example, to sort events by start date in ascending order, and then by modification date in descending order: 

```
?sort=start:asc,modified:desc
```

or 

```json
"sort": "start:asc,modified:desc"
```

Refer to the following tables to check which fields support sorting.

## List Agenda Items
| Field            | Description             | Sorting | Facets  |
|------------------|-------------------------|---------|---------|
| stage_name       |                         |         | Allowed |
| track_name       |                         |         | Allowed |
| host_name        |                         |         | Allowed |


[//]: # (Full list of operators for reference: $eq,$ne,$lt,$lte,$gt,$gte,$hasSome,$in,$contains,$startsWith,$endsWith,$urlized,$exists)
