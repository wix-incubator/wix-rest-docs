SortOrder: 0
# Introduction

The Time Slots API allows you to retrieve availability information for time slots at a reservation location on and around a given date and for a given party size.

A time slot represents a period of time in a restaurant’s calendar. Time slots can have any duration, and restaurants generally set their durations based on party size.

The following factors influence whether a time slot at a reservation location is available:
* The size of the party that must be seated.
* The reservation location’s table and seat pacing rules.
* The reservation location’s business schedule (operating hours).
* Existing reservations at the reservation location.

With the Time Slots API, you can:
* Get time slots for a reservation location.

A time slot can have the following statuses:
* `AVAILABLE` - The restaurant is open and available to seat a party of the given size at the given date and time.
* `UNAVAILABLE` - The restaurant is open but unable to seat a party of the given size at the given date and time.
* `NON_WORKING_HOURS` - The restaurant is not open at this time.

`timeSlot` objects also indicate whether manual approval is required to make a reservation at the given reservation location.

## Before you begin
It’s important to note the following points before starting to code:
* The site owner must install the Wix Table Reservations app.
* The site owner must have at least 1 location configured in their Dashboard under [Business Info](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Fbusiness-info).

## Use Cases
[Reservation app for restaurants on a Wix site](https://dev.wix.com/docs/rest/api-reference/wix-restaurants/reservations/sample-flows#reservation-app-for-restaurants-on-a-wix-site)

## Terminology
For a comprehensive glossary of Reservations terms, see [Terminology](https://dev.wix.com/docs/rest/api-reference/wix-restaurants/reservations/terminology).
