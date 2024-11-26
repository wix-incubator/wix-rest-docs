# Domain Search Errors


This article outlines error messages that might be issued when calling endpoints of the Domain Search API.


## Check Domain Availability Errors


The [Check Domain Availability](https://dev.wix.com/api/rest/account-level-apis/domain-search/check-domain-availibility) endpoint might issue the following error message:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `INVALID_ARGUMENT (400)` | `INVALID_DOMAIN` | Failed to extract root domain from `<domain>`, or TLD is missing or invalid. | Start a new query including a domain name and supported TLD. Domain name and TLD must be separated by a dot. For example, `my-new-domain.com`. |


## Suggest Domains Errors


The [Suggest Domains](https://dev.wix.com/api/rest/account-level-apis/domain-search/suggest-domains) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `INVALID_ARGUMENT (400)` | `INVALID_QUERY` | Query `<query>` has invalid characters. Only alphanumeric values, hyphens, dots, and spaces are supported. | Start a new query using only alphanumeric values, hyphens, dots, and spaces. |
| `INVALID_ARGUMENT (400)` | `INVALID_TLD_FORMAT` | At least one element of the `tlds` array has an invalid format. | Start a new query using the correct TLD format. TLDs must not include the dot. For example, `com`, not `.com`. |
| `INVALID_ARGUMENT (400)` | `TLD_NOT_SUPPORTED` | Unsupported TLDs `<tlds>` found. | Start a new query with supported TLDs such as `com`, `net`, and `org`. Contact the [Wix B2B sales team](bizdev@wix.com) for more information. |
