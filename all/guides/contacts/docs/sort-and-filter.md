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
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>' \
  --data-binary '{
    "query": {
      "filter": {
        "info.name.first": "John"
      }
    }
  }'
```

**Get contacts with last name 'Smith', sorted by date of creation**

```sh
curl 'https://www.wixapis.com/contacts/v4/contacts/query' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>' \
  --data-binary '{
    "query": {
      "filter": {
        "info.name.last": "Smith"
      },
      "sort": [
        {
          "fieldName": "createdDate",
          "order": "ASC"
        }
      ]
    }
  }'
```

**Get contacts by IDs**

```sh
curl 'https://www.wixapis.com/contacts/v4/contacts/query' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>' \
  --data-binary '{
    "query": {
      "filter": {
        "id": {
          "$in": [
            "de73c8ad-fbaf-490d-a385-2d53b26b3777",
            "4511f1d2-c129-4b4f-a17c-99dcf07e2a2e"
          ]
        }
      }
    }
  }'
```

[iso-4217-currency]: https://www.iso.org/iso-4217-currency-codes.html
[md-ext-fields]: ./extended-fields.md
