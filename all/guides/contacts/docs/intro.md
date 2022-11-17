SortOrder: 0
# About Contacts

<blockquote class="important">

__Important:__  
This article is being moved to the public docs.
The new URL will be <https://dev.wix.com/api/rest/contacts/introduction>.
After we publish the change,
we'll replace the content in this article with a link to the public introduction.

</blockquote>

When a new visitor first shares some of their contact information with a site,
they're added to the site's
[contact list](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Fcontacts).
Once that happens, their details are available through the Contacts APIs.

Some examples of how a person can become a contact are:

- A site visitor fills in a form with their contact details.
- A site visitor signs up as a member of the site.
- A site collaborator
  [imports a contact](https://support.wix.com/en/article/importing-contacts-by-uploading-a-csv-file-1066522) or
  [adds a contact manually](https://support.wix.com/en/article/manually-adding-contacts).
- A 3rd-party app
  [creates a contact](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/create-contact)
  with the Contacts API.

Site collaborators can use the contact list
to manage their contacts' information.
Learn more about how site collaborators can
[manage their contact list][kb-manage-contacts].

With the Contacts APIs, you can:

- Manage [site contacts](https://dev.wix.com/api/rest/contacts/contacts)
- Manage [contact labels](https://dev.wix.com/api/rest/contacts/labels)
- Manage [extended field definitions](https://dev.wix.com/api/rest/contacts/extended-fields)

## Terminology

- **Extended fields**: Additional properties that store additional contact information.
  A contact's extended field data is available
  in the contact object under `info.extendedFields`.
  Extended field definitions can be created and managed with
  the [Extended Fields API][svc-fields].

  There are 2 types of extended fields:

  - **System fields**: Extended fields added by Wix apps.
    System fields often enrich contacts with data from Wix apps,
    such as Wix Stores or Wix Members.
    System fields cannot be renamed and are typically read-only.
  - **Custom fields**: Extended fields added by site collaborators or 3rd-party apps.
    Custom fields can be renamed,
    and their data can be written by any site collaborators or 3rd-party app.

- **Labels**: Tags that help site contributors categorize and organize their contacts.
  Labels can be system-defined or user-defined.
  You can manage a site's labels through the [Labels API][svc-labels].
  A contact's assigned labels are available
  in the contact object under `info.labelKeys`.

[kb-manage-contacts]: https://support.wix.com/en/article/about-your-contact-list

[svc-fields]: https://dev.wix.com/api/rest/contacts/extended-fields
[svc-labels]: https://dev.wix.com/api/rest/contacts/labels
