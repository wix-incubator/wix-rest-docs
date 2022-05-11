# Example Use Cases and Flow: Loyalty
 
 
This article shares possible use cases your app could support, as well as example flows. You're certainly not limited to these use cases, but it can be a helpful jumping off point as you plan your app's implementation.
 
 
## Set Up Loyalty (Optional: by Syncing From an External Program)
 
Your app can help site owners set up Loyalty, add customer accounts, and help them sync their customers’ accounts from an external loyalty program.
 
 
### Step 1: Set Up Loyalty
 
By default, every Wix site includes a loyalty program in `DRAFT` status. Until it has been activated, customers cannot earn points or redeem rewards. Retrieving such a program will return dummy data. Your app can help the site owners customize their program by calling the [Update Loyalty Program endpoint](https://dev.wix.com/api/rest/loyalty/update-loyalty-program). In the body of the call, you’ll need pass a program name and its point definition, as well as a URL of the point icon.
 
>**Note:** The call will set up Loyalty with your customizations, but the program will stay in `DRAFT` status. Thus, customers cannot earn points or redeem rewards.
 
```sh
curl -X PATCH \
 https://www.wixapis.com/loyalty/v1/program
 --data-binary '{
   "loyaltyProgram": {
     "name": "Loyalty rewarded",
     "pointDefinition": {
       "custom_name": "stars",
       "icon": {
         "_id": "1bf8c6_2528eb509c0a4bcea5c39b923%7Emv2.jpg",
         "url": "https://my-icons.example/star.svg",
         "altText": "star icon"
       }
     }
   }
 }'
 -H 'Authorization: <AUTH>'
```
 
 
### Step 2: Activate Loyalty
 
To activate the program, call the [Activate Loyalty Program](https://www.dev.wix.com/api/rest/loyalty/activate-program) endpoint.
 
```sh
curl -X POST \
 https://www.wixapis.com/loyalty/v1/program/activate
 -H 'Authorization: <AUTH>'
```
 
 
### Step 3 (Optional): Prepare a Mapping Between Loyalty and the External Program
 
> **Note:** This step is only needed when syncing from an external loyalty program.
 
If the site owners already have an external loyalty program, your app could prepare a mapping between the two programs. Make sure to include the customers’ email addresses, their external loyalty account IDs, as well as the point balances in the mapping. Later, you’ll add the Loyalty account Ids. To allow future two-way syncs, you can save this mapping on your servers.
 
 
### Step 4: Retrieve a Customer’s Wix Contact or Member ID
 
In case your app is syncing from an external program, you’ll iterate through the list of customer emails from the previously prepared mapping. Alternatively, if your app is setting up Loyalty from scratch, you’ll iterate through another list of customer email addresses.
 
You’ll use each email address to retrieve either the corresponding `contactId` or `memberId`.
 
> **Retrieve a `contactId`:**
> + Call the [Query Contacts endpoint](https://dev.wix.com/rest/crm/contacts/contacts-v4/query-contacts) passing the customer’s email address.
> + In case a customer doesn’t yet have a `contact ID` you can call the [Create Contact endpoint](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/create-contact).
> + Learn more about the [Wix Contacts API](https://dev.wix.com/api/rest/contacts).
 
> **Retrieve a `memberId`:**
> + Call the [Query Members endpoint](https://dev.wix.com/api/rest/members/members/query-members) passing the customer’s email address.
> + Learn more about the [Wix Members API](https://dev.wix.com/api/rest/members).
 
 
### Step 5: Create a Loyalty Account for Every Customer
 
Now, your app could create a Loyalty account for every customer. To do so, call the [Create Account endpoint](https://www.dev.wix.com/api/rest/loyalty/create-account) once per customer. Each call needs to include either a `contact ID` or `member ID` as part of its body.
 
Example call using a `contactId`:
 
```sh
curl -X POST \
 https://www.wixapis.com/loyalty/v1/accounts
 --data-binary '{
   "contactId": "8046df3c-7575-4098-a5ab-c91ad8f33c47"
 }'
 -H 'Authorization: <AUTH>'
```
 
Example call using a `memberId`:
 
```sh
curl -X POST \
 https://www.wixapis.com/loyalty/v1/accounts
 --data-binary '{
   "memberId": "e62e3011-55cf-4de3-a497-e097b52d86b7"
 }'
 -H 'Authorization: <AUTH>'
```
 
 
### Step 6 (Optional): Retrieve the Customer’s Point Balance From the External Program
 
> **Note:** This step is only needed when syncing from an external loyalty program.
 
If the site owners already have an external loyalty program, your app needs to call the external endpoint that retrieves the customer’s point balances.
 
 
### Step 7 (Optional): Adjust the Customer’s Point Balance on Loyalty
 
> **Note:** This step is only needed when syncing from an external loyalty program.
 
Finally, your app could help the site owners sync their customers’ point balances from an external loyalty program. To do so, call the [Adjust Points endpoint](https://www.dev.wix.com/api/rest/loyalty/adjust-points). You’ll need to perform one call for every customer and include the `accountID` and point balance in the body of the request.
 
```sh
curl -X POST \
 https://www.wixapis.com/loyalty/v1/accounts/{account_id}/adjust-points
 --data-binary '{
   "accountId": "01e34b81-4e48-43e4-b178-c84f3b968574",
   "description": "Sync from external program",
   "type": {
     "balance": 42
   },
   "revision": "3"
 }'
 -H 'Authorization: <AUTH>'
```
 
 
## Two-way Sync Loyalty with an External Program
 
Your app could help businesses with an external loyalty program keep their programs synced.
 
1. Create a mapping between the external program and Loyalty.
	> **Note:** Make sure to include the customer’s email, both account IDs, and current point balance in the mapping. Store the mapping on your servers. You can see one example how to set up such a mapping in the [Set Up Loyalty Flow](https://dev.wix.com/api/rest/loyalty/example_flows#set_up_loyalty).
1. Listen to all relevant Loyalty and external webhooks:
    * Account created
    * Account deleted
    * Balance updated
1. Update the point balance, and add or delete accounts in the mapping accordingly.
1. Adjust Loyalty or the external program accordingly.
    > **Note:** Make sure to include logic that ignores webhooks triggered as the result of a sync. This will prevent your app from getting caught in an endless loop.
 
 
## Let Customers Earn Loyalty Points for Liking a Social Media Post
 
 
You could help customers earn Loyalty points when they like one of the site owner’s social media posts. To do so, your app will listen to an external webhook that is triggered for this event, identify the relevant Loyalty account and add points to it.
 
 
### Step 1: Listen to the Social Media’s Webhooks
 
First, your app will listen to an external webhook that is triggered when a customer likes a specific social media post.
 
> **Note:** Your app could also let customers earn loyalty points for following a social media channel, registering to a webinar, writing a product review, or similar actions.
 
 
### Step 2: Retrieve the Customer’s Wix `contactId`
 
Then you’ll retrieve the relevant customer’s email address from the webhook’s parsed data. You’ll use the email address to look up the `contactID` as described in step 3 of the [Set up a Site’s Loyalty Program](https://www.dev.wix.com/api/rest/loyalty/example_flows#set_up_a_sites_loyalty_program) flow.
 
 
### Step 3: Check that the Customer has a Loyalty Account
 
Then you’ll retrieve the customer’s `accountId`. To do so, your app will call the [Get Account endpoint](https://www.dev.wix.com/api/rest/loyalty/get-account).
 
```sh
curl -X GET \
 https://www.wixapis.com/loyalty/v1/accounts/fetch-by
 --data-binary '{
   "_id": {
     "contactId": "a string"
   }
 }'
 -H 'Authorization: <AUTH>'
```
 
If the response is empty, the customer doesn’t yet have a Loyalty account.
 
 
### Step 4 (Optional): Create a Loyalty Account
 
> **Note:** This step is only needed when the customer doesn’t yet have a Loyalty account.
 
In this case, your app will create a Loyalty account by calling the [Create Account endpoint](https://www.dev.wix.com/api/rest/loyalty/create-account).
 
```sh
curl -X POST \
 https://www.wixapis.com/loyalty/v1/accounts
 --data-binary '{
   "contactId": "a string"
 }'
 -H 'Authorization: <AUTH>'
```
 
 
### Step 5: Add Points to the Account
 
Finally, your app can call the [Earn Points endpoint](https://www.dev.wix.com/api/rest/loyalty/earn-points). You’ll need to pass the `accountID` and point amount as part of the call’s body.
 
```sh
curl -X POST \
 https://www.wixapis.com/loyalty/v1/accounts/{account_id}/earn-points
 --data-binary '{
   "accountId": "a string",
   "amount": 42,
   "description": "a string",
   "appId": "a string",
   "idempotencyKey": "a string"
 }'
 -H 'Authorization: <AUTH>'
 ```
 
 
## Create a Wix Coupon for Reaching a Milestone
 
Your app can check which customers are close to reaching a 1000 Loyalty points. Then you could email them that they’ll get a coupon for reaching this milestone. Finally, your app could get notified when a customer actually reaches this mark and create the coupon.
 
 
### Step 1: Identify Customers Who are Close to Reaching a Loyalty Milestone
 
As part of this flow, you’ll first identify which Loyalty accounts have between 900 and 999 points by calling the [List Accounts](https://www.dev.wix.com/api/rest/loyalty/list-accounts) endpoint.
 
```sh
curl -X GET \
 https://www.wixapis.com/loyalty/v1/accounts/
  -H 'Authorization: <AUTH>'
```
 
From the response, you’ll retrieve all accounts in the relevant point range and save their email addresses.
 
 
### Step 2: Contact the Customers
 
Then, your app will email every identified customer. You’ll let them know how many points they need to reach the 1000-point-milestone, and that they’ll get a coupon for reaching it.
 
>**Notes:**
> + Make sure to check whether the customers have agreed to receive emails from the site owners by calling the [Query Email Subscriptions](https://dev.wix.com/api/rest/marketing/email-subscriptions/query-email-subscriptions) endpoint.
> + Learn more about the [Email Subscriptions API](https://dev.wix.com/api/rest/marketing/email-subscriptions).
 
 
### Step 3: Get Notified When a Customer Reaches the Milestone
 
Listen to [Account Updated Domain Event](https://www.dev.wix.com/api/rest/loyalty/account-updated). Parse every event body’s data to check whether the new point balance is higher than 1000 while the previous balance was below. Make sure to save the relevant `accountId`.
 
 
### Step 4: Create the Coupon
 
Now, your app will create the coupon using the [Create Coupon endpoint] (https://dev.wix.com/api/rest/wix-coupons/coupons/coupon/create-a-coupon).
 
> **Note:** Learn more about the [Wix Coupons API](https://dev.wix.com/api/rest/wix-coupons/about-wix-coupons).
 
 
 
 
## Assign Milestone Badges
 
### Step 1: Get Notified When a Customer Reaches a Loyalty Milestone 
 
Listen to [Account Updated Domain Event](https://www.dev.wix.com/api/rest/loyalty/account-updated). Parse the event body’s data to check whether the new point balance is higher than your threshold and save the `accountId`.
 
### Step 2: Assign a Badge
 
Your app will use the ... API to assign a member badge. (https://www.wix.com/velo/reference/wix-users-backend/badges-obj/assignmembers)