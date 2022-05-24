# Example Flow
 
 
This article shares possible use cases your app could support, as well as example flows. You're certainly not limited to these use cases, but it can be a helpful jumping off point as you plan your app's implementation.
 
 
## Set Up and Activate a Loyalty Program (Optional: by Syncing From an External Program)

Your app can help site owners set up Wix Loyalty, add customer accounts, and help them sync their customers’ accounts from an external loyalty program.

 
### Step 1: Set Up Loyalty
 
By default, every Wix site includes a loyalty program in `DRAFT` status. Until it has been activated, customers cannot earn points or redeem rewards. Retrieving such a program will return sample data. Your app can help the site owners customize their program by calling [Update Loyalty Program](https://dev.wix.com/api/rest/loyalty/update-loyalty-program).

>**Note:** The call will set up Loyalty with your customizations, but the program will stay in `DRAFT` status. Therefore, customers cannot earn points or redeem rewards at this stage.
 
```sh
{
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
}
```
 
### Step 2: Activate the loyalty program
 
To activate the program, call [Activate Loyalty Program](https://www.dev.wix.com/api/rest/loyalty/activate-program).
 
### Step 3 (Optional): Prepare a Mapping Between Loyalty and the External Program
 
> **Note:** This step is only needed when syncing from an external loyalty program.
 
If the site owners already have an external loyalty program, your app could prepare a mapping between the two programs. Make sure to include the customers’ email addresses, their external loyalty account IDs, as well as the point balances. Later, you’ll add the Loyalty account IDs. To allow future 2-way syncs, you can save this mapping on your servers.
 
 
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
 
Now, your app could create a Loyalty account for every customer. To do so, call the [Create Account endpoint](https://www.dev.wix.com/api/rest/loyalty/create-account) once per customer. Each call needs to include either a `contactID` or `memberID` as part of its body.
 
### Step 6 (Optional): Retrieve the Customer’s Point Balance From the External Program
 
> **Note:** This step is only needed when syncing from an external loyalty program.
 
If the site owners already have an external loyalty program, your app needs to call the external endpoint that retrieves the customer’s point balances.
 
 
### Step 7 (Optional): Adjust the Customer’s Point Balance on Loyalty
 
> **Note:** This step is only needed when syncing from an external loyalty program.
 
Finally, your app could help the site owners sync their customers’ point balances from an external loyalty program. To do so, call the [Adjust Points endpoint](https://www.dev.wix.com/api/rest/loyalty/adjust-points). Perform one call for every customer, and include the `accountId` and `balance` in the body of the request.
 
```sh
{
  "accountId": "01e34b81-4e48-43e4-b178-c84f3b968574",
  "description": "Sync from external program",
  "type": {
    "balance": 42
  },
  "revision": "3"
}
```
 
 
## 2-way sync loyalty with an external program
 
Your app could help businesses with an external loyalty program keep their programs synced.
 
1. Create a mapping between the external program and Loyalty.
	> **Note:** Make sure to include the customer’s email, both account IDs, and current point balance in the mapping. Store the mapping on your server. You can see one example of how to set up such a mapping in the [Set Up Loyalty Flow](#set-up-loyalty).
1. Listen for all relevant Loyalty and external webhooks:
    * Account created
    * Account deleted
    * Balance updated
1. Update the point balance, and add or delete accounts in the mapping accordingly.
1. Adjust Wix Loyalty or the external program accordingly.
    > **Note:** Make sure to include logic that ignores webhooks triggered as the result of a sync. This will prevent your app from getting caught in an endless loop.
 
 
 
## Notify customers nearing a milestone and assign milestone badges when they reach it
 
Your app can check which customers are close to reaching 1,000 loyalty points. Then you could email them that they are close to reaching this milestone, and the benefits they'll receive when they do. Finally, your app could get notified when a customer actually reaches this mark and assign them a badge for that milestone.
  
### Step 1: Identify Customers Who are Close to Reaching a Loyalty Milestone
 
As part of this flow, you’ll first identify which Loyalty accounts have between 900 and 999 points by calling the [List Accounts](https://www.dev.wix.com/api/rest/loyalty/list-accounts) endpoint.
 
```sh
https://www.wixapis.com/loyalty/v1/accounts/
```
 
From the response, you’ll retrieve all accounts in the relevant point range and save their email addresses.
 
 
### Step 2: Contact the Customers
 
Then, your app will email every identified customer. You’ll let them know how many points they need to reach the 1000-point-milestone, and what they will receive for reaching it.
 
>**Notes:**
> + Make sure to check whether the customers have agreed to receive emails from the site owners by calling the [Query Email Subscriptions](https://dev.wix.com/api/rest/marketing/email-subscriptions/query-email-subscriptions) endpoint.
> + Learn more about the [Email Subscriptions API](https://dev.wix.com/api/rest/marketing/email-subscriptions).
 
 
### Step 3: Get Notified When a Customer Reaches the Milestone
 
Listen to [Account Updated Domain Event](https://www.dev.wix.com/api/rest/loyalty/account-updated). Parse the event body’s data to check whether the new point balance is higher than 1000 while the previous balance was below. Make sure to save the relevant `accountId`.
 
### Step 4: Assign a Badge
 
Your app will use the [Assign Badge to Members](https://dev.wix.com/api/rest/members/badges/assign-badge-to-members) API to assign a member badge to the .