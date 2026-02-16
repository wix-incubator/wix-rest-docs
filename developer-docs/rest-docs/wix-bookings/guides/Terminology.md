# Wix Bookings Terminology

[Wix Bookings](https://support.wix.com/en/article/about-wix-bookings) allows business owners to accept and manage bookings for their services.
This article lists terms and concepts used in Wix Bookings and its APIs.

## Add-on

An optional extra for a Wix Bookings service for an extra cost.
Add-ons are either duration-based (extending booking time in minutes) or quantity-based (purchased in multiple units up to a maximum quantity per add-on).
Add-ons must be included in [add-on groups](#add-on-group) before customers can select them during booking.
Use the [Add-Ons API](https://dev.wix.com/docs/rest/business-solutions/bookings/services/add-ons/introduction) to create and manage individual add-ons.

## Add-on group

A collection of related [add-ons](#add-on) linked to a booking service.
Groups define the maximum number of different add-ons customers can select from the group and include customer-facing information like prompts (instructional text displayed to customers to explain the group's purpose and selection rules) and display order (the sequence in which add-ons appear to customers in the group, determined by their order in the group's `add-on IDs` array).
Use the [Services V2 API](https://dev.wix.com/docs/rest/business-solutions/bookings/services/services-v2/about-add-on-groups) to organize add-ons into groups.

## Appointment

[Appointments](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#appointments) are bookings for on-demand services such as haircuts or consultations.
Customers choose their preferred time from available slots, with availability calculated based on [business hours](#business-hours), service duration, staff [working hours](#working-hours), and [booking policies](#policy).

## Booking

A booking represents a customer's reservation for a specific [service](#service).
The booking includes details about the time, location, and participants.
Use the [Bookings Writer V2 API](https://dev.wix.com/docs/api-reference/business-solutions/bookings/bookings/bookings-writer-v2/introduction) to create and manage bookings, and the [Bookings Reader V2 API](https://dev.wix.com/docs/api-reference/business-solutions/bookings/bookings/bookings-reader-v2/introduction) to retrieve booking information.

See also:
- [Status (booking)](#status-booking): Booking lifecycle and status transitions.
- [Extended booking](#extended-booking): Enhanced booking information with additional details.
- [Multi-service booking](#multi-service-booking): Booking multiple services together.
- [Order](#order): Payment and purchase records.

## Booking fee

A fee for a specific booking that's calculated according to the associated booking [policy](#policy).
For example, a cancellation or no-show fee.

## Business hours

The default operating hours when appointment-based services are available for booking.
You can use the [Locations API](https://dev.wix.com/docs/api-reference/business-management/locations/introduction) to manage individual business hours for each of the business locations.

## Business owner

The person responsible for managing the business that offers services to customers.
This can be the actual business owner or a manager, who may or may not be [staff members](#staff-member) themselves.
They make decisions such as confirming or declining a booking.

## Calendar

The [Wix Bookings Calendar](https://support.wix.com/en/article/wix-bookings-about-the-wix-booking-calendar) is the central interface for managing appointments, classes, and courses.
It displays business availability, staff schedules, confirmed bookings, and provides tools for scheduling, attendance tracking, and client management.
Wix Bookings automatically creates and manages the underlying [schedules](#schedule) and [events](#event) through the [Calendar APIs](https://dev.wix.com/docs/rest/business-management/calendar/introduction).

## `CANCELED` (booking status)

Indicates that the booking has been canceled by the customer.
Depending on the [policy](#policy), the customer may have to pay a cancellation fee. 

## Capacity

The maximum number of participants that can book a service.

- __ Appointments__ : Capacity is typically 1 but can be higher for group sessions.
- __ Classes__ : Capacity determines when individual sessions become fully booked and a [waitlist](#waitlist) activates.
- __ Courses__ : Capacity determines when the entire course becomes fully booked.

## Category

A label used to group services, helping business owners, app developers, and customers filter and organize services efficiently.

## Checkout

Customers must complete a checkout when booking a service.
Wix Bookings integrates with the [Wix eCommerce platform](https://dev.wix.com/docs/rest/business-solutions/e-commerce/introduction) to handle payments and [order management](#order).
To customize the checkout, you can either use the Wix eCommerce [Checkout APIs](https://dev.wix.com/docs/rest/business-solutions/e-commerce/checkout/introduction) or build your own payment interface and process payments with external providers.
For implementation examples, see [end-to-end booking flows](https://dev.wix.com/docs/api-reference/business-solutions/bookings/end-to-end-booking-flows).

## Choice

A specific value for a service [option](#option) that business owners define when setting up [varied pricing](#varied-pricing).
For example, the service option `ageGroup` may have these choices: `child`, `student`, `adult`, and `senior`.
Each choice may have a different price, and customers select from these predefined choices when booking.

## Class

[Classes](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#classes) are scheduled sessions that customers can book individually.
For example, drop-in yoga classes or weekly cooking lessons.
You can schedule classes on various days of the week, at different times, and with different staff members.
When a specific session is fully booked, customers can join a waitlist and are notified if a spot opens up.
Unlike [courses](#course) where customers must book all sessions, class customers can choose which sessions to attend.

## `CONFIRMED` (booking status)

Indicates that the business owner has confirmed the booking and it appears in the [Wix Bookings Calendar](#calendar).
Bookings can be confirmed in different ways:
- __Automatically__: Bookings are automatically confirmed when the service doesn't require manual approval and you use Wix eCommerce checkout.
  Wix Bookings listens to eCommerce order events and confirms a booking when the corresponding order is approved.
- __Manually__: If the service requires manual approval or you use a custom checkout, you can call [Confirm Or Decline Booking](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings-and-time-slots/bookings-v2/bookings-v2-and-confirmation/confirm-or-decline-booking).

## Course

[Courses](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#courses) are multi-session programs that customers must book in full.
For example, an 8-week programming bootcamp or a 3-day certification training program.
Business owners set the complete session timeline before offering the course, with courses starting and ending on pre-defined dates.
Customers must book all course sessions, while for [classes](#class) they're free to book only a single session or some sessions.

## Deposit

Amount that customers must pay immediately online when checking out the booking.
Only available for services with fixed or varied [pricing](#pricing).

## Double booking

A double booking occurs when a customer attempts to book a service that's already reserved.
This can happen when multiple customers book simultaneously.
When Wix Bookings detects insufficient availability during booking confirmation, the business must manually resolve the conflict.

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
Learn more about [Wix Forms integration](https://dev.wix.com/docs/rest/business-solutions/bookings/wix-forms-integration).

## Integration

A custom implementation that extends Wix Bookings functionality through [service plugins](#service-plugin).
Developers can inject custom logic into the booking flow, such as dynamic pricing or availability rules.

## Member

Someone who is a registered [member](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/introduction) in the Wix site and has a login.
Unlike [visitors](#visitor), members have persistent accounts and can access member-only features on the Wix site.

## Multi-service booking

Multi-service bookings enable businesses to offer comprehensive service packages where customers can book multiple related services together in a single transaction.
For example, a spa package that includes a massage, facial, and manicure, or a fitness package with a personal training session followed by a yoga class.
Each multi-service booking contains several single-service bookings.
Single-service bookings in the package must be scheduled sequentially with each booking starting when the previous booking ends.
Learn more about [multi-service bookings](https://dev.wix.com/docs/api-reference/business-solutions/bookings/bookings/bookings-writer-v2/introduction#multi-service-bookings).

## Option

A pricing category that business owners define when setting up [varied pricing](#varied-pricing) for a service.
For example, options can include staff member, customer age, appointment time, or equipment type.
Each option contains a list of predefined [choices](#choice) that customers can select from.

## Order

A record of a customer's purchase in the [Wix eCommerce system](https://dev.wix.com/docs/api-reference/business-solutions/e-commerce/introduction).
All bookings use [eCommerce orders](https://dev.wix.com/docs/rest/business-solutions/e-commerce/orders/introduction) to maintain proper records and functionality.
When you use an [eCommerce checkout](https://dev.wix.com/docs/rest/business-solutions/e-commerce/checkout/introduction), orders are automatically created and contain details about the booking, payment information, and customer data.
For custom checkouts, you must manually create an order in the Wix eCommerce platform and update the booking status to complete the booking flow.

## `PENDING` (booking status)

Indicates that the booking is waiting to be confirmed or declined by the business.
This status is used when the service requires manual business approval.

Bookings are set as `PENDING` in these scenarios:
- __Wix eCommerce checkout__: Wix Bookings automatically sets this status when an eCommerce order is created.
- __Custom checkout__: Developers must manually set this status using [Mark Booking as Pending](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings/bookings-writer-v2/mark-booking-as-pending).

Bookings in `PENDING` status are displayed in the business calendar and may block availability for the time slot, depending on whether the service allows multiple pending booking requests for the same time.

## Policy

Rules set by the business owner that govern how customers can book and cancel services.
Policies define booking windows, cancellation deadlines, participant limits, and other constraints.

When a booking is created, the current policy is saved as a [policy snapshot](https://dev.wix.com/docs/api-reference/business-solutions/bookings/policies/booking-policy-snapshots/introduction) to preserve the original terms.
This protects both customers and businesses by maintaining the original agreement terms throughout the booking lifecycle, even if policies change after a booking is made.

## Pricing

Businesses can offer services for free, with fixed pricing, or with [varied pricing](#varied-pricing).
Wix Bookings also supports custom pricing integrations through the [Pricing Integration service plugin](https://dev.wix.com/docs/rest/business-solutions/bookings/pricing/pricing-integration-spi/introduction), allowing you to implement dynamic pricing logic.
You can also create service packages and memberships using [Wix Pricing Plans](#wix-pricing-plans), which let customers purchase bundles of services or recurring access to bookings.
Learn more about [service payments](https://dev.wix.com/docs/api-reference/business-solutions/bookings/services/services-v2/about-service-payments).

## Resource

An asset the business needs in order to provide a service.
Each resource has an event [schedule](#schedule) that tracks when it's booked.
Customers can book a service only if at least 1 resource of each required [resource type](#resource-type) is available.

## Resource type

A classification that allows Wix Bookings to automatically check [resource](#resource) availability and avoid double bookings.
Examples include rooms, equipment, vehicles, or any other custom asset type that requires scheduling and availability management.
[Staff members](#staff-member) are treated as a special resource type with complex scheduling needs and have a [separate API](https://dev.wix.com/docs/api-reference/business-solutions/bookings/staff-members/introduction).

## Schedule

Organizes [events](#event) and defines when services are available and when resources are booked.
Wix Bookings automatically creates and manages schedules via the [Calendar APIs](https://dev.wix.com/docs/api-reference/business-management/calendar/introduction) when you create services, staff members, or bookings.
Learn more about [how Wix Bookings integrates with the Calendar APIs](https://dev.wix.com/docs/api-reference/business-management/calendar/wix-bookings-integration).

## Service

A business offering, which can be a [class](#class), a [course](#course), or [appointment-based](#appointment).
For example, a fitness studio may offer 30-minute 1-on-1 personal training sessions by appointment, 1-hour yoga classes every Monday at 7:00 PM, and introductory HIIT courses consisting of 3 training sessions on specific dates.
Learn more about [service types](https://dev.wix.com/docs/api-reference/business-solutions/bookings/services/services-v2/about-service-types).

## Service plugin

[Service plugins](https://dev.wix.com/docs/build-apps/develop-your-app/extensions/backend-extensions/service-plugins/about-service-plugin-extensions) are APIs defined by Wix, which you can choose to implement.
By doing so, you become a service provider.
Then, Wix calls your implementation during a specific flow, receives your response, and continues the flow considering your returned data.
For example, as a pricing provider you can offer custom pricing options for a business using the [Wix Bookings Pricing Integration service plugin](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi).

## Session

A single occurrence of a service at a specific time.
For example, a yoga class on Monday at 7 PM or a haircut appointment on Tuesday at 2 PM.
For [classes](#class) and [courses](#course), sessions are pre-created when the service is set up, and customers book into existing sessions.
For [appointments](#appointment), sessions are created dynamically when customers make bookings.

## Staff member

A person who provides services for the business.
Staff members have both working hour schedules (when they're available to work) and event schedules (when they're booked), which may involve complex scheduling needs.
By default, staff members work during the [business hours](#business-hours), but you can customize their working hours.
Staff members are also eligible to receive [tips](#tips).
Use the [Staff Members API](https://dev.wix.com/docs/api-reference/business-solutions/bookings/staff-members/introduction) to manage staff members and their schedules.

Not all staff members are registered Wix users, and not all Wix users related to the business are staff members.

## Status (booking)

Information about the life cycle status of the booking.
Booking statuses include: `CREATED`, `PENDING`, `CONFIRMED`, `DECLINED`, `WAITING_LIST`, `UPDATED`, and `CANCELED`.
Learn more about [the booking lifecycle and status transitions](https://dev.wix.com/docs/api-reference/business-solutions/bookings/bookings/bookings-writer-v2/introduction#booking-lifecycle).

## Time slot

Specific periods when a service is available for customer bookings.
You can use the [Time Slots API](https://dev.wix.com/docs/api-reference/business-solutions/bookings/time-slots/time-slots-v2/introduction) to find available slots for appointments and classes.
The API considers multiple factors to determine availability: service schedules, staff working hours, resource availability, booking policies, and existing bookings.
For courses, you can follow the [end-to-end booking flow](https://dev.wix.com/docs/api-reference/business-solutions/bookings/end-to-end-booking-flows#book-a-course) to check availability.

## Tips

Additional payments that customers can add to their bookings to show appreciation for service quality.
Wix Bookings automatically distributes tips among eligible [staff members](#staff-member) based on configurable settings.
Use the [eCommerce Tips APIs](https://dev.wix.com/docs/api-reference/business-solutions/e-commerce/other-services/tips/introduction) to manage tip settings, preview tips, and apply tips to [eCommerce orders](#order).

## Variant

The combination of all customer [choices](#choice) for a service's pricing options.
Business owners must define all possible variants and their prices when setting up [varied pricing](#varied-pricing) for a service.
Each variant represents a different combination of the available choices and can have a unique price.

## Varied pricing

[Varied pricing](https://support.wix.com/en/article/wix-bookings-understanding-price-options) allows businesses to charge for services based on different factors, such as the staff member providing the service or the equipment needed.
Wix Bookings supports custom pricing integrations through the [Pricing Integration service plugin](https://dev.wix.com/docs/rest/business-solutions/bookings/pricing/pricing-integration-spi/introduction), allowing you to implement dynamic pricing logic.

## Visitor

Anyone who isn't registered as a [member](#member) or hasn't logged in to the Wix site.
If a visitor creates a booking they're added as a contact to the Wix site.
Use the [Contacts API](https://dev.wix.com/docs/api-reference/crm/members-contacts/contacts/introduction) to manage visitor contact information.
Unlike members, visitors don't have persistent accounts and can't access member-only features on the Wix site.

## `WAITING_LIST` (booking status)

Indicates that the class booking is on a waitlist for a fully booked session.

## Waitlist

A feature for class services that allows customers to join a queue when sessions are fully booked.
When a spot opens due to cancellation, the first person on the waitlist (also called the suggested participant) is notified and given a time window to book the session.
If they don't book in the time window, the opportunity passes to the next person on the waitlist.
Waitlists aren't available for courses or appointment services.

## Wix Pricing Plans

[Wix Pricing Plans](https://support.wix.com/en/article/wix-bookings-about-wix-bookings#selling-membership-plans-and-packages) are prepaid bundles of services or memberships providing customers access to certain services.
You can create service packages and memberships that allow customers to purchase bundles of services or recurring access to bookings.

## Working hours

The specific times when a [staff member](#staff-member) is working, defined by their working hours [schedule](#schedule).
By default, staff members work during the [business hours](#business-hours).