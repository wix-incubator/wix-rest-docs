# Wix Bookings Terminology

[Wix Bookings](https://support.wix.com/en/article/about-wix-bookings) allows a business owner to set up a system to accept and manage bookings for services.

This article lists and defines the various terms and concepts used in Wix Bookings and its APIs. 


## Terminology

| Term | Definition |
|---------------|-------------------------|
| Appointment schedules | |
| [Appointment](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#appointments) | A specific time slot that a customer can book in a calendar. For example, your hair salon may be open for business from 9:00 AM to 7:00 PM and a customer can book a session at any available time during the day. | 
| Availability | Free time on a schedule that customers can book. |
| Booking | Information about the service that the customer has booked. A booking can be thought of as an order placed by a customer for a service. Includes details about the time, location, participants, and price. |
| Booking Status | Information about the status of the booking. Possible statuses are: xxx, xxx, xxx (all links) |
| [Calendar](https://support.wix.com/en/article/wix-bookings-about-the-wix-booking-calendar) | General overview about the availability and bookings of the business, including its services and resources. Manage your appointments, classes and courses on the calendar.| 
| CANCELED status | A status indicating that the booking has been canceled by the site owner or the customer. Cancel bookings using the `Cancel Booking` endpoint. |
| Catalog | A list of all the different services a business provides. | 
| Choices | | 
| Class schedule | | 
| [Class](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#classes) | A single session or a set of sessions that are offered on specific days and at specific times. Classes can be scheduled on different days, at different times, with different resources, such as staff members. Customers can sign up for single sessions or a class's recurring sessions. For example, a language school offers a beginner's Spanish class every Monday at 8:00 PM. Customers can join the session they want and don't have to commit to attending all sessions. | 
| CONFIRMED status | The site owner has confirmed the booking and it appears in the business calendar. You can confirm your bookings in one of the following ways: 
- Automatically. Bookings are automatically confirmed when the service is configured to do so and the order is approved during the checkout process. An automatic confirmation includes checking availability. 
- Manually. You can manually confirm a booking using Confirm Or Decline Booking(). slot's or schedule's availability. |
| Course schedules | |
| [Course](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#courses) | A multi-session course, or a workshop that starts and ends on a particular day. Customers sign up for the entire course and not one session. A limited number of sessions for the same service that starts and ends on a particular day. Customers sign up for the entire course and not one session. For example, a 12-session introductory course to Pilates, starting on February 1st and ending on March 17th. | 
| CREATED status | A status indicating that the potential booking has been created, but won’t yet appear in the calendar until verified. You can create bookings with the `Create Booking` endpoint. | 
| DECLINED status | A status indicating that the booking has been declined by the site owner. You can decline your bookings in one of the following ways: 
+ Manually. You can manually decline a booking with Decline Booking(). 
+ Automatically.Bookings are automatically declined when an eCommerce order has been declined or a double booking happened for free bookings. |
| Deposit | Amount the customer must pay immediately when checking out the booking. |
| Double booked | A double booking can happen in case of 2 or more simultaneous eCommerce checkout processes or if the site owner manually accepts bookings that exceed the service's capacity limit. When a double booking happens for paying customers, the doubleBooked boolean is set to true for the second booking and the owner is notified. They must then manually resolve the situation. When a double booking happens for free services, the second booking's status is set to DECLINED while the first booking is retained. | 
| Extended bookings | | 
| External calendar | | 
| Integration | | 
| Locked Sessions | Sessions that customers cannot book due to business reasons, such as the session being full and having a waitlist, or because an administrator wants to manually screen each customer before adding a customer to a session. | 
| Member | Someone who is a registered member in the Wix site and has a login. | 
| Merchant | The business that offers services that the public (customers) can book. The merchant's business is on a Wix site. |
| Options | | 
| PENDING status | A status indicating that the booking is waiting to be confirmed or declined. Bookings in PENDING status are displayed in the business calendar. Bookings are automatically set as PENDING when an eCommerce order related to the booking has been created. | 
| Policy | Terms the business wants to enforce when customers try to book a service. For example, how far in advance customers may book a service or until what point before the start of a session customers can cancel. |
| Pricing Provider | A 3rd-party app that implements custom logic for determining the price of a booking. | 
| Resource | A business asset, like a staff member, room, or equipment that's needed to provide a service. Resources can be “booked” or linked to a booking. | 
| Schedule | A collection of all sessions that belong to the same class, course, appointment, or resource. Schedules also comprise available slots that can still be booked. A schedule also contains information needed to calculate availability. 
| Service | Business offering, in the form of an appointment, class, or course. For example, a fitness studio may offer a 1-hour yoga class, a 45 minute HIIT training session, and a 30 minute 1-on-1 personal training. Services can be session-based or availability-based: 
- Session-based service: Generally a group session that has a set day and time, and takes place regardless of the number of participants that sign up (e.g., a yoga class that takes place every Tuesday at 16:00 or a class that has 8 sessions that take place on Wednesdays at 19:00). 
- Availability-based service: Generally a 1-on-1 or group session that is available for booking, but will only take place if a participant books it (e.g., a barber that is available for appointments Monday through Friday, from 08:00 to 17:00). |
| Session | An occupied or reserved period of time for an appointment, class, or course, or a period of availability for a resource. You can also think of a session as a time-specific instance of a service. Sessions are the building blocks of appointments, classes, and courses. Each of these types of services comprise sessions. The collection of related sessions for a service represent the service's schedule.| 
| Slot | An available period of time in a schedule that can be booked by a customer. While this includes existing sessions that are available for booking, it can also represent a period of time that can be booked based on the availability of a resource, such as a barber with appointments of 30 minutes each that are open for booking every weekday between 8:00 - 17:00. These slots are calculated according to the constraints of the schedule. | 
| SPI | | 
| Variant | Unique variation of the service. Each service variant may have a different price. | 
| Varied pricing | | 
| Visitor | Anyone who isn't registered as a member or hasn't logged in to the Wix site. If a visitor creates a booking they're added as a contact. | 
| WAITING_LIST status | An indication that the booking is on a waiting list. | 
| Waitlist | | 
| Membership plans with [Wix Pricing Plans](https://support.wix.com/en/article/wix-bookings-about-wix-bookings#selling-membership-plans-and-packages) | A pre-paid bundle of services or a membership that provides access to certain services. | 
| Wix site owner or site collaborator | The person managing the merchant's Wix site (which has Wix Bookings installed). |