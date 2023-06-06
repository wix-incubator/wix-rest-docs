SortOrder: 0
# About the eCommerce Abandoned Checkouts API

When a customer begins an eCommerce Checkout process but doesn't complete it (for example, after closing their browser tab before putting in their payment details and making a payment), that checkout becomes an abandoned checkout. The Abandoned Checkouts API allows an app developer to help a customer recover their abandoned checkout (return to their incomplete checkout and complete the checkout). When a customer completes their checkout and makes a purchase, the checkout becomes an [order](https://dev.wix.com/api/rest/wix-ecommerce/orders). 

An abandoned checkout holds buyer details, price, reference to the initial checkout, a checkout URL, and more.

The eCommerce Abandoned Checkouts API provides functionality for [getting information about an abandoned checkout](https://dev.wix.com/api/rest/wix-ecommerce/abandoned-checkouts/get-abandoned-checkout) and [retrieving a list of abandoned checkouts](https://dev.wix.com/api/rest/wix-ecommerce/abandoned-checkouts/query-abandoned-checkouts). You can also listen for events when an abandoned checkout is [created](https://dev.wix.com/api/rest/wix-ecommerce/abandoned-checkouts/abandoned-checkout-created-webhook) and [recovered](https://dev.wix.com/api/rest/wix-ecommerce/abandoned-checkouts/abandoned-checkout-recovered-webhook). 

To assist in migration from the Stores to eCommerce APIs, please refer to the [Stores Cart to eCommerce Checkout Conversion Table](https://dev.wix.com/api/rest/wix-ecommerce/checkout/stores-cart-to-ecommerce-checkout-object-conversion).

## Terminology

+ **Recovered**: When a customer returns to their abandoned checkout and completes the checkout.

+ **Activities**: This property is only relevant if the site owner set up [automations in the Dashboard](https://support.wix.com/en/article/wix-automations-creating-a-new-automation). The `activities` property is a list of all automation activities performed by [Wix Automations](https://support.wix.com/en/article/wix-automations-getting-started) regarding the abandoned checkout. Wix Automations updates the `activities` field for each actvity in the automation flow. For example, if a site owner set up an automation to send a notification to a site visitor an hour after their abandoned checkout is created, Wix automations does the following:
  + Updates the `activities` field to `SCHEDULED` when the abandoned checkout is created. 
  + Updates the `activities` field to `NOTIFICATION_SENT` after an hour, when the notification is sent to the site visitor.


  Other `actvities` include:
    + `EMAIL_SENT` 
    + `EMAIL_NOT_SENT`
    + `TASK_CREATED` 
