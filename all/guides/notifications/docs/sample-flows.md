SortOrder: 2
# Notifications: Sample Use Cases & Flows 

This article shares some possible use cases your app could support, as well as
a sample flow that could support each use case. This can be a helpful jumping
off point as you plan your app's implementation.

## Notify a Wix site owner when a customer makes a new room reservation using your app

When a customer makes a new reservation, notify the Wix site owner with the customer name, room type, and the day of the week. 

To notify a Wix site owner:

1. [Create a notification template](https:dev.wix.com/api/rest/wix-notifications/notifications/creating-a-notification-template) in the Wix Dev Center with the Wix site owner as the recipient.

For example:

> **Title:** New {{roomType}} reservation.
>
> **Message:** {{customerName}} just made a new {{roomType}} reservation for {{dayOfWeek}}.


Save the given notification template ID and note the dynamic values.


2. A customer makes a new room reservation. For example, Sally Jones reserves the studio for Friday.

3. Pass the given notification template ID and the dynamic values to the [Notify](https://dev.wix.com/api/rest/wix-notifications/notifications/notify) endpoint to trigger the notification based on the notification template.

  ```json
  {
    "notificationTemplateId": "<GIVEN_NOTIFICATION_TEMPLATE_ID>",
    "dynamicValues": {
      "roomType": {
        "text": "studio"
      },
      "customerName": {
        "text": "Sally Jones"
      },
      "dayOfWeek": {
        "text": "Friday"
      }
    }
  }
  ```

4. The Wix site owner receives the notification defined in the Wix Dev Center:

> **Title:** New studio reservation.
>
> **Message:** Sally Jones just made a new studio reservation for Friday.