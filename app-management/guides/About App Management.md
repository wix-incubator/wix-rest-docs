# About the App Management APIs

The App Management APIs allow you to manage user specific data for all individual
installations of your app. This includes receiving notifications whenever a new
user installs your app on their site or purchases a Premium version. Additionally,
you can use the APIs to implement an external pricing page and manage usage-based
pricing.

With the App Management APIs, you can:

+ [Track user specific data with app instance IDs](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/introduction)
+ [Manage usage-based pricing](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/custom-charges-provider-v1/introduction)
+ [Add embedded scripts to Wix sites](https://dev.wix.com/docs/rest/api-reference/app-management/apps/embedded-scripts/introduction)
+ [Notify Wix about your app's business events](https://dev.wix.com/docs/rest/api-reference/app-management/apps/bi-event/introduction)

Learn more about:

+ [Identifying users with App Instance ID](https://dev.wix.com/docs/build-apps/build-your-app/app-instance/identify-users-app-instance)
+ [Pricing options for your app](https://dev.wix.com/docs/build-apps/build-your-app/pricing-plans/set-up-your-app-pricing)
+ [Setting up embedded scripts](https://dev.wix.com/docs/build-apps/developer-tools/extensions/embedded-scripts)
  
## Use cases

+ [Reach out to new users](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/sample-flows#reach-out-to-new-users)
+ [Manage usage-based invoices](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/sample-flows#bill-a-customer)
+ [Identify a site's installed Wix business solutions](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/sample-flows#identify-a-sites-installed-wix-business-solutions)
+ [Automatically log users in to your app](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/sample-flows#automatically-log-users-in-to-your-app)

## Terminology

+ __App Instance__: Unique identifier of an app within a specific website. The
  app instance ID is ideal for identifying your users, the specific plan they’ve
  purchased from you and the features you're supporting for them.
+ __App Pricing__: You can choose the business model that works best for your app.
  Use the [Custom Charges SPI](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/custom-charges-provider-v1/introduction)
  to manage your app's usage-based pricing.
  + __Usage-based pricing__: You charge your users on a recurring, monthly basis.
    You can include a flat base fee and other fees if you want.
    + __Custom Charge__: Adjustable price for using your app. Each billing cycle
      you can add up to 5 charges to an invoice that Wix sends to your customer.
+ __Embedded script__: Script that you can add to a site's `<head>` tag.