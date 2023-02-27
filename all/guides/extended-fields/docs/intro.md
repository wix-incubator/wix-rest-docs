SortOrder: 0
# Extended Fields

While the Contact List contains the default fields you would expect to find
(such as name, address, phone, and email)
additional information about contacts can be stored in extended fields.

Extended fields can be created by site owners and contributors in the Dashboard,
or they can be created programmatically by Wix and 3rd-party apps.
Extended fields store data as text, URL, number, or date.

When a new extended field is created, it's available for use for all contacts,
and it's blank by default.

You can use the Extended Fields API
to view and manage extended field definitions.
To view and manage data in extended fields for individual contacts,
you'll need to use the [Contacts API][contacts-api].

Each extended field is represented in the contact object
in `info.extendedFields` as key-value pairs.
Each key is the extended field key,
and each value is the field's value for the contact.
Empty extended fields are not returned.

[contacts-api]: https://dev.wix.com/api/rest/contacts/contacts