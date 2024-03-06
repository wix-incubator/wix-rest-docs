SortOrder: 1
# Sample Use Cases & Flows: Registered Domains

This article shares a possible use case your app could support, as well as an example flow.
You're certainly not limited to this use case, but it can be a helpful jumping off point
as you plan your app's implementation.

## Identify and register an available domain

Your app could help site owners identify their favorite available domain.
Then, you could purchase the corresponding domain for them through Wix and
assign it to their site.

To register an available domain:

1. Call [Suggest Domains](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-search/suggestion-v2/suggestion-object)
    to retrieve a list of relevant available domains.
1. Display the suggestions to the site owners and let them select their preferred choice.
1. Optional: In case the relevant site is a free Wix site, use the
   [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to assign a Premium plan to it. Make sure to save the `productInstanceId`.
1. Use the [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to create a product instance for the relevant domain TLD and privacy. Don't
   assign the product instance to a site, but keep it floating in the relevant
   account.
1. Register the domain through Wix by calling
   [Create Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/create-registered-domain).
   Make sure to pass a site ID to assign it to the relevant Wix site.
1. Call [Get Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/get-registered-domain)
   in regular intervals to confirm that the registered domain's `status` has changed to `"ACTIVE"`.

## Connect a registered domain to an external site

You could purchase a domain through Wix and then update the MX and TXT records.
This allows you to connect the domain to a website that isn't build on Wix.

To update the DNS records for a registered domain:

1. Optional: In case the relevant site is a free Wix site, use the
   [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to assign a Premium plan to it. Make sure to save the `productInstanceId`.
1. Use the [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to create a product instance for the relevant domain TLD and privacy. Don't
   assign the product instance to a site, but keep it floating in the relevant
   account.
1. Call [Create Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/create-registered-domain)
   to start the domain registration process through Wix.
1. Use [Get Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/get-registered-domain)
   to confirm that the `status` has changed to `"PENDING_REGISTRATION"`.
1. Call [Update Dns Zone](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/update-dns-zone)
   to change the MX and TXT records in Google's Cloud DNS.
1. Connect the domain to the external site.