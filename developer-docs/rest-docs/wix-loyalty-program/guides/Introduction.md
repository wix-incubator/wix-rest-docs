SortOrder: 0
# About the Loyalty APIs

Wix users can install the [Wix Loyalty Program](https://www.wix.com/app-market/loyalty) to their site to create a loyalty program for their customers to increase customer retention. The program allows customers to earn points that they can redeem for rewards.

Wix Loyalty APIs allow you to activate, update, and manage a site’s loyalty program, including details about the overall loyalty program and customer accounts. Additionally, from [a site owner's dashboard](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Floyalty-accounts/wizard/), the site owner can define automations that give their customers points based on certain actions that are currently not available via the API. See an [overview of the wix loyalty program](https://support.wix.com/en/article/wix-loyalty-program-an-overview).

Wix Loyalty APIs allow you to:

* Activate the program.
* Customize the program, point name, and point icon.
* Create customer accounts.
* Manage account point balances.
* Create loyalty coupons.
* Apply a discount to checkout.
* Manage earning rules for loyalty programs.

## Before you begin
It's important to note the following points before starting to code:

* There can only be one loyalty program per Wix site.
* Only a [program that has been installed](https://www.wix.com/app-market/loyalty) in a Wix site can be activated.
* Each customer can have only one loyalty account.

## Use cases
+ [Activate a loyalty program and create loyalty accounts](https://dev.wix.com/docs/rest/crm/loyalty-program/example-flows#activate-a-loyalty-program-and-create-loyalty-accounts)
+ [2-way sync with an external system](https://dev.wix.com/docs/rest/crm/loyalty-program/example-flows#two-way-sync-with-an-external-system)
+ [Message site members with their loyalty points balance on a monthly basis](https://dev.wix.com/docs/rest/crm/loyalty-program/example-flows#message-site-members-with-their-loyalty-points-balance-on-a-monthly-basis)

## Terminology

* **Program name:** Customizable name of the program.
* **Point:** The collectible unit of the program.
* **Customer:** Must have a site contact ID to create a loyalty account.
* **Account:** An individual customer's loyalty account tracks their current point balance, as well as, their total points earned and redeemed historically.
