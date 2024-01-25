SortOrder: 5
# Domain DNS Errors

This articles outlines error messages that might be issued when calling
endpoints of the Domain DNS API.

## Create DNS Zone Errors

[Create DNS Zone](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/create-dns-zone) might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting <div> |
|---|---|---|---|
| `NOT_FOUND (404)` | `USER_ID_NOT_FOUND` | User id not found in request context. | Make sure to pass the correct authorization header. |
| `NOT_FOUND (404)` | `TARGET_ACCOUNT_NOT_FOUND` | Target account id not found in request context. | Make sure to pass the correct account ID in the header of the call. |
| `NOT_FOUND (404)` | `DNS_ZONE_NOT_FOUND` | No dns zone found for domain name `<domainName>`. | You must pass a `dnsZone` object when setting up a DNS zone in Google's Cloud DNS. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_NOT_PERMITTED` | Domain `<domain>` is not permitted to target account. | Make sure to pass the correct account ID in the header of the call. The target account must also have a Premium subscription that allows connecting a domain with the chosen TLD. See the [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/introduction) for more information. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_ALREADY_EXISTS` | Domain `<domain>` already exists. | You can create a DNS zone in Google's Cloud DNS that already exists. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_DNS_EMPTY_RECORD_VALUE` | Value of record `<recordType>` is empty. | You must pass values for each DNS record that you want to specify in Google's Cloud DNS. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_MX_RECORD_VALUE_INVALID` | Value of MX record `<value>` is invalid, it should start with a priority and then the mail server, for example `"5 aspmx.l.google.com"`. | Make sure to use this format `"5 aspmx.l.google.com"` when specifying the value of an MX record in Google's Cloud DNS. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_CNAME_RECORD_HOSTNAME_INVALID` | Host name of the CNAME record `$value` is invalid, it should end with the domain name but not equal to it, for example `"en.domain.com"`. | Make sure to use this format `"en.domain.com"` when specifying the value of a CNAME record in Google's Cloud DNS. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_MX_RECORD_VALUE_INVALID` | Multiple `<recordType>` records with the same hostName `<hostName>` not supported, the multiple values belong to the same hostName should be combined under one `<recordType>`. | Make sure that you pass all DNS record values that belong to the same type in a single `values` array of the relevant `records.type` object. You can't pass multiple `record` objects with the same record `type`. |

## Update DNS Zone Errors

[Update DNS Zone](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/update-dns-zone) might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting <div> |
|---|---|---|---|
| `NOT_FOUND (404)` | `USER_ID_NOT_FOUND` | User id not found in request context. | Make sure to pass the correct authorization header. |
| `NOT_FOUND (404)` | `TARGET_ACCOUNT_NOT_FOUND` | Target account id not found in request context. | Make sure to pass the correct account ID in the header of the call. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_NOT_PERMITTED` | Domain `<domain>` is not permitted to target account. | Make sure to pass the correct account ID in the header of the call. The target account must also have a Premium subscription that allows connecting a domain with the chosen TLD. See the [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/introduction) for more information. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_DNS_EMPTY_RECORD_VALUE` | Value of record `<recordType>` is empty. | You must pass at least one value for each DNS record type that you want to specify in Google's Cloud DNS. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_MX_RECORD_VALUE_INVALID` | Value of MX record `<value>` is invalid, it should start with a priority and then the mail server, for example `"5 aspmx.l.google.com"`. | Make sure to use this format: `"5 aspmx.l.google.com"`, when specifying the value of an MX record in Google's Cloud DNS. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_CNAME_RECORD_HOSTNAME_INVALID` | Host name of the CNAME record `$value` is invalid, it should end with the domain name but not equal to it, for example `"en.domain.com"`. | Make sure to use this format: `"en.domain.com"`, when specifying the value of a CNAME record in Google's Cloud DNS. |
| `FAILED_PRECONDITION (428)` | `DOMAIN_MX_RECORD_VALUE_INVALID` | Multiple `<recordType>` records with the same hostName `<hostName>` not supported, the multiple values belong to the same hostName should be combined under one `<recordType>`. | Make sure that you pass all DNS record values that belong to the same DNS record type in the `values` array of the relevant `record` object. You can't pass multiple `record` objects that have the same record `type`. |