SortOrder: 6
# Sorting, Filtering, and Searching

_List_ and _Query_ endpoints allow you to filter and sort results
based on some contact properties and extended field values.
This article covers field support for filtering and sorting.

## Sorting

The method you use to sort results depends
on whether you're calling a
[List endpoint](#sorting-list-endpoints)
or a
[Query endpoint](#sorting-query-endpoints).
Instructions for both methods are covered below.

By default, contacts are sorted by `createdDate` in ascending order.

### Sorting List Endpoints

_List_ endpoints are designed to be lightweight. They support basic functionality
for specifying which results you want returned.
For this reason, when working with a _List_ endpoint,
sorting is applied through the `sort.fieldName` and `sort.order` query parameters.

For example, to list contacts by last name in ascending order,
append these query parameters to the request:

```txt
?sort.fieldName=info.name.last&sort.order=DESC
```

### Sorting Query Endpoints

_Query_ endpoints contain more robust filtering capabilities
than _List_ endpoints.
When working with a _Query_ endpoint,
sorting is specified in the request body
with the `query.sort.fieldName` and `query.sort.order` parameters.

For example, to list contacts by last name in ascending order,
include this code in the request body:

```json
{
  "query": {
    "sort": {
      "fieldName": "info.name.last",
      "order": "ASC"
    }
  }
}
```

## Contact Properties: Filtering, Sorting, and Searching

The table below shows field support for filters, sorting,
and free-text searching.

| Field                        | Supported Filters                             | Sortable | Searchable |
| ---------------------------- | --------------------------------------------- | -------- | ---------- |
| `id`                         | `$eq`, `$ne`, `$in`, `$exists`                |          |            |
| `createdDate`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |            |
| `updatedDate`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    |          |            |
| `lastActivity.activityDate`  | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |            |
| `primaryInfo.email`          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `primaryInfo.phone`          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |            |
| `info.name.first`            | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable | Searchable |
| `info.name.last`             | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable | Searchable |
| `info.emails.email`          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          | Searchable |
| `info.phones.phone`          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          | Searchable |
| `info.addresses.street`      | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |            |
| `info.addresses.city`        | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` |          |            |
| `info.addresses.subdivision` | `$eq`, `$ne`, `$in`, `$exists`                |          |            |
| `info.addresses.country`     | `$eq`, `$ne`, `$in`, `$exists`                |          |            |
| `info.company`               | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `info.jobTitle`              | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith` | Sortable |            |
| `info.birthdate`             | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |            |
| `info.locale`                | `$eq`, `$ne`, `$in`, `$exists`                |          |            |
| `info.labelKeys`             | `$hasSome`, `$hasAll`                         |          |            |
| `info.locations`             | `$hasSome`, `$hasAll`                         |          |            |

## Extended Fields: Filtering, Sorting, and Searching

> **Deprecation Notice**
>
> These extended fields have been deprecated
> and will be removed on March 31, 2022:
>
> - `contacts.displayByFirstName`
> - `contacts.displayByLastName`
> - `ecom.lastPurchaseDate`
> - `ecom.numOfPurchases`
> - `ecom.totalSpentAmount`
> - `ecom.totalSpentCurrency`
> - `members.mobile`

[Extended fields](https://dev.wix.com/api/rest/contacts/contacts/extended-fields)
allow apps to add to the available data in the Contact List.
In addition to the default fields, some Wix apps manage their own extended fields.

> **Note:**
> When working directly with the [contact object](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-object),
> data in extended fields must be accessed using bracket notation, like this:
> `info.extendedFields["{key}"]`.
> However, when querying or sorting,
> extended field names are flattened with dot notation, like this:
> `"info.extendedFields.{key}"`.

| Field                                     | Supported Filters         | Sortable | Searchable |
| ----------------------------------------- | ------------------------- | -------- | ---------- |
| `invoices.vatId`                          |                           |          |            |
| `members.membershipStatus`                | `$eq`,`$ne`,`$in`, `$nin` |          |            |
| `emailSubscriptions.deliverabilityStatus` | `$eq`,`$ne`,`$in`, `$nin` |          |            |
| `emailSubscriptions.subscriptionStatus`   | `$eq`,`$ne`,`$in`, `$nin` |          |            |
| `emailSubscriptions.effectiveEmail`       | `$exists`                 | Sortable |            |

## Custom Fields: Filtering, Sorting, and Searching

Extended fields that are created by 3rd-party apps and site contributors
are known as _custom fields_.
Site contributors can add, remove, and change custom field names
from the
[Contact List](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Fcontacts)
in their site's Dashboard.

| Data Type/Format                   | Supported Filters                          | Sortable | Searchable |
| ---------------------------------- | ------------------------------------------ | -------- | ---------- |
| String                             | `$eq`, `$ne`, `$in`, `$startsWith`         | Sortable |            |
| Number                             | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |            |
| Date string in `YYYY-MM-DD` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |            |

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
