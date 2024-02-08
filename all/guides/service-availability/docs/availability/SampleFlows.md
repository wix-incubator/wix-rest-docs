SortOrder: 1
[//]: # (TODO: create an article for `book-an-appointment` which uses the new API & fix the link)
[//]: # (TODO: fix idention)
[//]: # (TODO: fix code snippets)
# Service Availability Time Slots API: Sample Use Cases and Flows

This article shares some possible use cases your app could support, as well as a sample flow that could support each use case.
This can be a helpful jumping off point as you plan your app's implementation.

## Let your customers to dynamically select an available time slot for any of your business services

Your app can show to your customers available time slots for a service, in order to let
them browse over the available time slots to book, and select their time slot of choice.

This flow is usually followed by the `book flow` in which a booking is being created for the selected time slot,
and confirmed if the customer met all the checkout and payment requirements.
In this case, make sure you save the customer's selected time slot in order to use the selected time slot within the `book flow` later.
You can see an example for the full [Wix Bookings Book an Appointment Flow](https://dev.wix.com/docs/rest/api-reference/wix-bookings/time-slots-and-bookings/bookings-v2/bookings-v2-and-confirmation/sample-booking-flows#book-an-appointment)
    
> __Note:__: For availability validation during the `book flow`, you should
> call `GetAvailabilityTimeSlot` with the propagated properties of the customer's selected time slot.

__1. Let your customers choose a service out of the services your business offer__
    Call [Query Services](https://dev.wix.com/docs/rest/api-reference/wix-bookings/services/services-v2/query-services)
    in order to retrieve all relevant services and showing your customers the list of services your business offers. 
    Then, let your customers select a service of their choice and save the ID of the service they selected to book.

<blockquote class="important">
    <p><strong>Important:</strong><br/>
    The `Service Availability Time Slots` API is currently supported only for services of type `Appointment`.
    If your business offering services of type `Course` or `Class`,
    add the following filter to your query:
        '''?type=APPOINTMENT''''
</p>
</blockquote>

__2. Let your customers select an available time slot from the first available date the service is available for__
   To show your customers a monthly calendar with all days in which the service has at least one available time slot for booking,
   starting from the first date the service is available for.

   + ##### Find the first date within the next 3 months that the selected service is available for
       Call [List Availability Time Slots](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/availability-time-slots/list-availability-time-slots)
       make sure to pass in request:

           ?serviceId=<selected-service-id-from-step-1>&
           fromLocalDate=<nowAsLocalDateTime>&
           toLocalDate=<nowAsLocalDateTime.plusMonths(3).dayOfTheMonth.withMaximumValue.setHours(23, 59, 0, 0)>&
           timeSlotsPerDays=1&
           bookable=true&
           cursorPaging.limit=100

     The first `TimeSlot` in response is the first available within the given range of time.

   + ##### Show your customers all available days from the first available date until the end of the month
     Show results for the whole month of the first available date.

__3. Let your customers browse over days in future months__
    You can allow your customer to browse over future months by sequentially calling [List Availability Time Slots](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/availability-time-slots/list-availability-time-slots)
    with the previous call returned `cursor`,
    in case there is no next page of results for the current request,
    make a new similar call as in step-2 with `fromLocalDate` equals to `toLocalDate` of the previous request.
    
Then, let your customers select an available day and save the specific day they selected to book.

__4. Let your customer select a specific time slot out of all available time slots within the specific day they selected to book__
    Call [List Availability Time Slots](https://dev.wix.com/docs/rest/api-reference/wix-bookings/wix-service-availability/availability-time-slots/list-availability-time-slots)
    make sure to pass in request:
    + the selected service ID from step-1 as `serviceId`
    + {selected-day-from-step-3}.setHours(00, 00, 0, 0) as `fromLocalDate`
    + {selected-day-from-step-3}.setHours(23, 59, 0, 0) as `toLocalDate`

      ?serviceId=<selected service ID from step-1>&
      fromLocalDate=<{selected-day-from-step-3}.setHours(00, 00, 0, 0)>&
      toLocalDate=<{selected-day-from-step-3}.setHours(23, 59, 0, 0)>&
      bookable=true
Then, let your customers select an available time slot of their choice and save the specific time slot they selected to book.

## Retrieve the availability for a service within a specific time slot during the `booking flow`
It is highly recommended to validate the selected time slot is still available and bookable during the `booking flow`, for example
before calling [createBooking](https://dev.wix.com/docs/rest/api-reference/wix-bookings/time-slots-and-bookings/bookings-v2/bookings-v2-and-confirmation/bookings-create-booking)
or before checkout and payment.

Call [Get Availability Time Slot](https://bo.wix.com/wix-docs/rest/all-apis/wix-service-availability/availability-time-slots/get-availability-time-slot)
with request parameters propagated from the selected `TimeSlot` entity.


## Add multiple custom availability calculations for the same service
The `The Service Availability Time Slots` API allows you to add multiple customized availability calculations for each service, by:
+ Customizing the service availability configuration.
  In order to do so, you should become a provider of the [Wix Bookings Availability Time Slots Configuration SPI](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/availability-time-slots-configuration-spi/introduction)
  Go over the `Wix Bookings Availability Time Slots Configuration` SPI [sample flows](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/availability-time-slots-configuration-spi/sample-flows)

+ Customizing the service's booking policies.
  In order to do so, you should become a provider of the [Wix Bookings Booking Policy SPI](https://dev.wix.com/api/rest/wix-bookings/booking-policy-spi)
  Go over the `Wix Bookings Booking Policy` SPI [sample flows](https://bo.wix.com/wix-docs/rest/drafts/service-availability-spis/booking-policy-spi/sample-flows)