SortOrder: 3
# Contact Validations

This article outlines field validations for the `contacts` object.
Wix only checks formal requirements of each field, such as
the maximum number of characters. Wix doesn't check whether the actual domain
registrar has additional requirements, for example that the postal code is valid in the
specified country. If there is such a mismatch between the request and the
registrar's requirements, the
[Create Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/create-registered-domain)
call succeeds, but the registration process can't succeed.
In this case you aren't immediately notified that the domain
can't be delivered and Wix tries to register the domain several times.
It may take up to 48 hours before the domain's `status` changes to
`"FAILED_REGISTRATION"`.

Therefore it's important to confirm the following points before calling
Create Registered Domain:

+ phone number belongs to the country
+ email address is valid
+ postal code belongs to the country

Wix performs the following validations as part of the Create Registered Domain
call:

| <div style="width:120px">Field Name</div> |  <div style="width:280px">Supported Characters and Format</div> | <div style="width:280px">Constraints </div> | 
| ---------- | ---------- | ---------- |
| `firstName` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `lastName` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `company` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `phone` |  Alphanumerical | Min: 2 characters  <br /> Max: 20 characters |
| `email` |  Alphanumerical and `@` | Must include a single `@`. <br /> Min: 3 characters  <br /> Max: 128 characters (64 before `@` and 63 after `@`) |
| `address` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `countryCode` |  Alphanumerical in [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format. | Min: 2 characters  <br /> Max: 32 characters |
| `city` |  Alphanumerical | Min: 2 characters  <br /> Max: 64 characters |
| `subdivisionCode` |  Alphanumerical in [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format. | __Required__ for these countries: `”AE"`, `"AR"`, `"AT"`, `"AU"`, `"BE"`, `"BR"`, `"CA"`, `"CH"`, `"CL"`, `"CO"`, `"CR"`, `"CZ"`, `"DE"`, `"DK"`, `"ES"`, `"FI"`, `"FR"`, `"GR"`, `"IE"`, `"IN"`, `"IT"`, `"JP"`, `"KR"`, `"MX"`, `"MY"`, `"NL"`, `"NO"`, `"NZ"`, `"PE"`, `"PL"`, `"PT"`, `"RU"`, `"SE"`, `"SG"`, `"TH"`, `"TR"`, `"TW"`, `"UA"`, `"US"`, `”ZA”`. <br /> Min: 2 characters <br /> Max: 32 characters|
| `postalCode` |  Alphanumerical | Min: 2 characters  <br /> Max: 16 characters |