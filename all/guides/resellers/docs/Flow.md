SortOrder: 1
# Resellers API: Sample Use Cases & Flows

This article shares some possible use cases your app could support, as well as
a sample flow that could support each use case. This can be a helpful jumping
off point as you plan your app's implementation.

## Set up a customer's site in your team account

You could set up a site for a customer in your agency's team account. This way,
the customer doesn't have access to the site until you've finished the setup
and testing. Then, transfer the site to the customer's Wix account and assign
a paid service to it. Note that you can't transfer sites with paid services.

To set up the site:

1. Create a new site in your agency's team account.
1. Finish the site's design, functionality, and testing.
1. Call the [Transfer Site](https://https://dev.wix.com/api/rest/account-level-apis/b2b-site-management/transfer-site)
    endpoint of the B2B Site Management API to give the customer access to the site.
1. Use the
    [Create Package](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2)
    to assign paid Wix services to the transferred site. Contact the
    [Wix B2B sales team](mailto:bizdev@wix.com) for details about the relevant
    product IDs for each service.

## Reassign a paid service to a different site

You could create a package of paid Wix services and assign the services to the
relevant sites. When the customer realizes that want to use one of the services
in a different site, you can re-assign it.

To re-assign a product instance:

1. Call
    [Create Package](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2)
    and pass the relevant site and product IDs.
1. Once the customer informs you, that they want to transfer a paid service
    from one site to another, let them select the product instance they want
    to transfer and the ID of the target site.
1. Pass the `productInstanceId` in the [Unassign Product Instance From Site](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/unassign-product-instance-from-site) call.
1. Use the [Assign Product Instance To Site](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/assign-product-instance-to-site)
    endpoint and pass the new site ID.

## Purchase a domain

You can help your customers find the best available domain, register it through
Wix and ensure that the domain is set up properly.

To add a domain to a site:

1. Retrieve the relevant site ID using the [Query Sites endpoint](https://dev.wix.com/api/rest/account-level-apis/sites/query-sites).
1. Call [Suggest Domains](https://dev.wix.com/api/rest/account-level-apis/domain-search/suggest-domains)
    of the Domain Search API to retrieve a list of relevant available domains.
1. Display the suggestions to the site owners and let them select their preferred choice.
1. Use the
    [Create Package](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2)
    endpoint to assign a Wix Premium plan that supports the
    chosen TLD to the Wix site. Contact the [Wix B2B sales team](mailto:bizdev@wix.com)
    for details about the relevant `productID` for each TLD.
1. Register the domain through Wix by calling the
    [Create Registered Domain](https://dev.wix.com/api/rest/account-level-apis/registered-domains/create-registered-domain)
    endpoint of the Registered Domains API. Make sure to pass the site ID to
    assign it to the relevant Wix site.
1. Call [Get Registered Domain](https://dev.wix.com/api/rest/account-level-apis/registered-domains/get-registered-domain)
    in regular intervals to confirm that the registered domain's `status` has changed to `"ACTIVE"`.