SortOrder: 6
# Orders: Sample Use Case & Flow
This article shares a possible use case your app could support, as well as a sample flow that could support the use case. 
This can be a helpful jumping off point as you plan your app's implementation.

## Send an email on successful payment of online orders

Site owners can use your app to reach out to their customers and send a confirmation email that a payment was successful. 
To begin, create an email template to use for these messages. Site owners can also design their own with their [email marketing dashboard](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Fshoutout/dashboard).  

To listen for successful payments and send a confirmation email to the customer, follow this flow:  
1. Listen for any new payments using the [Payment Webhook](https://dev.wix.com/api/rest/wix-cashier/cashier-pay/payment-event/payment-webhook).
1. When the webhook is triggered, check for a `wixAppId` of `1522827f-c56c-a5c9-2ac9-00f9e6ae12d3` (the Wix App ID for Pricing Plans) and extract the `wixAppOrderId`.
1. Call [Get Order](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/orders/get-order) using the `wixAppOrderId` as the `id` for the order to retrieve.
1. Extract the `order.buyer.memberId` to retrieve the buyer's `memberId`.
1. Use the ID to [Get Member](https://dev.wix.com/api/rest/members/members/get-member) and extract the member's `loginEmail`.
1. Call [Query Email Subscriptions](https://dev.wix.com/api/rest/marketing/email-subscriptions/query-email-subscriptions) and filter by the email address to confirm that the member has agreed to receive emails from the site owner.
1. Use [Get or Create Conversation](https://dev.wix.com/api/rest/inbox/conversations/get-or-create-conversation) and [Send Message](https://dev.wix.com/api/rest/inbox/messages/send-message) to send an email to the buyer.
