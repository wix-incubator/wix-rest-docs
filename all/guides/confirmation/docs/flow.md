SortOrder: 1

# How Bookings Are Confirmed or Declined

The following flow presents how `Confirm Or Decline Booking` determines the booking status.    

![flow](https://s3.amazonaws.com/wixplorer-readme-images/confirmation%2Fconfirmator_flow.png)

Calling a checkout after creating a booking, is optional, `Confirm or Decline Booking` can be called after `Create Booking`

+ **Whether the availability check is required** If  `skipAvailability` is `true`, it will skip the check and it will never be a `doubleBooking`.
+ **Whether the booking is paid for**.If the payment status is `PAID` or `PARTIALLY_PAID`, the booking is confirmed regardless of the `doubleBooking` parameter.    
+ **Wether the booking requires business confirmation**. Instead of `CONFIRMED` the status is set to `PENDING`. This happens since it needs to always be manually approved by the owner. You can bypass the confirmation check by setting the `skipBusinessConfirmation` property to `true` when [creating a booking](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/create-booking).   


