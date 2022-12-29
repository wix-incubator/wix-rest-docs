SortOrder: 3
# Wix Bookings V2 Errors


This articles outlines error messages that might be issued when calling 
endpoints of the Wix Bookings V2 API.


## Create Booking Errors


The [Create Booking](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/create-booking) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div>                                 | <div style="width:280px">Error message </div>                                                                                                                   | <div style="width:300px">Troubleshooting </div>                                                                                                                                                                                                                         |
|--------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FAILED_PRECONDITION (428)` | `SESSION_CAPACITY_EXCEEDED` | Not enough available spots for session `<sessionId>`. | Make sure that the booking doesn't exceed the [session's](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/session/get-session) `capacity` and `remainingCapacity`. |
| `FAILED_PRECONDITION (428)` | `SCHEDULE_CAPACITY_EXCEEDED` | Not enough available spots for schedule `<scheduleId>`. | Make sure that the booking doesn't exceed the [schedule's](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/schedule-object) `capacity`. |
| `FAILED_PRECONDITION (428)` | `SLOT_NOT_AVAILABLE` | The specified slot isn't available. | Make sure to [check](https://bo.wix.com/wix-docs/rest/bookings/availabilitycalendar---wip/get-slot-availability) that the requested slot is still available. |
| `NOT_FOUND (404)` | `BOOKING_NOT_FOUND` | Booking `<bookingId>` doesn't exist. | Make sure that the booking exists. |
| `FAILED_PRECONDITION (428)` | `CANCELATION_NOT_SUPPORTED` | You can't cancel a booking with status `<status>`. | You can only cancel bookings with a status of `CONFIRMED` or `WAITING_LIST`. |
| `PERMISSION_DENIED (403)` | `NOT_AUTHORIZED_TO_ALTER_FLOW` | The requested action alters the standard Wix Bookings flow. You don't have sufficient permissions to do so. | You must have the `MANAGE BOOKINGS` permission scope to alter the standard Wix Bookings flow. |
| `PERMISSION_DENIED (403)` | `NOT_AUTHORIZED_TO_UPDATE_INTERNAL_BUSINESS_NOTE` | The requested action updates `internalBusinessNote`. You don't have sufficient permissions to do so. | You must have the `MANAGE BOOKINGS` permission scope to update `internalBusinessNote`. |
| `PERMISSION_DENIED (403)` | `NOT_AUTHORIZED_TO_UPDATE_PARTICIPANTS_INFO` | The requested action updates `participantsInfo`. You don't have sufficient permissions to do so. | You must have the `MANAGE BOOKINGS` permission scope to update `participantsInfo`. |
| `PERMISSION_DENIED (403)` | `SERVICE_POLICY_VIOLATION` | The requested action violates the service's `<serviceId>` policy. | Make sure that your update complies with the [service's](https://dev.wix.com/api/rest/wix-bookings/services/service/service-object) policies. |
| `INVALID_ARGUMENT (400)`  | `MISSING_SLOT_DETAILS` | The provided `slot` is missing required fields. | When creating or rescheduling a booking for a class or an appointment, you can pass a session ID. Then, the slot's details are automatically calculated. If you omit the session ID, you must pass all of these fields: `startDate`, `endDate`, `location.locationType`, `resource.id`, and `scheduleId`. |
| `RESOURCE_EXHAUSTED (429)` | `FEATURE_LIMIT_EXCEEDED` | The requested action exceeds the limit for calling `<feature>`. | Make sure that you don't call any Wix Bookings endpoint more than its allowed limit. |
| `FAILED_PRECONDITION (428)` | `DECLINE_NOT_SUPPORTED` | It isn't supported to decline a booking with status `<status>`.  | You can only decline bookings with a status of `CREATED` or `PENDING`.  |
| `FAILED_PRECONDITION (428)` | `CONFIRMATION_NOT_SUPPORTED` | It isn't supported to confirm a booking with status `<status>`.  | You can only confirm bookings with a status of `CREATED` or `PENDING`.  |
| `INVALID_ARGUMENT (400)` | `INVALID_PARTICIPANT_INFO` | The requested action is missing or includes conflicting information about the participants. | Make sure that you pass exactly 1 of these fields: `participantsChoices`, `totalParticipants`, or `numberOfParticipants`. |