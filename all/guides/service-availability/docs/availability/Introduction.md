SortOrder: 0
# About the Wix Bookings Availability Time Slots API

[//]: # (TODO: Fix links)

With the Wix Bookings Availability Time Slots API, you can retrieve information about the
availability of a calendar's slots for a [Service](https://bo.wix.com/wix-docs/rest/bookings/bookings---services-v2/service-object) 
within a given range of time, by:

+ [Listing](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/availability-time-slots/list-availability-time-slots)
  all availability entries for a given service within a given range of time.
+  [Getting](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/availability-time-slots/get-availability-time-slot)
   the availability of a specific calendar's slot for a given service, in specific time and location.

The Availability Time Slots APIs calculates the availability of slots only for services
of type `APPOINTMENT`.

## About the `TimeSlot` object
The [TimeSlot](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/availability-time-slots/time-slot-object) object represents the availability information
for an `APPOINTMENT` service's specific slot, including:

1. Whether the slot is bookable for the given service?
2. In what location the service is available for this slot?
3. Which available resources can provide the service for this slot?
4. Does booking the slot for the service violates any of the service's booking policies?
5. What is the total capacity and remaining capacity of the service at the time of the calculation of the `TimeSlot`?

## More about the Wix Bookings Availability Time Slots API

##### Availability calculation
Availability is the existence of slots for a given service or resource within a given range of time. 
The availability calculation for a given service within a range of time, is based on:
+ The service configurations, such as: service duration and the buffer time required between sessions of the service.
+ The times in which the service is being provided. For `APPOINTMENT` services, derived from working hours of the resources providing the service.
+ The availability of the required resources in order to provide the service.

##### Availability VS Bookability:
An available time slot is not necessarily bookable.

Bookability indicates whether a specific slot can be booked within a specific period of time.
An __available__ slot for a service, is a slot which has all required resources available for the time slot.
A __bookable__ slot for a service, is an __available__ slot, which does not violate any
of the service's booking policies.

For example,
if a service has a booking policy which enforces booking the service up to 10 minutes before the session starts,
a slot that starts at `12:30` can not be booked later than `12:19`, 
even though all required resources are available to provide the service at that time.

##### Daylight Saving Time (DST) Handling:
  Because of DST, there are cases where certain times either do not exist
  or exist twice for a local time zone.

  For example, the time `00:05` on September 5th 2021 might not exist in Santiago, Chile,
  because at `00:00` the clock moved 1 hour forward to `01:00`.

  In this case, the Availability Time Slots API take this into account and mediate the time gaps automatically.
  The non-existent local time is automatically moved forward 1 hour to match local DST.
  Local times that exist do not change.


## Use cases

Common business usages for this API include:

+ Show your customers all days in a service's monthly calendar with at least one available time for booking.
+ Show your customers all of available, bookable slots for a [Service](https://bo.wix.com/wix-docs/rest/bookings/bookings---services-v2/service-object).
+ Retrieve all resources which are available to provide the service within a specific time slot.
+ Retrieve the availability for a specific time slot before booking the slot.

## Terminology
For a comprehensive glossary of Wix Bookings terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/terminology).
For a comprehensive glossary of Wix Bookings Services terms, see [Terminology](https://dev.wix.com/docs/rest/api-reference/wix-bookings/services/services-v2/introduction#terminology).
For a comprehensive glossary of Wix Bookings Availability Time Slots Configuration SPI terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/availability-time-slots-configuration-spi/introduction#terminology).
For a comprehensive glossary of Wix Bookings Booking Policy SPI terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/booking-policy-spi/introduction#terminology).

+ __Booking__: 
  Information about a service's available time slot that was ordered by a customer
  (but not necessarily paid for) for a specific time and location.

+ __Service__: A service is an online or in-person offering that a business provides to its customers, such as classes and private sessions. For
  example, a fitness studio may offer a 1-hour , a 45 minute HIIT training session, and a 30 minute 1-on-1
  personal training.

  + __Appointment__: An appointments is a 1-time session that can be booked by a customer. The appointment takes place whenever a customer books a specific time slot. For example, your hair salon may be open for business from 9:00 AM to 7:00 PM and a customer can book a session at any available time during the day.

  + __Booking Policy__: Booking policies define a set of rules on how customers can book a service provided by the business.
    For example, how far in advance customers
    may book a service or until what point before the start of a session
    customers can cancel.

  + __Service Availability Configuration__: A set of service rules to consider during the availability calculation of time slots, such as:
    + Service duration.
    + Split interval and buffer time.
    + Service locations.
    + Required resource types and the potential resources available.

  + __Resource__: A business asset like a staff member, room, or equipment that's
    needed to provide a service.
    + __Resource Type__: 
      A classification of resources. For example, `StaffMember` or `Room`.


+ __Calendar__: General overview about the availability and bookings of a business, including its services and resources.

  + __Time Slot__: An _available_, unnecessarily __bookable__ period of time in the business calendar that can be booked by a
    customer. For `APPOINTMENT` services the availability of a time slot within a specific period of time is determined based on
    the service's configuration and the availability of the required resources. For example, a barber with appointments of 30
    minutes each that are open for booking every weekday between 8:00 - 17:00.

  + __Session__: An _occupied_ period of time in a calendar.


## Before you begin

Before using the API, make sure to set up [Wix Bookings](https://support.wix.com/en/article/wix-bookings-about-wix-bookings) and [create the right services for your business](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business).

Before using the API, explore its extended optional capabilities.
The `Wix Bookings Availability Time Slots` API allows you to add multiple customized availability calculations for each service, by:
+ Customizing the service availability configuration. 
  In order to do so, you should become a provider of the [Wix Bookings Availability Time Slots Configuration SPI](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/availability-time-slots-configuration-spi/introduction)
+ Customizing the service's booking policies. 
  In order to do so, you should become a provider of the [Wix Bookings Booking Policy SPI](https://dev.wix.com/api/rest/wix-bookings/booking-policy-spi)

### Coming soon!
A parallel, more advanced API which retrieves the availability of sequenced time slots for a list of services.
This allows you offering your customers to book multiple services, without waiting time in between the different services sessions.
You can learn more about the [Wix Bookings Multi Service Availability Time Slots](https://bo.wix.com/wix-docs/rest/all-apis/wix-service-availability/multi-service-availability-time-slots/introduction) API,
and [MultiServiceBookings](TODO: add link) API.
  > __Note:__
  > The `TimeSlot` object is shared for both `Availability Time Slots` API and `Multi Service Availability Time Slots` API.
  > You can ignore the specific `Multi Service Availability Time Slots` fields which are marked in the [TimeSlot](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/availability-time-slots/time-slot-object)
  > object description.