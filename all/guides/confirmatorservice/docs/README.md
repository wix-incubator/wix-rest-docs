SortOrder: 0
# Introduction
With Bookings Confirmator service you can handle checkout completion with a logic to prevent double bookings.  
After checkout is complete, call `confirmOrDeclineBooking` to apply the checkout to the booking.  
In most cases the booking status will be set to `CONFIRMED`, and the booking will be visible in the calendar.  
In some cases, the booking might be declined, for example if it will cause over-booking.  
See `ConfirmOrDeclineBooking` endpoint docs for more details.