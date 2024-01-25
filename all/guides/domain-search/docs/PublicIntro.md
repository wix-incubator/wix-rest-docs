SortOrder: 0
# About the Domain Search API

The Domain Search API allows you to retrieve suggestions for domains that are
spot-on for your customers' sites and check the availability of a specific
domain.

With the Domain Search API you can:

- Check whether a specific domain is available for purchase.
- Generate suggestions for available domains.

You can use the
[Registered Domains API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/introduction)
to purchase domains through Wix. Learn more about managing DNS zones with the
[Domain DNS API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/introduction).
If you've bought a domain externally, you can connect it to the relevant Wix
site with the
[Connected Domains API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/introduction).

## Before you begin

+ Not all TLDs can be registered through Wix. Contact the
  Wix B2B team at [bizdev@wix.com](mailto:bizdev@wix.com) for more information.
+ If you want to register a domain to a Wix site, the site must have an active
  [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683).
  Learn more about
  [registering domains through Wix](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/introduction).

## Use cases

+ [Discover and register a domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-search/sample-flows#discover-and-register-a-domain)
+ [Check a domain's availability and register it](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-search/sample-flows#check-a-domains-availability-and-register-it)

## Terminology

+ __Domain__: Domain name including [Top-level domain](https://en.wikipedia.org/wiki/Top-level_domain) (TLD).
+ __Suggestion__: A suggested domain that's available for purchase.
+ __Registered domain__: Domain that's purchased, registered, and billed
  through Wix.
+ __External domain__: Domain that has been purchased through an external
  provider, not Wix. You can use the Connected Domains API to connect external domains to Wix sites.
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