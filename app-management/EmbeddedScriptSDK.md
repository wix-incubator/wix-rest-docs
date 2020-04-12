# Embedded Script SDK

> **Note:**
This functionality is currently in beta testing and is not currently available for all users. If you would like to request access to this functionality, [submit a proposal](https://dev.wix.com/proposal).

This SDK allows apps with embedded script components to:
- Listen to predefined Wix events 
- Report and listen to custom events 

> Note:
This SDK is not related to or dependent on the old JS SDK. 

## Listening to a Predefined Wix Event
Add this code to your embedded script component, and make sure to point to the events you are interested in:
```
<script id='my_app_js' src='https://cdn.domain.com/pixel.js?id={{pixel_id}}' async='true'></script> 
<script> 
window.wixDevelopersAnalytics.register('app-ID', function report(eventName, data) { 
  switch(eventName) { 
    case 'pageview':
      callMyPageViewFunction(); 
      break; 
    case 'addToCart':
      callMyAddToCartFunction(); 
      break;
</script>
```
### Predefined Wix Events
- **addProductImpression**: When a user views a product. 
- **clickProduct**: When a user clicks on a product.
- **viewContent**: When a key page is viewed.
- **addToCart**: When a user adds a product to the shopping cart.
- **removeFromCart**: When a user removes a product from the shopping cart. 
- **initiateCheckout**: When a user starts the checkout process.
- **startPayment**: When a user starts the payment process.
- **addPaymentInfo**: When a user saves payment information.
- **checkoutStep**: When a user completes a custom checkout step. 
- **purchase**: When the checkout process is complete.
- **lead**: When a user subscribes to a newsletter or submits a contact form.

## Reporting a Custom Event
Call a trigger event, passing the following properties:
- eventName
- eventData / eventParams - an object with the data to be passed
```
window.wixDevelopersAnalytics.triggerEvent(<'FORMSUBMIT'>, {name: <'TEST'>})
```
**Reporting and Listening to a Custom Event**
```
<script>
window.wixDevelopersAnalytics.register("billys_app", function report(eventName, data) {
  console.log('eventName: '+eventName);  
});
setTimeout(function(){ 
  window.wixDevelopersAnalytics.triggerEvent('billyTestEvent', {eventName: 'TEST'})
}, 5000);
</script>
```
### On Ready Event
To make sure you aren't calling the SDK before it is fully initiated, here is an on-ready event you can listen to:
```
function registerListener(){
    window.wixDevelopersAnalytics.register('head', (eventName, eventParams) => console.log('wix dev head', eventName, eventParams));
  }
  window.wixDevelopersAnalytics ?
    registerListener() :
    window.onWixDevelopersAnalyticsReady = function() {
      registerListener();
    }
```
## Response Data
The returned data will vary based on the specific event, but will always include the following:
- **isPremium**: true if the site owner has a premium plan, false if they have a free plan.
- **uuid**: The site owner's unique ID in Wix.
- **msid**: The unique ID of the Wix Site.


# Embedded Script Dynamic Parameters  

You may choose to embed dynamic parameters in your script, if you have any custom keys per user. For example:
```
<script id="my-script" src="https://cdn.myap.com/pixel.js?id={{dynamic_key}}" async='true'></script>
```
### Using Dynamic Key Parameters
Dynamic parameters must be:
- Wrapped in double curly braces.
- Within a quote (") in order to avoid code evaluation.
- Set using the [Embedded Scripts API](https://dev.wix.com/api/app-management#apps.embedded-scripts).
>**Note:**
You can also inject script into [placeholders](https://devforum.wix.com/en/article/placeholders) provided by Wix Stores.

>**Important:**
Test your app on your site to make sure everything is connected and working properly. If everything it working properly, you should see your script injected to the site with the appropriate parameter in place.


## Embedded Script Placeholders

Wix Stores provides two placeholders where you can inject your embedded scripts:
[image]
Below the product SKU, you would find:
```
<div data-hook="details-placeholder"></div>
```
And, below the product page, you'll find:
```
<div data-hook="bottom-placeholder></div>
```

The placeholders are empty divs with data-hooks that allow you to add content to these specific page locations. 

To inject data into one of these placeholders, append your DOM element to the relevant placeholder once the page is loaded.
