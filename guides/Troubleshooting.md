# Troubleshooting

This article provides troubleshooting steps for common issues encountered while using the Wix APIs.

## Expected fields aren’t returning
### My app has a flow that is dependent on a specific field that I expect to be returned in a specific call. But sometimes, the field isn’t returned.
Wix’s calls are designed to support the full list of parameters you see in the documentation. However, not all parameters will always be filled - for example, 
if a site customer doesn’t fill in their province during checkout when they make a purchase, then when you call Wix eCommerce’s [Get Order](https://dev.wix.com/docs/rest/business-solutions/e-commerce/orders/get-order) 
or receive the [Order Created](https://dev.wix.com/docs/rest/business-solutions/e-commerce/orders/order-created) webhook about their order, 
the billingInfo > address > subdivision won’t be returned. If your app is dependent on a specific field, your app should be prepared to handle a case where it isn't returned.

## Limitations aren’t documented
### I often come across parameters that must have limitations, but they aren’t documented, for example min/max.
Wix’s documentation is designed to display limitations automatically, based on the developer’s code. However, there are various reasons why these might not have come through, 
especially in older APIs. If you come across one of these, please [let us know](https://www.wix.com/support-chatbot?nodeId=25a57397-ccf7-4376-8b74-48d51edf7159&referral=devRels).

## I got a 403 error and don’t know what to do about it
There are 2 primary reasons for a 403 error:
1. App didn’t request the right permissions in the Dev Center. Make sure to add the relevant permissions to your app.
2. The user doesn’t have the right permissions - SDK / Client only

## I got a 409 error and don’t know what to do about it
### I got a 409 error - “entity has already changed since the requested revision”.   
The entity you want to update is protected by a revision number, to prevent accidental overrides. To prevent this error, first call the relevant GET call for the entity you want to update, 
and then copy the returned revision into your update call. Don’t rely on the revision received in a webhook, as you might have received it with a delay.
