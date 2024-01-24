SortOrder: 0
# About the Wix Bookings Reader V2 API


With the Wix Bookings Reader V2 API you can retrieve bookings for a site's 
services.  
The [booking object](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/booking-object) holds information about the customer and the session or schedule they have booked. 

For more information about the terminology, use cases and related APIs read 
[introduction to the Wix Bookings V2 API](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/introduction).

You can then use the 
[Wix Bookings V2 APIs](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/introduction)
to manage the booking life cycle and the 
Ecommerce APIs (coming soon) 
to handle the checkout and payment flow.


## Before you begin


+ `fields` and `fieldsets` aren't supported in the `query` object.
+ Bookings for courses don't include a `sessionId`. To filter these bookings 
  by session ID, you must pass `sessionId` on the root level of the request 
  body, and can't use the filter that's part of the `query` object.
+ The `participantNotification` field holds only information about the last 
  message sent to the customer. It also doesn't include details which type of 
  message has been sent. 