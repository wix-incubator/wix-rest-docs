SortOrder: 8
# Extended Fields

Extended fields allow apps to extend the default set of information
stored in the Contact List.
In addition to the core set of Contact List fields,
Wix manages some fields that integrate with apps created by Wix.
Just like the core Contact List fields,
these Wix-managed extended fields support field masks, field projection,
fieldsets, filtering, sorting, and searching.
See [Extended Fields Managed by Wix][wix-ext-fields] (below)
for more details.

Contact data in extended fields can be accessed
in the [Contact object][contact-obj]
under `info.extendedFields.{namespace}.{key}`.
The namespace is unique for each Wix app (for example, `ecom` or `members`).
All third party apps share the `custom` namespace.
All field keys must be unique within a namespace.

> **Note:**
> To view extended field definitions,
> or to manage your app's extended fields,
> use the [Extended Fields API][svc-fields].

## Custom Fields

Extended fields that are created by third party apps and site contributors
are known as _custom fields_.
Site contributors can add, remove, and change custom field names
from the [Contact List][dashboard-contact-list] in their site's Dashboard.

All custom fields use the `custom` namespace.
The following table shows sorting, filtering, and search support
for each custom field data type.

| Field                              | Data Type/Format                   | Supported Filters                          | Sortable |
| ---------------------------------- | ---------------------------------- | ------------------------------------------ | -------- |
| `info.extendedFields.custom.{key}` | String                             | `$eq`, `$ne`, `$in`, `$startsWith`         | Sortable |
| `info.extendedFields.custom.{key}` | Number                             | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `info.extendedFields.custom.{key}` | Date string in `YYYY-MM-DD` format | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |

## Extended Fields Managed by Wix

Some Wix apps add their own extended fields.
The table below shows a list of these fields and their attributes
so your app can make use of them through the REST API.

| Field                                                         | Description                                                                    | Read-Only | Data Type | Supported Filters                          | Sortable |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------- | --------- | ------------------------------------------ | -------- |
| `info.extendedFields.contacts.displayByFirstName`             | Concatenated name, starting with first name.                                   | Read-only | `TEXT`    | `$exists`                                  |          |
| `info.extendedFields.contacts.displayByLastName`              | Concatenated name, starting with last name.                                    | Read-only | `TEXT`    |                                            |          |
| `info.extendedFields.ecom.lastPurchaseDate`                   | Last Wix Stores purchase in UTC datetime `YYYY-MM-DDThh:mm[:ss][.sss]` format. | Read-only | `DATE`    | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `info.extendedFields.ecom.numOfPurchases`                     | Count of Wix Stores purchases.                                                 | Read-only | `NUMBER`  | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `info.extendedFields.ecom.totalSpentAmount`                   | Total currency amount of Wix Stores purchases.                                 | Read-only | `NUMBER`  | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte` | Sortable |
| `info.extendedFields.ecom.totalSpentCurrency`                 | [Three-letter currency code][iso-4217-currency] of Wix Stores purchases.       | Read-only | `TEXT`    |                                            |          |
| `info.extendedFields.emailSubscriptions.deliverabilityStatus` | Supported values: `VALID`, `BOUNCED`, `SPAM_COMPLAINT`, `INACTIVE`.            | Read-only | `TEXT`    | `$eq`,`$ne`,`$in`, `$nin`                  |          |
| `info.extendedFields.emailSubscriptions.effectiveEmail`       |                                                                                | Read-only | `TEXT`    | `$exists`                                  | Sortable |
| `info.extendedFields.emailSubscriptions.subscriptionStatus`   | Supported values: `SUBSCRIBED`, `UNSUBSCRIBED`, `NOT_SET`, `PENDING`.          | Read-only | `TEXT`    | `$eq`,`$ne`,`$in`, `$nin`                  |          |
| `info.extendedFields.invoices.vatId`                          | Government-issued VAT ID.                                                      |           | `TEXT`    |                                            |          |
| `info.extendedFields.members.membershipStatus`                | Supported values: `APPROVED`, `DENIED`, `PENDING`, `INACTIVE`.                 | Read-only | `TEXT`    | `$eq`,`$ne`,`$in`, `$nin`                  |          |
| `info.extendedFields.members.mobile`                          | Supported values: `true`, `false`.                                             |           | `TEXT`    |                                            |          |

[wix-ext-fields]: #extended-fields-managed-by-wix
[svc-fields]: https://dev.wix.com/api/rest/contacts/extended-fields
[contact-obj]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-object
[iso-4217-currency]: https://www.iso.org/iso-4217-currency-codes.html
[dashboard-contact-list]: https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Fcontacts
