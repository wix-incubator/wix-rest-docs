SortOrder: 0
# About the Redirect Session API

Wix Headless provides you with the flexibility to create an app or site on any platform and take advantage of Wix's backend business solutions via APIs. However, for some processes, such as authentication and checkout, you can save time and effort by using standard frontend pages produced by Wix. The Redirect Session API enables you to temporarily redirect visitors from your external site to a Wix-managed page for these processes, and then return them to your site. These Wix-managed pages are seamlessly incorporated into the user experience of your external site.

With the Redirect Session API, you can:

+ Redirect a site visitor to a Wix authentication page, then have them redirected back to your external site with authorization credentials.
+ Take advantage of Wix frontend functionality by redirecting users to Wix-managed pages for bookings, eCommerce, events, and paid plans transaction checkouts.
+ Customize your flow, integrating Wix-managed pages alongside custom external pages. For example, use a Wix checkout with an external thank you page.

## Before you begin

It's important to note the following points before starting to code:

+ After a redirect session for authentication, Wix returns visitors to the redirect URI you provide only if the full **URI** has been authorized in advance. Make sure to add approved authentication URIs in the [Headless Settings menu](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Foauth-apps-settings) in the Wix project dashboard.
+ After all other redirect sessions, Wix returns visitors to the post-flow URL you provide only if the **domain** has been authorized in advance. Make sure to add approved domains in the [Headless Settings menu](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Foauth-apps-settings) in the Wix project dashboard.

## Terminology

+ **Redirect session:** A temporary redirection of a visitor from an external site to a Wix-managed page for a process such as authentication or checkout.
