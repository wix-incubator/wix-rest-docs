SortOrder: 5
# Field Masks in Update Requests

When updating a contact,
the Contacts API uses field masks.
Field masks explicitly state the fields to update,
which helps prevent unintended changes to a contact.

The logic of a field mask is fairly straightforward:

- Fields that aren't included in the field mask are not updated.
- If a field is included in the field mask
  but is not given an explicit value in the request,
  the field is set to `null` for the contact.

You'll define field masks in the `fieldMask.paths` parameter
in these update requests:

- [Update Contact][update-contact]
- [Bulk Update Contacts][bulk-update-contacts]

[update-contact]: crm.contacts.contacts-v4.update-contact
[bulk-update-contacts]: crm.contacts.contacts-v4.bulk-update-contacts
