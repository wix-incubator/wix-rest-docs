# About Account Level APIs

Wix's account level APIs enable developers to access and manage account level functionality, including domains, transfering sites between accounts, and inviting team members.

Accounts are particularly useful when a business employs multiple staff members who all should have access to and permissions to manage one or more sites created for the business, and when a design company creates and designs sites for clients. In these cases, creating a team and sharing account access with the relevant users allows them access to account-level (domains, payment and billing info, etc.) and site-level data. This allows the right people to edit the relevant sites and other account assets to get their work done and keep sites and businesses running smoothly.  

Account owners can use roles to limit team members’ access to various tasks and/or interfaces of the account (for example, blocking access to specific sites or blocking access to adding features that require payment). See [About Team Management](https://support.wix.com/en/article/about-team-management) and [Wix Partners: Default Team Management Roles & Permissions](https://support.wix.com/en/article/default-team-management-roles-permissions#roles-and-permissions-summary-table) for more information.

## Authorization strategies for account level APIs
The APIs in this category require using an [authorization strategy](https://dev.wix.com/docs/sdk/articles/get-started/authorization-strategies) that utilizes an [API key](https://dev.wix.com/api/rest/getting-started/api-keys):
- Headless projects and apps should use the [Headless admin with API key strategy](https://dev.wix.com/docs/sdk/articles/get-started/authorization-strategies#headless-admin-with-api-key).  
To learn how to implement this strategy, see [Create a Client with an API Key](https://dev.wix.com/docs/go-headless/coding/java-script-sdk/admin/create-a-client-with-an-api-key).
- Channel partners should use the [Channel admin with API key strategy](https://dev.wix.com/docs/sdk/articles/get-started/authorization-strategies#channel-admin-with-api-key).  
To learn how to implement this strategy, see the ApiKeyStrategy in [About the Wix Client](https://dev.wix.com/docs/sdk/articles/work-with-the-sdk/about-the-wix-client).  

### About API keys
API keys are authentication tools that account owners and co-owners can create, enabling them and any developers they share the key with to make API calls at the account and site levels. 

> **Note:**
> Currently only account owners and co-owners can create API keys. 

If you are an account owner or co-owner, you can create and manage [API keys](https://support.wix.com/en/article/about-wix-api-keys) in the [API Keys Manager](https://manage.wix.com/account/api-keys), where you can assign a set of permissions that determine the types of APIs the key can access.

![API Keys Manager](./../../media/APIKeysManager.jpg)

