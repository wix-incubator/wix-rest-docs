SortOrder: 2
# Filter and Sort

Select endpoints allow sorting results by field. Use `"order": "ASC"` to sort results in ascending order, and `"order": "DESC"` to sort in descending order.

For example, to sort plans by created date in descending order:

```json
"sort": { "fieldName": "createdDate", "order": "DESC" }
```

Refer to the following tables to check which fields support sorting.

## Query Public Plans
[//]: # (https://bo.wix.com/wix-docs/rest/drafts/pricing-plans/plan-v2/query-public-plans)

| Field     | Description       | Query Filter Operators                                  | Sorting | 
|-----------|-------------------|---------------------------------------------------------|---------|
| id   |     Plan ID   |   $eq, $ne, $hasSome                      |  |         
| primary  | Whether the plan is marked as primary, and highlighted in the site with a custom ribbon |     $eq, $ne             | Allowed |        
| slug     | URL-friendly version of the plan name. Unique across all plans in the same site        |  $eq, $ne, $startsWith, $endsWith, $contains | Allowed | 
| createdDate       | Date plan was created           |    $eq, $ne, $gt, $ge, $lt, $le, $between    | Allowed |         
| updatedDate     |    Date plan was updated               | $eq, $ne, $gt, $ge, $lt, $le, $between   | Allowed |       
