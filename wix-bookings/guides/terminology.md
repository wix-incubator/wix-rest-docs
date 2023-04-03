# Wix Bookings Terminology

[Wix Bookings](https://support.wix.com/en/article/about-wix-bookings) allows a business owner to set up a system to accept and manage bookings for services.

This article contains a comprehensive list of the various terms and concepts used in all of Wix Bookings and its APIs. 


| Term | Definition |
|---------------|-------------------------|
| [Appointment](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#appointments) | A specific time slot that a customer can book in a calendar. For example, your hair salon may be open for business from 9:00 AM to 7:00 PM and a customer can book a session at any available time during the day. | 
| Appointment schedule | The schedule determines when customers can book a session. Bookability is determined using the specified session's duration, the time between sessions, and the schedules of staff members who provide the service.<br />For example, given the following scheduling criteria for a business offering haircuts, the schedule allows customers to book sessions from 9:00 AM to 5:30 PM with the possibility of booking a maximum of 9 sessions per day:<br />+ The business offers a 30-minute haircut service.<br />+ The schedule allows customers to book 30-minute sessions with 30 minutes between each session.<br />+ The staff members are available from 9:00 AM to 6:00 PM. |
| Availability | Free time on a schedule that customers can book. |
| Booking | Information about the service that the customer has booked. A booking can be thought of as an order placed by a customer for a service. Includes details about the time, location, participants, and price. |
| Business owner | The owner of the business offering services that are managed on the Wix site. May or may not be the site owner. This person makes logical, business decisions regarding bookings, such as whether to decline a booking.
| [Calendar](https://support.wix.com/en/article/wix-bookings-about-the-wix-booking-calendar) | General overview about the availability and bookings of the business, including its services and resources. Manage your appointments, classes and courses on the calendar.| 
| `CANCELED` status (Booking) | A status indicating that the booking has been canceled by the site owner or the customer. Cancel bookings using the `Cancel Booking` endpoint. |
| Catalog | A list of all the different services a business provides. | 
| Category (Service)| The category to which the service belongs. |
| Choice (Pricing) | A specific value for a service option the customer can choose to book. For example, the service option `ageGroup` may have these choices: `child`, `student`, `adult`, and `senior`. Each choice may have a different price. | 
| [Class](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#classes) | A single session or a set of sessions that are offered on specific days and at specific times. Classes can be scheduled on different days, at different times, with different resources, such as staff members. Customers can sign up for single sessions or a class's recurring sessions. For example, a language school offers a beginner's Spanish class every Monday at 8:00 PM. Customers can join the session they want and don't have to commit to attending all sessions. | 
| Class schedule | For classes and courses, the business decides when to schedule a session. This is in contrast to appointments, where the customer decides when to book a session. For classes and courses, the schedule is used to manage the available sessions and holds some aggregated information, such as the start time and end time of a course. | 
| `CONFIRMED` status (Booking)  | A status indicating that the site owner has confirmed the booking and it appears in the business calendar. You can confirm your bookings in one of the following ways:<br />+ Automatically. Bookings are automatically confirmed when the service is configured to do so and the order is approved during the checkout process. An automatic confirmation includes checking availability.<br />+ Manually. You can manually confirm a booking using `Confirm Or Decline Booking`. |
| [Course](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#courses) | A multi-session course, or a workshop that starts and ends on a particular day. For example, an academic course or fitness boot camp. |
| Course schedule | For classes and courses, the business decides when to schedule a session. This is in contrast to appointments, where the customer decides when to book a session. For classes and courses, the schedule is used to manage the available sessions and holds some aggregated information, such as the start time and end time of a course. | 
| Deposit | Amount the customer must pay immediately when checking out the booking. |
| Double booking | A double booking is when a customer attempts to book an already-reserved service. This can occur, for example, when multiple customers try to check out at the same time or when the business owner manually confirms more bookings than the service's capacity allows. If trying to book at the same time as:<br />+ An existing paid booking: The new booking is declined.<br />+ An existing free booking: The new booking is accepted. | 
| Extended booking | In addition to basic booking information, an extended booking contains additional extended details, such as attendance, and whether the booking can be refunded or rescheduled. | 
| External calendar | A calender hosted by a  3rd-party calendar service. | 
| External calendar connection | A linkage established between a Wix site’s calendar and one or more external calendars, to enable importing and/or exporting calendar events. |
| External calendar event | A single session or recurring session instance that appears in a specific block of time in a calendar, such as an appointment or class. | 
| External calendar provider | The  3rd-party service providing an external calendar. For example: Google, Apple, or Microsoft. |
| External calendar resource | A resource not necessarily related to Wix Bookings resources that owns a scheduler in Wix Bookings and has a calendar external to Wix Bookings. For example, a staff member in a business registered with Wix Bookings that also has a Gmail account and a Google calendar. |
| Form | The booking form used to collect the customer's input while booking the service. | 
| Integration | Provision of extended functionality from a service provider to a Wix site. The extended functionality is implemented by the  3rd-party service provider using their API, and made available to the Wix site using Wix SPIs. For example, you, as a pricing provider, can offer custom varied pricing options to a Wix site using the [Wix Bookings Pricing Integration REST SPI](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi). | 
| Locked session | A session that customers cannot book due to business reasons, such as the session being full and having a waitlist, or because an administrator wants to manually screen each customer before adding a customer to a session. | 
| Member | Someone who is a registered member in the Wix site and has a login. | 
| Merchant | The business that offers services that the public (customers) can book. The merchant's business is on a Wix site. |
| Option (Pricing) | The pricing possibilities for the service. For example, a service may have different options based on which staff member provides the service, the age of the customer, the time of the appointment, or the type of equipment. Each option has a list of supported choices. Options may affect the service price. | 
| `PENDING` status (Booking) | A status indicating that the booking is waiting to be confirmed or declined. Bookings in `PENDING` status are displayed in the business calendar. Bookings are automatically set as `PENDING` when an eCommerce order related to the booking has been created. | 
| Policy (Bookings) | Terms the business wants to enforce when customers try to book a service. For example, how far in advance customers may book a service or until what point before the start of a session customers can cancel. |
| Pricing provider | A 3rd-party app that implements custom logic for determining the price of a booking. | 
| Resource | A business asset, like a staff member, room, or equipment that's needed to provide a service. Resources can be “booked” or linked to a booking. | 
| Schedule | A collection of all sessions that belong to the same class, course, appointment, or resource. Schedules also comprise available slots that can still be booked. A schedule also contains information needed to calculate availability. 
| Service | Business offering, in the form of an appointment, class, or course. For example, a fitness studio may offer a 1-hour yoga class, a 45 minute HIIT training session, and a 30 minute 1-on-1 personal training. Services can be session-based or availability-based: <br />+ Session-based service: Generally a group session that has a set day and time, and takes place regardless of the number of participants that sign up (for example, a yoga class that takes place every Tuesday at 4:00 PM or a class that has 8 sessions that take place on Wednesdays at 7:00 PM). <br />+ Availability-based service: Generally a 1-on-1 or group session that is available for booking, but will only take place if a participant books it (for example, a barber that is available for appointments Monday through Friday, from 08:00 AM to 5:00 PM). |
| Status (Booking) | Information about the status of the booking. Possible statuses include: `CREATED`, `PENDING`, `CONFIRMED`, `DECLINED`, `WAITING-LIST`, `UPDATED`, `CANCELED` |
| Status (Service) | Information about the status of a service. Statuses include: `ACTIVE`, `DELETED`.
| Session | An occupied or reserved period of time for an appointment, class, or course, or a period of availability for a resource. You can also think of a session as a time-specific instance of a service. Sessions are the building blocks of appointments, classes, and courses. Each of these types of services comprise sessions. The collection of related sessions for a service represent the service's schedule.| 
| Slot | An available period of time in a schedule that can be booked by a customer. While this includes existing sessions that are available for booking, it can also represent a period of time that can be booked based on the availability of a resource, such as a barber with appointments of 30 minutes each that are open for booking every weekday between 8:00 AM - 5:00 PM. These slots are calculated according to the constraints of the schedule. | 
| [Service Provider Interface (SPI)](https://dev.wix.com/api/rest/getting-started/service-provider-interface#getting-started_service-provider-interface_introduction) | An API specification that is implemented by service providers on their side to provide a specific service to a Wix, such as customized tax or shipping rates. For example, you, as a pricing provider, can offer custom varied pricing options to a Wix site using the [Wix Bookings Pricing Integration REST SPI](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi).  | 
| Site owner | The person managing the merchant's Wix site (which has Wix Bookings installed). This includes site contributors. |
| Suggested participant (Waitlist) | When a spot opens up in a session with a waitlist, the session is locked for bookings from any participant, other than the participant that is currently in queue in the waitlist - so that only the "suggested" participant is able to book the session. | 
| Variant (Pricing) | Unique variation of the service. Variants are defined by the combination of choices. For example: `{"time": "afternoon", "ageGroup": "adult", "equipment": "kettlebells"}`. Each variant may have a different price. | 
| [Varied pricing](https://support.wix.com/en/article/wix-bookings-understanding-price-options) | The ability to charge for services based on different factors, such as the staff member providing the service or the equipment needed.  | 
| Visitor | Anyone who isn't registered as a member or hasn't logged in to the Wix site. If a visitor creates a booking they're added as a contact. | 
| `WAITING_LIST` status (Booking) | An indication that the booking is on a waiting list. | 
| Waitlist | A list of participants that requested to be added to a session that is fully booked, if there should be a cancelation. | 
| Waitlist time window | How much time a customer has to book a place in the session, before it is offered to the next customer on the waitlist. | 
| Membership plans with [Wix Pricing Plans](https://support.wix.com/en/article/wix-bookings-about-wix-bookings#selling-membership-plans-and-packages) | A pre-paid bundle of services or a membership that provides access to certain services. | 