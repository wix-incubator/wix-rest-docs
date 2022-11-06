SortOrder: 1
# Sample Use Case & Flow: Domain Search


This article shares a possible use case your app could support, as well as an example flow. 
You're certainly not limited to this use case, but it can be a helpful jumping off point 
as you plan your app's implementation.


## Help site owners set up their domain


Your app could help site owners identify their favorite available domain. 
Then, you could purchase it for them through an external registrar and 
assign it to their Wix site.

1. Optional: Identify the relevant Wix site through the 
    [Query Sites endpoint](https://dev.wix.com/api/rest/account-level-apis/sites/query-sites).
1. Call [Suggest Domains](https://dev.wix.com/api/rest/account-level-apis/domain-search/suggest-domains) 
    to retrieve fitting available domains.
1. Display the suggestions to the site owners and let them select their preferred choice.
1. Purchase the domain through an external registrar.
1. [Connect the domain](https://dev.wix.com/api/rest/account-level-apis/domains/connect-domain)
    to the Wix site. Note that you can only connect a domain to a Wix site with an active 
    [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683) 
    that supports domains of the corresponding TLD. You can use the 
    [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) 
    to add such a Premium plan to the site.

