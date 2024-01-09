# About the App Management APIs

The App Management APIs allow you to manage user specific data for all individual
installations of your app. This includes receiving notifications whenever a new
user installs your app on their site or purchases a Premium version.

With the App Management APIs, you can:

+ [Track user specific data with app instance IDs](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/introduction)
+ [Manage usage-based pricing](https://dev.wix.com/docs/rest/api-reference/app-management/)
+ [Add embedded scripts to Wix sites](https://dev.wix.com/docs/rest/api-reference/app-management/apps/embedded-scripts/introduction)
+ [Notify Wix about your app's business events](https://dev.wix.com/docs/rest/api-reference/app-management/apps/bi-event/introduction)

Learn more about:

+ [Pricing options for your app](https://dev.wix.com/docs/build-apps/build-your-app/pricing-plans/set-up-your-app-pricing)

## Before you begin

It’s important to note the following points before starting to code:

+ You can't switch the pricing model of your app after the original set up.
+ Currently, there are no notifications about the payment status of an invoice.

## Use cases

+ [Track new app instances](link-to-the-relevant-flow)
+ [Manage invoices with usage-based charges](link-to-the-relevant-article)

## Terminology

+ __App Instance__: Unique identifier of an app within a specific website. The
  app instance ID is ideal for identifying your users, the specific plan they’ve
  purchased from you and the features you're supporting for them.
+ __App Pricing__: You can choose the business model that works best for your app:
  + __Freemium__: We recommend to choose Freemium pricing. You offer both free
    and paid versions of your app. Users can upgrade to Premium at any time.
  + __Free__: You don't charge your users.
  + __Premium__: Users must pay to use your app.
  + __Pay as you go__: ???
  + __Usage-based pricing__: You charge your users on a recurring, monthly basis.
    You can include a flat base fee and other fees if you want.
  + __Combination of business models__: ???
    + __Custom Charge__: Adjustable price for using your app. Each billing cycle
      you can add up to 5 charges to an invoice that Wix sends to your customer.
+ __Embedded script__: Script that you can add to a site's `<head>` tag.