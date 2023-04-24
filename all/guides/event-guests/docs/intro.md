SortOrder: 0
# About Event Guests

The Event Guests API allows you to retrieve information about all guests who bought tickets to an event or who RSVP'ed. This can be particularly useful for event organizers who need to manage large numbers of attendees or who want to integrate their event management system with other software tools. Additionally, with the Event Guests API you can create custom applications that leverage event guest data, such as mobile event apps or marketing automation systems.  

The Event Guests API allow you to:  

* Retrieve a list of guests by event ID.
* Get information about each individual ticket buyer.
* Find out the attendance status of each guest.

## Before you begin

It’s important to note the following points before starting to code:

- Install the **Wix Events & Tickets** app from [Wix App Market](https://www.wix.com/app-market/wix-events?referral=category&appIndex=5&referralTag=booking--events).
- Guest details are returned only when the `guestDetails` fieldset is sent in the request.
- In some situations, certain webhooks might be triggered twice. For example, changing a guest's name triggers the [Event Guest Updated](https://dev.wix.com/api/rest/wix-events/event-guests/event-guest-updated-webhook) webhook 2 times -- once for the change of name and once for the change of order, which also occured. While technically correct behavior, this might cause the undesired side effect of duplicated actions. Make sure to explicitly add code to make sure parts of your code only run once.

## Terminology

- **Guest**: The individual who has been invited to the event.
- **RSVP**: A response from the guest indicating whether they plan to attend the event.
- **Ticket buyer**: The individual who bought 1 or more tickets to the event.
- **Check-in**: The process of verifying a guest's attendance at the event.
- **Guest list**: A summary of all guests who have been invited to the event.
- **Organizer**: The person or entity responsible for planning and hosting the event.