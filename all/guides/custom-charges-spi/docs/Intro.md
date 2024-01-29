SortOrder: 0
# About the Custom Charges SPI

The Custom Charges SPI allows you to manage what customers must pay to use
your app. This includes regularly recurring base prices, installation and usage
fees, and any other custom charges.

With the Custom Charges SPI, you can:

+ Add your app's charges to the invoice that Wix sends to site owners.
+ Receive notifications about charges that Wix doesn't accept, created
  invoices, or when customers increase their charge limit.
+ Keep your customers informed about how much your app would charge them if Wix
  were to send an invoice at this moment.

See the [App Instance API](https://dev.wix.com/docs/rest/api-reference/app-management/apps/app-instance/introduction)
for more details about the notifications you receive when a customer installs
an instance of your app on their site.

## How to become a provider

When configuring your app in the [Wix Developers Center](https://dev.wix.com):

+ Set up [Usage-Based Pricing](https://dev.wix.com/docs/build-apps/build-your-app/pricing-plans/usage-based-pricing)
  for your app. Note that Usage-Based Pricing is in Alpha and may change in the
  future.
+ Add a __Premium Custom Charges__ integration component.
+ Use the JSON editor to update the `baseUri`. Make sure to include only
  the base part of your integration's URI. For example, if Wix should call your
  integration at `https://provider.example.com/v1/charge-limit` for the
  [Get Charge Limit](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/custom-charges-provider-v1/get-charge-limit)
  endpoint set `{"baseUri": "https://provider.example.com"}`.

## Before you begin

It’s important to note the following points before starting to code:

+ Before you can implement the Custom Charges SPI, it's essential to set up
  [Usage-Based Pricing](https://dev.wix.com/docs/build-apps/build-your-app/pricing-plans/usage-based-pricing)
  for your app in the [Wix Developers Center](https://dev.wix.com/). Note that
  you have to [submit a request](https://devforum.wix.com/account/connect-sso?redirectUrl=https:~2F~2Fdevforum.wix.com~2Fen~2Fcontact)
  to enable Usage-Based Pricing. Keep in mind that Usage-Based Pricing is
  currently in Alpha, this means it's still in development and may change in
  the future.
+ You can't bill your customers before they
  [upgrade](https://support.wix.com/en/article/upgrading-an-app-from-the-wix-app-market)
  to a paid version of your app.
+ You're able to include up to 5 custom charges per invoice.
+ You must set an initial charge limit and can't bill customers more than this
  limit per billing cycle. You can't change the limit later, but customers are
  able to increase it themselves.
+ You receive notifications in case Wix doesn't accept the charges you return
  via the SPI. Currently, there is no notification if the customer agrees to
  your proposed charge limit or pays an invoice.
+ Currently, Wix supports the following currencies: `AUD`, `BRL`, `CAD`, `EUR`,
  `GBP`, `ILS`, `INR`, `JPY`, `MXN`, `PLN`, `RUB`, `TRY`, `USD`. Wix may add
  more currencies in the future.
+ We recommend to use the `instanceId` instead of the `subscriptionId` to track
  usage and billing for apps, because this field is also used in the
  [App Management API](https://dev.wix.com/docs/rest/api-reference/app-management/about-app-management).
+ If we discover that your app has charged customers for usage outside of an
  invoice's specified period, we may take action such as blocking your app from
  charging the customer, removing your app from the Wix App Market, revoking
  your access to the Wix developer program, or pursuing legal action to recover
  damages caused by overcharging. We understand that mistakes can happen and
  encourage you to contact
  [the Wix App Market team](https://devforum.wix.com/kb/en/contact) immediately if you
  become aware of any overcharging issues so that we can work together to
  resolve the situation.

## Use cases

+ [Support app upgrades](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/sample-flows#support-app-upgrades)
+ [Bill a customer](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/sample-flows#bill-a-customer)
+ [Get Notified when an app instance is canceled](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/sample-flows#get-notified-when-an-app-instance-is-canceled)

## Terminology

+ __App instance__: Particular installation of an app that let's you identify
  your customer. Learn more about how to retrieve the instance ID from an
  [SPI request envelope](https://dev.wix.com/api/rest/getting-started/service-provider-interface#getting-started_service-provider-interface_request-envelope).
+ __Customer__: Site owner who installs your app on their Wix site.
+ __Invoice__: Document that Wix sends to customers specifying the price they
  have to pay for using the Wix platform. Includes charges for 3rd-party apps
  associated with the site.
+ __Charge__: Price for using your app that you can add to an invoice. You can
  add up to 5 charges per invoice.
+ __Charge limit__: Maximum amount that you're allowed to charge customers for
  using your app per billing cycle. It helps ensure that customers are aware of
  their potential costs upfront.
+ __Subscription ID__: Unique identifier for the agreement that specifies the
  product or service to which the customer has access to and how they are billed.
  Currently, Wix doesn't provide an API to retrieve information about
  subscriptions. In case the product is an app, we recommend to use the app
  instance ID instead of the subscription ID to track usage and billing, because
  this field is also used in the
  [App Management API](https://dev.wix.com/docs/rest/api-reference/app-management/about-app-management).
