SortOrder: 2
# Events v3: Sample Use Cases & Flows

This article presents possible use cases and corresponding sample flows that your app can support. It provides a useful starting point as you plan your app's implementation. 

## Cancel a concert tour and send cancellation emails for customers

This use case demonstrates the automation of event cancellation. For example, when a concert tour is canceled, the Events API allows you to bulk cancel all scheduled concerts simultaneously. Additionally, automated cancellation emails can be sent to notify customers about the tour cancellation, providing essential information and any available alternatives or refunds.

To cancel events and send cancellation emails, follow these steps:

1. [Query Event Guests](https://dev.wix.com/api/rest/wix-events/event-guests/query-event-guests) by `eventId` of the events that are going to be cancelled.

1. Retrieve all the email addresses from the `guestDetails` object, and write your code so that the email address can be passed to your marketing tool.

1. On an ongoing basis, listen for the [Event Canceled Webhook](). 

1. [Bulk Cancel Events by Filter](). Specify `categoryId` of the recurring events in the filter object to cancel all events.

1. When the webhook is triggered for your event, send the cancellation email from your marketing tool.

## Send reminders to guests before an event

Send timely notifications and important details leading up to the event for your attendees. Organizers can schedule automated reminders to be sent to registered attendees a specific number of days or hours before the event:

- 7 days
- 3 days
- 1 day
- 2 hours
- 1 hour
- 30 minutes

These reminders can include event date, time, location, agenda, and any additional instructions or updates. This use case reduces the likelihood of no-shows, and enhances attendee engagement.

To send reminders, follow these steps:

1. [Query Event Guests](https://dev.wix.com/api/rest/wix-events/event-guests/query-event-guests) by `eventId`.

1. Retrieve all the email addresses from the `guestDetails` object, and write your code so that the email addresses can be passed to your marketing tool.

1. On an ongoing basis, listen for [Event Reminder Webhook](). 

1. When the webhook is triggered for your event, send the reminder email from your marketing tool.
