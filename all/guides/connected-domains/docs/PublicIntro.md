SortOrder: 0
# About the Connected Domains API

The Connected Domains API allows you to connect domains that haven't been
registered through Wix to a Wix site. You can connect domains either by
nameservers or pointing. The domain can be assigned as the primary
domain or a redirect. It may take up to 48 hours for the DNS changes to take
effect when creating a connected domain.

With the Connected Domains API you can:

+ Create and retrieve connected domains
+ Retrieve setup information

Read more about
[primary and redirected domains](https://support.wix.com/en/article/switching-your-primary-and-redirected-domains).
You can use the [Domain DNS API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/introduction)
to manage DNS zones for domains that are connected by nameservers. If you plan
to register available domains through Wix you can use the
[Registered Domains API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/introduction).

## Before you begin

It’s important to note the following points before starting to code:

+ The Connected Domains API is accessible via API keys. You can't access this
  API with a standard Auth header. We recommend authenticating calls with an
  API key for your main account instead of using a key for the relevant
  sub-account. But the responses to calls remain consistent across API
  keys, provided you have the necessary permissions.
+ Once you create a connected domain, it may take up to 48 hours for the DNS
  changes to take effect. Learn more about [domain propagation](https://support.wix.com/en/article/about-domain-propagation).
+ You can only connect domains to a Wix site with an active
  [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683).
  Use the [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/introduction)
  to add Premium plans and other paid Wix services to your customers' sites.
+ Wix doesn't manage DNS records for domains that are connected by pointing.
  That means you can use the [Domain DNS API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/introduction)
  to update DNS zones only for domains that are connected by nameservers.
+ You can't connect [registered domains](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/introduction)
  to Wix sites with the Connected Domains API.

## Use Cases

+ [Connect an external domain using name servers](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/sample-flows#connect-an-external-domain-using-name-servers)
+ [Connect an external domain by pointing](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/sample-flows#connect-an-external-domain-by-pointing)
+ [Connect a subdomain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/sample-flows#connect-a-subdomain)

## Terminology

+ __Connected domain__: A domain that's owned by an external provider, not Wix.
  Also called external domain.
+ __Registered domain__: A domain that's owned by Wix and billed through Wix.
+ __Connection type__: Information about how the domain is connected to the Wix
  site.
  + __Nameserver__: A server component of the DNS that stores human-readable
    domain names. With this connection type, Wix hosts your DNS, while your
    domain remains registered with its current host.
  + __Pointing__: A connection type for cases where the DNS is hosted outside of
    Wix. Read more about [connecting a domain to Wix by pointing](https://support.wix.com/en/article/connecting-a-domain-to-wix-using-the-pointing-method).
+ __Setup information__: Information that helps site owners navigate the
  connection process. Includes the name of the domain's external registrar and
  information about DNS records.
+ __Reseller__: Strategic partner that offers Wix services to their customers.
  Read more about [resellers](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/introduction).
+ __Account__: Wix account that includes access to associated sites.
  + __Team account__: Account type that supports collaborative work by having
    multiple sets of login credentials. This is especially helpful for agencies
    and resellers when managing a large number of customer sites. In Wix Studio
    team accounts are called workspaces. An agency may have multiple workspaces
    in Wix Studio, while in Wix Editor they're limited to a single team account.
  + __Sub-account__: Account that's contained within another account, forming a
    hierarchical structure. The owners of the sub-account are only able to
    interact with sites that belong to the sub-account. This setup is
    particularly useful for agencies and resellers since it limits client access
    to relevant sites only.