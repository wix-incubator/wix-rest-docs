SortOrder: 0
# Services API

A service is an offering that a business provides to its customers. 

For example, a fitness studio may offer a one-hour yoga class, a 45 minute HIIT training session and a 30 minute one-on-one personal training session among its services, and a hair salon may offer a 30 minute haircut appointment, a 15 minute blow-out appointment and a two-hour hair coloring appointment among its services.

The service object includes: service details, payment options (to pay for the service once it is booked), and a bookings policy, which defines its booking rules. 

A service must be associated with a category that groups multiple services by theme or type. 

A service’s location and the rate (price) are defined in the service’s schedule.

Each service is linked to a schedule which defines when it can be booked, as well as its location and price (multiple price points are supported); and to a form object, which defines the details customers must provide when booking the service.

## Bookings Policy Terminology
- `book_up_to_x_minutes_before`:  Until what point before the start of a session customers can book a service.
- `futureBookingPolicy`: How far in advance customers may book a service.
- `cancel_reschedule_up_to_x_minutes_before`: Until what point before the start of a session customers can cancel or reschedule.

## Payment Options
The following payment options available via the Wix Bookings UI:

- **Wix pay online** (not available via API) - when this option is selected, a booking made for this service can be paid online using the Wix Payment service. In case this option is the only payment option set, the client won't be able to complete the booking flow without paying online for the service.
- **Wix pay in-person -** when this option is selected, a booking made for this service can be paid in person (up to the business to charge the payment, externally to Wix). In case this option is the only payment option set, the service will be booked without a payment being charged.
- **Custom** - when this option is selected, a booking made for this service can be paid for in a custom way which is up to the API user to define. 
- **Wix Paid Plan** - when a service is connected to a Wix Paid Plan (e.g., a membership or a package of sessions), a booking made for this service can be paid using WiX Paid Plans. To retrieve the Wix Paid Plan that a site member has available for a specific service/booking, call the [Checkout Options]() endpoint.

> **Important**:
Wix Bookings users can select any or all of these payment options. A Wix Bookings user who selects Wix pay online as their only payment option will not be able to integrate their bookings payment flow with an external platform.
