SortOrder: 1
# About the Domain Connections API


With the Domain Connections API you can connect a domain or subdomain to a Wix site. Both Wix domains and external domains are supported.

The domain can be assigned as a primary domain or a redirect. You can read more about [primary and redirected domains](https://support.wix.com/en/article/switching-your-primary-and-redirected-domains).


## Terminology


+ **Wix Domain:** A domain owned by Wix and billed through Wix.
+ **External Domain:** A domain owned by an external provider, not Wix.
  
  > __Note:__ You can only connect domains to a Wix site with a 
  > [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683). 
  > This also applies to external domains.
+ **DNS:** The Domain Name System helps users identify computers connected to the internet.
+ **Nameserver:** A server component of the DNS that stores human-readable domain names.
+ **Pointing:** A connection type for cases where the DNS is hosted outside of Wix. Read more about [connecting a domain to Wix by pointing](https://support.wix.com/en/article/connecting-a-domain-to-wix-using-the-pointing-method).


## Limitations


+ You can only connect domains to a Wix site with a [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683).
+ The `dnsRecords` array doesn't include the default nameserver record. Instead, the default nameserver is stored in a separate read-only `nsRecord` object.
+ Wix doesn't manage the DNS records for domains connected by pointing.
