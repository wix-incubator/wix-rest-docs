SortOrder: 8
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
> Some apps from Wix create their own extended fields.
> For a list of those fields and their filter and sorting options, see
> [Extended Fields Managed by Wix](#extended-fields-managed-by-wix)

| Field | Data Type/Format | Supported Filters | Sortable | Searchable |
|---|---|---|---|---|
| `id` | GUID string | `$eq`, `$ne`, `$in`, `$nin` | | |
| `createdDate` | UTC datetime string in `YYYY-MM-DDThh:mm:ss.sss` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable | |
| `updatedDate` | UTC datetime string in `YYYY-MM-DDThh:mm:ss.sss` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | | |
| `lastActivity.activityDate` | UTC datetime string in `YYYY-MM-DDThh:mm:ss.sss` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable | |
| `primaryInfo.email` | Valid email string | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | Sortable | |
| `primaryInfo.phone` | Valid phone string | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | | |
| `info.name.first` | String | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | Sortable | Searchable |
| `info.name.last` | String | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | Sortable | Searchable |
| `info.emails.email` | Valid email string | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | | Searchable |
| `info.phones.phone` | String | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | | Searchable |
| `info.addresses.street` | String | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | | |
| `info.addresses.city` | String | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | | |
| `info.addresses.subdivision` | ISO 3166-2 subdivision code (e.g., `US-NY`) | `$eq`, `$ne`, `$in`, `$nin` | | |
| `info.addresses.country` | Country ISO 2 letter code | `$eq`, `$ne`, `$in`, `$nin` | | |
| `info.company` | String | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | Sortable | |
| `info.jobTitle` | String | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith` | Sortable | |
| `info.birthdate` | Date string in `YYYY-MM-DD` format. | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable | |
| `info.locale` | Locale code (Example: `en-us` for U.S. English) | `$eq`, `$ne`, `$in`, `$nin` | | |
| `info.labelKeys` | String | `$hasSome`, `$hasAll` | | |
| `info.locations` | GUID string | `$hasSome`, `$hasAll` | | |
| `info.extendedFields.custom.{key}` | String | `$eq`, `$ne`, `$in`, `$startsWith` | Sortable | |
| `info.extendedFields.custom.{key}` | Number | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable | |
| `info.extendedFields.custom.{key}` | Date string in `YYYY-MM-DD` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable | |

### Extended Fields Managed by Wix

Some Wix apps add their own extended fields.
The table below shows a list of these fields and their attributes
so your app can make use of them through the REST API.

| Field | Description | Read-Only | Data Type | Supported Filters | Sortable |
|---|---|---|---|---|---|
| `info.extendedFields.contacts.displayByFirstName` | Concatenated name, starting with first name. | Read-only | `TEXT` | `$exists` | |
| `info.extendedFields.contacts.displayByLastName` | Concatenated name, starting with last name. | Read-only | `TEXT` | | |
| `info.extendedFields.ecom.lastPurchaseDate` | Last Wix Stores purchase in UTC datetime `YYYY-MM-DDThh:mm[:ss][.sss]` format. | Read-only | `DATE` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `info.extendedFields.ecom.numOfPurchases` | Count of Wix Stores purchases. | Read-only | `NUMBER` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `info.extendedFields.ecom.totalSpentAmount` | Total currency amount of Wix Stores purchases. | Read-only | `NUMBER` | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `info.extendedFields.ecom.totalSpentCurrency` | [Three-letter currency code][iso-4217-currency] of Wix Stores purchases. | Read-only | `TEXT` | | |
| `info.extendedFields.emailSubscriptions.deliverabilityStatus` | Supported values: `VALID`, `BOUNCED`, `SPAM_COMPLAINT`, `INACTIVE`. | Read-only | `TEXT` | `$eq`,`$ne`,`$in`, `$nin` | |
| `info.extendedFields.emailSubscriptions.effectiveEmail` | | Read-only | `TEXT` | `$exists` | Sortable |
| `info.extendedFields.emailSubscriptions.subscriptionStatus` | Supported values: `SUBSCRIBED`, `UNSUBSCRIBED`, `NOT_SET`, `PENDING`. | Read-only | `TEXT` | `$eq`,`$ne`,`$in`, `$nin` | |
| `info.extendedFields.invoices.vatId` | Government-issued VAT ID. | | `TEXT` | | |
| `info.extendedFields.members.membershipStatus` | Supported values: `APPROVED`, `DENIED`, `PENDING`, `INACTIVE`. | Read-only | `TEXT` | `$eq`,`$ne`,`$in`, `$nin` | |
| `info.extendedFields.members.mobile` | Supported values: `true`, `false`. | | `TEXT` | | |

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