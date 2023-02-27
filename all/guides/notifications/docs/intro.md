SortOrder: 0
# About the Notifications API

The Notifications API enables you to trigger the sending of predefined notifications to Wix site owners and contributors.

With Notifications, you can trigger notifications that Wix users can receive:

+ In the site feed on the Dashboard.
+ In the Wix Owner app notification center.
+ As a mobile push notification from the Wix Owner app.

## Before you begin

It's important to note the following points before starting to code:

+ You need to [create a notification template](https://dev.wix.com/api/rest/wix-notifications/notifications/creating-a-notification-template) in the Wix Dev Center before you can send notifications with the Notifications API. A notification template specifies the text and recipients for notifications. It can include both standard text and placeholders for dynamic values you provide when you send notifications using the Notifications API.
+ An app can call the [Notify](https://dev.wix.com/api/rest/wix-notifications/notifications/notify) endpoint up to 100,000 times per month for each site.

## Terminology

+ **Notification template:** Specification of standard text, placeholders, and recipients for a particular type of notification. Created in the Wix Dev Center.
+ **Dynamic values:** Text that replaces a notification template's placeholders when sending notifications from your code.
+ **Notification:** An individual message sent to a Wix user by the Notifications API as part of a notification batch.
+ **Notification batch:** All the notifications triggered by a single call to the Notify endpoint.
