SortOrder: 1
# OAuth Apps: Sample Use Cases & Flows

This article shares some possible use cases your app could support, as well as a sample flow that could support each use case. This can be a helpful jumping off point as you plan your app's implementation.

## Connect a custom template on any platform to an existing Wix project

You can create a frontend template, on an external platform, that takes advantage of business solutions on a Wix project.

For any external app or site to access a Wix project's data, it must be authorized in advance by creating an OAuth app. To enable project owners to connect a site or app built on your template to their existing Wix project data, follow these steps:

1. Create a template on any platform and integrate API calls from the [Wix JavaScript SDK](https://dev.wix.com/api/sdk) to access and manage business solutions in a Wix project.
1. Create a [Wix app](https://devforum.wix.com/kb/en/article/wix-for-developers) that a project owner can install.
1. Make sure your app requests the Manage OAuth Apps permission scope.
1. Obtain the domain name for the deployment of the site or app built on the template.
1. In your app code, call [Create OAuth App](https://dev.wix.com/api/rest/auth-management/oauth-apps/create-oauth-app). Specify a `name` and optional `description` that identify the client clearly. In the `allowedDomains` array, provide the deployment domains from the previous step.
1. Store the returned OAuth app's `id` and `secret` securely. **Note:** The OAuth app secret is returned only when creating the OAuth app, and can't be retrieved later.
1. Assign the ID and secret to secure environment variables in the template code. The template can now access the Wix project's data.

## Change allowed redirect domains for an external client app or site

Whenever an external client redirects a user to Wix for authentication, the client provides a URL for Wix to redirect the user back to after authentication. To ensure security, Wix only redirects the user if the domain has been approved in advance in the OAuth app's settings. To update an external client's approved URLs, follow these steps:

1. Make sure you have the OAuth app ID for the external client.
1. Obtain a complete list of domains to approve for the external site or app.
1. Call [Update OAuth App](https://dev.wix.com/api/rest/auth-management/oauth-apps/update-oauth-app) with the OAuth app ID as a path parameter. Pass all approved domains in the `oAuthApp.allowedDomains` body parameter, and pass `["allowedDomains"]` in the `mask.paths` body parameter.
1. The external app or site can now provide any redirect URL from the updated list.

## Prevent an existing client app or site from connecting to a Wix project

To prevent a client site or app from accessing a Wix project's data, you can disable its permissions by deleting the OAuth app it connects through. To delete the OAuth app, follow these steps:

1. Obtain the OAuth app ID used by the client app or site.
1. Call [Delete OAuth App](https://dev.wix.com/api/rest/auth-management/oauth-apps/delete-oauth-app) with the OAuth app ID as a path parameter.
1. The client app or site can no longer connect to the Wix project. If you wish to reactivate its connection in future, create a new OAuth app with [Create OAuth App](https://dev.wix.com/api/rest/auth-management/oauth-apps/create-oauth-app) and update the OAuth app ID used in the client app or site code.
