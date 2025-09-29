# Wix Bookings Terminology

[Wix Bookings](https://support.wix.com/en/article/about-wix-bookings) allows business owners to accept and manage bookings for their services.

This article lists the terms and concepts used in Wix Bookings and its APIs.

## Appointment

[Appointments](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#appointments) are on-demand bookings for available time slots.
For example, haircuts or consultations.
Customers choose their preferred time from available slots, with availability calculated based on business hours, session duration, staff working hours, and booking policies.

## Booking

Information about the service that the customer has booked.
You can think of a booking as an order placed by a customer for a service.
The booking includes details about the time, location, participants, and price.

## Booking fee

A fee for a specific booking that's calculated according to the associated booking [policy snapshot](#policy-snapshot).
Currently, only cancellation fees, including no-show fees, are supported.

## Business hours

The default operating hours when services are available for booking.
Business hours serve as the foundation for staff working hours and resource availability.
Use the [Calendar APIs](https://dev.wix.com/docs/rest/business-management/calendar/introduction) to configure business hours through schedule events.

## Business owner

The owner of the business that offers services to customers.
Can be a different person than the Wix user.
The business owner makes decisions such as confirming or declining a booking.

## Calendar

The [Wix Bookings Calendar](https://support.wix.com/en/article/wix-bookings-about-the-wix-booking-calendar) displays business availability, staff schedules, and confirmed bookings in a unified interface.
Wix Bookings automatically manages the underlying [schedules](#schedule) and [events](#event) with the [Calendar APIs](https://dev.wix.com/docs/rest/business-management/calendar/introduction) integration.
For technical details, see [How Wix Bookings Uses the Calendar APIs](https://dev.wix.com/docs/rest/business-solutions/bookings/calendar/how-wix-bookings-uses-the-calendar-apis).

## `CANCELED` (booking status)

Indicates that the booking has been canceled by the site owner or the customer.
Cancel bookings using [Cancel Booking](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings/bookings-writer-v2/cancel-booking).

## Capacity

The maximum number of participants that can book a service or session.
For classes and courses, capacity determines when sessions become fully booked and waitlists activate.
For appointments, capacity is typically 1 but can be higher for group sessions.
Capacity is defined in the service configuration and affects availability calculations.

## Category

A label used to group services, helping business owners, app developers, and customers filter and organize services efficiently.

## Checkout

Customers must complete a checkout when booking a service.
Wix Bookings integrates with the [Wix eCommerce platform](https://dev.wix.com/docs/rest/business-solutions/e-commerce/introduction) to handle payments and order management.
To customize the checkout, you can either use the Wix eCommerce [Checkout APIs](https://dev.wix.com/docs/rest/business-solutions/e-commerce/checkout/introduction) or build your own payment interface and process payments with external providers.

## Choice

A specific value for a service option that business owners define when setting up varied pricing.
For example, the service option `ageGroup` may have these choices: `child`, `student`, `adult`, and `senior`.
Each choice may have a different price, and customers select from these predefined choices when booking.

## Class

[Classes](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#classes) are scheduled sessions that customers can join individually.
For example, drop-in yoga classes or weekly cooking lessons.
You can schedule classes on various weekdays, at different times, and with different staff members.
Customers can sign up for 1 or multiple sessions, unlike courses where all sessions must be booked.
When a specific session is fully booked, customers can join a waitlist and are notified if a spot opens up.

## `CONFIRMED` (booking status)

Indicates that the business owner has confirmed the booking and it appears in
the business calendar. You can confirm your bookings in different ways:
- Automatically. Bookings are automatically confirmed when the service is set
  up for automatic confirmation and the order is approved during checkout,
  including an availability check.
- Manually. You can manually confirm a booking using [Confirm Or Decline
  Booking](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings-and-time-slots/bookings-v2/bookings-v2-and-confirmation/confirm-or-decline-booking).

## Course

[Courses](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#courses) are multi-session programs that customers must book in full.
For example, 8-week programming bootcamps or certification training programs.
Business owners set the complete session timeline before offering the course, with courses starting and ending on pre-defined dates.
Customers must book all course sessions, while they're free to book only a single or some sessions for classes.

## Deposit

Amount the customer must pay immediately when checking out the booking.

## Double booking

A double booking occurs when a customer attempts to book a service that's already reserved.
This can happen if multiple customers are checking out simultaneously or if the business owner manually confirms more bookings than the service's capacity allows.

## Event

Time-specific instances of services, such as an appointment or class session.
Wix Bookings automatically creates and manages events via the [Calendar APIs](https://dev.wix.com/docs/api-reference/business-management/calendar/introduction) when you create services, staff members, or bookings.

## Extended booking

A booking object with additional details beyond the basic booking information.
Extended bookings include attendance details, refund eligibility, reschedule permissions, and other management data.
Use the [Extended Bookings API](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings/bookings-reader-v2/introduction) to retrieve this enhanced booking information.

## External calendar integration

The synchronization between Wix Bookings and 3rd-party calendar services like [Google Calendar](https://developers.google.com/calendar/api/guides/overview), [Apple Calendar](https://developer.apple.com/documentation/foundation/calendar), or [Microsoft Outlook](https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0).
This integration allows bidirectional sync of booking events and availability, preventing double-bookings across platforms.
Use the [External Calendar API](https://dev.wix.com/docs/rest/business-solutions/bookings/calendar/external-calendar-v2/introduction) to set up and manage these connections.

## Form

The [booking form](https://support.wix.com/en/article/wix-bookings-creating-and-setting-up-your-booking-forms) collects customer information required to complete a booking.
Forms can include fields for contact details, special requests, service preferences, and custom questions.
Learn more about [how Bookings technically integrates with Wix Forms](https://dev.wix.com/docs/rest/business-solutions/bookings/wix-forms-integration).

## Integration

A custom implementation that extends Wix Bookings functionality through service plugins.
Developers can inject custom logic into the booking flow, such as dynamic pricing or availability rules.

## Member

Someone who is a registered [member](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/introduction) in the Wix site and has a login.

## Option

A pricing category that business owners define when setting up varied pricing for a service.
Options can vary based on factors such as staff member, customer age, appointment time, or equipment type.
Each option contains a list of predefined [choices](#choice) that customers can select from, and these choices may have different prices.

## Order

A record of a customer's purchase in the [Wix eCommerce system](https://dev.wix.com/docs/api-reference/business-solutions/e-commerce/introduction).
All bookings use [eCommerce orders](https://dev.wix.com/docs/rest/business-solutions/e-commerce/orders/introduction) to maintain proper records and functionality.
When you use an [eCommerce checkout](https://dev.wix.com/docs/rest/business-solutions/e-commerce/checkout/introduction), orders are automatically created and contain details about the booking, payment information, and customer data.
For custom checkouts, you must manually create an order in the Wix eCommerce platform and update the booking status to complete the booking flow.

## `PENDING` (booking status)

Indicates that the booking is waiting to be confirmed or declined. Bookings in
`PENDING` status are displayed in the business calendar. Bookings are
automatically set as `PENDING` when an
[eCommerce order](https://dev.wix.com/docs/rest/business-solutions/e-commerce/orders/introduction)
related to the booking has been created.

## Policy

Rules set by the business owner that govern how customers can book and cancel services.
Policies define booking windows, cancellation deadlines, participant limits, and other constraints.
When a booking is created, the current policy is saved as a policy snapshot to preserve the original terms.

## Pricing provider

A 3rd-party app that implements custom logic to determine the price of a booking
with the [Pricing Integration Service Plugin](https://dev.wix.com/docs/rest/business-solutions/bookings/pricing/pricing-integration-spi/introduction).
Services can have fixed pricing or varied pricing based on different factors like staff member, time of day, or customer type.

## Policy snapshot

A saved version of a service's booking policy captured when a booking is created.
Policy snapshots preserve the original terms, which is useful if policies change after a booking is made.
This protects both customers and businesses by maintaining the original agreement terms throughout the booking lifecycle.

## Resource

Physical assets like rooms, equipment, or facilities needed for services.
Resources only have event schedules showing when they're booked, with
availability based on business hours. Each resource has a schedule that
defines its availability.

## Schedule

Organizes events and defines when services are available or when resources are booked.
Wix Bookings automatically creates and manages schedules via the [Calendar APIs](https://dev.wix.com/docs/api-reference/business-management/calendar/introduction) when you create services, staff members, or bookings.
For more details, see appointment schedule, class schedule, and course schedule.

## Service

A business offering, which can be a class, course, or appointment-based.
For example, a fitness studio may offer 30-minute 1-on-1 personal training sessions by appointment, 1-hour yoga classes every Monday at 7:00 PM, and introductory HIIT courses consisting of 3 training sessions on specific dates. For more information, see [appointment](#appointment), [class](#class), and [course](#course).

## Service plugin

[Service plugins](https://dev.wix.com/docs/build-apps/develop-your-app/extensions/backend-extensions/service-plugins/about-service-plugin-extensions)
(formerly SPIs) are APIs that are defined by Wix, which you can choose to implement.
By doing so, you become a service provider.
Then, Wix calls your service during a certain flow, waits for your response, and continues the flow with it.
For example, as a pricing provider you can offer custom pricing options for a business using the [Wix Bookings Pricing Integration REST Service Plugin](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi).

## Session

A specific instance of a service occurring at a particular time, such as an appointment, class session, or course session.
Sessions are represented as events in the [Calendar APIs](https://dev.wix.com/docs/rest/business-management/calendar), which Wix Bookings automatically creates and manages when bookings are made.
For classes and courses, the aggregation of all sessions constitutes the service's schedule.
For appointments, sessions are created dynamically when customers book available time slots.

## Site owner

The owner of the Wix site that has Wix Bookings installed and all
[site contributors](https://support.wix.com/en/article/inviting-people-to-contribute-to-your-site).

## Staff member

People who provide services and have complex scheduling needs.
Staff members have both working hours (when they're available to work) and event schedules (when they're actually booked).
Staff members are eligible to receive tips.
Not all staff members are [site collaborators](https://support.wix.com/en/article/inviting-people-to-contribute-to-your-site) and not all site contributors are staff members.

## Status (booking)

Information about the life cycle status of the booking. Booking statuses
include: `CREATED`, `PENDING`, `CONFIRMED`, `DECLINED`, `WAITING_LIST`,
`UPDATED`, `CANCELED`.
Learn more about [booking lifecycle and status transitions](https://dev.wix.com/docs/api-reference/business-solutions/bookings/bookings/bookings-writer-v2/introduction#booking-lifecycle).

## Time slot

Specific periods when services can be booked.
The [Time Slots API](https://dev.wix.com/docs/api-reference/business-solutions/bookings/pricing/introduction) helps find available time slots for appointments and classes.
The availability calculation considers multiple factors: service schedules, staff working hours, resource availability, booking policies, and existing reservations.

## Variant

The combination of all customer [choices](#choice) for a service's pricing options.
Business owners must define all possible variants and their prices when setting up varied pricing for a service.
Each variant represents a different combination of the available choices and has its own price.

## Varied pricing

[Varied pricing](https://support.wix.com/en/article/wix-bookings-understanding-price-options) allows businesses to charge for services based on different factors, such as the staff member who provides the service or the equipment needed.
Wix Bookings supports custom pricing integrations through the [Pricing Integration service plugin](https://dev.wix.com/docs/rest/business-solutions/bookings/pricing/pricing-integration-spi/introduction), allowing you to implement dynamic pricing logic.

## Visitor

Anyone who isn't registered as a member or hasn't logged in to the Wix site.
If a visitor creates a booking they're added as a [contact](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/introduction).

## `WAITING_LIST` (booking status)

Indicates that the booking is on a waitlist for a fully booked class session.

## Waitlist

A feature for class services that allows customers to join a queue when sessions are fully booked.
When a spot opens due to cancellation, the first person on the waitlist (called the suggested participant) is notified and given a specified time window to book the session.
If they don't book within the time window, the opportunity passes to the next person on the waitlist.
Not available for courses or appointment services.

## Working hours

The specific times when staff members are available to provide services.
Working hours are different from business hours and event schedules, they define when staff can work, not when they're actually booked.
Staff members can have custom working hours that override the default business hours, enabling flexible scheduling for different team members.

## Wix Pricing Plans

[Wix Pricing Plans](https://support.wix.com/en/article/wix-bookings-about-wix-bookings#selling-membership-plans-and-packages)
are prepaid bundles of services or memberships providing customers access to certain services.
You can create service packages and memberships that allow customers to purchase bundles of services or recurring access to bookings.