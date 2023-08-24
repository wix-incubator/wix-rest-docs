SortOrder: 1
# About the Domain Connections API

<blockquote class='warning'>

__Deprecation Notice:__

Domain Connections has been replaced with
[Connected Domains](https://dev.wix.com/docs/rest/api-reference/account-level-ap-is/connected-domains/introduction)
and will be removed on December 31, 2023.

</blockquote>

With the Domain Connections API you can connect a root domain or subdomain to a Wix
site. You can only connect external domains.

The domain can be assigned as a primary domain or a redirect. You can read more
about [primary and redirected domains](https://support.wix.com/en/article/switching-your-primary-and-redirected-domains).

## Before you begin

+ You can only connect domains to a Wix site with an active [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683) that supports domains with the relevant TLD.
+ The `dnsRecords` array doesn't include the default nameserver record. Instead, the default nameserver is stored in a separate read-only `nsRecord` object.
+ Wix doesn't manage the DNS records for domains connected by pointing.

## Terminology

+ __Wix Domain__: A domain owned by Wix and billed through Wix.
+ __External Domain__: A domain owned by an external provider, not Wix.
+ __DNS__: The Domain Name System helps users identify computers connected to the internet.
+ __Nameserver__: A server component of the DNS that stores human-readable domain names.
+ __Pointing__: A connection type for cases where the DNS is hosted outside of Wix. Read more about [connecting a domain to Wix by pointing](https://support.wix.com/en/article/connecting-a-domain-to-wix-using-the-pointing-method).
+ __TLD__: [Top-level domain](https://en.wikipedia.org/wiki/Top-level_domain). For example, `com`, `net`, or `org`.
+ __Root domain__: Highest hierarchy level of the DNS. 
  Consists of the domain name and TLD. For example, `my-example-domain.com`.
+ __Subdomain__: Lower hierarchy level of the DNS. For example, `support.my-example-domain.com`.