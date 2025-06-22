# Loyalty APIs: Sample Use Cases and Flows
This article presents possible use cases and corresponding sample flows that you can support. This can be a helpful jumping off point as you plan your implementation.
 
## Activate a loyalty program and create loyalty accounts

You can activate a Loyalty Program and create loyalty accounts for each of a site's customers.

1. Call [Activate Loyalty Program](https://dev.wix.com/docs/rest/crm/loyalty-program/program/activate-loyalty-program) to activate the site's loyalty program.

>**Note:** A must install the [Wix Loyalty Program](https://www.wix.com/app-market/loyalty) before activating.
  
2. Call [List Contacts](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/contacts/contact-v4/list-contacts) to get all contacts for a site.

3. Call [Create Account](https://dev.wix.com/docs/rest/crm/loyalty-program/accounts/create-account) to create a loyalty account for each contact.
 
## 2-way sync with an external system

You can keep an external loyalty program up to date with a site's Wix loyalty accounts with a 2-way sync.

### Initial setup
+ Create a mapping from Wix loyalty accounts to the external accounts using a common field, like email address.
+ Store this mapping on your server. Then follow these flows to create the 2-way sync.

### Synchronize to the external system
1. Use [Points Updated](https://dev.wix.com/docs/rest/crm/loyalty-program/accounts/points-updated) to listen for any changes to the points in Wix loyalty accounts.
1. When one of the events is triggered, retrieve the `latestTransaction` from the event's response.
1. Use the mapping from the initial setup to copy the relevant information to the external loyalty system.
1. Ignore the resulting event from the external system so that you don't create an endless loop of updates.

### Synchronize to Wix
1. Listen for any changes to the loyalty accounts from the external system.
1. When you detect a change that needs to synchronize, call [Adjust Points](https://dev.wix.com/docs/rest/crm/loyalty-program/accounts/adjust-points) to copy the details to the relevant Wix loyalty account.
1. Ignore the resulting event from Wix so you don't create an endless loop of updates.
 
## Message site members with their loyalty points balance on a monthly basis
Businesses can send their customers a monthly message that includes the customer's loyalty points and encourages them to earn more.
 
1. Call [Query Loyalty Accounts](https://dev.wix.com/docs/rest/crm/loyalty-program/accounts/query-loyalty-accounts) to get the loyalty accounts for a site.
1. Pull out only the accounts that contain a `memberId`.
1. Call [Get or Create Conversation](https://dev.wix.com/docs/rest/crm/communication/inbox/conversations/get-or-create-conversation) and [Send Message](https://dev.wix.com/docs/rest/crm/communication/inbox/messages/send-message) to send a new message at the beginning of every month to each member that includes their loyalty account points `balance`.
