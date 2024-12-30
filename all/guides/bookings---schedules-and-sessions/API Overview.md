SortOrder: 0

# About the Schedules and Sessions API

<blockquote class='warning'>

__Deprecation Notice:__

**Schedules and Sessions** has been replaced with
[Calendar V3](https://dev.wix.com/docs/rest/business-management/calendar/introduction)
and will be removed on June 30, 2025.

</blockquote>

Create, modify and delete bookable schedules and sessions.

> **Note**:  
Read schedule and session data using the [Calendar API](https://dev.wix.com/api/rest/wix-bookings/calendar).

## Terminology

* **Session**: An *occupied* period of time on a schedule (e.g., if a “Vinyasa Yoga” service is offered every Monday between 6-7pm, the class on Monday June 7, 2020 from 6-7pm is one session on a schedule with a recurring session every Monday).

* **Slot**: An *available* period of time in a schedule that can be booked by a customer. While this includes existing sessions that are available for booking, it can also represent a period of time that can be booked based on the availability of a resource (e.g., a barber with appointments of 30 minutes each that are open for booking every weekday between 8:00 - 17:00). These slots are calculated by the constraints of the schedule - they are not *occupied* sessions until they are booked.

* **Schedule**: A collection of sessions related to a specific entity (session, resource, etc.), with relevant metadata. The schedule entity represents all available information about when its owner can be booked for a service (both *occupied* and *available*).

> **Important**:  
The owner of the schedule can be a resource (e.g., a staff member or room) or a collection of sessions (e.g., a course with multiple sessions) - or you can create your own schedule owner ID for any entity of your choosing.

## Schedule Tags
Every schedule can be tagged for easy reference and filtering. The Wix Bookings UI uses the following tags:
* INDIVIDUAL - for appointments (slots)
* GROUP - for classes (sessions)
* COURSE - for courses (schedules)

When creating schedules via API, adding the relevant tag is recommended so that Wix Bookings will display the related service correctly in the UI.

## Use Cases

### Create a Recurring Event on Fridays at 10am beginning May 15th, 2020

Call [Create Schedule](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/create-schedule). Parameters to include:  
1. scheduleOwnerId (writable)  
2. intervals.interval.daysOfWeek = FRI  
3. intervals.interval.hourOfDay = 10 (for AM. 22 for PM)  
4. intervals.interval.minuteOfHour = 0  
5. intervals.start = 2020-05-15T21:00:00Z [(Google Protobuf Timestamp format)](https://developers.google.com/protocol-buffers/docs/reference/csharp/class/google/protobuf/well-known-types/timestamp)  
6. title = e.g., Reminder   

### Set up a Fitness Instructor's Work Schedule, Including Group Classes and Availability for 1-on-1 Appointments
The fitness instructor will exist as a resource in the system, with their own personal schedule. They will also be linked to both the group class's schedule, and the schedule detailing their availaibility for 1-on-1 appointments. 

1. Call [Create Resource](https://dev.wix.com/api/rest/wix-bookings/resources/create-resource) to add the instructor to the system and create their personal schedule.   
Parameters to include:  
   a. tags = StaffMember  
   b. schedules.schedule.intervals.interval.intervalType = AVAILABILITY  
   c. schedule.intervals.interval.daysOfWeek = MON  
   d. schedule.intervals.interval.hourOfDay = 9  
   e. schedule.intervals.interval.minuteOfHour = 0  
   f. schedule.intervals.interval.duration = 570  
2. Collect the returned resource ID and schedule ID. 
Note: the resource's schedule owner ID will equal the resource ID)  
3. Call [Create Schedule](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/create-schedule) to set up the instructor's group class (on Mondays from 5:30-6:30pm).  
Parameters to include:  
   a. scheduleOwnerId = service ID  
   b. schedule.intervals.affectedSchedules.scheduleId = instructor's schedule ID  
   c. schedule.intervals.affectedSchedules.transparency = BUSY  
   d. schedule.intervals.interval.daysOfWeek = MON  
   e. schedule.intervals.interval.hourOfDay = 17  
   f. schedule.intervals.interval.minuteOfHour = 30  
   g. schedule.intervals.interval.duration= 60  
4. Collect the returned schedule ID.  
5. Call [Create Schedule](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/create-schedule) again to set the logic for the instructor's availability for 1-on-1 appointments of 60 minutes. Parameters to include:  
   a. scheduleOwnerId (service ID - e.g., "1-on-1 training")  
   b. schedule.availability.linkedSchedules.transparency = BUSY  
   c. schedule.availability.linkedSchedules.scheduleId = (instructor's schedule ID)   
   d. schedule.availability.start = e.g.,2020-05-15T21:00:00Z [(Google Protobuf Timestamp format)](https://developers.google.com/protocol-buffers/docs/reference/csharp/class/google/protobuf/well-known-types/timestamp)  
   e. schedule.availability.constraints.slotDuration = 60  
