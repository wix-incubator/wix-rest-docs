SortOrder: 0
# About the Registered Domains API

The Registered Domains API allows you to register domains through Wix. The
registration process may take up to 48 hours to resolve.

With the Registered Domains API you can:

+ Create registered domains
+ Retrieve registered domains

You can use the [Domain Search API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-search/suggestion-v2/suggestion-object)
to check which domains are available for purchase. Learn more about managing
DNS zones with the
[Domain DNS API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/introduction).

## Before you begin

It’s important to note the following points before starting to code:

+ The Registered Domains API is accessible via API keys. You can't access this
  API with a standard Auth header. We recommend authenticating calls with an
  API key for your main account instead of using a key for the relevant
  sub-account. But the responses to calls remain consistent across API
  keys, provided you have the necessary permissions.
+ Not all TLDs can be registered through Wix. Contact the
  Wix B2B team at [bizdev@wix.com](mailto:bizdev@wix.com) for more information.
+ You can only register root domains through Wix. You can't register subdomains.
+ If you want to register a domain to a Wix site, the site must have an active
  [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683).
  You don't need to have an active Premium plan in case you want to register a
  domain without assigning it to a site. Then, the domain remains floating in
  the account.  
  In both situations, your account must own a product instance that supports
  connecting a domain with the chosen TLD. Use the
  [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
  to add these products to the site or account before calling
  [Create Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/create-registered-domain).
+ Calling Create Registered Domain starts an asynchronous registration process
  that may take up to 48 hours to resolve. There is no webhook that notifies you
  when the process succeeds or fails. You can call
  [Get Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/get-registered-domain)
  to check the domain's status.
+ When calling Create Registered Domain Wix only checks formal requirements of
  each field in the `contacts` object, such as the maximum number of characters.
  Wix doesn't check whether the actual domain registrar has additional
  requirements, for example that the postal code is valid in the specified
  country. Read more about
  [contact validations](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/contact-validations).

## Use cases

+ [Identify and register an available domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/sample-flows#identify-and-register-an-available-domain)
+ [Connect a registered domain to an external site](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/sample-flows#connect-a-registered-domain-to-an-external-site)

## Terminology

+ __Registered domain__: Domain that's purchased, registered, and billed through Wix.
+ __External domain__: Domain that has been purchased through an external provider, not Wix.
  You can use the [Connected Domains API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/introduction)
  to connect external domains to Wix sites.
+ __Contact__: For each registered domain you can list 3 different contacts.
  + __Registrant__: Domain owner or contract partner for the domain name. Can be
    an actual person or a company representative.
  + __Admin__: Administrative contact that's listed in the [Whois database](https://www.whois.com/)
    unless the domain includes privacy. Note that not all TLDs can be purchased
    with privacy.
  + __Tech__: Technical contact.  
+ __DNS propagation__: The process of updating name servers around the world
  that follows every change to your DNS records. It can take up to 48 hours to
  complete. Read more about [DNS propagation](https://support.wix.com/en/article/about-domain-propagation).
+ __Reseller__: Strategic partner that offers Wix services to their customers.
  Read more about [resellers](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/introduction).
+ __Product instance__: Specific instance of a reseller product. Before you can
  register a domain to a Wix account, the account must own a product that
  supports the chosen domain TLD. Additionally, if you want to
  assign the domain to a site, the site must own a
  [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683).
  Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for a list of
  available reseller products.
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
