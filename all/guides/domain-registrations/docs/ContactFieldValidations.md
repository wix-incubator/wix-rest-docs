SortOrder: 5
# Contact Field Validations


This article outlines field validations for the `contact` object in the Domain 
Registration API. Wix only checks formal requirements of each field, such as 
the maximum number of characters. Wix doesn't check whether the actual domain 
registrar has additional requirements, for example that the postal code is valid in the 
specified country. If there is such a mismatch between the request and the 
registrar's requirements, the 
[Register Domain](https://dev.wix.com/api/rest/account-level-apis/domain-registrations/register-domain) 
call still succeeds, but the external provider may 
not deliver the domain. Then, you aren't immediately notified that the domain 
can't be delivered, but only after the last attempt to register the domain has 
failed.

These are the validations that Wix doesn't perform:
+ phone number belongs to the specified country
+ postal code is valid for the given country
+ email address exists


Wix performs these validations as part of the 
[Register Domain](https://dev.wix.com/api/rest/account-level-apis/domain-registrations/register-domain) 
call:

| <div style="width:100px">Field Name</div> |  <div style="width:280px">Supported Characters and Format</div> | <div style="width:280px">Constraints </div> | 
| ---------- | ---------- | ---------- |
| `firstName` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `lastName` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `organization` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `phone` |  Alphanumerical | Min: 2 characters  <br /> Max: 20 characters |
| `email` |  Alphanumerical and `@` | Must include a single `@`. <br /> Min: 3 characters  <br /> Max: 128 characters (64 before `@` and 63 after `@`) |
| `address` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `country` |  Alphanumerical in [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format. | Min: 2 characters  <br /> Max: 32 characters |
| `city` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `subdivision` |  Alphanumerical in [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format. | Min: 2 characters  <br /> Max: 32 characters |
| `postalCode` |  Alphanumerical | Min: 2 characters  <br /> Max: 16 characters | 