SortOrder: 2
# About the Domain Registrations API


With the Domain Registration API you can register a domain through Wix.

You can use the [Domain Search API](https://dev.wix.com/api/rest/account-level-apis/domain-search/introduction) 
to check which domains are available for purchase and the 
[Domain Connections API](https://dev.wix.com/api/rest/account-level-apis/domain-connections/introduction) 
to connect an externally purchased domain to a Wix site.


## Terminology


+ __Domain__: Domain name including TLD.
+ __TLD__: [Top-level domain](https://en.wikipedia.org/wiki/Top-level_domain). 
  For example, `com`, `net`, or `org`.
+ __DNS__: [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) of the internet.
+ __Root domain__: Highest hierarchy level of the DNS. 
  Consists of the domain name and TLD. For example, `my-example-domain.com`.
+ __Subdomain__: Lower hierarchy level of the DNS. For example, `support.my-example-domain.com`.
+ __Wix Domain__: A domain owned by Wix and billed through Wix.
+ __External Domain__: A domain owned by an external provider, not Wix.
+ __Product Instance__: Specific instance of a Wix service that a 
  [reseller](https://dev.wix.com/api/rest/account-level-apis/resellers/introduction) 
  provides to one of their customers. Before you can register a domain, you 
  must assign a Wix Premium service that supports the relevant TLD to the Wix 
  site.


## Before you begin


+ Not all TLDs can be registered through Wix. Contact the 
  Wix B2B team at [bizdev@wix.com](mailto:bizdev@wix.com) for more information.
+ You can only register a domain to a Wix site with an active 
  [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683). 
  There are different plans for different TLDs. Contact the 
  [Wix B2B team](mailto:bizdev@wix.com) for more information. 
  Use the [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) 
  to add such a Premium plan to your customer's site before calling [Register Domain](https://dev.wix.com/api/rest/account-level-apis/domain-registrations/register-domain).
+ When calling [Register Domain](https://dev.wix.com/api/rest/account-level-apis/domain-registrations/register-domain) 
  Wix only checks formal requirements of each field in the `contact` object, such as 
  the maximum number of characters. Wix doesn't check whether the actual domain registrar has 
  additional requirements, for example that the postal code is valid in the 
  specified country.
+ Calling [Register Domain](https://dev.wix.com/api/rest/account-level-apis/domain-registrations/register-domain) 
  starts an asynchronous registration process that may take up to 48 hours to resolve.