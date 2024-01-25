SortOrder: 1
# Sample Use Cases & Flows: Domain Search

This article shares possible use cases your app could support, as well as example flows.
You're certainly not limited to these use cases, but they can be a helpful jumping off point
as you plan your app's implementation.

## Discover and register a domain

Your app could help site owners identify an available, spot-on domain.
Then, you could purchase the domain for them and assign it to their site.

To discover and register a domain:

1. Call [Suggest Domains](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-search/suggestion-v2/suggestion-object)
    to retrieve a list of relevant available domains.
1. Display the suggestions to the site owners and let them select their preferred choice.
1. Optional: In case the relevant site is a free Wix site, use the
   [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to assign a Premium plan to it. Make sure to save the `productInstanceId`.
1. Use the [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to create a product instance for the relevant domain TLD and privacy.
1. Register the domain through Wix by calling
    [Create Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/create-registered-domain).
    Make sure to pass a site ID to assign it to the relevant Wix site.
1. Call [Get Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/get-registered-domain)
    in regular intervals to confirm that the registered domain's `status` has changed to `"ACTIVE"`.

## Check a domain's availability and register it

Your app could help the site owner check the availability of their favorite
domain. Then, you could purchase the domain for them and assign it to their
site.

To check a domain's availability and register it:

1. Ask the site owners what their favorite domain is.
1. Call [Check Domain Availability](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-search/availability-v2/check-domain-availability)
    to verify that the domain is still available. If its isn't available, start
    over or follow the
    [flow above](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-search/sample-flows#discover-and-register-a-domain).
1. Optional: In case the relevant site is a free Wix site, use the
   [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to assign a Premium plan to it. Make sure to save the `productInstanceId`.
1. Use the [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to create a product instance for the relevant domain TLD and privacy.
1. Register the domain through Wix by calling
    [Create Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/create-registered-domain).
    Make sure to pass a site ID to assign it to the relevant Wix site.
1. Call [Get Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/get-registered-domain)
    in regular intervals to confirm that the registered domain's `status` has changed to `"ACTIVE"`.