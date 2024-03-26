SortOrder: 1
# B2B Site Management Errors


This articles outlines error messages that might be issued when calling endpoints of the B2B Site Management API.


## Transfer Site Errors


The [Transfer Site](https://dev.wix.com/api/rest/account-level-apis/b2b-site-management/transfer-site) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `FAILED_PRECONDITION (428)` | `TARGET_ACCOUNT_ID_NOT_FOUND` | Target account wasn't found. | Check that the target account ID exists. |
| `PERMISSION_DENIED (403)` | `SITE_TRANSFER_NOT_ALLOWED` | Site transfer isn't allowed for `sourceAccountId` and `targetAccountId`.  | Contact the [Wix B2B Sales team](mailto:bizdev@wix.com) to check that the specified target and source accounts are supported for site transfers. |
| `INVALID_ARGUMENT (400)` | `SITE_NOT_FOUND` | `siteId` wasn't found in `accountId`. | Check that the site exists and that it belongs to the source account. |
| `FAILED_PRECONDITION (428)` | `SITE_TRANSFER_NOT_SUPPORTED` | Site transfer isn't supported for sites with paid Wix services. | The specified site includes a paid Wix service. Use the [Cancel Package endpoint of the Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/cancel-package) to remove the paid service before trying to transfer the site again. After the transfer, you can use the [Create Package endpoint of the Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) to add the paid Wix service to the site again. |