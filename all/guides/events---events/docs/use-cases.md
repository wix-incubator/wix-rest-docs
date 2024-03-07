SortOrder: 9
# Use Cases

The Wix Events API allows third party developers to manage events through their whole lifecycle, and customize each step.

## Automate event scheduling based on demand

An event organiser wants to ensure their resources are used efficiently, so they decide to
 - cancel events that are under-booked
 - set up provisional events as soon as existing events are over-booked

This can be automated, e.g. in a dedicated event management app, by a third party developer, as follows:

1. Decide on minimum and maximum booking levels for events, and input these settings in the third-party app
1. List events to get event IDs
1. Get tickets for each event ID
1. Analyze ticketing numbers to see which events are over- or under-booked
1. Cancel (unpopular events) or copy (popular) events accordingly

## Create an events dashboard based on event categories <--- needs category endpoint!

A third party wants to create feeds of events in specific categories (e.g., theater, concert, networking, fitness) to promote in multiple contexts around the web, linking back to the site owner for ticket sales.

1. Consume event webhooks to get updates when events are created, updated (maybe with a different category), etc.
1. List all categories to get category IDs
1. List all events, filtering by category ID
1. Repeat previous step for each category
1. Pass events to event feed
