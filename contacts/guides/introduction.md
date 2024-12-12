# About the Contacts API

The Contacts API provides functionality for creating and managing contacts. 


The Contacts API contains the following APIs:

- [Contacts](https://dev.wix.com/api/rest/contacts/contacts) - This API allows you to manage the contact details for contacts on a site. 
- [Labels](https://dev.wix.com/api/rest/contacts/labels) - This API allows you to manage contact labels. Once a label is created, it can be assigned to a contact using the Contacts API.
- [Extended Fields](https://dev.wix.com/api/rest/contacts/extended-fields) -  This API allows you to create and manage additional fields for contacts. 


## Use Cases
- [Periodically export new Wix contacts to an external CRM](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/sample-flows#periodically-export-new-wix-contacts-to-an-external-crm)
- [Sync with an external system in Real Time](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/sample-flows#real-time-2-way-sync-with-an-external-system)
- [Create new contacts from an external form](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/sample-flows#create-new-contacts-from-an-external-form)
- [Sync subscribed enails with an email delivery service](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/sample-flows#sync-subscribed-emails-with-an-email-delivery-service)


## Terminology

- **Labels**: Tags that help Wix users categorize and organize their contacts.
  Labels can be system-defined or user-defined.
  You can manage a site's labels with the [Labels API](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/labels/introduction).
  A contact's assigned labels are available
  in the contact object under `info.labelKeys`.

- **Extended fields**: Additional properties that store additional contact information.
  A contact's extended field data is available
  in the contact object under `info.extendedFields`.
  Extended field definitions can be created and managed with
  the [Extended Fields API](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/extended-fields/introduction).

  There are 2 types of extended fields:

  - **System fields**: Extended fields created by apps built by Wix.
    System fields often enrich contacts with data from apps built by Wix,
    such as Wix Stores or Wix Members.
    System fields can't be renamed and are typically read-only.
  - **Custom fields**: Extended fields added by Wix users.
    Custom fields can be renamed,
    and their data can be written by any Wix user.
