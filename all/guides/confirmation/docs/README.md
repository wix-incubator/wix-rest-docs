SortOrder: 0
# Introduction
With Bookings Confirmation service, you can ensure that checkout completion is handled in a way that prevents double bookings.    
Once the checkout is complete, call the `confirmOrDeclineBooking` function to apply it to the booking.     
Typically, the booking status will be updated to `CONFIRMED`, and you'll see it on the calendar.    
However, in some cases, such as when over-booking could occur, the booking may be declined.    
For more information about the `ConfirmOrDeclineBooking` endpoint, please refer to its [documentation](/docs/link).

## Terminology

+ __Booking__: Information about the service that the customer has booked. 
  Includes details about the time, location, participants, and price.
  + __Service__: Online or in-person business offerings, such as courses and private sessions. For
  example, a fitness studio may offer a 
  1-hour yoga class, a 45 minute HIIT training session, and a 30 minute 1-on-1 
  personal training. Bookings offers 3 types of services: 
    + __Appointments__: Appointments take place whenever a customer books a specific 
      time slot. For example, your hair salon may be open for business from 9:00 AM 
      to 7:00 PM and a customer can book a session at any available time during the day.
    + __Classes__: Classes can be scheduled on different days, at different times, 
      with different resources, such as staff members. Customers can sign up for single sessions
      or a class's recurring sessions. For example, a language school offers a beginner's Spanish 
      class every Monday at 8:00 PM. Clients can join the session they want and don't have to commit
      to attending all sessions.
    + __Courses__: A limited number of sessions for the same service that starts and ends 
      on a particular day. Customers sign up for the entire course and not one session. For example, 
      a 12-session introductory course to Pilates, starting on February 1st and
      ending on March 17th.
+ __Schedule__: A collection of all sessions that belong to the same class, course, appointment, or resource. Schedules also comprise available slots that can still be booked.
    + __Session__: An _occupied_ period of time in a schedule. Sessions are the 
      building blocks of appointments, classes, and courses. Each of these types of 
      services comprise sessions. The collection of related sessions for a service represent the 
      service's schedule. 
    + __Slot__: An _available_ period of time in a schedule that can be booked by a 
      customer. While this includes existing sessions that are available for
      booking, it can also represent a period of time that can be booked based on
      the availability of a resource, such as a barber with appointments of 30 
      minutes each that are open for booking every weekday between 8:00 - 17:00.
      These slots are calculated according to the constraints of the schedule.
+ __Calendar__: General overview about the availability and bookings of the 
  business, including its services and resources. Manage your appointments, classes 
  and courses on the calendar.
+ __Resource__: Business asset like a staff member, room, or equipment that's 
  needed to provide a service.
+ __Availability__: Free time on a schedule that customers can book. 
  You can read more about 
  [Query Availability](https://bo.wix.com/wix-docs/rest/bookings/availabilitycalendar---wip/introduction).
  The [Create Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/create-booking) and
  [Reschedule Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/reschedule-booking) 
  endpoints check if a slot or schedule is available, unless you pass
  `skipAvailabilityValidation` in the body of the request.
  [Confirm Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/confirm-booking) 
  doesn't check availability. Instead, the availability is checked during the 
  ecom payment flow(coming soon).
+ __Double Bookings__: Double bookings occur if the total number of bookings for a period of time is greater than the number of spots or resources for the same period of time. Regarding sessions or a schedule, when it does not have enough capacity to accommodate the booking's participants, and for appointments bookings when the same staff member and service overlap.   