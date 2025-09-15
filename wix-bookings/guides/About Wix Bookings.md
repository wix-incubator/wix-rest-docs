# About Wix Bookings

The Wix Bookings APIs allow you to build and customize booking experiences for any service-based business.
You can manage services, staff members, pricing, availability, and customer bookings throughout their entire lifecycle.

## Wix Bookings APIs

Wix Bookings APIs include:

- [Services](https://dev.wix.com/docs/rest/business-solutions/bookings/services/services-v2/introduction): Create, manage, and query the specific offerings a business provides.
- [Staff Members](https://dev.wix.com/docs/rest/business-solutions/bookings/staff-members/introduction): Manage people who provide services, including their working hours.
- [Resources](https://dev.wix.com/docs/rest/business-solutions/bookings/resources/resources-v2/introduction): Manage physical assets like rooms and equipment that the business needs to provide a service.
- [Pricing](https://dev.wix.com/docs/rest/business-solutions/bookings/pricing/introduction): Calculate booking costs and implement custom pricing logic through service plugins.
- [Policies](https://dev.wix.com/docs/rest/business-solutions/bookings/policies/booking-policies/introduction): Define rules for when and how customers can book, cancel, or reschedule services.
- [Time Slots](https://dev.wix.com/docs/rest/business-solutions/bookings/time-slots/availability-calendar/introduction): Check availability of appointment slots and class events for efficient booking and scheduling.
- [Bookings](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings/about-the-bookings-apis): Manage customer bookings to individual services or multiple services at once.
- [External Calendar](https://dev.wix.com/docs/rest/business-solutions/bookings/calendar/external-calendar-v2/introduction): Connect and sync with external calendar providers like Google, Microsoft, and Apple calendars.

## Key concepts

These concepts form the foundation of the Wix Bookings platform.

### Service types

Wix Bookings supports 3 service types:

- Appointments: On-demand bookings for available time slots. For example, hair cuts or consultations.
- Classes: Scheduled sessions that customers can join individually. For example, drop-in yoga classes or weekly cooking lessons.
  When a specific event is fully booked, customers can join a [waitlist](https://dev.wix.com/docs/api-reference/business-solutions/bookings/bookings/waitlist/api-overview) and are notified if a spot opens up.
- Courses: Multi-session programs that customers must book in full. For example, 8-week programming bootcamps or certification training programs.

For detailed information, see [About Service Types](https://dev.wix.com/docs/sdk/backend-modules/bookings/services/about-service-types).

### Scheduling and availability

Wix Bookings integrates with the [Calendar APIs](https://dev.wix.com/docs/rest/business-management/calendar) to manage when services can be booked.

#### How scheduling works

Each service, [staff member](https://dev.wix.com/docs/rest/business-solutions/bookings/staff-members/introduction), and [resource](https://dev.wix.com/docs/rest/business-solutions/bookings/resources/resources-v2/introduction) has associated schedules and events in the calendar system.
For details about how staff and resources affect scheduling, see the [Staff members and resources](#staff-members-and-resources) section below.

- Events are time-specific instances of services (like an appointment or class session).
- Schedules organize these events and define when services are available or when resources are booked.
  Wix Bookings automatically creates and manages schedules and events when you create services, staff members, or bookings.

#### How availability works

Time slots represent specific periods when services can be booked.
The Wix Bookings and Calendar APIs work together to manage availability:

- Wix Bookings APIs handle availability queries and booking validation.
  Use the [Time Slots API](https://dev.wix.com/docs/rest/business-solutions/bookings/time-slots/availability-calendar/query-availability) to find available time slots for appointments and classes.
  The availability calculation considers multiple factors: service schedules, staff working hours, resource availability, booking policies, and existing reservations.
  For courses, you need to manually calculate availability based on total capacity since customers must book the entire program, as described in the [end-to-end booking flow](https://dev.wix.com/docs/api-reference/business-solutions/bookings/end-to-end-booking-flows#book-a-course).
- Wix Calendar APIs manage the underlying schedule data and events. Wix Bookings automatically creates and updates calendar events when bookings are made.
  For most use cases, you'll use Calendar APIs to retrieve schedule and event data for display purposes, while Wix Bookings handles creation and management automatically.

For detailed information about the integration, see [How Wix Bookings Uses the Calendar APIs](https://dev.wix.com/docs/rest/business-solutions/bookings/calendar/how-wix-bookings-uses-the-calendar-apis).

### Staff members and resources

Staff members are people who provide services and have complex scheduling needs.
They have both working hours (when they're available to work) and event schedules (when they're actually booked).

Resources are physical assets like rooms, equipment, or facilities needed for services. They only have event schedules showing when they're booked, with availability based on business hours.

For detailed information, see [About Resources](https://dev.wix.com/docs/api-reference/business-solutions/bookings/resources/about-resources).

### Pricing

Services can be free or have fixed pricing or varied pricing based on different factors like staff member, time of day, or customer type.
Wix Bookings supports custom pricing integrations through the [Pricing Integration service plugin](https://dev.wix.com/docs/api-reference/business-solutions/bookings/pricing/pricing-integration-service-plugin/introduction), allowing you to implement dynamic pricing logic.

You can also create service packages and memberships using [Wix Pricing Plans](https://dev.wix.com/docs/api-reference/business-solutions/pricing-plans/introduction), which allow customers to purchase bundles of services or recurring access to bookings.

For detailed information, see [About Service Payments](https://dev.wix.com/docs/api-reference/business-solutions/bookings/services/services-v2/about-service-payments).

### Checkout and order

Wix Bookings integrates with the [Wix eCommerce platform](https://dev.wix.com/docs/api-reference/business-solutions/e-commerce/introduction) to handle payments and order management.
All bookings use [eCommerce orders](https://dev.wix.com/docs/api-reference/business-solutions/e-commerce/orders/introduction) to maintain proper records and functionality.

By default, Wix Bookings handles the entire checkout and order creation process automatically.
To customize the checkout process, you can choose between 2 approaches:

- Wix eCommerce checkout: Use the Wix eCommerce [Checkout APIs](https://dev.wix.com/docs/api-reference/business-solutions/e-commerce/purchase-flow/checkout/introduction). Wix Bookings automatically processes payments, creates eCommerce orders, and updates booking statuses.
- Custom checkout: Build your own payment interface and process payments with external providers.
  You must still manually create an eCommerce order and update the booking status to complete the booking flow.

For step-by-step implementation examples, see [End-to-End Booking Flows](https://dev.wix.com/docs/api-reference/business-solutions/bookings/end-to-end-booking-flows).

## See also

- [Wix Bookings Terminology](https://dev.wix.com/docs/rest/business-solutions/bookings/terminology)
- [Architecture and Data Flow](https://dev.wix.com/docs/rest/business-solutions/bookings/architecture-and-data-flow)