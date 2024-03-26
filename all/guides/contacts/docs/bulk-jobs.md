SortOrder: 2
# About Bulk Jobs

The Contacts API allows you to perform these actions in bulk:

- [Bulk Label and Unlabel Contacts][bulk-label-unlabel]
- [Bulk Update Contacts][bulk-update]
- [Bulk Delete Contacts][bulk-delete]

When your app calls one of the bulk endpoints listed above,
a new bulk job is started, and the `jobId` is returned.
You can use the Bulk Jobs API
to get the status of any active or completed bulk job.

[bulk-label-unlabel]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/bulk-label-and-unlabel-contacts
[bulk-update]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/bulk-update-contacts
[bulk-delete]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/bulk-delete-contacts