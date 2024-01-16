SortOrder: 1
# About the Domain DNS API

With the Domain DNS API you can manage DNS zones in
[Google's Cloud DNS](https://cloud.google.com/dns). This allows you to connect
domains that you've registered through Wix to non-Wix websites. You can also use
the Domain DNS API to manage DNS records for external domains that are connected
by nameservers to Wix sites.

Using the Domain DNS API you can:

+ Preview DNS zones
+ Manage DNS zones in Google's Cloud DNS

Learn more about:

+ Registering domains through Wix with the [Registered Domains API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/introduction)
+ Connecting external domains to Wix sites with the [Connected Domains API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/introduction)
+ Managing Wix Premium subscriptions with the [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-ap-is/resellers/introduction)

## Before you begin

It’s important to note the following points before starting to code:

+ The Domain DNS API is accessible via API keys. You can't access this
  API with a standard Auth header. We recommend authenticating calls with an
  API key for your main account instead of using a key for the relevant
  sub-account. But the responses to calls remain consistent across API
  keys, provided you have the necessary permissions.
+ Wix limits DNS records to 50 values per type. External providers may support
  a different maximum number of DNS records for a specific type, Wix doesn't
  validate that you don't exceed these external limits.
+ You can only [update DNS zones](https://dev.wix.com/docs/rest/api-reference/account-level-ap-is/domain-dns/update-dns-zone)
  for external domains that are connected by nameservers to a Wix site. You
  can't use the Domain DNS API for external domains that are connected by
  pointing to a Wix site because the DNS isn't saved in Wix for this connection
  type.

## Use cases

+ [Update DNS records for a registered domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/sample-flows#update-dns-records-for-a-registered-domain)
+ [Connect an external domain by nameservers to a Wix site](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/sample-flows#connect-an-external-domain-by-nameservers-to-a-wix-site)

## Terminology

+ __Registered domain__: Domain that's purchased, registered, and billed through Wix.
+ __External domain__: Domain that has been purchased through an external provider, not Wix.
+ __Domain name__: The domain name includes the
  [top-level domain](https://en.wikipedia.org/wiki/Top-level_domain) (TLD).
  Examples for TLDs are `com`, `net`, or `org`.
+ __DNS record__: Database record in the
  [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) that's
  used to map a human-readable URL to an IP address.
+ __DNS zone__: A [DNS zone](https://en.wikipedia.org/wiki/DNS_zone)
  is an administrative subdivision of the DNS namespace. When you
  [Create a DNS zone](https://dev.wix.com/docs/rest/api-reference/account-level-ap-is/domain-dns/create-dns-zone)
  the values are uploaded to
  [Google's Cloud DNS](https://cloud.google.com/dns).
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