SortOrder: 8
# Extended Fields

Extended fields allow apps to add to the available data in the Contact List.
In addition to the core set of fields,
some Wix apps manage their own extended fields.

Just like the core Contact List fields,
these Wix-managed extended fields support field masks, field projection,
fieldsets, filtering, sorting, and searching.
See [Extended Fields Managed by Wix][wix-ext-fields] (below)
for details on what each field supports.

Data in extended fields can be accessed
in the [Contact object][contact-obj]
under `info.extendedFields[{namespace}.{key}]`.
The namespace is unique for each Wix app (for example, `ecom` or `members`).
All 3rd-party apps share the `custom` namespace.
All field keys must be unique within a namespace.

> **Note:**
> To view extended field definitions,
> or to manage your app's extended fields,
> use the [Extended Fields API][svc-fields].

## Custom Fields

Extended fields that are created by 3rd-party apps and site contributors
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

Some Wix apps add their own extended fields to the Contact List.
The table below shows a list of these fields and their attributes
so your app can make use of them through the REST API.

| Field                                                         | Description                                                                                            | Read-Only | Data Type | Supported Filters | Sortable |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------- | --------- | ----------------- | -------- |
| `info.extendedFields.emailSubscriptions.deliverabilityStatus` | Supported values: `VALID`, `BOUNCED`, `SPAM_COMPLAINT`, `NOT_SET`, `INACTIVE`.                         | Read-only | `TEXT`    | `$eq`,`$ne`,`$in` |          |
| `info.extendedFields.emailSubscriptions.effectiveEmail`       | First email that has `VALID/NOT_SET` deliverability status and subscription status isn't `UNSUBSCRIBED`| Read-only | `TEXT`    | `$exists`         | Sortable |
| `info.extendedFields.emailSubscriptions.subscriptionStatus`   | Supported values: `SUBSCRIBED`, `UNSUBSCRIBED`, `NOT_SET`, `PENDING`.                                  | Read-only | `TEXT`    | `$eq`,`$ne`,`$in` |          |
| `info.extendedFields.invoices.vatId`                          | Government-issued VAT ID.                                                                              |           | `TEXT`    |                   |          |
| `info.extendedFields.members.membershipStatus`                | Supported values: `APPROVED`, `DENIED`, `PENDING`, `INACTIVE`.                                         | Read-only | `TEXT`    | `$eq`,`$ne`,`$in` |          |
| `info.extendedFields.members.mobile`                          | Supported values: `true`, `false`.                                                                     |           | `BOOLEAN` |                   |          |

[wix-ext-fields]: #extended-fields-managed-by-wix
[svc-fields]: https://dev.wix.com/api/rest/contacts/extended-fields
[contact-obj]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-object
[iso-4217-currency]: https://www.iso.org/iso-4217-currency-codes.html
[dashboard-contact-list]: https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Fcontacts
