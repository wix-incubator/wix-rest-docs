# App Versions

## Introduction

Wix manages versioning of apps. Minor updates are given to users automatically. Major versions require notifying users who must then click to accept the update.
Version Numbers

The list of app submissions shows the history of your app’s versions, v1, v2, v3, etc. Whenever a new version is published, for example v2 in the image below, a copy is made, designated v3 and this is the draft that you will work on next. Older versions are archived.

![Version Submissions](./../app-submissions2.png)

Wix reviews the submission and determines the version number to give it. This is an internal  versioning system that contains major and minor version information. The format of this version is:

<div align="center">
1.2.0
</div>

Where 1 is the major version, 2 is the minor version, and 0 is for internal use while the version is still a draft.

## Retrieve the App Version

Use the [Get App Instance](https://dev.wix.com/api/rest/app-management/apps/app-instance/get-app-instance) API to retrieve the version of your app running on each of your user’s sites. The response contains app information:

```JSON
"instance":   {
   "appName": "MY_APP",
   "appVersion": "2.10.0",
```

As well as site information:

```JSON
"site":   {
   "locale": "en",
   "siteDisplayName": "Mysite 34",
   "url": "https://doereg11.wixsite.com/mysite-34",
   "description": "My awesome site is all about selling stuff",
   "ownerEmail": "site-owner@test.com",
   "ownerInfo":     {
     "email": "site-owner@test.com",
     "emailStatus": "VERIFIED_OPT_IN"
   }
```

On this user’s site, the app’s major version is 2 and minor version is 10. Users will get minor updates, for example to 2.11, automatically. However, the next major version, 3.0.0, will require the user to actively accept it.

## How Each Update Happens

### No Update Required

Some changes don’t require you to submit the app, and they take effect as soon as they're saved. These are:

* OAuth endpoints
* Webhooks
* Adding or removing team members

### Minor Updates

Other than the exceptions above, an updated app must be submitted for review. Once approved, a new version number (v1, v2, etc.) appears on the App Submissions page.

Most changes will be considered minor. Wix assigns a new minor version number and the update will **automatically be given** to all users that are on the **same major** version. Users with an older major version will see an Update button on the Manage Apps page, as described below for major updates.

### Major Updates

Wix may determine that changes to the app require a new major version. Such changes include:
* Adding or removing [Permissions](https://devforum.wix.com/kb/en/article/about-permissions)
* Adding an [Embedded Script](https://devforum.wix.com/kb/en/article/set-up-an-embedded-script-component) component
* Changing [Dynamic Key Parameters](https://devforum.wix.com/kb/en/article/embedded-script-dynamic-parameters) of an Embedded Script

Major versions are not automatically sent to users. Instead, users are informed on the Manage Apps page that an update for the app is available. The user simply clicks the Update button and follows the on-screen instructions to complete the update.

> **Note:**
> Only site owners can update an app, not contributors. Be sure to [test your app as a contributor](https://devforum.wix.com/kb/en/article/test-your-app-as-a-contributor) to see how this flow works for them.

<blockquote class='important'><p>
<strong>Important:</strong>
A major update essentially takes the user through the [OAuth flow](https://dev.wix.com/api/rest/getting-started/authentication). You will receive an authorization code with which you must request a new refresh token. Store the refresh token in your database for later use with the user's instance ID.
</blockquote>

![Manage Apps](./../app-manager-update.png)

For major updates, Wix recommends letting users know that they should update your app. Sending an email to site owners or placing a banner in the app are good ways to do that. You may also include a link to the Wix installer as described [here](https://dev.wix.com/api/rest/getting-started/authentication#getting-started_authentication_step-2-app-sends-users-to-authorize-the-app) so they can easily update the app.
