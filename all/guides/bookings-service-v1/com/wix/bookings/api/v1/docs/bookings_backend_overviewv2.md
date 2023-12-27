SortOrder: 0
# Wix Bookings Overview (v2)

Wix Bookings is a scheduling platform to manage your bookings, appointments, and calendar.

The Bookings APIs provide functionality to

- Offer Services: Let clients book 1-on-1 appointments, intro calls, group sessions, classes, workshops, and more.
- Manage All Calendars: Add custom working hours, sync staff Google calendars, include your own booking policy and manage all of your schedules.
- Offer Memberships and Packages: Boost client loyalty with free trials, membership plans, punch cards and coupons.
- Manage Clients: View member profiles, bookings history, payment status, notes and, more.
- Send SMS and Email notifications: Notify clients of successful bookings, wait list spots, and remind clients about upcoming sessions and expiring plans to reduce no-shows.


The Bookings API consists of the following primary objects:
  + Bookings
  + Resources
  + Services
  + Schedules
  + Sessions
  + Slots

  The following diagram shows the relationships between these objects.

  ![image](https://s3.amazonaws.com/wixplorer-readme-images/bookings-service-v1%2Fbookings-erd.png) 
  ## Services
  A [service](https://dev.wix.com/api/rest/wix-bookings/services/introduction) is an offering that a business provides to its customers. A service has a schedule which defines the service's availability for booking, the service's locations, and price.

  ## Resources
  A [resource](https://dev.wix.com/api/rest/wix-bookings/resources/introduction) is an entity that is used to provide a service. Typically, resources are staff who provide the service, but a resource can also be a classroom, or a piece of equipment. Resources have a schedule which defines when they are available to be booked. 

  ## Schedules
  A [schedule](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction) is a collection of sessions with associated metadata and related to a single service or resource. The schedule entity represents all information about when its owner can be booked. This includes both booked sessions and available slots. The schedule is used to calculate the availability of the schedule owner, that is the availability for booking a service or resource.
  
  Each site has a business schedule which defines its default operating hours. Link to this schedule when creating new staff members to set staff availability to the default business hours.  

  The schedule is used for booking and availability for courses.

  ## Sessions
  A [session](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction) is an occupied period of time on a schedule. For example, if a fitness class service is offered every Monday from 6 to 7 PM, the class on Monday, June 7, from 6 to 7 PM is 1 session on the service's schedule. Booked sessions have a `type` of "`EVENT"`". An `"EVENT"` session can also be be tagged 
  
  A session can be a available period of time for a resource. These sessions have a `type` of `"WORKING_HOURS"`. 
    
  A session is related to a single schedule.

  A session is used for booking and availability for appointments and individual classes. 

  ## Slots
  A slot is an available period of time on a schedule that has not been booked yet. Slots are calculated from the schedule's metadata each time they are required. Slots are not stored in a data collection. When a booking is made, the slot that has been booked becomes a session.


  ## Bookings
  A [booking](https://dev.wix.com/api/rest/wix-bookings/bookings/introduction) is a service's session that was ordered for a specific time and payment rate, for a customer. A booking can be for a single session, for example a one-time appointment, or multiple sessions, for example a series of classes. A booking is made on a schedule. Schedules contain sessions and available slots for services. A booking is made for a specific service, resource, time, and, location.
  Where a session already exists, - such as a class the booking will be added to that session. IF the booing is the first for the class, or it is for a n appointment, a session will be created by the booking.

## Key Concepts

  ### Availability  
  Availability is the existence of slots for a given service or resource. To determine availability for a given service or resource, the slots are calculated based on the schedule's `availability` metadata. This metadata includes the start and end time of the slot, constraints such as duration and the amount of time required between slots, and any other linked schedules who's metadata affects the given schedule.

  When checking availability for a single class or an appointment, check the availability of the session. When checking the availability of a course, check the availability of the   . 


  ### Linked Schedules
  The [schedule](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/schedule-object)'s `availability` object contains an array of `linkedSchedules`. This array contains a list of other schedules that impact the schedule’s availability. 
  Linked schedules include a `transparency` property defines how the schedules’ availability is affected:
   - When `transparency` is set to `”FREE"`:
     - Availability is calculated for the schedule based on the linked schedule.
     - Bookings made on the linked schedules do not affect the schedule. 
   - When `transparency` is set to `”BUSY”`:
     - Availability is calculated for the schedule based on the linked schedule.
     - Bookings made on the linked schedules make the schedule unavailable
       
  For example, the instructor for a class is a resource with a schedule. The class is a service with a schedule. The instructor's schedule is listed in the class's schedule as a linked schedule. If the instructor is not available and the transparency is set to `"BUSY"`, then the service is also not available.

  ### Affected Schedules
  Is an object on a session specifying a list of schedules and the way each schedule’s availability is affected by the session. For example, the schedule of an instructor is affected by sessions of the class that they instruct. The array is inherited from the schedule and can be overridden even if the session is a recurring session.  
  
  ### Courses, Classes and Appointments
  An appointment and a single class are stored as [sessions](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction), and are booked from available slots.
  A Course is a series of classes and is stored as, and booked form a [schedule](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction).
  System assigned tags for sessions and schedules are are as follows:
   + "INDIVIDUAL" Appointments, including appointments with more than 1 participant.
   + "GROUP" Individual classes.
   + "COURSE" Courses.