SortOrder: 0
# About the OAuth Apps API

The OAuth Apps API enables you to manage OAuth apps for a [Wix Headless](https://dev.wix.com/api/sdk/about-wix-headless/overview) project or site. An OAuth app authorizes an external client app or site, on any platform, to authenticate with a Wix site or project and manage its data using the [Wix JavaScript SDK](https://dev.wix.com/api/sdk/introduction/about-the-wix-javascript-sdk).

With the OAuth Apps API, you can:

+ Create a new OAuth app to enable an external client to access a Wix project or site.
+ Query and retrieve information about existing OAuth apps.
+ Update details of an existing OAuth app.
+ Delete an OAuth app.

To use Wix Headless functionality you need to create an OAuth app, either using the OAuth Apps API or in the project or site's [dashboard](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Foauth-apps-settings). For instructions on how to do this, see how to [Set Up Authorization](https://dev.wix.com/api/sdk/sdk-setup:-wix-headless/authorization) for Wix Headless.

Once you have created an OAuth app, learn how to [Set Up the Wix JavaScript SDK for Wix Headless](https://dev.wix.com/api/sdk/sdk-setup:-wix-headless/set-up-the-wix-sdk).

## Before you begin

It's important to note the following points before starting to code:

+ The client secret is provided only when an OAuth app is created, and can't be retrieved later.
+ Each external client should authenticate using its own OAuth app.
+ After you delete an OAuth app, an external client can no longer make API calls by authenticating with its client ID.

## Use cases

+ [Connect a custom template on any platform to an existing Wix project](https://dev.wix.com/api/rest/auth-management/oauth-apps/sample-flows#connect-a-custom-template-on-any-platform-to-an-existing-wix-project)
+ [Change allowed redirect domains for an external client app or site](https://dev.wix.com/api/rest/auth-management/oauth-apps/sample-flows#change-allowed-redirect-domains-for-an-external-client-app-or-site)
+ [Prevent an existing client app or site from connecting to a Wix project](https://dev.wix.com/api/rest/auth-management/oauth-apps/sample-flows#prevent-an-existing-client-app-or-site-from-connecting-to-a-wix-project)

## Terminology

+ **OAuth app:** An intermediary application that authorizes and authenticates an external client to access data on a Wix project or site.
+ **Project:** A Wix business backend incorporating Wix business solutions, but which doesn't necessarily have a Wix site frontend.
+ **Client:** An external app or site, built on any platform, which accesses or manages data on a Wix project or site using Wix APIs.
+ **Client ID:** A unique ID that an external client uses to authenticate for making API calls.
+ **Client secret:** A unique credential that an external client uses to authenticate for admin access to a Wix project or site.
