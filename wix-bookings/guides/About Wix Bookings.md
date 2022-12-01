# About Wix Bookings

[Wix Bookings](https://support.wix.com/en/article/about-wix-bookings) allows a business owner to set up a system to accept and manage bookings for services.

Some examples of Wix Bookings use cases are:

- **Beauty & wellness services:** e.g., book a haircut or a massage
- **Fitness services:** e.g., book a yoga class or a private training session
- **Education services:** e.g., book a programming course or a personal math tutor

Learn more how site collaborators can [create and manage their bookings](https://support.wix.com/en/article/wix-bookings-about-wix-bookings). 

Wix Bookings APIs include:

- **Services**: Manage the specific offerings this business provides
- **Catalog**: View a list of all the different services this business provides
- **Resources**: Manage each of the business staff members, locations/rooms, and equipment that can be “booked” or linked to a booking
- **Bookings**: Manage bookings to individual services - create, update and cancel bookings for services
- **Calendar**: A broad view of the business calendar, where you can easily view sessions available for booking, sessions taught per staff member, etc.
- **Schedules and Sessions**: Manage the individual schedules of each staff member, location, etc. (i.e., resource) and session 

## Before you begin

It's important to note the following points before starting to code:
- A session is a time-specific instance of a service. 
- A business that provides multi-session services (e.g., a 4-meeting class, a weekly event) will manage these as schedules. See [Schedules and Sessions API Terminology](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction) for more details.


Wix Bookings supports 2 different types of services:
- Session-based service: Generally a group session that has a set day and time, and takes place regardless of the number of participants that sign up (e.g., a yoga class that takes place every Tuesday at 16:00 or a class that has 8 sessions that take place on Wednesdays at 19:00).
- Availability-based service: Generally a 1-on-1 or group session that is available for booking, but will only take place if a participant books it (e.g., a barber that is available for appointments Monday through Friday, from 08:00 to 17:00).
- Both of these types of services can exist within one business - see [Schedules and Sessions Use Cases](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction).

</blockquote>

![AboutBookingsImage](../../media/BookingsSchedules.png)

## Terminology

- **Site owner:** The Wix site owner (who has Wix Bookings installed).

- **Resource:** A business asset like a staff member, a room, or equipment needed to provide a service.

- **Service:** A business offering that you can book. For example, a fitness studio may offer a 1-hour yoga class, a 45 minute HIIT training session, and a 30 minute 1-on-1 personal training. Wix Bookings offers 3 types of services:

  + [**Appointment**](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#appointments): A specific time slot that a customer can book in a calendar.

  + [**Class**](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#classes): A single session or a set of sessions that are offered on specific days and at specific times.
  + [**Course**](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#courses): A multi-session course, or a workshop that starts and ends on a particular day. Customers sign up for the entire course and not one session.

- **Sessions:** A reserved period of time for an appointment, class, or course, or a period of availability for a resource.

- **Schedule:** A collection of sessions and the information needed to calculate availability.

- **Booking:** Information about an order placed by a customer for a service or series of services. Includes details about the time, location, participants, and price.

- **Slot:** An available period of time in a schedule that can be booked by a customer. While this includes existing sessions that are available for booking, it can also represent a period of time that can be booked based on the availability of a resource (e.g., a barber with appointments of 30 minutes each that are open for booking every weekday between 8:00 - 17:00). These slots are calculated by the constraints of the schedule.

- [**Calendar**:](https://support.wix.com/en/article/wix-bookings-about-the-wix-booking-calendar) A collection of all schedules, appointments, classes, and courses.

- [**Membership plans with Wix Pricing Plans**:](https://support.wix.com/en/article/wix-bookings-about-wix-bookings#selling-membership-plans-and-packages) A pre-paid bundle of services, or a membership including access to certain services.