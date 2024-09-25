SortOrder: 0
# About the External Calendar Sync API

Use the external calendar sync API to sync the Wix Bookings Calendar and an external calendar - currently supports Google Calendar.

When a Wix calendar and an external calendar are synced, the following occurs:
- A session that is created in the Wix Bookings schedule will also be created in the external calendar.
- An event that is created on the external calendar will affect the availability of a Wix schedule, and the slots that are returned in the [Query Availability](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings-and-time-slots/time-slots/availability-calendar/query-availability) endpoint.
    - The events from the external calendar will be returned in the [List Sessions](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/session/list-sessions) endpoint,  and will hold a `tag` with the value "`google`"
- When an session is modified / deleted in Wix Bookings, it will also be modified / deleted in the external calendar.
- When an event is modified / deleted in the external calendar service,  it will also be modified / deleted in Wix Bookings.

## Terminology:

- **External Calendar**: A non Wix calendar (e.g., Google Calendar). 

- **Resource** (not necessarily related to the Resource API): An entity with two defining features:
	- it is a schedule owner in Wix Bookings,
	- it has a calendar in an external calendar. 
	For example: A staff member in a business registered with Wix Bookings that also has a Gmail account and a Google calendar.

- **Events**: The external calendar equivalent of sessions in Wix Bookings.

## Syncing process

1. A sync request triggers an email which is sent to the owner of the external calendar (to the email associated with the external calendar).
2. The external calendar owner opens the email and approves Wix's request to access their external calendar.
3. All events that appear on the external schedule will be displayed on the resources Wix schedule, and all sessions that appear on the resource's Wix schedule will appear on the external calendar (two-way sync). 

The following data is synced from a schedules session to an external calendar event:

- Title
- Description
- location
- Start Time
- End Time

You can use a session's (or schedule's) `ExternalCalendarOverrides` property to modify the title and description that appear on the external calendar event.
