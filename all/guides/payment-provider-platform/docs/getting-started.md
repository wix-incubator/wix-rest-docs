SortOrder: 3
# Getting started
As a payment provider, you can integrate various payment methods and make them available to merchants and their buyers on Wix, including:
- Cards
- Alternative payment methods (APM) such as iDEAL or PayPal
- Hosted page, where buyer can select actual payment method (on provider's side)

Part of the integration process is working with [Wix Developer Center](https://dev.wix.com/) - an environment used to set up new payment providers and focused on app integrations.

Complete the following steps to adapt Wix system's integration to make your payment methods available to merchants:
1. [Create a Developer Center account](https://providers-platform.wixanswers.com/kb/en/article/how-to-open-a-devcenter-account).
3. Before you can integrate with Wix, you must create an app in the [Developer Center](https://dev.wix.com) to configure required parameters.
    1. [Create your first app](https://providers-platform.wixanswers.com/kb/en/article/adding-your-payment-providermethod-to-your-testing-site) and add your payment provider/method to your testing site.
    2. Add the following email address to your list of team members: [cashier-provider-integration@wix.com](mailto:cashier-provider-integration@wix.com). For more detailed instructions, see step three [here](https://providers-platform.wixanswers.com/kb/en/article/how-to-open-a-devcenter-account)
5. While Wix adds the [payment gateway extension](https://providers-platform.wixanswers.com/kb/en/article/adding-your-payment-providermethod-to-your-testing-site) to your app, you can start reviewing the documentation to configure the following endpoints to process payments:
- **Connect Account**. `ConnectAccount` endpoint will be triggered when a merchant provides the required data to connect a payment provider account to their Wix site. This allows you to verify the merchant's credentials, and confirm that the merchant is registered to your service, as well as the merchant is allowed to perform business in the provided country and with provided currency.
- **Create Transaction**. `CreateTransaction` endpoint will be triggered when a buyer initiates the payment on a WIX site. Initiate payment when you receive this call. Make sure to use the `wixTransactionId` parameter as an idempotency key, as WIX will retry the call in case of failure.
- **Refund Transaction**. For any transaction initiated by Wix, a Payment Plugin (your web application) must:
    - process `RefundTransaction` requests from Wix
    - notify Wix about all refunds including but not limited to those initiated by Wix by calling `SubmitEvent`
- **Submit Event**. Submit event (webhook) allows providers to inform Wix about changes of *Transaction* status, such as approval, decline, or refund. This method must be used to update the payment status on Wix.

>**Note:**
>Find more details on what to expect when working with DevCenter [here](https://providers-platform.wixanswers.com/kb/en/article/getting-started-what-to-expect).