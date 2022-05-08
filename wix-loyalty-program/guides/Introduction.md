SortOrder: 0
# About Wix Loyalty Program

With Loyalty site owners can create a loyalty program to increase customer retention. It allows customers to earn points that they can then redeem for rewards. Each Wix site can have only one loyalty program.

Loyalty APIs allow you to set up and manage a site’s loyalty program, including settings, customer accounts, and rewards. In the UI, site owners can define automations to give customers points for certain actions, which are not accessible via API. See [Loyalty](https://support.wix.com/en/article/wix-loyalty-program-an-overview) for more details.

Loyalty APIs allow your app to:

* Set up the program 
* Customize program and point name, point icon, and description
* Create and manage rewards
* Create customer accounts
* Manage account point balances

## Terminology

* **Program name:** Customizable name of the program.
* **Point name:** Customizable name for the points used in the program.
* **Point Icon:** Customizable icon for the points used in the program.
* **Reward:** Defines how many points are needed to get a specific benefit.
* **Program description: ** Customizable description of the program that can include text, rich content text, links, pictures, and buttons.
*  **Account:** Every customer has an account that tracks the point balance, earned and redeemed points. 

## Limitations

* There can only be one loyalty program per Wix site.
* Every Wix site comes with a pre-installed loyalty program in `DRAFT` status.
* Customers cannot earn or redeem points while the program is not `ACTIVE`.
* Only programs that have been set up by the site owners in the Business Manager or by calling the [Update Loyalty Program](https://dev.wix.com/api/rest/loyalty/update-loyalty-program) endpoint can be activated.
* Each customer can only have one account.
* Currently, your app cannot set automatic earning rules for purchases.