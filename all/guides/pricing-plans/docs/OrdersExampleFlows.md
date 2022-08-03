SortOrder: 6
# Example Flow
This article shares a possible use case your app could support, as well as an example flow. You're certainly not limited to this use case, but it can be a helpful jumping off point as you plan your app's implementation.

## Send an email on successful payment (online orders)
Your app can help site owners reach out to their customers and confirm that a payment was successful with an email. To get started, first, create an email template to send when a payment is successful. Then, listen for any new payments using the [Payment Webhook](https://dev.wix.com/api/rest/wix-cashier/cashier-pay/payment-event/payment-webhook).

1. When the webhook is triggered, check for a `wixAppId` of `1522827f-c56c-a5c9-2ac9-00f9e6ae12d3`, the Wix App ID for Pricing Plans.
1. Extract the `wixAppOrderId`.
1. Call [Get Order](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/orders/get-order) using the `wixAppOrderId` as the `id` for the order to retrieve.
1. Extract the `order.buyer.memberId` to retrieve the buyer's `memberId`.
1. Use the ID to [Get Member](https://dev.wix.com/api/rest/members/members/get-member).
1. Extract the member's `loginEmail`.
1. Call [Query Email Subscriptions](https://dev.wix.com/api/rest/marketing/email-subscriptions/query-email-subscriptions) and filter by the email address to confirm that the member has agreed to receive emails from the site owner.
1. Use [Get or Create Conversation](https://dev.wix.com/api/rest/inbox/conversations/get-or-create-conversation) and [Send Message](https://dev.wix.com/api/rest/inbox/messages/send-message) to send an email to the buyer.