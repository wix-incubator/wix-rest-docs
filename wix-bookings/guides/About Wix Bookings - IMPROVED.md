# About Wix Bookings

The Wix Bookings APIs allow you to customize scheduling and booking functionality for appointments, classes, and courses. You can manage services, staff members, and other resources, handle bookings, check availability, and configure pricing.

## Wix Bookings APIs

Wix Bookings APIs include:

- [Services](https://dev.wix.com/docs/rest/business-solutions/bookings/services/services-v2/introduction): Create, manage, and query the specific offerings a business provides.
- [Staff Members](https://dev.wix.com/docs/rest/business-solutions/bookings/staff-members/introduction): Manage people who provide services, including their working hours and availability schedules.
- [Resources](https://dev.wix.com/docs/rest/business-solutions/bookings/resources/resources-v2/introduction): Manage physical assets like rooms and equipment that can be booked for services.
- [Pricing](https://dev.wix.com/docs/rest/business-solutions/bookings/pricing/introduction): Calculate booking costs and implement custom pricing logic through service plugins.
- [Policies](https://dev.wix.com/docs/rest/business-solutions/bookings/policies/booking-policies/introduction): Define rules for how customers can book, cancel, or reschedule services.
- [Time Slots](https://dev.wix.com/docs/rest/business-solutions/bookings/time-slots/availability-calendar/introduction): Check availability of appointment slots and class events for efficient booking and scheduling.
- [Bookings](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings/about-the-bookings-apis): Manage customer bookings to individual services or multiple services at once.
- [External Calendar](https://dev.wix.com/docs/rest/business-solutions/bookings/calendar/external-calendar-v2/introduction): Connect and sync with external calendar providers like Google, Microsoft, and Apple calendars.

## Key concepts

### Service types

Wix Bookings supports 3 service types:

- **Appointments**: On-demand bookings for available time slots.
- **Classes**: Scheduled sessions that customers can join individually.
- **Courses**: Multi-session programs that customers must book in full.

For detailed information about each service type, see [About Service Types](https://dev.wix.com/docs/sdk/backend-modules/bookings/services/about-service-types).

### Calendar integration

Wix Bookings uses the [Calendar APIs](https://dev.wix.com/docs/rest/business-management/calendar) to manage all scheduling and availability. Each service, staff member, and resource has associated schedules and events in the calendar system. This unified approach handles appointments, classes, courses, and resource scheduling through a single calendar system.

### Events and schedules

An event is a time-specific instance of a service (like an appointment or class session). Events are organized within schedules, which define when services are available or when resources are booked. Wix Bookings automatically creates and manages schedules and events when you create services, staff members, or bookings.

### Staff members and resources

**Staff members** are people who provide services and have complex scheduling needs - they have both working hours (when they're available to work) and event schedules (when they're actually booked).

**Resources** are physical assets like rooms, equipment, or facilities needed for services. They only have event schedules showing when they're booked, with availability based on business hours.

### Pricing

Services can have fixed pricing or varied pricing based on different factors like staff member, time of day, or customer type. Wix Bookings supports custom pricing integrations through service plugins, allowing you to implement dynamic pricing logic.

### Payment and checkout

Wix Bookings supports 2 checkout approaches:

- **Wix eCommerce checkout**: Automated payment handling with built-in checkout pages, order management, and payment processing.
- **Custom checkout**: Build your own payment flow using external payment providers while still integrating with Wix order management.

### Waitlists

For class services, customers can join a waitlist when sessions are fully booked. If a spot opens up due to a cancellation, the first person on the waitlist is notified and given a chance to book the session.

## Before you begin

It's important to note the following points before starting to code:

- **Calendar API dependency**: Wix Bookings relies on the [Calendar APIs](https://dev.wix.com/docs/rest/business-management/calendar) for all scheduling functionality. Wix Bookings automatically manages schedules and events, so you primarily retrieve calendar data rather than create it.
- **App ID filtering**: When working with Calendar APIs in a Bookings context, filter schedules using the Wix Bookings app ID (`13d21c63-b5ec-5912-8397-c3a5ddb27a97`) to show only Bookings-related data.
- **eCommerce integration**: Bookings integrate with Wix eCommerce for payment processing during checkout.
- **Service setup**: Services must be properly configured with schedules, resources, and policies before customers can make bookings.

## See also

- [Wix Bookings Terminology](https://dev.wix.com/docs/rest/business-solutions/bookings/terminology)
- [Architecture and Data Flow](https://dev.wix.com/docs/rest/business-solutions/bookings/architecture-and-data-flow)
- [End-to-End Booking Flows](https://dev.wix.com/docs/sdk/backend-modules/bookings/end-to-end-booking-flows)
- [How Wix Bookings Uses the Calendar APIs](https://dev.wix.com/docs/rest/business-solutions/bookings/calendar/how-wix-bookings-uses-the-calendar-apis)
- [Calendar APIs](https://dev.wix.com/docs/rest/business-management/calendar)
- [Wix eCommerce APIs](https://dev.wix.com/docs/api-reference/business-solutions/e-commerce/introduction)
- [About Service Types](https://dev.wix.com/docs/sdk/backend-modules/bookings/services/about-service-types)
