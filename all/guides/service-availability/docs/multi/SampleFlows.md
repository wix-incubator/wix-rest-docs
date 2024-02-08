SortOrder: 3
[//]: # (TODO: create an article for `book-a-multi-service-booking` which uses the new API & fix the link)
[//]: # (TODO: fix idention)
[//]: # (TODO: fix code snippets)
# Multi Service Availability Time Slots API: Sample Use Cases and Flows

This article shares some possible use cases your app could support, as well as a sample flow that could support each use case.
This can be a helpful jumping off point as you plan your app's implementation.

## Let your customers to dynamically select an available time slot for multiple services of your business

Your app can show to your customers available time slots for booking a sequence of __up__ to 8 services, in order to let
them browse over the available time slots to book, and select their time slot of choice.

This flow is usually followed by the `multiService book flow` in which a [MultiServiceBooking]() is being created for the selected multiService time slot,
and confirmed if the customer met all the checkout and payment requirements.
In this case, make sure you save the customer's selected multiService time slot in order to use the selected multiService time slot within the `multiService book flow` later.
You can see an example for the full [Wix Bookings Book Multiple Appointment Services Flow]()

> __Note:__: For availability validation during the `multiService book flow`, you should
> call `GetMultiServiceAvailabilityTimeSlot` with the propagated properties of the customer's selected multiService time slot.

__1. Let your customers choose up to 8 services out of the services your business offer__
Call [Query Services](https://dev.wix.com/docs/rest/api-reference/wix-bookings/services/services-v2/query-services)
in order to retrieve all relevant services and showing your customers the list of services per location your business offers.
Then, let your customers select a location and services of their choice 
and save the location and ID's of the services they selected to book.

<blockquote class="important">
    <p><strong>Important:</strong><br/>
    The `Service Availability Time Slots` API is currently supported only for services of type `Appointment`.
    If your business offering services of type `Course` or `Class`,
    add the following filter to your query:
        '''?type=APPOINTMENT''''
</p>
</blockquote>

__2. Let your customers select an available multiService time slot from the first available date all services are available for__
To show your customers a monthly calendar with all days in which there is at least one available multiService time slot for booking,
starting from the first date all services are available for.

+ ##### Find the first date within the next 3 months that all selected services are available for.
  Call [List Multi Service Availability Time Slots](https://bo.wix.com/wix-docs/rest/all-apis/wix-service-availability/multi-service-availability-time-slots/list-multi-service-availability-time-slots)
  make sure to pass in request:

        ?services=<services-with-selected-service-ids-from-step-1>&
        fromLocalDate=<nowAsLocalDateTime>&
        toLocalDate=<nowAsLocalDateTime.plusMonths(3).dayOfTheMonth.withMaximumValue.setHours(23, 59, 0, 0)>&
        location=<selected-location-from-step-1>&
        timeSlotsPerDays=1&
        bookable=true&
        cursorPaging.limit=100

  The first `TimeSlot` in response is the first available within the given range of time.

+ ##### Show your customer all available days from the first available date until the end of the month
  Show results for the whole month of the first available date.

__3. Let your customers browse over days in future months__
You can allow your customer to browse over future months by sequentially calling [List Multi Service Availability Time Slots](https://bo.wix.com/wix-docs/rest/all-apis/wix-service-availability/multi-service-availability-time-slots/list-multi-service-availability-time-slots)
with the previous call returned `cursor`,
in case there is no next page of results for the current request,
make a new similar call as in step-2 with `fromLocalDate` equals to `toLocalDate` of the previous request.

Then, let your customers select an available day and save the specific day they selected to book.

__4. Let your customers select a specific time slot out of all available time slots within the specific day they selected to book__
Call [List Multi Service Availability Time Slots](https://bo.wix.com/wix-docs/rest/all-apis/wix-service-availability/multi-service-availability-time-slots/list-multi-service-availability-time-slots)
make sure to pass in request:
+ the selected service ID from step-1 as `serviceId`
+ {selected-day-from-step-3}.setHours(00, 00, 0, 0) as `fromLocalDate`
+ {selected-day-from-step-3}.setHours(23, 59, 0, 0) as `toLocalDate`

      ?serviceId=<selected service ID from step-1>&
      fromLocalDate=<{selected-day-from-step-3}.setHours(00, 00, 0, 0)>&
      toLocalDate=<{selected-day-from-step-3}.setHours(23, 59, 0, 0)>&
      bookable=true
Then, let your customers select an available time slot of their choice and save the specific time slot they selected to book.

## Retrieve the availability for a service within a specific time slot during the `multiService booking flow`
It is highly recommended to validate the selected time slot is still available and bookable during the `multiService booking flow`, for example
before calling [createMultiServiceBooking]()
or before checkout and payment.

Call [Get Multi Service Availability Time Slot](https://bo.wix.com/wix-docs/rest/all-apis/wix-service-availability/multi-service-availability-time-slots/get-multi-service-availability-time-slot)
with request parameters propagated from the selected `TimeSlot` entity.


## Add multiple custom availability calculations for the same service
The `The Wix Multi Service Availability Time Slots` API allows you to add multiple customized availability calculations for each service, by:
+ Customizing the service availability configuration.
  In order to do so, you should become a provider of the [Wix Bookings Availability Time Slots Configuration SPI](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/availability-time-slots-configuration-spi/introduction)
  Go over the `Wix Bookings Availability Time Slots Configuration` SPI [sample flows](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/availability-time-slots-configuration-spi/sample-flows)

+ Customizing the service's booking policies.
  In order to do so, you should become a provider of the [Wix Bookings Multi Service Booking Policy SPI](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/multi-service-booking-policy-spi/introduction)
  Go over the `Wix Bookings Multi Service Booking Policy SPI` SPI [sample flows](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/multi-service-booking-policy-spi/sample-flows#drafts_service-availability-spis_multi-service-booking-policy-spi_sample-flows_sample-flows)