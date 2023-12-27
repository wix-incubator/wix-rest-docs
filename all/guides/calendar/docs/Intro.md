SortOrder: 0
# About Wix Bookings Calendar V2

Wix Bookings Calendar V2 enables you to retrieve information about the business calendar.

With the Calendar V2 API, you can:

+ Retrieve information about a specific session or multiple sessions.
+ Query event instances in the calendar between specified dates.
+ Query sessions with advanced filtering and paging functionality.
+ Retrieve information about calendar availability.

## Before you begin

It's important to note the following points before starting to code:

+ To query all event instances within a time range of up to 1 year, use [Query Sessions](#query-sessions) with `fromDate`, `toDate`, and `type` set to `EVENT`.
+ By default, [Get Session](#get-session), [Query Sessions](#query-sessions), and [List Sessions](#list-sessions) return session objects without personal information. To retrieve full session objects including personal information, use the `ALL_PI` fieldset.
+ [List Sessions](#list-sessions) is for retrieving multiple sessions by their IDs. Use [Query Sessions](#query-sessions) to retrieve based on other filters.
+ [Query Sessions](#query-sessions) sorts results by `start.timestamp` in ascending order. You can't override this default sorting.

## Terminology

* __Calendar:__ General overview about the availability and bookings of the business, including its services and resources.
* __Resource:__ Business asset like a staff member, room, or equipment that's needed to provide a service.
* __Schedule:__ Collection of all sessions that belong to the same class, course, appointment, or resource. 
* __Schedule tag:__ Type of the schedule. Used to display Wix Bookings services correctly in the UI. Supported schedule tags are:
  + __INDIVIDUAL:__ One-time session that customers can book based on availability. 
    For example, a company can book a single Tai Chi session as a team-building event for its employees on a specific date.
  + __GROUP:__ An unlimited number of sessions for the same service. 
    For example, a Yoga class that happens every Monday and Wednesday at 5pm. 
  + __COURSE:__ A limited number of sessions for the same service. 
    For example, a 12-session introductory course to Pilates, starting on February 1st and ending on March 17th. 
* __Session:__ An _occupied_ period of time on a schedule. A session of type `EVENT` is a recurring or single session that appears in a specific block of time in a calendar, such as an appointment or class.
* __Recurring session:__ A recurring session defines a pattern for repeating sessions that occur on a regular basis.
* __Slot:__ An _available_ period of time in a schedule that can be booked by a customer.