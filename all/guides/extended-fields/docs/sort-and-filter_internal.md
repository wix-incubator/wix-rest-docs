SortOrder: 2
# Sort and Filter

_Query_ endpoint allows sorting results by field.
Use `field:ASC` to sort results in ascending order,
and `field:DESC` to sort in descending order.

For example, to sort extended fields by first name in descending order:

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
| `fieldType`                        | String ( `SYSTEM` / `USER_DEFINED`)                     | `$eq`                                      |          |
| `dataType`                         | String ( `TEXT` / `NUMBER` / `DATE` / `URL` )           | `$eq`, `$ne`                               |          |

## Examples

**Get extended fields with namespace 'custom'**

```sh
curl 'https://www.wixapis.com/contacts/v4/extended-fields/query' \
  --data-binary '{"filter":{"namespace": "custom"}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get extended fields with label type 'USER_DEFINED', sorted by date of creation**

```sh
curl 'https://www.wixapis.com/contacts/v4/extended-fields/query' \
  --data-binary '{"filter": {"fieldType": "USER_DEFINED"}, \
  "sort": [{"fieldName": "createdDate","order" : "ASC"}}]' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get extended fields by keys**

```sh
curl 'https://www.wixapis.com/contacts/v4/extended-fields/query' \
  --data-binary '{"filter":{"key": {"$in": ["custom.number","custom.website-1"]}}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```
