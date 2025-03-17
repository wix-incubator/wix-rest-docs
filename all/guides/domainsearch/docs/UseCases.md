# Sample Use Case & Flow: Domain Search


This article shares a possible use case your app could support, as well as an example flow.
You're certainly not limited to this use case, but it can be a helpful jumping off point
as you plan your app's implementation.


## Help site owners set up their domain


Your app could help site owners identify their favorite available domain name.
Then, you could purchase the corresponding domain for them and connect it to
their site.


1. Call the [Suggest Domains endpoint](https://dev.wix.com/api/rest/account-level-apis/domain-search/suggest-domains).
1. Display the suggestions to the site owners and let them select their preferred choice.
1. Purchase the domain through an external provider.
1. Identify the relevant site through the
   [Query Sites endpoint](https://dev.wix.com/api/rest/account-level-apis/sites/query-sites).
1. Use the
   [Create Package endpoint of the Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2)
   to offer the domain to the site owners.
1. Call the
   [Connect Domain endpoint](https://dev.wix.com/api/rest/account-level-apis/domain-search/connect-domain)
   to connect the domain to the relevant site.
