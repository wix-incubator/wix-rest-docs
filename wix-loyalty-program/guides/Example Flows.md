# Example Flows
 
 
This article shares possible use cases your app could support, as well as example flows. You're certainly not limited to these use cases, but it can be a helpful jumping off point as you plan your app's implementation.
 
 
## Activate a loyalty program and create loyalty accounts

Your app can help site owners activate their Loyalty Program and create loyalty accounts for each of their customers.

1. Use [Activate Loyalty Program](https://dev.wix.com/api/rest/wix-loyalty/program/activate-loyalty-program) to activate the site's loyalty program.

>**Note:** The Wix site owner must install the Wix Loyalty Program app before activating.
  
2. Use [List Contacts](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/list-contacts) to get all contacts.

3. Create a loyalty account for each contact with [Create Account](https://dev.wix.com/api/rest/wix-loyalty/accounts/create-account).
 
## Two-way sync with an external system

Your app can help business owners keep their external loyalty program updated with their Wix loyalty accounts with a two-way sync.

First, create a mapping from Wix loyalty accounts to the external accounts using a common field, like email address. Store this mapping on your app's server. Then you will follow these two flows to create the two-way sync:
+ Synchronizing to the external system
+ Synchronizing to Wix

#### Synchronizing to the external system
1. Listen for any changes to Wix loyalty accounts using the [Points Updated Webhook](https://dev.wix.com/api/rest/wix-loyalty/accounts/points-updated-webhook).
1. When the webhook is triggered, parse the data object for the `latestTransaction`.
1. Use the initial mapping to copy the relevant information to the external loyalty system.
1. Ignore the resulting event from the external system so that you don't create an endless loop of updates.

#### Synchronizing to Wix
1. Listen for any changes to the loyalty accounts from the external system.
1. When your app detects a change that it needs to synchronize, use [Adjust Points](https://dev.wix.com/api/rest/wix-loyalty/accounts/adjust-points) to copy the details to the relevant Wix loyalty account.
1. Ignore the resulting event from Wix so you don't create an endless loop of updates.
 
## Message site members with their loyalty points balance on a monthly basis
 Businesses can send their customers a monthly message that includes the customer's loyalty points and encourages them to earn more.
 
1. Use [List Accounts](https://dev.wix.com/api/rest/wix-loyalty/accounts/list-accounts) to get all loyalty accounts.
2. Pull out only the accounts that contain a `memberId`.
2. Use [Get or Create Conversation](https://dev.wix.com/api/rest/inbox/conversations/get-or-create-conversation) and [Send Message](https://dev.wix.com/api/rest/inbox/messages/send-message) to send a new message at the beginning of every month to each member that includes their loyalty account points `balance`.