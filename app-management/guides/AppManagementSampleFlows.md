# App Management: Sample Use Cases and Flows

This article shares some possible use cases your app could support, as well as
a sample flow that could support each use case. This can be a helpful jumping
off point as you plan your app's implementation.

## Encourage new users to upgrade

You could reach out to new users who install the free version of your app and
encourage them to upgrade.

To encourage upgrades:

1. Listen to the [Instance App Installed](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/instance-app-installed)
   webhook. Make sure to save the `data.instanceId` from the payload.
1. Pass the `instanceID` when calling
   [Get App Instance](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/get-app-instance).
1. In the response data, confirm that the site owner's have installed the free
   version of your app by checking `instance.isFree`. Also save the site owner's
   email, you can find it in `instance.ownerInfo.email`.
   Make sure to confirm that the user has opted in to receive communication by
   checking that `instance.ownerInfo.emailStatus` is either `"VERIFIED_OPT_IN"` or
   `"NOT_VERIFIED_OPT_IN"`. Note that you must have added the
   __Read Site Owner Email__ permission scope to your app during the setup
   process in the [Wix Developers Center](https://dev.wix.com/docs/build-apps/developer-tools/developers-center/example-app-walkthrough/build-an-app#4-add-permissions).
   In case you, haven't requested this permission, the `ownerInfo` object is
   always returned empty.
1. In case the owner's have opted in to receive notifications, send them an email that includes a link to the
   [Upgrade Button]().
1. Listen to the [Paid Plan Purchased](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/paid-plan-purchased)
   webhook to get notified about the upgrade.

We recommend signing up for the [Instance App Installed](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/instance-app-installed)
webhook. In case your app is using Wix REST APIs, you would also receive an
access token that includes the app instance ID during the
[OAuth setup](https://dev.wix.com/docs/rest/articles/getting-started/authentication#the-oauth-flow),
but listening to the webhook ensures the installation process has succeeded.

## Identify a site's installed Wix business solutions

In case your app requires that the site owners have also installed a specific
[Wix business solution](https://dev.wix.com/docs/rest/articles/getting-started/wix-business-solutions),
you can verify that the relevant app is installed on that site. During your app's
setup process in the Developers Center you can mark one or more Wix app's as
requirements, but we recommend to follow this flow since you may support different use
cases, depending on which Wix app is installed. For example, your app may support
different use cases, depending on whether the site includes [Wix Stores](https://www.wix.com/app-market/wix-stores?referral=collection&appIndex=2&referralTag=made-by-wix&referralSectionName=made-by-wix)
or [Wix Bookings](https://www.wix.com/app-market/bookings?referral=collection&appIndex=6&referralTag=made-by-wix&referralSectionName=made-by-wix).

To Identify a site's installed Wix apps:

1. Listen to the [Instance App Installed](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/instance-app-installed)
   webhook. Make sure to save the `data.instanceId` from the payload.
1. Pass the `instanceID` when calling
   [Get App Instance](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/get-app-instance)
   to retrieve installed Wix apps. You can find them as human-readable names in
   the `site.installedWixApps` array. In case your app supports multiple use cases,
   see if you can identify the user's intent from the list of returned apps alone.
1. Optional: If they have installed multiple Wix apps for which you support
   different flows, reach out to the site owner to check their preference. Make
   sure to confirm that the user has opted in to receive communication by
   checking that `ownerInfo.emailStatus` is either `"VERIFIED_OPT_IN"` or
   `"NOT_VERIFIED_OPT_IN"`. Note that you must have added the
   __Read Site Owner Email__ permission scope to your app during the setup
   process in the [Wix Developers Center](https://dev.wix.com/docs/build-apps/developer-tools/developers-center/example-app-walkthrough/build-an-app#4-add-permissions).
   In case you, haven't requested this permission, the `ownerInfo` object is
   always returned empty.

## Automatically create user login

You could automatically create a user login for new customers of your app.

To create user logins:

1. Listen to the [Instance App Installed](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/instance-app-installed)
   webhook. Make sure to save the `data.instanceId` from the payload.
1. Pass the `instanceID` when calling
   [Get App Instance](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/get-app-instance)
   to retrieve the site owner's email, you can find it in `instance.ownerInfo.email`.
   Note that you must have added the
   __Read Site Owner Email__ permission scope to your app during the setup
   process in the [Wix Developers Center](https://dev.wix.com/docs/build-apps/developer-tools/developers-center/example-app-walkthrough/build-an-app#4-add-permissions).
   In case you, haven't requested this permission, the `ownerInfo` object is
   always returned empty.
1. Set up the automatic user login on your app's side.