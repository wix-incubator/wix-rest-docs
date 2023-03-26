SortOrder: 2
# Best Practices

This article presents some best practices for designing your pricing app for integration with Wix.

## Recommended App Features

We recommend you do the following while implementing your app:

+ Make sure you are familiar with the [`booking`](https://dev.wix.com/api/rest/wix-bookings/bookings-v2/booking-object) object and its properties. When you receive this object from Wix, you can retrieve the values necessary for calculating the price. For example: 
  
  + To determine the sales tax based on the customer's address: `booking.contactDetails.fullAddress.subdivision`

  + To get additional information submitted on a booking form, such as a checkbox indicating if the customer is a student: `booking.additionalFields.id` and `booking.additionalFields.value`

  
+ Include feedback and notifications, some of which the site owner will pass along to the customer. This includes feedback to the customer about the pricing. For example, sending text message notifications about how long this price will be honored.

+ Specify clear terms and conditions. You want to make sure the site owner fills out all necessary legal and contractual agreements, and that you inform the site owner of your fees and payment terms.
