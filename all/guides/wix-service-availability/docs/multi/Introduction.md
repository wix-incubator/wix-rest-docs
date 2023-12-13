SortOrder: 1
# About the Wix Bookings Multi Service Availability Time Slots API

[//]: # (TODO: Fix links)

With the Wix Bookings Multi Service Availability Time Slots API, you can retrieve information about the
availability of multiple sequenced slots for multiple [Services](https://bo.wix.com/wix-docs/rest/bookings/bookings---services-v2/service-object) in your business calendar,
within a given range of time, by:

+ [Listing](https://bo.wix.com/wix-docs/rest/all-apis/wix-service-availability/multi-service-availability-time-slots/list-multi-service-availability-time-slots)
  all availability entries for a given list of services within a given range of time.

+  [Getting](https://bo.wix.com/wix-docs/rest/all-apis/wix-service-availability/multi-service-availability-time-slots/get-multi-service-availability-time-slot)
   the availability of a multiple specific sequenced calendar's time slots for the given sequence of services, in specific time and location.

The Multi Service Availability Time Slots APIs calculates the availability of multiService slots only for services
of type `Appointment`.

## About the `TimeSlot` object
The [`TimeSlot`](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/multi-service-availability-time-slots/time-slot-object) object 
represents the availability information of a given list of services in a specific location within a given range of time, including:

1. Whether the slot is bookable for the given list of services?
2. In what location all services are available for this slot?
3. Which available resources can provide each service?
4. Does booking the slot for the services violates any of the service's booking policies?
   If one of the nested time slots violates any of it's service's booking policies, the entire
   `TimeSlot` is returned as un-bookable.

Each `TimeSlot`.`NestedTimeSlot` represents a single service from the given list. The order of the `NestedTimeSlots` is the same as the order
of the given services in request.

The first `NestedTimeSlot` has `localStartDate` within the given `fromLocalDate` and `toLocalDate` - exclusive,
and each following `NestedTimeSlot` has a `localStartDate` that equals to the previous `NestedTimeSlot`'s `localEndDate`.

For example, for a business with 3 services:
+ `Full Body Massage` with duration of `45` minutes and ID `09012d6c-3a33-4c9f-9f67-8c1573d74b3e`.
+ `Facial Massage` with duration of `30` minutes and ID `f25a2c1d-cbc2-4d3f-883f-4a8c2d0a468b`.
+ `Sauna Room` with duration of 15 minutes and ID `3ae0a5a7-5059-4b79-9a6e-2d8b1d36b74e`.
A customer may choose to book a `Full Body Massage` followed by a `Facial Massage`, on `2024-10-01` between `10:00` and `12:00`.
In this case, an example for a possible returned `TimeSlot`'s `NestedTimeSlot`'s is:
```json
  {
  "nestedTimeSlots": [
    {
      "serviceId": "09012d6c-3a33-4c9f-9f67-8c1573d74b3e",
      "localStartDate": "2024-10-01T11:15:00.000",
      "localEndDate": "2024-10-01T12:00:00.000"
    },
    {
      "serviceId": "f25a2c1d-cbc2-4d3f-883f-4a8c2d0a468b",
      "localStartDate": "2024-10-01T12:00:00.000",
      "localEndDate": "2024-10-01T12:30:00.000"
    }
  ]
}
```

## More about the Wix Multi Service Availability Time Slots API

##### Availability calculations:
Availability is the existence of slots for a given service or resource within a given range of time.
The availability calculation for a given service within a range of time, is based on:
+ The service configurations, such as: service duration and the buffer time required between sessions.
+ The times in which the service is being provided. For `Appointment`, derived from working hours of the resources providing the service.
+ The availability of the required resources in order to provide the service.
A multiService `TimeSlot` is available if forall its `NestedTimeSlot`, the `NestedTimeSlot`.`serviceId` is available at between
`NestedTimeSlot`.`localStartDate` and `NestedTimeSlot`.`localEndDate`

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

A multiService `TimeSlot` is `bookable` if forall its `NestedTimeSlot`, booking the `NestedTimeSlot`.`serviceId` at
`NestedTimeSlot`.`localStartDate` does not violate any of the service's booking policies.

##### Daylight Saving Time (DST) Handling:
*Handling Daylight Savings Time (DST) for local time zones:*

Because of DST, there are cases where certain times either do not exist
or exist twice for a local time zone.

For example, the time `00:05` on September 5th 2021 might not exist in Santiago, Chile,
because at `00:00` the clock moved 1 hour forward to `01:00`.

In this case, the Service Availability Time Slots API take this into account and mediate the time gaps automatically.

The non-existent local time is automatically moved forward 1 hour to match local DST.
Local times that exist do not change.


## Use cases
*The Wix Service Availability Time Slots API is mainly used within a `book flow`*

Common business usages for this API include:

+ Allow your customers book multiple services without waiting in between sessions.
+ Show your customers all the possible multiService `TimeSlot`'s for booking the list of services.
+ Retrieve all resources which are available to provide the services within a specific time slot.
+ Retrieve the availability for a specific multiService `TimeSlot` before booking the slot.

## Terminology
For a comprehensive glossary of Wix Bookings terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/terminology).
For a comprehensive glossary of Wix Bookings Services terms, see [Terminology](https://dev.wix.com/docs/rest/api-reference/wix-bookings/services/services-v2/introduction#terminology).
For a comprehensive glossary of Wix Bookings Availability Time Slots Configuration SPI terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/availability-time-slots-configuration-spi/introduction#terminology).
For a comprehensive glossary of Wix Bookings Multi Service Booking Policy SPI terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/multi-service-booking-policy-spi/introduction#terminology).

+ __MultiServiceBooking__:
  Information about a service's available time slot that was ordered by a customer
  (but not necessarily paid for) for a specific time and location.

+ __Service__: A service is an online or in-person offering that a business provides to its customers, such as classes and private sessions. For
  example, a fitness studio may offer a 1-hour , a 45 minute HIIT training session, and a 30 minute 1-on-1
  personal training.

  + __Appointment__: An appointments is a 1-time session that can be booked by a customer.
    The appointment takes place whenever a customer books a specific time slot. For example,
    your hair salon may be open for business from 9:00 AM to 7:00 PM and a customer can book a session at any available time during the day.

  + __Resource__: A business asset like a staff member, room, or equipment that's
    needed to provide a service.
    + __Resource Type__: A classification of resources. For example, `StaffMember` or `Room`.

  + __Booking Policy__: Booking policies define a set of rules on how customers can book a service provided by the business.
    For example, how far in advance customers
    may book a service or until what point before the start of a session
    customers can cancel.

  + __Service Availability Configuration__: A set of service rules to consider during the availability calculation of
    time slots, such as:
    + Service duration.
    + Split interval and buffer time.
    + Service locations.
    + Required resource types and the potential resources available.

+ __Calendar__: General overview about the availability and bookings of a business, including its services and resources.

  + __Time Slot__: An _available_, unnecessarily __bookable__ period of time in the business calendar that can be booked by a
    customer. For `Appointment` services the availability of a time slot within a specific period of time is determined based on
    the service's configuration and the availability of the required resources. For example, a barber with appointments of 30
    minutes each that are open for booking every weekday between 8:00 - 17:00.

  + __Session__: An _occupied_ period of time in a calendar.


## Before you begin

Before using the API, make sure to set up [Wix Bookings](https://support.wix.com/en/article/wix-bookings-about-wix-bookings) and [create the right services for your business](https://support.wix.com/en/article/creating-the-right-booking-service-for-your-business).
Before using the API, make sure to read about [Wix Multi Service Bookings](https://support.wix.com/en/article/wix-bookings-about-wix-multi-service-bookings)

Before using the API, explore its extended optional capabilities.
+ The `The Service Availability Time Slots` API allows you to add multiple customized availability calculations for each service, by:
  + Customizing the service availability configuration.
    In order to do so, you should become a provider of the [Wix Bookings Availability Time Slots Configuration SPI](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/availability-time-slots-configuration-spi/introduction)
  + Customizing the service's booking policies.
    In order to do so, you should become a provider of the [Wix Bookings Multi Service Booking Policy SPI](https://dev.wix.com/api/rest/wix-bookings/multi-service-booking-policy-spi)

+ There is a parallel, less complex API which calculates the availability of time slots for a single service.
  You can learn more about the [Wix Service Availability Time Slots]() API.
  > __Note:__
  > The `TimeSlot` object is shared for both `ServiceAvailabilityTimeSlots` API and `MultiServiceAvailabilityTimeSlots` API.
  > You can consider only the specific `MultiServiceAvailabilityTimeSlots` fields which are marked in the [`TimeSlot`](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/availability-time-slots/time-slot-object)
  > object description.