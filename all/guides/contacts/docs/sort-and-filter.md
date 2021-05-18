SortOrder: 9
# Sort and Filter

_List_ and _Query_ endpoints allow sorting results by field.
Use `field:ASC` to sort results in ascending order,
and `field:DESC` to sort in descending order.

For example, to sort contacts by first name in descending order:

```json
{
  "sort": {
    "fieldName": "info.name.first",
    "order": "DESC"
  }
}
```

The default sort is `createdDate:ASC`.

Refer to the table below to check which fields support sorting.

## Field Support for Filtering, Sorting, and Searching

The table below shows field support for filters, sorting,
and free-text searching.

> **Note:**
> This table lists only the core Contact List fields.
> For information on working with extended fields —
> including fields managed by other Wix apps —
> see [Extended Fields][md-ext-fields].

| Field                        | Data Type/Format                                                                                                                 | Supported Filters                             | Sortable | Searchable |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | -------- | ---------- |
| `id`                         | GUID string.                                                                                                                     | `$eq`, `$ne`, `$in`, `$exists`                |          |            |
| `createdDate`                | UTC datetime string in `YYYY-MM-DDThh:mm:ss.sss` format.                                                                         | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |            |
| `updatedDate`                | UTC datetime string in `YYYY-MM-DDThh:mm:ss.sss` format.                                                                         | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    |          |            |
| `lastActivity.activityDate`  | UTC datetime string in `YYYY-MM-DDThh:mm:ss.sss` format.                                                                         | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |            |
| `primaryInfo.email`          | Valid email string.                                                                                                              | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `primaryInfo.phone`          | Valid phone string.                                                                                                              | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |            |
| `info.name.first`            | String.                                                                                                                          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable | Searchable |
| `info.name.last`             | String.                                                                                                                          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable | Searchable |
| `info.emails.email`          | Valid email string.                                                                                                              | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          | Searchable |
| `info.phones.phone`          | String.                                                                                                                          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          | Searchable |
| `info.addresses.street`      | String.                                                                                                                          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |            |
| `info.addresses.city`        | String.                                                                                                                          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |            |
| `info.addresses.subdivision` | Code for a subdivision (such as state, prefecture, or province) in [ISO 3166-2](https://www.iso.org/standard/72483.html) format. | `$eq`, `$ne`, `$in`, `$exists`                |          |            |
| `info.addresses.country`     | Two-letter country code in [ISO-3166 alpha-2](https://www.iso.org/obp/ui/#search/code/) format.                                  | `$eq`, `$ne`, `$in`, `$exists`                |          |            |
| `info.company`               | String.                                                                                                                          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `info.jobTitle`              | String.                                                                                                                          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `info.birthdate`             | Date string in `YYYY-MM-DD` format.                                                                                              | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |            |
| `info.locale`                | Locale code (for example, `en-us` for U.S. English).                                                                             | `$eq`, `$ne`, `$in`, `$exists`                |          |            |
| `info.labelKeys`             | String.                                                                                                                          | `$hasSome`, `$hasAll`                         |          |            |
| `info.locations`             | GUID string.                                                                                                                     | `$hasSome`, `$hasAll`                         |          |            |

## Examples

**Get contacts named 'John'**

```sh
curl 'https://www.wixapis.com/contacts/v4/contacts/query' \
  --data-binary '{"filter":{"info.name.first": "John"}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get contacts with last name 'Smith', sorted by date of creation**

```sh
curl 'https://www.wixapis.com/contacts/v4/contacts/query' \
  --data-binary '{"filter": {"info.name.last": "Smith"}, \
  "sort": {"fieldName": "createdDate","order" : "ASC"}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get contacts by IDs**

```sh
curl 'https://www.wixapis.com/contacts/v4/contacts/query' \
  --data-binary '{"filter":{"id": {"$in": ["CONTACT_ID_1","CONTACT_ID_2"]}}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

[iso-4217-currency]: https://www.iso.org/iso-4217-currency-codes.html
[md-ext-fields]: ./extended-fields.md
