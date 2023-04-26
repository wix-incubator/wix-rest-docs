SortOrder: 2
# Event Guests: Sample Use Cases & Flows

This article shares some possible use cases your app could support, as well as a sample flow that could support each use case. This can be a helpful jumping off point as you plan your app's implementation.  

## Send invitations to customers for a new event

A lot of users aim to re-engage attendees who have previously participated in similar events or activities. With your app, you can retrieve the guest list from a past event and create a targeted email campaign that includes details about the upcoming event. The invitation can be tailored based on the past attendance history (see [Get guest attendance analytics from your analytics system](https://dev.wix.com/api/rest/wix-events/event-guests/sample-use-cases-and-flows#wix-events_event-guests_sample-use-cases-and-flows_get-guest-attendance-analytics-from-your-analytics-system)) or preferences of guests. This use case can be an effective way to increase attendance at future events, and generate more interest in them.

> **Note**: This flow assumes your guests already have the ability to subscribe to your newsletters.

To send invitations about an upcoming event, follow these steps:

1. [Query Event Guests](https://dev.wix.com/api/rest/wix-events/event-guests/query-event-guests) by past `eventId`.

2. Retrieve all the email addresses from the `guestDetails` object, and write your code so that they can be passed to your marketing tool.

3. Request and filter the list of subscribers in your external marketing tool by the retrieved emails. 

4. Filter the list once again by the subscription status.

5. The contacts who have opted-in to marketing emails is now ready to receive the invitations.

## Get guest attendance analytics from your analytics system

An analytics system can provide valuable insights into guest attendance at events, making it easier to track and analyze data on attendance patterns, behavior, and preferences. For example, you can use your app to periodically check attendance for your events to determine which events often have no-shows. This information could help you determine if certain events need more advertising, reminders, or a change to pricing (for example, people are more likely to attend if they have paid, even a small amount, to attend).

To get attendance analytics, follow these steps:

1. [Query Event Guests](https://dev.wix.com/api/rest/wix-events/event-guests/query-event-guests) of each past event, filtering by `eventId`.

2. For each event and each of its guests, retrieve the `guestDetails.checkedIn` value, and ensure that your code is capable of passing it to your analytics tool.

3. In your analytics tool, calculate for each event how many `guestDetails.checkedIn` values are `false` and compute the attendance ratio.