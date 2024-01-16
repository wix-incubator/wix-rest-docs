SortOrder: 4
# About the API


The Domain Dns API allows you to:

- create DNS zone in google cloud dns and delete previous zone if existed. 
- get DNS zone from google cloud dns if exists.
- update DNS zone records in google cloud dns.
- delete DNS zone in google cloud dns.
- preview DNS zone and it's records from google cloud dns, returns calculated dns records required to connect the domain to wix.

> **Note:**
> - The service is idempotent, i.e. can be called more than once and will return the same result.

## High level Diagram

![alt text](https://s3.amazonaws.com/wixplorer-readme-images/domaindns%2Fdomain-dns.png)

## Terminology

**A record** - The "A" stands for "address" and this is the most fundamental type of DNS record: it indicates the IP address of a given domain.

**CName record** - CNAME record is a type of DNS record that maps an alias name to a true domain name.

**MX record** - MX record directs email to a mail server.

**TXT record** - TXT record lets a domain admin enter text into the DNS.

**SPF record** - SPF records are used for email authentication.


## Limitations

- The only limitation is google's dns service rate-limit.
- specific types of dns records are allowed

## Error Handling

The api will throw errors if something goes wrong.

User input validation for domain:

- domain - required field.
- domain - must be in a hostname domain format.

User input validation for dns record:

- type - type field must be a value out of the RecordType enum.
- host name - must be in a hostname format.
- values - must be a min size of 1 value.

Business error thrown by the API:

- DnsZoneNotFound - if user tries to 'get' a dns zone and there is none under this domain.
- UserIdNotFound - if user tries to 'preview' a dns zone, yet we couldn't extract the requesting userId.  
