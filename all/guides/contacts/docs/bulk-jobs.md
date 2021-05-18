SortOrder: 3
# Working with Bulk Jobs

The Contacts API allows you to perform these actions in bulk:

- [Bulk Label and Unlabel Contacts][bulk-label-unlabel]
- [Bulk Update Contacts][bulk-update]
- [Bulk Delete Contacts][bulk-delete]

When your app calls one of the bulk endpoints listed above,
a new bulk job is created, and the `jobId` is returned.
You can get the status of any active or completed job with
[Get Bulk Job][get-bulk-job] and [List Bulk Jobs][list-bulk-jobs].

## Performing a dry run

Your app will use [`filter`][md-field-support]
and plain text `search` parameters
to specify the target contacts for a bulk job.
All contacts that meet the filter and search criteria
will be affected by the bulk operation.

Before running a bulk operation, can optionally perform a dry run
by running a [query][query] with the intended filter and search options.
You can show the query results to the user
and ask them to confirm that they want to continue with the bulk action.

[bulk-label-unlabel]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/bulk-label-and-unlabel-contacts
[bulk-update]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/bulk-update-contacts
[bulk-delete]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/bulk-delete-contacts
[get-bulk-job]: https://dev.wix.com/api/rest/contacts/contacts/bulk-jobs/get-bulk-job
[list-bulk-jobs]: https://dev.wix.com/api/rest/contacts/contacts/bulk-jobs/list-bulk-jobs
[query]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/query-contacts
[md-field-support]: https://dev.wix.com/api/rest/contacts/contacts/sort-and-filter#contacts_contacts_sort-and-filter_field-support-for-filtering-sorting-and-searching