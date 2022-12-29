SortOrder: 2
# Sample Flows


This article shares possible use cases your app could support, as well as 
example flows. You're certainly not limited to these use cases, but it can be 
a helpful jumping off point as you plan your app's implementation. Your app 
could help site owners add bookings to their business calendar. These bookings 
can be for appointment based services, classes, and courses. They may also 
use all payment methods that are supported in 
[Wix eCommerce](https://dev.wix.com/api/rest/wix-ecom) in addition to 
[Wix Pricing Plans](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/introduction). 


## Book a class session with in-person payment


Your app could display available sessions for a class to the customer, let 
them select their session of choice, create the related booking, and handle the 
in-person payment flow.

1. _Optional_: Call [Query Services](https://dev.wix.com/api/rest/wix-bookings/service-catalog/services/query-service-catalog) 
   to retrieve all relevant services and display them to the customer. Save the 
   ID of the service the customer wants to book.
1. Call [Query Availability](https://bo.wix.com/wix-docs/rest/bookings/availabilitycalendar---wip/query-availability). 
   Make sure to pass `serviceID` and the relevant `startDate` and `endDate` as 
   filters.
1. Display the retrieved sessions to the customer and let them select their 
   preferred option. Make sure to save the corresponding session ID.
1. Call [Create Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/create-booking) 
   and pass the `sessionId`. The status of the new booking is  `CREATED`.  This 
   call also automatically double checks the slot's availability by envoking 
   [Get Slot Availability](https://bo.wix.com/wix-docs/rest/bookings/availabilitycalendar---wip/get-slot-availability). 
   If the slot isn't available any longer, the Create Booking call fails with an error.
1. Call eCommerce's [Create Checkout](https://bo.wix.com/wix-docs/rest/ecommerce/checkout/create-checkout) 
   to start the payment flow in Wix eCommerce. Make sure to save the checkout ID.
1. Use the [Create Order from checkout](https://bo.wix.com/wix-docs/rest/ecommerce/checkout/create-order-from-checkout) endpoint
   to continue the payment flow.
1. Wix Bookings automatically listens to the relevant eCommerce webhooks and marks 
   a booking as `CONFIRMED` once the related eCommerce order is approved.
1. _Optional_: Allow the site owner to notify you in your app when the customer has 
   paid in person. Then you can call 
   [Mark Order as paid](https://bo.wix.com/wix-docs/rest/ecommerce/orders/mark-order-as-paid) 
   to update the payment status.
 

## Book an appointment with online payment


Your app could display available slots for an appointment service to the 
customer, let them select their slot of choice and create the related booking. 
Then, you could handle the online payment flow.

1. _Optional_: Call [Query Services](https://dev.wix.com/api/rest/wix-bookings/service-catalog/services/query-service-catalog) 
   to retrieve all relevant services and display them to the customer. Then, save the 
   ID of the service the customer wants to book.
1. Call [Query Availability](/docs/o.wix.com/wix-docs/rest/bookings/availabilitycalendar---wip/query-availability). 
   Make sure to pass the `serviceID` and the relevant `startDate` and `endDate` as 
   filters.   
1. Display the relevant slots to the customer and let them select their 
   preferred time. Save the corresponding session ID.
1. Call [Create Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/create-booking) 
   and pass the `sessionId`. The status of the new booking is  `CREATED`.  This 
   call also automatically checks the slot's availability by envoking 
   [Get Slot Availability](https://bo.wix.com/wix-docs/rest/bookings/availabilitycalendar---wip/get-slot-availability).
1. Call eCommerce's [Create Checkout](https://bo.wix.com/wix-docs/rest/ecommerce/checkout/create-checkout) 
   to start the online payment flow in Wix eCommerce. Make sure to save the checkout ID.
1. Use the [Create Order from checkout](https://bo.wix.com/wix-docs/rest/ecommerce/checkout/create-order-from-checkout) endpoint
   to continue the payment flow.
1. Let the customer pay for the service.    
1. Call eCommerce's [Add Payment](https://https://bo.wix.com/wix-docs/rest/ecommerce/order-payments/add-payments) 
   endpoint to update the information about the payment in Wix. The eCommerce 
   order is then marked as `APPROVED`.
1. Wix Bookings automatically listens to the relevant eCommerce webhooks and marks 
   the booking as `CONFIRMED` when the eCommerce order is approved.
 

## Manual confirmation flow


Your app could help site owner manage their bookings' approvals according to 
your custom logic. You can set up a service with manual confirmation, get 
notified when a customer books the service, and then confirm or decline the 
booking according to your custom logic. Currently, we recommend to use this 
flow only for services with in-person payments to avoid unneccessary refunds 
in case a session isn't available any longer by the time the customer has 
completed the online payment flow. 

1. Set up the service with the 
   [Create Service](https://dev.wix.com/api/rest/wix-bookings/services/service/create-service) endpoint. 
   In `paymentOptions`, make sure to set only `wixPayInPerson` to `true`. 
1. Sign up for the [Booking Created](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/booking-created) 
   webhook.
1. Listen to the Booking Created events and filter them by service ID.
1. When a booking for your service is created, call eCommerce's 
   [Create Checkout](https://bo.wix.com/wix-docs/rest/eCommercemerce/checkout/create-checkout) 
   endpoint to start the payment flow.
1. The booking's status is now `PENDING` and it appears in the business 
   calendar.
1. Implement your custom logic when to confirm the booking. For example, 
   confirm bookings whenever there are 3 or more bookings for a specific day. 
   This could help small business owner like make-up artists manage their 
   schedule more efficiently, so they work only on days when they have multiple 
   clients.
1. We recommercemmend to check the slot's or schedule's availability with the 
   [Availability Calendar APIs](https://bo.wix.com/wix-docs/rest/bookings/availabilitycalendar---wip) 
   just before confirming the booking.
1. Call [Confirm Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/confirm-booking) 
   to approve the relevant bookings. Note that this endpoint doesn't check the 
   availability.
1. _Optional_: Notify the customers of all `PENDING` bookings 48 hours before 
   the session's scheduled start to give them the option to 
   [reschedule](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/reschedule-booking) 
   or [decline](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/decline-booking) 
   their booking.


> __Notes__:
> - If you want to create a booking for a class, make sure to pass the
>   `sessionId` in [Create Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/create-booking).
> - If you want to skip availability checks, for example when creating a 
>   booking on behalf of the site owner, you can call the endpoint while 
>   passing the relevant `flowControlSettings` like 
>   `skipAvailabilityValidation=true`.
> - Passing other `flowControlSettings` lets you also override more limits such 
>   as the maximum number of particpants per session, the payment methods 
>   supported for a specific service. Note that you can't accept payments 
>   for a method that the site owner hasn't connected to their site at all.