SortOrder: 0
# About the Calendar API

The calendar service includes read-only endpoints that allow the retrieval of business-related events, in integration with Wix Bookings.

## Terminology

*   **Session**: An *occupied* period of time on a schedule (e.g., if a “Vinyasa Yoga” service is offered every Monday betwen 6-7pm, the class on Monday June 7, 2020 from 6-7pm is one session on a schedule with a recurring session every Monday).

*   **Slot**: An *available* period of time in a schedule that can be booked by a customer. While this includes existing sessions that are available for booking, it can also represent a period of time that can be booked based on the availability of a resource (e.g., a barber with appointments of 30 minutes each that are open for booking every weekday between 8:00 - 17:00). These slots are calculated by the constraints of the schedule - they are not *occupied* sessions until they are booked.

*   **Schedule**: A collection of sessions related to a specific entity (session, resource, etc.), with relevant metadata. The schedule entity represents information about when its owner can be booked for a service.

>**Important**:  
The owner of the schedule can be a resource (e.g., a staff member or room) or a collection of sessions (e.g., a course with multiple sessions).
