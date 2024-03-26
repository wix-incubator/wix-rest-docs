SortOrder: 4
# About the API


The Domain Connect API allow you to:

- connect a domain.
- connect a subdomain.
- connect a domain by pointing.
- connect a domain to a site.
- connect a domain by wix nameservers.
- connect as hidden from my-domains.
- connect with silent mode (no email or any notification will be sent to the client).

> **Note:**
> - The service is resumable, i.e. can be called again if it fails and will continue from the state where it previously failed.
> - The service is idempotent, i.e. can be called more than once and will return the same result.

## High level Diagram

![alt text](https://s3.amazonaws.com/wixplorer-readme-images/domainconnections%2Fdiagram.png)

## Terminology

### Domain

- **Wix Domain**
  <br>
  A domain purchased and managed by Wix. To connect this domain to a specific Wix site, the site must have a Premium
  Plan with can_connect_domain capability.

- **External Domain**
  <br>
  A domain that is not owned or billed by Wix, but is configured to point to Wix's nameservers.    
  Although the domain itself is billed by a 3rd party, the ability to connect a domain to the site still requires a paid
  Premium Plan.  
  There are two types of external domains:

  **External Domain Pointing** - Domain which was purchased outside of Wix and is connected to a site through the
  external registrar DNSs. Wix does not manage the DNS records for these domains.

  **External Domain DNS Managed** - Domain which was purchased outside of Wix and is connected to a site and Wix manages
  its DNS records.

## Limitations

- The only limitation is google's dns service rate-limit.

## Error Handling

The api will throw errors if something goes wrong.

User input validation for root domain:

- domain - required field.
- domain - must be in a hostname domain format.
- connection_type - required field and must be NAMESERVERS or POINTING.
- additional_dns_records - can only be CNAME, TXT, or MX.

User input validation for subdomain:

- domain - required field.
- domain - must be in a hostname domain format.
- connection_type - required field and must be either UNKNOWN or INTERNAL.

Business error thrown by the API:

- AccountNotFound - if no user found with the specified account_id
- SiteNotFound - if no meta site found with the specified site_id
