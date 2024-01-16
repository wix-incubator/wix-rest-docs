SortOrder: 1
# Custom Charges SPI: Sample Use Cases & Flows

This article shares some possible use cases your app could support, as well as
a sample flow that could support each use case. This can be a helpful jumping
off point as you plan your app's implementation.

## Support app upgrades

Every time a customer upgrades an instance of your app, Wix
retrieves an initial charge limit from your app. Wix displays this limit to the
customer in the checkout page of the upgrade process. This helps customers
understand how much they may have to pay maximally for using your app per
billing cycle.

To support app upgrades:

1. Wix calls [Get Charge Limit](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/custom-charges-provider-v1/get-charge-limit).
2. Return the initial charge limit that your app is allowed to charge the customer per billing cycle.
3. Wix displays the limit to the customer for approval. Note that your app can't change this limit later, but customers are able to increase it themselves.

## Bill a customer

Your app can add custom charges to an invoice that Wix sends to a customer
at the end of the billing cycle.

To bill a customer:

1. Wix calls [List charges](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/custom-charges-provider-v1/list-charges). Note that Wix sends `{"intent": "CREATE_INVOICE"}` to actually create an invoice with the charges you return. For other purposes, Wix sends `{"intent": "DISPLAY_ONLY"}`.
2. Return up to 5 charges that Wix adds to the invoice.
3. In case Wix accepts your charges, Wix calls [Invoice Created Event](https://dev.wix.com/docs/rest/api-reference/app-management/apps/custom-charges-spi/custom-charges-provider-v1/invoice-created-event) and sends the invoice to the customer.

## Get notified when an app instance is canceled

Currently, you can't receive notifications when a payment for an
invoice has failed. If that happens, Wix sends an email to the customer and
retries to collect the payment several times. In case all retries fail, Wix
cancels the app instance. Your app could get notified in this situation, and
you could reach out to the customer.

To receive notifications when an app instance is canceled:

1. Sign up for the [Paid Plan Auto Renewal Cancelled Webhook](https://dev.wix.com/api/rest/app-management/apps/app-instance/paid-plan-auto-renewal-cancelled-webhook) of the App Instance API.
2. Listen to the webhook. Wix sends `{"cancelReason": "FAILED_PAYMENT"}` in case an app instance is canceled due to a failed payment.
3. Reach out to the relevant customer.
