SortOrder: 0
# About Contacts

When a visitor first interacts with a site in a number of ways —
such as submitting a contact form or subscribing to a newsletter —
they're added to the site's [Contact List][contact-list-deeplink]
and their details are available through the Contacts APIs.
Here are some examples of how a visitor could be converted to a contact:

- A site visitor fills in a form with their contact details.
- A site visitor signs up as a member of the site.
- A site contributor [imports a contact][kb-import-contacts] or
  [adds a contact manually][kb-add-contacts].
- A 3rd-party app adds a contact via the Contacts API.

Site owners can use the Contact List to manage information about their contacts.
Read more about how site owners can
[manage their Contact List][kb-manage-contacts].

## Terminology

- **Extended fields**
  Extended fields store information beyond the default contact fields,
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
[contact-list-deeplink]: https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Fcontacts

[svc-fields]: https://dev.wix.com/api/rest/contacts/extended-fields
[svc-labels]: https://dev.wix.com/api/rest/contacts/labels
