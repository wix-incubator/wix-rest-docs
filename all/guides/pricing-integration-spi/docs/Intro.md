SortOrder: 0
# About the Wix Bookings Pricing Integration SPI

As a bookings pricing service provider, you can integrate your pricing service with Wix to allow a merchant to apply more sophisticated varied pricing options for their bookings on their Wix sites. This allows site owners to offer different prices for the same service.

The integration is done via an app you create in the Wix App Market (created in the [Wix Developer Center](https://dev.wix.com/)) and Wix Bookings Pricing Integration SPIs:

+ The [Wix Developer Center](https://dev.wix.com/) is an environment used to set up new service providers and focus on app integrations.

+ Using the SPIs, you can design your app to provide custom pricing calculations for your merchant's bookings. The custom pricing logic can be based on, for example: 

    + Taxes for a particular region.
    + Discounts based on who is signing up for the booking, such as student, soldier, senior citizen, special needs, financial assistance, and so on.
    + A combination of the above, and more!

Complete the following steps to adapt Wix system's integration to make your pricing methods available to merchants and their customers.


## Ways to set up pricing for bookings

There are various ways to set up pricing for bookings. The SPIs are the way to go for
flexibility and granularity of how bookings prices are calculated.

+ Using the [Wix Bookings Pricing API](https://dev.wix.com/api/rest/wix-bookings/pricing/introduction), you can retrieve the standard prices and/or set up basic varied pricing using the
  Wix Bookings app on the site.

+ For more robust varied pricing, the site owner can offer different prices for the same
  service using [service options and variants APIs](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants/introduction). 

+ To set up your own custom logic for robust varied pricing, you can use
  [Wix Bookings Pricing Integration SPI](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi) without having to set up service variants. With the Wix Bookings Pricing Integration SPI, your app can calculate the price of a booking based on your own custom logic.  



## Terminology

For a comprehensive glossary of Wix Bookings terms, see [Terminology](https://dev.wix.com/api/rest/wix-bookings/terminology).


## Before you begin

It's important to note the following points before starting to code your integration:

+ When Wix calls your implementation of the [Calculate Price](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi/calculate-price) SPI endpoint, the app must return either a calculated price (number) or a price description (text). Returning the calculated price enables the Wix site owner to perform additional calculations based on your pricing. 

+ After a Wix site owner installs your app, the Bookings Pricing [Preview Price](https://dev.wix.com/api/rest/wix-bookings/pricing/preview-price) API endpoint succeeds only if your app returns the price description. If your app returns a calculated price, calling Preview Price fails and an error is thrown.

+ The [Calculate Price](https://dev.wix.com/api/rest/wix-bookings/pricing-integration-spi/calculate-price) SPI endpoint can only be called after a booking has been created and a `booking` object already exists. You cannot use this SPI in advance, for example, to display a price list for various options.

## Prerequisites

1. Create an [app](https://dev.wix.com/dc3/my-apps/) and retrieve its app ID either from the URL or as displayed in the My Apps dashboard in the [Wix Developer Center](https://dev.wix.com/). 
    
    ![Sample App ID](https://s3.amazonaws.com/wixplorer-readme-images/pricing-integration-spi%2Fappid.png "Sample App ID")
    

## Signing up to the integration

Send an email to this email address: `bookings-provider-integration@wix.com` to request sign-up. Enter "Bookings Pricing Integration" as the subject, and provide the following details: 

- Type of business (gym, spa, ...)
- A few words about your business and the market you serve (for example, continuing
  education for senior citizens, online sessions, and so on)
- The URL of the site hosting your app 
- The ID of the app you created

Your sign-up request will be reviewed and you will be notified by return email.