SortOrder: 0
# About the Wix Bookings Attendance API


With the Wix Bookings Attendance API,  you can retrieve and manage a booked session's attendance information by: 

* [Setting](https://dev.wix.com/api/rest/wix-bookings/attendance/set-attendance) the attendance for a given booked session.
* [Getting](https://dev.wix.com/api/rest/wix-bookings/attendance/get-attendance) the attendance information for a given booked session by ID.
* [Querying](https://dev.wix.com/api/rest/wix-bookings/attendance/query-attendance) the attendance by given filters, sorting, and paging.

## About the attendance object

The [attendance object](https://dev.wix.com/api/rest/wix-bookings/attendance/attendance-object) holds information about the attendance of a booked session, such as: 
* Did anyone attend the session? 
* How many people attended the session?

The number of session `Attendance` objects available depends on session types:  
+ Appointment sessions have 1 `Attendance` object per appointment.
+ Class sessions have an `Attendance` object for each session of the class. The number of sessions for a class is defined in Schedule and Sessions' [`schedule.capacity`](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/schedule-object) property.
+ Course sessions have an `Attendance` object for each session of the course. The number of sessions for a class is defined in Schedule and Sessions' [`schedule.capacity`](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/schedule-object) property.


## Use cases

Common business usages for this API include:

* Set the attendance for a given booked session to reflect how many attendees checked in.
* Query the attendance for a given participant in a course booking.
* Query attendance for a particular booking's sessions over time to see if a particular session has frequent no-shows. You can compare the number of attendees to the number of participants that signed up for that booking's sessions. 

## Terminology

For a comprehensive glossary of Wix Bookings terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/terminology).


## Before you begin

Validation capabilities are limited. Make sure your code validates that: 
+ There is no mismatch between `numberOfAttendees` and `attendanceStatus` to make sure, for example, that `attendanceStatus` is not `NOT_ATTENDED` while `numberOfAttendees` is `5`. 
+ The attendance's `numberOfAttendees` and the booking's `numberOfParticipants` correspond. For example, the number of attendees usually should not exceed the booking's intended number of participants (unless perhaps you allow walk-ins that did not sign up in advance).