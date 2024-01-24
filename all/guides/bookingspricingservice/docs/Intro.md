SortOrder: 0
# About the Wix Bookings Pricing API


With the Wix Bookings Pricing API, you can preview and calculate the 
price of a booking. 

+ The [`Preview Price`](https://dev.wix.com/api/rest/wix-bookings/pricing/preview-price) endpoint lets you retrieve information about how much a customer would have to pay for a booking's line items before the actual booking has been created.
+ The [`Calculate Price`](https://dev.wix.com/api/rest/wix-bookings/pricing/calculate-price) endpoint determines the base price of a booking.  

The price of the booking can be fixed, free, or varied. With [varied pricing](https://support.wix.com/en/article/wix-bookings-creating-a-course#step-2-set-the-price-and-payment-options-for-the-course), site owners can offer different prices for the same service based on their customers' choices. 
+ Site owners can set up basic varied pricing options in the site's dashboard. 
+ You can use the [Wix Bookings Service Options and Variants APIs](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants) to set up more robust pricing options. 
+ You can use the [Wix Bookings Pricing Integration SPI](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi) to implement your own custom pricing logic.


## Terminology

For a comprehensive glossary of Wix Bookings terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/terminology).


## Before you begin


+ You can only preview the price for line items belonging to the same 
  service.
+ If using the 
  [Wix Bookings Pricing Integration SPI](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi) to use your own 
  custom logic for varied pricing, the [Preview Price](https://dev.wix.com/api/rest/wix-bookings/pricing/preview-price) endpoint is not supported and an error is issued.
  