# App Versions

## Introduction

During the normal life cycle of your app, periodic updates will be required. Each update must be submitted to Wix and when the update is approved it can be sent to your users. Wix determines whether an update is major or minor and manages the versioning of the app accordingly. Minor updates are sent to users automatically, while major updates require an opt-int.

This article explains which updates are major, which are minor, and how the versioning and update process differs between them.
## Submitting an App Update for Review

When you have updated an app, submit it to Wix for review by going to App Submissions in the dashboard and follow the instructions in the submission checklist. Details about the submission process can be found [here](https://devforum.wix.com/kb/en/article/submit-your-app-for-review).

Once approved, the updated app is given a new version number following the sequence v1, v2, v3, etc. Internally, the new version is marked as either a major or minor revision. Wix archives all versions of your app.

In the example below, version v2 has been approved and published. This is the version that users will get. A draft version with the next version number, v3, is created automatically once v2 was approved. Changes to the app will be saved to v3 from now on.

![alt_text](images/image1.png "image_tooltip")

## Major and Minor Updates

#### **Major Updates**

Some changes to your app require a **major** update. These are:

* Adding or removing [Permissions](https://devforum.wix.com/kb/en/article/about-permissions)
* Adding an [Embedded Script](https://devforum.wix.com/kb/en/article/set-up-an-embedded-script-component) component
* Changing [Dynamic Key Parameters](https://devforum.wix.com/kb/en/article/embedded-script-dynamic-parameters) of an Embedded Script

Major updates are not automatically sent to users. Instead, users are informed that the update is available. A user must click the Update button and follow any on-screen instructions to get the update.

![alt_text](images/image2.png "image_tooltip")

> **Note:** Only site owners can update an app, not contributors. Be sure to test your app as a contributor to see how this flow works for them.

<blockquote class='important'>
  <p>
    <strong>Important:</strong><br/>
    A major update essentially takes the user through the OAuth flow. You will receive an authorization code with which you must request a new refresh token. Store the refresh token in your database for later use together with the user's instance ID.
  </p>
</blockquote>

With major updates, Wix recommends you let users know that they should update your app. Sending an email to site owners or placing a banner in the app are good ways to do that. You may include a link to the Wix installer as described [here](https://dev.wix.com/api/rest/getting-started/authentication#getting-started_authentication_step-2-app-sends-users-to-authorize-the-app) so they can easily update the app.

#### **Minor Updates**

Most updates are considered **minor**. Users will automatically receive minor updates but only if they have the most recent major update. If not, they will be offered an update with the Update button on the Manage Apps page. This will provide the update via the major update flow.

> **Note:** Some changes don't need a new version and don't require an update. Changes to OAuth endpoints, Webhooks and adding or removing team members take effect as soon as you save the app.

### How to Tell Major from Minor Updates

Wix maintains an internal versioning system that contains the major and minor version information. The format of this version is:

> <font size="+1">&nbsp;&nbsp; **Version 2.10.0**</font>

where 2 is the major version and 10 is the minor version. (The last number is for internal use while the version is still a draft.)

Use the [Get App Instance](https://dev.wix.com/api/rest/app-management/apps/app-instance/get-app-instance) API to retrieve the internal version of your app that is installed on each of your users’ sites. The response contains app information:

```JSON
"instance":   {
   "appName": "MY_APP",
   "appVersion": "2.10.0",
```

as well as site information:

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

On this user’s site, for example, the app’s major version is 2 and minor version is 10. Users will get minor updates automatically, for example to 2.11 and 2.12. However, the next major version, 3.0.0,  will require the user to click the Update button or follow the instructions in your email or banner.
