SortOrder: 0
# About the Restaurants Point of Sale (POS) SPI

As a POS service provider, you can integrate your point of sale service with Wix to allow merchant's restaurants to synchronize menus with yours and to create orders that originate from their Wix sites. 

The integration is done via an app in the Wix App Market (created in the [Wix Developer Center](https://dev.wix.com/)) and Wix POS SPIs:

* The [Wix Developer Center](https://dev.wix.com/) is an environment used to set up new service providers and focus on app integrations.

* Using the SPIs, you can design your app to: 
    * Pair your locations with the configurations (locations) defined in Wix.
    * Synchronize your menus. Keep in mind that any menus already defined on the Wix site 
        will be disabled.
    * Accept orders from Wix.

Complete the following steps to adapt Wix system's integration to make your POS methods available to merchants and their customers.

## Signing up to the Integration

Send an email to this email address: `restaurant-provider-integration@wix.com` to request sign-up. Enter "POS Integration" as the subject, and provide the following details: 

- Type of business (store, restaurant...)
- Type of integration you want to provide (local delivery, point of sale...)
- A few words about your business and the market you serve (for example, countries)

Your sign-up request will be reviewed and you will be notified by return email. 

## Prerequisites

1.  You and the merchant must provide information that Wix and your app need, such as an API keys, to connect between the two systems. 

1.  Create an [app](https://dev.wix.com/dc3/my-apps/) with a Dashboard component. 

    The app should have the Wix Restaurants Manage Orders permissions.

    The Dashboard component represents the POS Locations dashboard page(s) to add to the merchant’s Wix site.
    
    When designing these dashboard pages in your app, add functionality for mapping the POS locations to Wix location configurations. 
    
    The dashboard pages will be accessible from the Dashboard: **Settings > Order Settings > POS Integration > *<Your POS integration>* > Open Integration Settings**

1. Manage the locations on your platform. 
    
    To facilitate orders, Wix needs to know the status of each customer's locations on your platform. Make sure to set each of the customer's location statuses to "READY." This indicates to Wix that the merchant can start receiving POS orders for these locations. 
    
## Limitations

Note the following limitation.

* Multiple accounts are useful for supporting different merchant’s accounts per location configuration (e.g. the New York location uses one POS service provider's account while the San Francisco location uses a different POS service provider's account).

    For now, Wix supports only 1 account for a merchant (instance), regardless of how many locations the merchant has. In the future, multiple accounts per instance (1 for each location) will be supported.