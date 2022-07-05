SortOrder: 5
# Extended Fields

Basic contact information is stored in the default contact properties.
This includes information such as contact name, company, phone numbers,
addresses, and email addresses.
Additional properties are stored in extended fields.

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

There are 2 types of extended fields:

- **System fields** are added by Wix apps.
  They often enrich contacts with data from Wix products,
  such as Wix Stores or Wix Members.
  System fields cannot be renamed.
  When viewing system field settings, `fieldType` is `SYSTEM`.
- **Custom fields** can be added by site contributors or 3rd-party apps.
  Custom fields can be renamed,
  and their data can be written by site contributors and 3rd-party apps.
  When viewing custom field settings, `fieldType` is `USER_DEFINED`.

When you create, update, or retrieve contacts,
you'll find extended field data under `info.extendedFields.items`.
Most system fields are read-only, while all custom fields can be written to.

You can also manage a site's extended fields with these endpoints
in the Extended Fields API:

- To define new custom fields: [Find Or Create Extended Field](https://dev.wix.com/api/rest/contacts/extended-fields/find-or-create-extended-field)
- To rename a custom field: [Update Extended Field](https://dev.wix.com/api/rest/contacts/extended-fields/update-extended-field)
- To delete a custom field: [Delete Extended Field](https://dev.wix.com/api/rest/contacts/extended-fields/delete-extended-field)
- To retrieve system field definitions: [Get Extended Field](https://dev.wix.com/api/rest/contacts/extended-fields/get-extended-field), [List Extended Fields](https://dev.wix.com/api/rest/contacts/extended-fields/list-extended-fields)

> **Note:**
> To view extended field definitions,
> or to manage your app's extended fields,
> use the [Extended Fields API](https://dev.wix.com/api/rest/contacts/extended-fields).
