SortOrder: 0
# Getting started
As a Payment Service Provider, you can integrate various payment methods and make them available to merchants and their buyers on Wix, including:
- Cards
- Alternative payment methods (APM) such as iDEAL or PayPal
- Hosted page, a 3rd-party web page for secure processing of electronic transactions

Before taking any technical efforts or tasks involving the API exposed on this page, every Payment Service Provider needs to go through an onboarding process with the business development team at Wix.com.
The onboarding flow includes getting to know the Payment Service Provider and how they can benefit merchants. 
The first step in the onboarding process is to gather details of the provider via an onboarding form that is being sent by the Wix Business Development team. Following that action is the completion of the legal agreements that mark the start of the business relationship between Wix and Payment Service Provider.

Part of the integration process is working with [Wix Developer Center](https://dev.wix.com/) - an environment used to set up new payment service providers and focused on app integrations.

Complete the following steps to adapt Wix system's integration to make your payment methods available to merchants:

1. [Create a Wix Developers Center account](https://providers-platform.wixanswers.com/kb/en/article/how-to-open-a-devcenter-account).
2. Create an app in the [Wix Developers Center](https://dev.wix.com).
3. Add the following email address to your list of team members: [cashier-provider-integration@wix.com](mailto:cashier-provider-integration@wix.com). For more detailed instructions, see step three [here](https://providers-platform.wixanswers.com/kb/en/article/how-to-open-a-devcenter-account).
4. Create a test site and [add your payment provider/method to your testing site.](https://providers-platform.wixanswers.com/kb/en/article/adding-your-payment-providermethod-to-your-testing-site) 
5. Wix adds a payment gateway extension to your app. 
6. You can start reviewing the documentation to configure the following endpoints to process payments:
    - [Connect Account](https://dev.wix.com/api/rest/payment-provider/provider-platform/account/connect-account) plugin endpoint, which is triggered when a merchant provides the required data to connect their [PSP](https://en.wikipedia.org/wiki/Payment_service_provider) account to a Wix site.
    - [Create Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/create-transaction) plugin endpoint, which is triggered when a buyer pays on a Wix site.
    - [Refund Transaction](https://dev.wix.com/api/rest/payment-provider/provider-platform/transaction/refund-transaction) plugin endpoint, which is triggered when a merchant refunds a payment made on a Wix site.
    - [Submit Event](https://dev.wix.com/api/rest/payment-provider/provider-platform/event/submit-event) webhook, which is used by a payment plugin to send payment state updates to Wix.

>**Note:**
>Find more details on what to expect when working with Wix Developers Center [here](https://providers-platform.wixanswers.com/kb/en/article/getting-started-what-to-expect).
