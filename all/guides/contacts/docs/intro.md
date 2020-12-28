SortOrder: 0
# About Contacts

When a visitor first interacts with a site in a number of ways —
such as submitting a contact form or subscribing to a newsletter —
they're captured in the site's Contact List as a new contact.
and their details will be available through the contacts APIs.
Here are some examples for how a visitor could be converted to a contact:

- A site visitor fills in a form with their communication details
- A site visitor signs up as a member of the site
- A site contributor [imports a contact][kb-import-contacts] or
  [adds a contact manually][kb-add-contacts]
- A third party app adds a contact via the Contacts API

Site owners can use the Contact List to manage information about their contacts.
Read more about how site owners can
[manage their Contact List][kb-manage-contacts].

## Terminology

- **Extended fields**
  can be added to the Contact List by site contributors or apps.
  Extended fields store information beyond the default fields,
  and apps can create and manage their own extended fields.
  To view and manage extended field _data_,
  use the Contacts API.
  To view and manage extended field _definitions_,
  use the [Extended Fields API][svc-fields].
- **Labels** help contributors segment
  and organize their site’s contacts.
  Labels can be system-defined or user-defined,
  and the contact labels for a site are available
  through the [Labels API][svc-labels].

[kb-import-contacts]: https://support.wix.com/en/article/importing-contacts-by-uploading-a-csv-file-1066522
[kb-add-contacts]: https://support.wix.com/en/article/manually-adding-contacts
[kb-manage-contacts]: https://support.wix.com/en/article/about-your-contact-list

[svc-fields]: crm.contacts.extended-fields
[svc-labels]: crm.labels
