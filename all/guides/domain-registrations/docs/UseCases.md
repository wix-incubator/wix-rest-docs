SortOrder: 3
# Sample Use Case & Flow: Domain Registration


This article shares a possible use case your app could support, as well as an example flow. 
You're certainly not limited to this use case, but it can be a helpful jumping off point 
as you plan your app's implementation.


## Help site owners identify and register a domain


Your app could help site owners identify their favorite available domain. 
Then, you could purchase the corresponding domain for them through Wix and 
assign it to their site.


1. Call the [Suggest Domains endpoint](https://dev.wix.com/api/rest/account-level-apis/domain-search/suggest-domains) 
    to retrieve relevant available domains.
1. Display the suggestions to the site owners and let them select their preferred choice.
1. Use the 
    [Create Package](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) 
    endpoint of the Resellers API to provide a Wix Premium plan that supports domains of 
    the chosen TLD to the site owners. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) 
    for details about the relevant `productID` for each TLD. 
1. [Register](https://dev.wix.com/api/rest/account-level-apis/domain-registrations/register-domain) 
    the domain through Wix. Pass a site ID in the header of the call 
    to assign it to the relevant site.
1. Listen to the [Domain Registration Upated](https://dev.wix.com/api/rest/account-level-apis/domain-registrations/domain-registration-updated-webhook) 
    webhook to get notified whenever there is an update to the relevant registration process.

