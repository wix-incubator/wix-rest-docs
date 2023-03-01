SortOrder: 1
# Creating a Notification Template

Create a notification template in the Wix Dev Center to specify the standard text, placeholders, and recipients of notifications.
You can then call the [Notify](https://dev.wix.com/api/rest/wix-notifications/notifications/notify) endpoint from your code to trigger sending notifications based on the template you defined.

## Accessing notifications in your app's dashboard

1. Sign in to the Wix Dev Center, then click "My Apps" in the navigation menu.

2. Click on the app you want to create a notification template for. This opens the app's dashboard.

3. Click "Notifications" in the sidebar menu. This opens the Notifications page for your app, where you can find all previously defined notification templates.

4. Click "Create Notification". This opens the form for defining a new notification template.

## Defining a notification template

Fill out the notification template creation form to define a new notification template, then click "Save" to enable it. The form includes the following sections:

### 1. Basic info

Give your notification template an internal name and description for managing it in the Wix Dev Center.
These are visible only to you.

Choose a name and description that make clear what the notification is about and who receives it.
For example, you might choose a name like "New reservation" and a description like "Sent to the site owner when a customer makes a new reservation."

Here you can also find the **notification template ID**. You need this ID to identify your notification template in API calls.

### 2. Recipients

Define who receives notifications of this type and where they receive them.

Choose whether all site contributors or only site owners receive notifications.

Choose where recipients receive notifications: in the site feed on the Dashboard, in the Wix Owner mobile app, or in both.
Recipients who receive notifications in the mobile app receive push notifications on their mobile device and can see the notifications in the app's notification center.

### 3. Message

Create the notification content.

If you enable notifications to the mobile app in the Recipients section, a "Title" field appears here. Enter a notification title that recipients will see.

In the "Message" field, enter the text of your notification.

The message and the title can include placeholders for dynamic values you provide each time you send an HTTP request to trigger notifications. For example:

> **Title:** Item delivered: {{itemType}}.
>
> **Message:** {{customerName}} has received a {{itemType}} delivery.

When triggering a notification with the [Notify](https://dev.wix.com/api/rest/wix-notifications/notifications/notify) endpoint in your code, you pass values for `itemType` and `customerName`, so a recipient sees a customized notification like this:

> **Title:** Item delivered: television.
>
> **Message:** Sally Jones has received a television delivery.


### 4. API consumption

Remember your notification template ID and the names of placeholders for dynamic values in your message and title, as you'll need them to invoke the API and trigger notifications.
But don't worry if you forget them - you can always return to the Wix Dev Center to look these details up.

Press "Save" to generate your notification template. You can now trigger notifications with the [Notify](https://dev.wix.com/api/rest/wix-notifications/notifications/notify) endpoint!