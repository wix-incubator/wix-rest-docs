SortOrder: 5
# About the Orders API

The Order entity includes all of the details of Pricing Plans Orders and their statuses. Using the Orders API, you can create and manage orders or change access to content on Wix or external apps upon plan purchase or cancellation.

Use the Orders API to:
- List orders and get information about them
- Preview an order to show price, tax and other details, as well to check if user is eligible for trial or purchase, before completing an order
- Create an offline order
- Change an order start date
- Mark an order as paid
- Extend an order's duration
- Cancel an order
- Suspend and resume an order


## Terminology
- **Order**: A purchase of a subscription to a Pricing Plan - including price, duration and billing schedule data. Orders can be free.
- **Offline Order**: A purchase of a subscription to a Pricing Plan where the payment will not be handled via Wix. This type of order can be created via API.
- **Online Order**: A purchase of a subscription to a Pricing Plan where the payment will be handled via Wix. This type of order is not eligible for creation via API.
- **Order Status**: An order can have one of the following statuses:  
  - `PENDING` - order has been purchased and its start date is in the future, so it is not yet valid.
  - `ACTIVE` - order is active.
  - `CANCELED` - order has been canceled.
  - `EXPIRED` - order expiration date has passed and is no longer active.
  - `PAUSED` - order was active, and then paused before the expiration date. The order can be resumed to return it to `ACTIVE` status with a new expiration date.
  - `PENDING_CANCELLATION` - the site owner has selected to discontinue (cancel) the order, but the plan remains active until the end of the current payment period.


## User Flows
Below are some possible use cases your app could support, as well as an example flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.

### Send an Email on Plan Purchase

1. Sign up for the [Order Created](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/orders/order-created-webhook) webhook.
2. Create an email template.
3. When the webhook is triggered, collect one of the customer identifiers:
    - `buyer.contactId`
    - `buyer.memberId`
4. Call the relevant endpoint to get customer's email address:
    - [Get Contact](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/get-contact) if passing a contact ID  
    - [Get Member](https://dev.wix.com/api/rest/members/members/get-member) if passing a member ID
5. Collect the returned email address.
6. Call the [Query Email Subscriptions](https://dev.wix.com/api/rest/marketing/email-subscriptions/query-email-subscriptions) endpoint and filter by the email address to confirm that the member has agreed to receive emails from the site owner.  
7. Populate your email template.
8. Send the email.


### Send an Email Upon Successful Payment (Online Orders)

1. Sign up for the [Payment Event](https://dev.wix.com/api/rest/wix-cashier/cashier-pay/payment-event/payment-event-webhook) webhook.
2. Create an email template.
3. When the webhook is triggered, check that the wixAppId = 1522827f-c56c-a5c9-2ac9-00f9e6ae12d3.
4. Collect the `wixAppOrderId`.
5. Call the [Get Order](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/orders/get-order) endpoint and pass the `wixAppOrderId` collected above as the `orderId`.  
6. Collect the `order.buyer.contactId`.  
7. Call [Get Contact](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/get-contact) and pass the contact ID collected above.  
8. Collect the returned email address.  
6. Call the [Query Email Subscriptions](https://dev.wix.com/api/rest/marketing/email-subscriptions/query-email-subscriptions) endpoint and filter by the email address to confirm that the member has agreed to receive emails from the site owner.  
7. Populate your email template.  
8. Send the email.  

## Limitations
- Pricing plan orders created via API can't be paid for using the Wix Payment system.
- The application of tax to orders is defined at the site level, and isn't accessible via API. Site owners can [set up tax collection manually](https://support.wix.com/en/article/pricing-plans-setting-up-tax-collection).
