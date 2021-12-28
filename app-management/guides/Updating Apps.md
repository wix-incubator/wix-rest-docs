# Updating Apps

## Introduction

It is easy to manage and deploy new versions of your apps. Wix handles the versioning process differentiating between major and minor updates.

## App Versions

An app’s version is a set of three numbers separated by periods, for example '**1.16.0**'. The first number indicates the major version (‘1’), and the second number indicates the minor version (‘16’). The third number is currently not in use and is always '0'.

The version number can be retrieved using the [Get App Instance](https://dev.wix.com/api/rest/app-management/apps/app-instance/get-app-instance) API, where the App ID is used to obtain an access token that is then passed in the authorization header of the request.

When you first submit an app, it is designated ‘v1’ with an Actual Version of “Draft”. Once it is approved, it is given the version number ‘1.0.0’. At the same time, a new version ‘v2’ is created as a copy of ‘v1’ and it is given the Actual Version of Draft. This means that v1 is now frozen and any changes you make will occur in v2 Draft.

![App Submissions](./../app-submission.png)

## App Updates

Some changes to your app do not require a version change or update for your users. They are:
- OAuth endpoints
- Webhooks
- Addition or removal of team members.

These changes take effect immediately as soon as they are saved.

All other changes require you to submit the Draft app for approval. Once approved, the Draft is assigned the new version number, a new Draft is prepared from it, and the new version is available to users as an update.

How the update gets to users depends on whether the new version represents a major or a minor change.

## Major vs Minor Updates

The majority of the changes you will make to your app are minor. As Wix approves them, the minor version number will be incremented (say, from '1.16.0' to '1.17.0'). Minor versions are then automatically made for all users, but **only** if they already have the same major version. Consider:

- User A installed app version 2.0.0. As you update your app to 2.1.0, 2.2.0, and more, User A will automatically get the updated versions.
- User B installed an older version of your app, 1.15.0. As you update your app from 2.0.0 to 2.1.0, 2.2.0, and more, User B will **not** get these updates until first upgrading or reinstalling a version 2.x.0.

It is important, then, to make sure that your users stay current with your major version updates. Major changes include:

- Adding or removing Permissions
- Certain changes to Embedded Scripts

## Getting Major Updates to Your Users

Users do not automatically get major updates. It is up to both Wix and the app developer to inform users about a major update and provide the means for getting it.

When a major update is available, an Update button is added in the App Manager.

![Update App](./../app-manager-update.png)

The user must click the Update button and follow any on-screen directions for the update to be installed.

Wix also recommends that you inform users that a major update is available, say, with a **banner** or via **email**. Provide a link to https://www.wix.com/installer/install with the appId and a redirect URL as described [here](https://dev.wix.com/api/rest/getting-started/authentication#getting-started_authentication_step-2-app-sends-users-to-authorize-the-app). This will initiate the same update process described above.

> Note:
> Only site owners can update an app, not contributors. Please [make this clear](https://devforum.wix.com/kb/en/article/test-your-app-as-a-contributor) in your communications.

One more thing: Getting a major update essentially takes the user through the OAuth 2 flow. You will receive an authorization code with which you must request a new **refresh token**. Store the refresh token in your database for later use with this instance ID.
