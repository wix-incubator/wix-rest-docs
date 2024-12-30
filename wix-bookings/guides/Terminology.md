# Wix Bookings Terminology

[Wix Bookings](https://support.wix.com/en/article/about-wix-bookings) allows
business owners to accept and manage bookings for their services.

This article contains a comprehensive list of the various terms and concepts
used in all of Wix Bookings and its APIs.

## Appointment

[Appointments](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#appointments)
are specific time slots that customers can book in a calendar. For example, a
hair salon may be open Monday to Friday from 9:00 AM to 7:00 PM. Customers could
book a session at any available time during these hours.

## Appointment schedule

Defines when customers can book a session for an appointment-based service.
Bookings are based on the business’s opening hours, session duration, time
between sessions, and staff availability. For example, a hair salon operates
Monday to Friday, 9:00 AM to 7:00 PM, offering 30-minute and 1-hour haircuts.
One staff member is available from 9:00 AM to 5:00 PM, and another from 11:00 AM
to 7:00 PM, with 15-minute buffers between sessions. Customers can book an
appointment if the service and at least one staff member are available,
considering the 15-minute buffer before and after the session.

## Availability

Free time on an appointment schedule that customers can book.

## Booking

Information about the service that the customer has booked. You can think of a
booking as an order placed by a customer for a service. Includes details about
the time, location, participants, and price.

## Booking fee

Fee for a specific booking that's calculated according to the associated booking
policy snapshot. Currently, only cancellation fees, including no-show fees, are
supported.

## Business owner

The owner of the business that offers services through Wix. Can be a different
person than the site owner. The business owner makes decisions such as
confirming or declining a booking.

## Calendar

The [Calendar](https://support.wix.com/en/article/wix-bookings-about-the-wix-booking-calendar)
is a general overview about the availability and bookings of the business,
including its services and resources. You can manage appointments, classes, and
courses on the calendar.

## `CANCELED` (booking status)

Indicates that the booking has been canceled by the site owner or the customer.
Cancel bookings using [Cancel Booking](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings-and-time-slots/bookings-v2/bookings-v2-and-confirmation/bookings-cancel-booking).

## Catalog

A list of all the different Bookings services a business provides.

## Category (service)

A label used to group services, helping business owners, app developers, and
customers filter and organize services efficiently.

## Checkout

Customers must complete a [checkout](https://dev.wix.com/docs/rest/business-solutions/e-commerce/checkout/introduction)
when booking a service. The checkout is the second stage of the
[eCommerce](https://dev.wix.com/docs/rest/business-solutions/e-commerce/introduction)
purchase flow: cart; checkout; order.

## Choice (pricing)

A specific value for a service option that customers can book. For example, the
service option `ageGroup` may have these choices: `child`, `student`, `adult`,
and `senior`. Each choice may have a different price.

## Class

[Classes](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#classes)
are either a single session or a set of sessions that's offered by a business
on specific day and time. Classes can be scheduled on various weekdays, at
different times, and with different resources, including staff members.
Customers can sign up for one or multiple sessions, unlike courses where all
sessions must be booked. For example, a language school offers an open
discussion class in Spanish every Monday at 8:00 PM. Customers can book one or
multiple sessions of this class.

## Class schedule

Before offering a class or course service, the business owner must decide when
to schedule sessions. This is in contrast to appointment services, where
customers are free to decide when they want to book a session. Wix uses the
class schedule to calculate which sessions are still available.

## `CONFIRMED` (booking status)

Indicates that the business owner has confirmed the booking and it appears in
the business calendar. You can confirm your bookings in different ways:
- Automatically. Bookings are automatically confirmed when the service is set
  up for automatic confirmation and the order is approved during checkout,
  including an availability check.
- Manually. You can manually confirm a booking using [Confirm Or Decline
  Booking](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings-and-time-slots/bookings-v2/bookings-v2-and-confirmation/confirm-or-decline-booking).

## Course

[Courses](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business#courses)
start and end on pre-defined dates with a limited number of sessions. For
example, an academic course or fitness boot camp during the summer holidays.
Customers must book all course sessions, while they're free to book only a
single or some sessions for classes.

## Course schedule

Before offering a course service, the business owner must decide when to
schedule sessions. This is in contrast to appointment services, where customers
are free to decide when they want to book a session. Wix uses the course
schedule to calculate availability, when the first session starts, and when the
last session ends.

## Deposit

Amount the customer must pay immediately when checking out the booking.

## Double booking

A double booking occurs when a customer attempts to book a service that's
already reserved. This can happen if multiple customers are checking out
simultaneously or if the business owner manually confirms more bookings than
the service's capacity allows.

## Extended booking

In addition to basic information about the booking, an extended booking contains
additional details. For example, attendance details, and whether the customer
can demand a refund or reschedule the booking.

## External calendar

A calendar hosted by a 3rd-party provider.

## External calendar connection

A linkage between a Wix Bookings calendar and one or more external calendars.
External calendar connections allow you to import and export calendar events.

## External calendar event

A single session or an instance of recurring session that appears in a calendar.
For example, an appointment or a class session.

## External calendar provider

The 3rd-party service that provides an external calendar such as,
[Google](https://developers.google.com/calendar/api/guides/overview),
[Apple](https://developer.apple.com/documentation/foundation/calendar),
or [Microsoft](https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0).

## External calendar resource

A resource that doesn't have a Wix Bookings calendar. Instead, the resource's
availability is managed with an external calendar. For example, your app or the
business owner may decide to manage availability through a staff member's Gmail
account, and Google calendar.

## Form

The [booking form](https://support.wix.com/en/article/wix-bookings-customizing-booking-form-fields)
that's displayed to customers in the Wix site when they book the service. For
example, customers can input their name into the bookings form.

## Integration

Extended functionality that's implemented by a 3rd-party service provider and
made available to the merchant using Wix service plugins. For example, you, as
a pricing provider, can offer custom varied pricing options to a Wix site using
the [Wix Bookings Pricing Integration REST Service Plugin](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi).

## Locked session

A session for a class that customers can't book. For example, because the
session is full, has a waitlist, or an administrator needs to manually screen
each customer before adding them to the session.

## Member

Someone who is a registered [member](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/introduction)
in the Wix site and has a login.

## Merchant

The business that offers services to customers. The merchant has a Wix site for
their business, unless your app is working with a
[Headless](https://dev.wix.com/docs/go-headless/getting-started/about-headless/about-wix-headless)
project (in which case the site is hosted outside of the Wix ecosystem).

## Option (pricing)

The pricing possibilities for a service, which can vary based on factors such
as the staff member, customer age, appointment time, or type of equipment. Each
option has a list of supported choices that may affect the service price or the
option may have a uniform price.

## `PENDING` (booking status)

Indicates that the booking is waiting to be confirmed or declined. Bookings in
`PENDING` status are displayed in the business calendar. Bookings are
automatically set as `PENDING` when an
[eCommerce order](https://dev.wix.com/docs/rest/business-solutions/e-commerce/orders/introduction)
related to the booking has been created.

## Policy

Rules set by the merchant regarding booking and canceling a service. These may
include how far in advance customers can book, the deadline for cancellations,
and the maximum number of participants allowed per booking.

## Pricing provider

A 3rd-party app that implements custom logic to determine the price of a booking
with the [Pricing Integration Service Plugin](https://dev.wix.com/docs/rest/business-solutions/bookings/pricing/pricing-integration-spi/introduction).

## Policy snapshot

The version of a service's booking policy saved at the time a booking is
created. Snapshots preserve the original terms, which is useful if policies
change after a booking is made.

## Resource

A business asset. For example, a staff member, a room, or equipment that's
needed to provide a service. Each resource has a schedule that defines its
availability.

## Schedule

A collection of all sessions associated with a specific service or resource. It
includes information necessary to calculate availability. For more details, see
appointment schedule, class schedule, and course schedule.

## Service

A business offering, which can be a class, course, or appointment-based. For
example, a fitness studio may offer 30-minute 1-on-1 personal training sessions
by appointment, 1-hour yoga classes every Monday at 7:00 PM, and introductory
HIIT courses consisting of 3 training sessions on specific dates. For more
information, see appointment, class, and course.

## Service plugin

[Service plugins](https://dev.wix.com/docs/build-apps/develop-your-app/extensions/backend-extensions/service-plugins/about-service-plugin-extensions)
(formerly SPIs) are APIs that are defined by Wix, which you can choose to
implement. By doing so, you become a service provider. Then, Wix calls your
service during a certain flow, waits for your response, and continues the flow
with it. For example, as a pricing provider you can offer custom varied pricing
options to a Wix site using the [Wix Bookings Pricing Integration REST Service
Plugin](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi).

## Session

A booked or reserved period of time for an appointment, class, or course.
Alternatively, you can consider a session as a specific instance of a service
occurring at a particular time. The aggregation of all sessions for a service
constitutes the service's schedule.

## Site owner

The owner of the Wix site that has Wix Bookings installed and all
[site contributors](https://support.wix.com/en/article/inviting-people-to-contribute-to-your-site).

## Slot

A time period that customers can book for a service. For appointments, it
includes all the times available to book. For classes, it refers to sessions
that are open for booking. For more details, see appointment schedule and class
schedule.

## Staff member

Team member of the business who provides a Bookings service. Staff members are
eligible to receive tips. Not all staff members are
[site collaborators](https://support.wix.com/en/article/inviting-people-to-contribute-to-your-site)
and not all site contributors are staff members.

## Status (booking)

Information about the life cycle status of the booking. Booking statuses
include: `CREATED`, `PENDING`, `CONFIRMED`, `DECLINED`, `WAITING_LIST`,
`UPDATED`, `CANCELED`.

## Suggested participant (waitlist)

When a session is fully booked, customers can join the waitlist. If a spot
opens up due to a cancellation, the first person on the waitlist (the suggested
participant) is notified and given a chance to book the session within a
specified time. If they don't book it, the opportunity is passed to the next
person on the list.

## Variant (pricing)

Unique combination of choices for a service. For example: `{"time": "afternoon",
"ageGroup": "adult", "equipment": "kettlebells"}`. Each variant may have a
different price.

## Varied pricing

[Varied pricing](https://support.wix.com/en/article/wix-bookings-understanding-price-options)
allows businesses to charge for services based on different factors, such as
the staff member who provides the service or the equipment needed.

## Visitor

Anyone who isn't registered as a member or hasn't logged in to the Wix site. If
a visitor creates a booking they're added as a
[contact](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/introduction).

## `WAITING_LIST` (booking status)

Indicates that the booking is on a waitlist. Currently, waitlists are available
only for classes and not for courses or appointment-based services.

## Waitlist

A feature available for class services, allowing customers to request to be
added to a fully booked session in case of cancellations. Not available for
courses or appointment services.

## Waitlist time window

The duration that's given to the suggested participant to book a place in the
session before it's offered to the next customer on the waitlist.

## Wix Pricing Plans

[Wix Pricing Plans](https://support.wix.com/en/article/wix-bookings-about-wix-bookings#selling-membership-plans-and-packages)
are prepaid bundles of services or memberships providing customers access to
certain services.