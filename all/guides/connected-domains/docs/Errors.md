SortOrder: 2
# Connected Domains API: Errors

This articles outlines error messages that might be issued when calling endpoints of the Connected Domains API.

## Create Connected Domain Errors

The [Create Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/create-connected-domain) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `INVALID_ARGUMENT (400)` | `Invalid domain` | Unable to connect domain `<domainName>`, it's available for purchase. | You must purchase the domain before you can connect it to a Wix site. |
| `INVALID_ARGUMENT (400)` | `Invalid domain` | Domain `<domainName>` is Wix restricted. | Not all TLDs are supported for Wix sites. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for a list of supported TLDs and then try connecting a domain that's supported. |
| `INVALID_ARGUMENT (400)` | `Invalid connection type` | Invalid connection type `<connectionType>`. | Choose a connection type that's supported for the domain. To connect a root domain, you can only connect via `POINTING` or `NAMESERVERS`. For subdomains, you aren't allowed to pass any connection type. |
| `INVALID_ARGUMENT (400)` | `DOMAINS_GUID_NOT_VALID` | Wix site id and/or Wix account ID is invalid. | Check that the site and account ID are correct. |
| `ALREADY_EXISTS (409)` | `DOMAINS_ALREADY_EXISTS` | Domain `<domainName>` with different settings is already connected. | Make sure to connect the domain only once to the relevant account or site. |
| `ALREADY_EXISTS (409)` | `DOMAINS_ALREADY_EXISTS` | Domain `<domainName>` with different connection type is already connected. | Make sure to connect the domain only with the relevant connection type to the account or site. |
| `PERMISSION_DENIED (403)` | `DOMAINS_PERMISSION_DENIED` | Permission denied for account ID `<accountId>`. | Check that the account ID is correct and that you have permissions to access it. |
| `PERMISSION_DENIED (403)` | `DOMAINS_DOMAIN_NOT_PERMITTED` | Domain `<domain>` isn't permitted for the account. | Make sure that you have permissions to access the account. |
| `PERMISSION_DENIED (403)` | `INVALID_DOMAINS_PREVIEW_RECORDS` | Missing A, and/or CName, and/or NS preview records for domain `<domainName>`. | Make sure to pass the relevant DNS records. |
| `PERMISSION_DENIED (403)` | `DOMAINS_GUID_NOT_FOUND` | - | Make sure to pass a valid account ID. |
| `PERMISSION_DENIED (403)` | `NON_PREMIUM_SITE` | Domain `<domain>` can't be assigned to free Wix site `<siteId>`. | Make sure to [assign a Premium Plan](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2) to the site before connecting the domain. |


## Get Connected Domain Errors

The [Get Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/get-connected-domain) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `INVALID_ARGUMENT (400)` | `DOMAINS_GUID_NOT_VALID` | Wix site and/or account ID are invalid. | Check that the site and account ID are correct. |
| `NOT_FOUND (404)` | `NOT_FOUND` | Domain name `<domainName>` wasn't found. | Make sure to pass the correct domain name. |
| `PERMISSION_DENIED (403)` | `DOMAINS_PERMISSION_DENIED` | Permission denied for account ID `<accountId>`. | Check that the account ID is correct and that you have permissions to access it. |
| `PERMISSION_DENIED (403)` | `DOMAINS_DOMAIN_NOT_PERMITTED` | Domain `<domain>` isn't permitted for the account. | Make sure that you have permissions to access the account. |
| `PERMISSION_DENIED (403)` | `DOMAINS_GUID_NOT_FOUND` | - | Make sure to pass a valid account ID. |

## Get Connected Domain Setup Info Errors

The [Get Connected Domain Setup Info](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-setup-info-v1/get-connected-domain-setup-info) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `INVALID_ARGUMENT (400)` | `DOMAINS_GUID_NOT_VALID` | Wix site and/or account ID are invalid. | Check that the site and account ID are correct. |
| `PERMISSION_DENIED (403)` | `DOMAINS_PERMISSION_DENIED` | Permission denied for account ID `<accountId>`. | Check that the account ID is correct and that you have permissions to access it. |
| `PERMISSION_DENIED (403)` | `DOMAINS_DOMAIN_NOT_PERMITTED` | Domain `<domain>` isn't permitted for the account. | Make sure that you have permissions to access the account. |
| `PERMISSION_DENIED (403)` | `DOMAINS_GUID_NOT_FOUND` | - | Make sure to pass a valid account ID. |