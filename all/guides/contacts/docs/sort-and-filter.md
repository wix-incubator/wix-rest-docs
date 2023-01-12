SortOrder: 5

# Contacts: Supported Filters, Sorting, and Search

This article covers field support for filtering, sorting, and searching
in the Contacts API,
including for extended fields.

## Contact properties: Supported filters, sorting, and search

The table below shows field support for filters, sorting,
and free-text searching
for the base set of contact properties.
It doesn't include extended fields (those are covered in the sections below).

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

## Extended Fields: Supported filters, sorting, and search

The table below shows field support for filters, sorting,
and free-text searching
for the Wix-defined extended fields (also known as system fields).

> **Note:**
> When querying or sorting,
> extended field names are flattened to a dot-separated string, like this:
> `"info.extendedFields.{key}"`.
> For example, to query the `emailSubscriptions.effectiveEmail` extended field,
> use this flattened field name:
> `"info.extendedFields.emailSubscriptions.effectiveEmail"`.

| Field                                     | Supported Filters         | Sortable | Searchable |
| ----------------------------------------- | ------------------------- | -------- | ---------- |
| `invoices.vatId`                          |                           |          |            |
| `members.membershipStatus`                | `$eq`,`$ne`,`$in`, `$nin` |          |            |
| `emailSubscriptions.deliverabilityStatus` | `$eq`,`$ne`,`$in`, `$nin` |          |            |
| `emailSubscriptions.subscriptionStatus`   | `$eq`,`$ne`,`$in`, `$nin` |          |            |
| `emailSubscriptions.effectiveEmail`       | `$exists`                 | Sortable |            |

## Custom Fields: Supported filters, sorting, and search

Extended fields that are created by 3rd-party apps or site contributors
are known as _custom fields_.
Site contributors can add, remove, and change custom field names
from the
[Contact List](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Fcontacts)
in their site's Dashboard.

The table below shows field support for filters, sorting,
and free-text searching
for custom fields.

> **Note:**
> When querying or sorting,
> extended field names are flattened to a dot-separated string, like this:
> `"info.extendedFields.{key}"`.
> For example, to query the `custom.newCustomer` extended field,
> use this flattened field name:
> `"info.extendedFields.custom.newCustomer"`.

| Data Type/Format                   | Supported Filters                          | Sortable |
| ---------------------------------- | ------------------------------------------ | -------- |
| String                             | `$eq`, `$ne`, `$in`, `$startsWith`         | Sortable |
| Number                             | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| Date string in `YYYY-MM-DD` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Contacts](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/query-contacts)
