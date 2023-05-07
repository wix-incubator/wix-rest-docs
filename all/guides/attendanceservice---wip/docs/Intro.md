SortOrder: 0
# About the Wix Bookings Attendance V2 API


With the Wix Bookings Attendance V2 API you can manage the bookings attendances by
* setting an attendance for a given booking.
* getting an attendance by id.
* querying for attendances by given filters, sorting and paging.

The [attendance object](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/attendance/attendance-object) holds information about the attendance of a booking's booked contact to a booked session.

Common business usages for this API:
* Set an attendance for a given booking.
* Query all attended bookings of a given session.
* Query all attended sessions for a given course booking.

For more information about the terminology, use cases and related APIs read
[introduction to the Wix Bookings V2 API](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/introduction).

You can then use the
[Wix Bookings V2 APIs](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/introduction)
to manage the booking life cycle and the
Ecommerce APIs (coming soon)
to handle the checkout and payment flow.


>## Before you begin

> + `fields` and `fieldsets` aren't supported in the `query` object.
> + There is no validation on the number of attendees or on the relationship between `numberOfAttendees` and `attendanceStatus`.
> + There is no validation on the number of attendees or on the relationship between `numberOfAttendees` and the booking's `numberOfParticipants`.
