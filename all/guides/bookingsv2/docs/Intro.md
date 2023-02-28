SortOrder: 1
# About the Wix Bookings V2 API


With the Wix Bookings V2 API you can manage bookings for a site's services. 
The booking object holds information about the customer and the session or 
schedule they have booked. You can then use the 
eCommerce APIs (coming soon) to handle the checkout and payment flow.

The Wix Bookings V2 API allows your app to:

+ Create new bookings (coming soon)
+ Retrieve existing bookings
+ Manage the booking's life cycle


You can read more about:

+ The [Wix Bookings service catalog](https://dev.wix.com/api/rest/wix-bookings/service-catalog/introduction)
+ Using the [Wix Bookings waitlist](https://dev.wix.com/api/rest/wix-bookings/waitlist/introduction)
+ Customer payments using [Wix Pricing Plans](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/introduction)


## Terminology


+ __Booking__: Information about the service that the customer has booked. 
  Includes details about the time, location, participants, and payment.
+ __Booking Status__: Information about the booking's life cycle.
    + `CREATED`: The booking has been created, but doesn't yet appear in the 
      business calendar. 
      You need to create a booking before you can start the 
      checkout flow in eCommerce (coming soon).
    + `CONFIRMED`: The site owner has confirmed the booking and it appears in 
      the business calendar.
        + You can manually confirm a booking via the 
          [API](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/confirm-booking).
        + Bookings are automatically confirmed when the 
          [service](https://dev.wix.com/api/rest/wix-bookings/services/service/create-service) 
          is configured to do so and the eCommerce order (coming soon) 
          has been approved. An automatic confirmation includes checking the 
          slot's or schedule's availability.
    + `PENDING`: The booking is waiting to be confirmed or declined by the 
      owner and is displayed in the business calendar.
      You can't manually set bookings as `PENDING` via an API.
      Bookings are automatically set as `PENDING` when an eCommerce order related to the booking has been created (coming soon).
    + `WAITING_LIST`: The booking is pending on a waiting list.
      You must use the [Waitlist APIs](https://dev.wix.com/api/rest/wix-bookings/waitlist/introduction) 
      to create bookings in status `WAITING_LIST`. You can't change a booking's 
      status from `CREATED` to `WAITING_LIST` with the Bookings V2 APIs.
    + `DECLINED`: The booking has been declined by the site owner.
        + You can manually decline a booking with the 
          [Decline Booking endpoint](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/decline-booking).
        + Bookings are automatically declined when an eCommerce order has been 
          declined or a double booking happened for free bookings.
    + `CANCELED`: The booking has been canceled by the site owner or the customer.
        You can cancel bookings with the [API](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/cancel-booking).
+ __Double booked__:
  A double booking can happen in case of 2 or more simultaneous eCommerce checkout 
  processes or if the site owner manually accepts bookings that exceed the 
  service's capacity limit.
  + When a double booking happens for paying customers, the `doubleBooked` 
    boolean is set to `true` for the second booking and the owner is notified. 
    They must then manually resolve the situation.
  + When a double booking happens for free services, the second 
    booking's status is set to `DECLINED` while the first booking is retained.
+ __Service__: Business offering. For example, a fitness studio may offer a 
  1-hour yoga class, a 45 minute HIIT training session, and a 30 minute 1-on-1 
  personal training. Learn more about [services](https://dev.wix.com/api/rest/wix-bookings/services/introduction).
+ __Variant__: Unique variation of the service. Each service variant may have 
  a different price. Read more about 
  [service variants](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants/introduction).
+ __Availability__: Free time on a schedule that customers can book. 
  You can read more about 
  [Query Availability](https://bo.wix.com/wix-docs/rest/bookings/availabilitycalendar---wip/introduction).
  The Create Booking (coming soon) and
  [Reschedule Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/reschedule-booking) 
  endpoints check if a slot or schedule is available, unless you pass
  `skipAvailabilityValidation` in the body of the request.
  [Confirm Booking](https://bo.wix.com/wix-docs/rest/bookings/bookingsgateway-v2---wip/confirm-booking) 
  doesn't check availability. Instead, the availability is checked during the 
  eCommerce payment flow (coming soon).
+ __Schedule__: Entity that holds availability information. A 
  [schedule](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/introduction) can 
  either belong to a resource (for example, a staff member) or a service. 
  When creating a booking (coming soon)
  for a course, you need to pass the service's schedule in the body of the 
  request.
+ __Session__: An occupied period of time on a schedule. When 
  creating a booking (coming soon) 
  for a class you need to pass the service's relevant existing session as 
  `slot` in the body of the request.
+ __Slot__: An available period of time in a schedule that can be booked by a 
  customer. When 
  creating a booking (coming soon) 
  for an appointment you need to pass the relevant slot in the body of the request.
+ __Deposit__: Amount the customer must pay immediately when checking out the 
  booking.
+ __Visitor__: Anyone who isn't registered as a member or hasn't logged in to 
  the Wix site. If a visitor creates a booking they're added as a contact.
+ __Member__: Someone who is a registered member in the Wix site and has a 
  login.
+ __[Wix Pricing Plans](https://support.wix.com/en/article/about-pricing-plans)__: 
  A pre-paid bundle of services or a membership that provides access to certain
  services.


## Before you begin

+ The `participantNotification` field holds only information about the last 
  message sent to the customer. It also doesn't include details which type of 
  message has been sent.