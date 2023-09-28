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
- **Calendar**: A broad view of the business calendar, where you can easily view sessions available for booking, sessions taught per staff member, and so on
- **Schedules and Sessions**: Manage the individual schedules of each resource (staff member, location, and so on) and sessions

## Before you begin

It's important to note the following points before starting to code:
- A session is a time-specific instance of a service. 
- A business that provides multi-session services (e.g., a 4-meeting class, a weekly event) will manage these as schedules. See [Schedules and Sessions API Terminology](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction) for more details.


Wix Bookings supports 2 different types of services:
- Session-based service: Generally a group session that has a set day and time, and takes place regardless of the number of participants that sign up (e.g., a yoga class that takes place every Tuesday at 16:00 or a class that has 8 sessions that take place on Wednesdays at 19:00).
- Availability-based service: Generally a 1-on-1 or group session that is available for booking, but will only take place if a participant books it (e.g., a barber that is available for appointments Monday through Friday, from 08:00 to 17:00).
- Both of these types of services can exist within one business - see [Schedules and Sessions Use Cases](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction).


![AboutBookingsImage](../../media/BookingsSchedules.png)
