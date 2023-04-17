SortOrder: 0
# About the Wix Bookings Service Options and Variants API


With the Wix Bookings Service Options and Variants API, you can manage custom options 
and variants for services. This allows site owners to offer different prices for the 
same service based on their customers' choices. 


You can read more about using the:
+ [Wix Bookings Pricing API](https://dev.wix.com/api/rest/wix-bookings/pricing/introduction) to preview and calculate the price.
+ [Wix Bookings Pricing Provider SPI](https://dev.wix.com/spi/rest/wix-bookings/pricing-integration-spi/introduction) that allows site owners to implement custom pricing logic.


## Checking for Existing Pricing Options 

You can check whether a service has existing pricing options, and what they are, by retrieving the
`rate` object of the service's active schedule. Check [this flow](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants/sample-flows#create-staff-member-based-service-variants) for more details. 

There are 3 different possible rates:

   + `labeledPriceOptions`: For services with the standard Wix Bookings pricing.
   + `priceText`: For services with prices manually set by the business.
   + `defaultPrice`: For services with [varied pricing](https://dev.wix.com/api/rest/wix-bookings/pricing/introduction).

If any of theses 3 rates are defined in the service's active schedule, pricing options have already been defined.


## Terminology

For a comprehensive glossary of Wix Bookings terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/terminology).


## Before You Begin

It's important to note the following points before starting to code:

+ Only a single [`serviceOptionsAndVariants`](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants/service-options-and-variants-object) object is supported per service.

+ Currently, only a single option is supported per `serviceOptionsAndVariants` object.

+ You need to manually calculate and then pass all variants in the request of 
  [Create Service Options And Variants](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants/create-service-options-and-variants). 
  Variants aren't automatically calculated from the specified options.

+ New variants are automatically created for services with staff member-based 
  options whenever a new staff member is added to the service. The new 
  variant gets the default price specified in the service's
  `schedule.rate.default_varied_price`.

+ Variants are automatically deleted for services with staff member based 
  options whenever a staff member is removed from the service or the 
  business.
