SortOrder: 0
# About the Calendar API

The calendar service includes read-only endpoints that allow the retrieval of business-related events, in integration with Wix Bookings.


<blockquote class='warning'>

__Deprecation Notice:__

The [List Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar/sessions/list-sessions) endpoint will be removed on June 30, 2023. Please use [Query Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar/sessions/query-sessions) instead.

</blockquote>

## Terminology

*   **Session**: An *occupied* period of time on a schedule (e.g., if a “Vinyasa Yoga” service is offered every Monday between 6-7pm, the class on Monday June 7, 2020 from 6-7pm is one session on a schedule with a recurring session every Monday). A session of type `EVENT` is a recurring or single session that appears in a specific block of time in a calendar, such as an appointment or a class.

*   **Slot**: An *available* period of time in a schedule that can be booked by a customer. While this includes existing sessions that are available for booking, it can also represent a period of time that can be booked based on the availability of a resource (e.g., a barber with appointments of 30 minutes each that are open for booking every weekday between 8:00 - 17:00). These slots are calculated by the constraints of the schedule - they are not *occupied* sessions until they are booked.

*   **Schedule**: A collection of sessions related to a specific entity (session, resource, etc.), with relevant metadata. The schedule entity represents information about when its owner can be booked for a service.

>**Important**: The owner of the schedule can be a resource (e.g., a staff member or room) or a collection of sessions (e.g., a course with multiple sessions).
