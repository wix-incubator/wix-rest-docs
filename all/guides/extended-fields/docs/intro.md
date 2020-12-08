SortOrder: 0
# Extended Fields

While the Contact List contains the default fields you would expect to find —
such as name, address, phone, and email —
additional information about contacts can be stored in extended fields.

Extended fields can be created by site owners and contributors in the Wix UI,
or they can be created programmatically by Wix and third party apps.
Extended fields store data as text, URL, number, or date.

When a new extended field is created, it's available for use for all contacts,
and it's blank by default.
Data held in extended fields
can be accessed with these endpoints in the [Contacts API](crm.contacts):

- [Get Contact](crm.contacts.contacts-v4.get-contact)
- [Query Contacts](crm.contacts.contacts-v4.query-contacts)
- [List Contacts](crm.contacts.contacts-v4.list-contacts)

Each extended field is represented in the contact object
in `info.extendedFields` as key-value pairs.
Each key is the extended field key,
and each value is the field's value for the contact.
Empty extended fields are not returned.

Extended fields are also called custom fields in the Wix UI.
Read more on
[adding custom fields](https://support.wix.com/en/article/adding-custom-fields-to-contacts)
to the Contact List in the Wix UI.
