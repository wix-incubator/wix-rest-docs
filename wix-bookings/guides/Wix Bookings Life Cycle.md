# Wix Bookings Lifecycle

To manage bookings, a life cycle status is used to track their progression through different stages. This status is essential for controlling the possible actions that can be taken, such as confirming a pending booking. By utilizing this life cycle status, the system effectively regulates the booking process from start to finish.

A booking can go through checkout for payment or have no payment, in any case, the validation occurs through [Confirm or decline](https://dev.wix.com/api/rest/wix-bookings/confirmation/confirm-or-decline-booking), where availability, payment and the need for business confirmation are checked.

A booking does not need payment to be confirmed, but payment will make sure that the booking is confirmed, even in a case of `DOUBLEBOOKING`, another way of allowing `DOUBLEBOOKING` is passing `skipAvailability` as `true` when creating the booking. 

The following table describes all the possible status for a booking:

| Status | Definition |
|---------------|-------------------------|

| `CREATED` | The booking has been created, but doesn't yet appear in the business calendar. 
The first step and status of a booking is created, it can be used for checkout or processed without it.
You can create a booking with [Create booking](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/create-booking)
| `CONFIRMED` | The site owner has confirmed the booking and it appears in the business calendar.
    + You can manually confirm a booking from pending with [Confirm Booking](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/confirm-booking).
    + Bookings are automatically confirmed when the [service](https://dev.wix.com/api/rest/wix-bookings/services/service/create-service) is configured to do so and the eCommerce order (coming soon) has been approved. An automatic confirmation includes checking the slot's or schedule's availability.
    + Bookings are also automatically confirmed if `skipBusinessConfirmation` is passed as `true` when creating the booking, `false` is default.
| `PENDING` | The booking is waiting to be confirmed or declined by the owner and is displayed in the business calendar.
You can't manually set bookings as `PENDING` via an API.
Bookings are automatically set as `PENDING` when an eCommerce order related to the booking has been created (coming soon).
| `WAITING_LIST` | The booking is pending on a waiting list.
You must use the [Waitlist APIs](https://dev.wix.com/api/rest/wix-bookings/waitlist/introduction) 
to create bookings in status `WAITING_LIST`. You can't change a booking's status from `CREATED` to `WAITING_LIST` with the Bookings V2 APIs.
| `DECLINED` | The booking has been declined by the site owner.
    + You can manually decline a booking with 
    [Decline Booking](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/decline-booking).
    + Bookings are automatically declined when an eCommerce order has been 
    declined or a double booking happened for free bookings.
| `CANCELED` | The booking has been canceled by the site owner or the customer.
You can cancel bookings with [Cancel Booking](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/cancel-booking).