SortOrder: 2
# Sort and Filter

_List_ and _Query_ endpoints allow you to sort and filter results
based on some label properties.
This article covers field support for sorting and filtering.

## Sorting

The method you use to sort results depends on whether you're calling a
[List endpoint](#sorting-list-endpoints)
or a
[Query endpoint](#sorting-query-endpoints).
Instructions for both methods are covered below.

By default, labels are sorted by `createdDate` in descending order.

### Sorting List Endpoints

_List_ endpoints are designed to be lightweight. They support basic functionality
for specifying which results you want returned.
For this reason, when working with a _List_ endpoint,
sorting is applied through the `sort.fieldName` and `sort.order` query parameters.

For example, to list labels by display name in ascending order,
append these query parameters to the request:

```txt
?sort.fieldName=displayName&sort.order=ASC
```

### Sorting Query Endpoints

_Query_ endpoints contain more robust filtering capabilities
than _List_ endpoints.
When working with a _Query_ endpoint,
sorting is specified in the request body
with the `query.sort.fieldName` and `query.sort.order` parameters.

For example, to list labels by display name in ascending order,
include this code in the request body:

```json
{
  "query": {
    "sort": {
      "fieldName": "displayName",
      "order": "ASC"
    }
  }
}
```

Refer to the table below to check which fields support sorting.

## Field Support for Sorting and Filtering

The table below shows field support for filters and sorting.

| Field                              | Data Type/Format                                        | Supported Filters                          | Sortable |
| ---------------------------------- | ------------------------------------------------------- | ------------------------------------------ | -------- |
| `key`                              | String                                                  | `$eq`, `$ne`, `$in`                        |          |
| `displayName`                      | String                                                  | `$eq`, `$ne`, `$in`, `$startsWith`         | Sortable |
| `createdDate`                      | UTC datetime string in `YYYY-MM-DDThh:mm:ss.sss` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `updatedDate`                      | UTC datetime string in `YYYY-MM-DDThh:mm:ss.sss` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `namespace`                        | String                                                  | `$eq`, `$ne`                               |          |
| `labelType`                        | String ( `SYSTEM` / `USER_DEFINED` / `WIX_APP_DEFINED` )| `$eq`                                      |          |

## Examples

**Get labels with namespace 'custom'**

```sh
curl 'https://www.wixapis.com/contacts/v4/labels/query' \
  --data-binary '{"filter":{"namespace": "custom"}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get labels with label type 'USER_DEFINED', sorted by date of creation**

```sh
curl 'https://www.wixapis.com/contacts/v4/labels/query' \
  --data-binary '{"filter": {"labelType": "USER_DEFINED"}, \
  "sort": [{"fieldName": "createdDate","order" : "ASC"}]}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get labels by keys**

```sh
curl 'https://www.wixapis.com/contacts/v4/labels/query' \
  --data-binary '{"filter":{"key": {"$in": ["custom.demo-label","custom.awesome"]}}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```
