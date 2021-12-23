# Updating Apps

## Introduction

It's easy to manage and deploy updates to your apps. Wix handles the versioning process for you, differentiating between major and minor updates.

## App Versions

An app’s version number is composed of three numbers separated by periods, for example '1.16.0'. The first number indicates the major version ('1'), and the second number indicates the minor version ('16'). The third number is currently not in use and is always '0'.

> Note:
> After an app is approved for the first time, the **Actual Version** - an internal numbering sequence -  is set to 'DRAFT' while the **Version** is set to 'v1' (see the App Submissions page). Once the app is approved the Version becomes '1.0.0'.

![App Versions](app-submission.png)

## App Updates

Some changes do not require an update. These are OAuth endpoints, Webhooks and addition or removal of team members. Once saved, these changes take effect immediately.

With all other changes, apps must be submitted for approval before they can be republished to users. During the approval process, the app remains unchanged. Once approved, the app is assigned a new version number and republished to the app market.

Most other changes are minor, and the minor version number is incremented, for example, from '1.16.0' to '1.17.0'. The app will automatically update to all users who are on the same **major** version, without any input from you or your users.

Major changes include changes to **Embedded Scripts** and adding or removing **Permissions**. The app's major version number will be incremented, but existing users will not be automatically updated.

## Strategies for Major Updates

Wix and the app developer share in managing major updates. When a major update is available, an **Update** button is added in the App Manager.

![App Manager](./../app-manager-update.png)

Clicking the button displays a popup showing the available update version and the changes that were made.

![App Manager](./../update-popup.png)

The user clicks to agree, the app is updated and the user is then further instructed, if necessary,  to open the app's settings and allow other changes there.

We recommend you inform your users with a banner or email to site owners that an update is available . Provide this link: https://www.wix.com/installer/install with your **app ID** and a **redirect URL** as described in detail [here](https://dev.wix.com/api/rest/getting-started/authentication#getting-started_authentication_step-2-app-sends-users-to-authorize-the-app). This will initiate the same update process described above.

> Note:
> Only site owners are allowed to update an app so you may want to email or display a banner only to them. Learn more about contributors [here](https://devforum.wix.com/kb/en/article/test-your-app-as-a-contributor).
