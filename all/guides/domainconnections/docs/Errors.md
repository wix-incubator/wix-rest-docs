SortOrder: 3
# Domains Errors


This articles outlines error messages that might be issued when calling endpoints of the Domain Search API.


## Connect Domain Errors


The [Connect Domain](https://dev.wix.com/api/rest/account-level-apis/domain-connections/connect-domain) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `INVALID_ARGUMENT (400)` | `Invalid domain` | Unable to connect domain `<domainName>`, it is available for purchase. | You must purchase the domain before you can connect it to a Wix site. |
| `INVALID_ARGUMENT (400)` | `Invalid domain` | Domain `<domainName>` is restricted. | Not all TLDs are supported for Wix sites. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for a list of supported TLDs and then try connecting a domain that's supported. |
| `INVALID_ARGUMENT (400)` | `Invalid connection type` | Invalid connection type: `<connectionType>`. | Choose a connection type that's supported for the domain. To connect a root domain, you can only connect via `POINTING` or `NAMESERVERS`. For subdomains, you aren't allowed to pass any connection type. |
| `INVALID_ARGUMENT (400)` | `Invalid type of record` | Additional DNS records can not be provided for `<connectionType>`. | It isn't supported to pass additional DNS record information in the request. Omit the additional DNS records and try again. |
| `INVALID_ARGUMENT (400)` | `DOMAINS_GUID_NOT_VALID` | Wix site id / Wix account ID is invalid. | Check that the site and account ID are correct. |
| `INVALID_ARGUMENT (400)` | `DOMAINS_MISSING_SITE_ID_FOR_ASSIGN_AS` | Missing `siteId` for assignAs `<assignAs>`. | Make sure to pass a site ID when setting up a primary domain or redirect. |
| `PERMISSION_DENIED (403)` | `DOMAINS_PERMISSION_DENIED` | Permission denied for target accountId: `<targetAccountId>`. | Check that the account ID is correct and that you have permissions to access it. |
| `PERMISSION_DENIED (403)` | `DOMAINS_DOMAIN_NOT_PERMITTED` | Domain `<domain>` is not permitted to target account. | Make sure that you have permissions to access the account. |
| `PERMISSION_DENIED (403)` | `DOMAINS_NO_THROTTLER_KEY` | Cannot consume this service. | Make sure that your app has the `Manage Domains` permission scope. |
| `PERMISSION_DENIED (403)` | `DOMAINS_SITE_NOT_PERMITTED` | SiteId: `<siteId>` is not permitted to target account. | Check that site belongs to the account. |
| `PERMISSION_DENIED (403)` | `INVALID_DOMAINS_PREVIEW_RECORDS` | Preview records are missing A and/or CName and/or NS for domain: `<domainName>`. | Make sure to pass the releavant DNS records. |
| `PERMISSION_DENIED (403)` | `DOMAINS_GUID_NOT_FOUND` | - | Make sure to pass a valid account ID. |
