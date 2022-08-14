SortOrder: 0
# About Wix Bookings Calendar V2

With Wix Bookings Calendar V2, you can retrieve information about the business calendar. 

Calendar V2 replaces the [List Sessions V1 endpoint](https://dev.wix.com/api/rest/wix-bookings/calendar/sessions/list-sessions) 
and offers advanced filtering and paging functionality in [Query Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar-v2/query-sessions).

You can read more about setting up and managing sessions for a business calendar with the 
[Sessions API](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/session/create-session).

To retrieve information about the calendar availablity, you need to use the 
[List Slots endpoint](https://dev.wix.com/api/rest/wix-bookings/calendar/sessions/list-slots).




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
* __Session:__ An _occupied_ period of time on a schedule.
* __Slot:__ An _available_ period of time in a schedule that can be booked by a customer. 



## Limitations


+ [Query Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar-v2/query-sessions) sorts results by `start.timestamp` in ascending order. 
  You can't override this default sorting.
+ You can retrieve either the full session object or session objects without any personal information. 
  You can't customize which fields are returned.