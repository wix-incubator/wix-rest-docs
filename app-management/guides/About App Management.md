# About the App Management APIs

The App Management APIs allow you to manage user specific data for all individual
installations of your app. This includes receiving notifications whenever a new
user installs your app on their site or purchases a Premium version. Additionally,
you can use the APIs to add custom charges to your users' invoices.

With the App Management APIs, you can:

+ [Track user specific data with app instance IDs](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/introduction)
+ [Manage usage-based pricing](https://dev.wix.com/docs/rest/api-reference/app-management/)
+ [Add embedded scripts to Wix sites](https://dev.wix.com/docs/rest/api-reference/app-management/apps/embedded-scripts/introduction)
+ [Notify Wix about your app's business events](https://dev.wix.com/docs/rest/api-reference/app-management/apps/bi-event/introduction)

Learn more about:

+ [Pricing options for your app](https://dev.wix.com/docs/build-apps/build-your-app/pricing-plans/set-up-your-app-pricing)
+ [Setting up embedded scripts](https://dev.wix.com/docs/build-apps/developer-tools/extensions/embedded-scripts)
+ [Identifying users with App Instance ID](https://dev.wix.com/docs/build-apps/build-your-app/app-instance/identify-users-app-instance)

## Before you begin

It’s important to note the following points before starting to code:

+ The Wix pricing page for your app supports only 4 plans for users to choose
  from. This includes your app's free plan if you offer one. In case you want
  to offer more than 4 plans, your app needs to build an external pricing
  page and [redirect users back to the Wix checkout](https://dev.wix.com/docs/rest/api-reference/app-management/apps/billing/get-url).
+ You can't delete an app's pricing plan after you have set it up, but you can
  add more plans.
+ Currently, Wix doesn't notify you about changes to the payment status of an
  invoice.

## Use cases

+ [Reach out to new users](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/sample-flows#reach-out-to-new-users)
+ [Manage usage-based invoices](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/sample-flows#bill-a-customer)
+ [Identify a site's installed Wix business solutions](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/sample-flows#identify-a-sites-installed-wix-business-solutions)
+ [Automatically create user logins](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/sample-flows#automatically-create-user-logins)

## Terminology

+ __App Instance__: Unique identifier of an app within a specific website. The
  app instance ID is ideal for identifying your users, the specific plan they’ve
  purchased from you and the features you're supporting for them.
+ __App Pricing__: You can choose the business model that works best for your app:
  + __Freemium__: We recommend to choose Freemium pricing. You offer both free
    and paid versions of your app. Users can upgrade to Premium at any time.
  + __Free__: You don't charge your users.
  + __Premium__: Users must pay to use your app.
  + __Pay as you go__: ??? External pricing for not supported models
  + __Usage-based pricing__: You charge your users on a recurring, monthly basis.
    You can include a flat base fee and other fees if you want.
  + __Combination of business models__: ???
    + __Custom Charge__: Adjustable price for using your app. Each billing cycle
      you can add up to 5 charges to an invoice that Wix sends to your customer.
+ __Embedded script__: Script that you can add to a site's `<head>` tag.