SortOrder: 2
# Sort and Filter

_Query_ endpoint allows sorting results by field.
Use `field:ASC` to sort results in ascending order,
and `field:DESC` to sort in descending order.

For example, to sort labels by first name in descending order:

```json
{
  "sort": {
    "fieldName": "createdDate",
    "order": "DESC"
  }
}
```

The default sort is `createdDate:ASC`.

Refer to the table below to check which fields support sorting.

## Field Support for Filtering, Sorting

The table below shows field support for filters and sorting.

| Field                              | Data Type/Format                                        | Supported Filters                          | Sortable |
| ---------------------------------- | ------------------------------------------------------- | ------------------------------------------ | -------- |
| `key`                              | String                                                  | `$eq`, `$ne`, `$in`                        |          |
| `legacyId`                         | String                                                  | `$eq`, `$ne`, `$in`                        |          |
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
  "sort": [{"fieldName": "createdDate","order" : "ASC"}}]' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get labels by keys**

```sh
curl 'https://www.wixapis.com/contacts/v4/labels/query' \
  --data-binary '{"filter":{"key": {"$in": ["custom.demo-label","custom.awesome"]}}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```
