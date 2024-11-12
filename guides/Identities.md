# About Identities

Every request to a Wix API is made by a specific identity type. For each call, the caller's identity is checked and confirmed to have the necessary permissions.  
If a [method has identity restrictions](#methods-with-restricted-identities), the reference documentation will include a note specifying the allowed identity types. 

Wix's identity types include:

- [Site visitor](#site-visitor) 
- [Site member](#site-member) 
- [Wix user](#wix-user) 
- [Wix app](#wix-app) 
- [API key admin](#api-key-admin) 

> **Note**: Additional identities are supported for app flows using the [SDK](https://dev.wix.com/docs/sdk).

## Site visitor

An anonymous site visitor is a site visitor who hasn't logged in. Methods that can be called by this identity usually involve operations specific to a particular visitor. 

**Context**:  
- [Headless](https://dev.wix.com/docs/go-headless/getting-started/about-headless/about-wix-headless) flows can make calls as site visitors.

**Example use cases**:
- A headless site can make calls to Wix's APIs as an anonymous site visitor to access a list of products, create and manage a cart, or access a login page to authenticate as a member.

## Site member

- A site member a site visitor who has logged in. Methods that can be called by this identity usually involve operations specific to a registered member. These include accessing or managing personal data.

**Context**:   
- [Headless](https://dev.wix.com/docs/go-headless/getting-started/about-headless/about-wix-headless) flows can make calls as site members.

**Example use cases**:
A headless site can make calls to Wix's APIs as a site member to access personal order data or edit their personal member profile.  

## Wix user

A Wix user is someone who is logged into their account on **.wix.com**. Users can be site owners or site collaborators, as well as app owners and collaborators who create test sites. Users who create a site are automatically designated as the owner of that site. 

Methods that can be called by this identity usually involve site maintenance operations. These include managing site products, media, and marketing campaigns.

Site owners can invite collaborators and assign them specific [user roles](https://support.wix.com/en/article/roles-permissions-overview) to control permissions. In this case, the methods that the app can access when making calls as a collaborator are limited by the collaborator's user roles.

**Context**:   
- [Headless](https://dev.wix.com/docs/go-headless/getting-started/about-headless/about-wix-headless) flows can make calls as Wix users.
- Apps can make calls [on behalf of Wix users](https://dev.wix.com/docs/build-apps/develop-your-app/access/authentication/about-authentication#authentication-on-behalf-of-a-wix-user).

**Example use cases**:
- A headless site can make calls to Wix's APIs as a Wix user to edit store products, create a coupon, or create a bookings calendar.
- An app can make calls to Wix's APIs on behalf of a Wix user to edit store products, create a coupon, or create a bookings calendar. These calls are authenticated with the Wix app identity, and XXX

## Wix app

Wix apps are packages of reusable functionality that users can add to their sites. When an app is installed or updated on a Wix site, Wix generates an [app instance](https://dev.wix.com/docs/build-apps/develop-your-app/access/app-instances/about-app-instances) with a unique ID. This ID represents the installed version of the app on that particular site. 
A call authenticated with the Wix app identity is a call made by an app for a specific app instance.

Methods that can be called by this identity usually involve site-level operations. These include managing the site's data collections, contacts, or products.

Each method requires certain permissions when called by a Wix App. To check which permissions a method requires, refer to its API reference.

Learn more about [configuring app permissions](https://dev.wix.com/docs/build-apps/develop-your-app/access/authorization/configure-permissions-for-your-app).

**Context**:
- Apps can make calls as apps.

**Example use cases**:
- An app can make calls to Wix's APIs as a Wix app to edit store products, create a loyalty program, or import an order.

## API key admin

An API key admin is an account admin with customized administrative access to a Wix account's sites and projects. [API keys](https://support.wix.com/en/article/about-wix-api-keys) are created and managed in the [API Keys Manager](https://manage.wix.com/account/api-keys) where site owners and co-owners can assign a set of permissions that determine the types of APIs each key can access. 

Methods that can be called by this identity can involve administrative operations at the site or account level. These include managing members or business data. 

Because API keys must be created by the site owners or co-owners, and passed manually to any developer who wants to use them, they aren't recommended for apps.

**Context**:
- [Headless](https://dev.wix.com/docs/go-headless/getting-started/about-headless/about-wix-headless) flows can make calls as API key admins.
- Site admin flows can make calls as API key admins. 
- [Channel](https://support.wix.com/en/article/wix-channels-dashboard-overview) and [Enterprise](https://support.wix.com/en/article/wix-enterprise-an-overview) admin flows can make calls as API key admins.

**Example use cases**:
- A headless admin can make calls to Wix's APIs as an API key admin to invite team members to join the account, manage domains and create store products.
- A Channel or Enterprise admin can make calls to Wix's APIs as an API key admin to invite team members to join the account, manage domains and create store products.


## Methods with restricted identities
By default, methods can be called using any identity.
In cases when there are restrictions on which identities can call a method, one of the following notes appears in the reference:

> **Admin Method**
> You can only call this method when authenticated as a Wix app or Wix user identity.

> **Note:** Only logged-in members can call this method without elevated permissions. To call this method as a different identity, elevated permissions are required.
