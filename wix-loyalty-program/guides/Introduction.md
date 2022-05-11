SortOrder: 0
# About Wix Loyalty Program

With Wix Loyalty Program, site owners can create a loyalty program to increase customer retention. It allows customers to earn points that they can then redeem for rewards. Each Wix site can have only one loyalty program.

Loyalty APIs allow you to set up and manage a site’s loyalty program, including program details and customer accounts. In the UI, site owners can define automations to give customers points for certain actions, which are not accessible via API. See [Wix Loyalty Program: An Overview](https://support.wix.com/en/article/wix-loyalty-program-an-overview) for more details.

Loyalty APIs allow your app to:

* Set up the program 
* Customize the program, point name, point icon and description
* Create customer accounts
* Manage account point balances

## Terminology

* **Program name:** Customizable name of the program.
* **Point name:** Customizable name for the points used in the program.
* **Point icon:** Customizable icon for the points used in the program.
* **Program description:** Customizable description of the program that can include text, rich content text, links, pictures, and buttons.
* **Account:** Every customer has an account that tracks their point balance, points earned and points redeemed. 

## Limitations

* There can only be one loyalty program per Wix site.
* Every Wix site comes with a pre-installed loyalty program in `DRAFT` status.
* Customers cannot earn or redeem points while the program is not `ACTIVE`.
* Only programs that have been set up by the site owners in the Business Manager or by calling the [Update Loyalty Program](https://dev.wix.com/api/rest/loyalty/update-loyalty-program) endpoint can be activated.
* Each customer can only have one account.
* Currently, your app cannot set automatic earning rules for purchases. You can set them up in the UI, see [this article](https://support.wix.com/en/article/wix-loyalty-program-an-overview) to learn how.