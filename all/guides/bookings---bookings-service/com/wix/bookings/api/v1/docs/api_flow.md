SortOrder: 0
# About the Bookings API

Use this API to manage bookings to a site's services.

A booking is an entity that represents a session that was ordered (but not necessarily paid for) for a specific time and rate for a specific customer. A customer can book a single class or an appointment (= session), or book an bundle of sessions at once, e.g., a course (= schedule).  

> **Note**:  
A booking that has not been paid for (when the service requires payment) will be created with status = PENDING. A booking that requires business approval will be created with status = PENDING CHECKOUT.

A booking contains the following:
- **Customer information**: Contact details (contact ID, name, email, address, phone number), and any additional fields set by the owner - under `formInfo`.
- **Booked session details**: Session name, date, start & end time, location and rate.
- **Payment details**: Final price that the customer is being charged, payment option the customer chose when booking (online payment, in-person payment, membership) and the payment method used in case of an online payment (e.g., credit card, Paypal). Will also contain coupon code if entered during checkout.
- **Status**: Current booking status (confirmed, declined, canceled, etc.).

## Terminology
- **Visitor**: Anyone who is not registered as a member in the Wix site (upon booking, visitors are registered as contacts).
- **Member**: Someone who is registered as a member in the Wix site.
- **Owner**: The Wix site owner (who has Wix Bookings installed).
- **Slot**: An available period of time in a schedule that can be booked by a customer. While this includes existing sessions that are available for booking, it can also represent a period of time that can be booked based on the availability of a resource (e.g., a barber with appointments of 30 minutes each that are open for booking every weekday between 8:00 - 17:00). These slots are calculated by the constraints of the schedule.
- **[Wix Paid Plans](https://support.wix.com/en/article/about-pricing-plans)**: A pre-paid bundle of services or membership including access to certain services. Access a member's pricing plans by calling the [Checkout Options](https://dev.wix.com/api/rest/wix-bookings/checkout-options/checkout-options) endpoint with the member's contact ID.

## Bookings Statuses
Each booking has a status. Statuses include:
- **Confirmed**: When the session is free, when payment is expected in person, or when online payment was approved.
- **Pending**: When a booking requires the owner's approval, it is "pending" until the owner either confirms or declines the booking. In addition, if a customer is booked to a waitlist, the booking will be "pending" until it is added to the session.
- **Pending Checkout**: When the booking's online payment is waiting for payment approval. Will automatically change to "confirmed" when the payment is approved.
- **Declined**: When the owner has declined a booking that requires their approval. 
- **Canceled**: When the customer or the business owner has canceled the previously confirmed booking.

## Use Cases

### Book a visitor (i.e., anyone, not necessarily known to the site owner in advance) to a given service, including payment
![image](https://s3.amazonaws.com/wixplorer-readme-images/bookings---bookings-service%2FBookWithID-Slot.png)
1. To display the various services available for booking on your platform, call the [List Services](https://dev.wix.com/api/rest/wix-bookings/services/service/list-services) endpoint.  
2. When a visitor selects a service, call [Query Availability](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings-and-time-slots/time-slots/availability-calendar/query-availability) to display the sessions available for booking.  
2a. Provide the visitor with a form to fill out that matches the data required in this session's form, as returned in the [List Services](https://dev.wix.com/api/rest/wix-bookings/services/service/list-services) response.
3. When a visitor selects a slot to book, call [Checkout Options](https://dev.wix.com/api/rest/wix-bookings/checkout-options/checkout-options) to display the payment options available for this service. At this time, payment via WixPayOnline is not supported via API.
4. When a visitor continues with the checkout process - if a significant amount of time has passed, call [Is Available](https://dev.wix.com/api/rest/wix-bookings/bookings/availability/is-available) to confirm that the slot is still available before continuing.
5. When a visitor completes the checkout process, call [Create Booking](https://dev.wix.com/docs/rest/business-solutions/bookings/bookings-and-time-slots/bookings-v2/bookings-v2-and-confirmation/create-booking). Include formInfo and either scheduleId or by bySessionId.
