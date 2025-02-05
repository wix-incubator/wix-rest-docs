# About Wix Business Solutions

Wix offers a range of powerful business solutions that extend the functionalities of its existing products or add new capabilities. Wix business solutions are apps created by Wix that Wix users can use to enhance their sites. A Wix user can install one or more Wix business solutions o manage specific data on their site. 

You may want to access site data that is managed by a Wix business solution. When making API calls to access Wix site data, some API calls require a reference to the specific Wix business solution. For example, to add a comment with [`Create Comment`](https://dev.wix.com/docs/rest/api-reference/comments/comments/create-comment) API, pass an `appId` to specify where to create the comment, such as in Wix Blog. 

Other API calls may return a reference to the Wix business solution. For example, calling the [`Get a Coupon`](https://dev.wix.com/docs/rest/api-reference/coupons/coupons/get-a-coupon) API returns a coupon object with an `appId` referring to the ID of the Wix business solution that created the coupon, such as Wix Bookings or Wix Events. 

See the following Wix business solution and their corresponding IDs. Regardless of the API call, each Wix business solution always has the same `app ID`.

| **Wix Business Solution**    | **App ID**                          |
|------------------------|--------------------------------------|
| Wix Bookings           | 13d21c63-b5ec-5912-8397-c3a5ddb27a97 |
| Wix Blog               | 14bcded7-0066-7c35-14d7-466cb3f09103 |
| Wix eCommerce          | 1380b703-ce81-ff05-f115-39571d94dfcd |
| Wix Events             | 140603ad-af8d-84a5-2c80-a0f60cb47351 |
| Wix Forms              | 14ce1214-b278-a7e4-1373-00cebd1bef7c |
| Wix Hotels             | 135aad86-9125-6074-7346-29dc6a3c9bcf |
| Wix Inbox              | 141fbfae-511e-6817-c9f0-48993a7547d1 |
| Wix Invoices           | 13ee94c1-b635-8505-3391-97919052c16f |
| Wix Music              | 13bb5d67-1add-e770-a71f-001277e17c57 |
| Wix Online Programs    | 2936472a-a1ed-4ae5-9f71-614313a9f4e7 |
| Wix Pay Button         | 3575d251-42c3-4992-adff-170b2af90a2c |
| Wix Pricing Plans      | 1522827f-c56c-a5c9-2ac9-00f9e6ae12d3 |
| Wix Restaurants Orders | 13e8d036-5516-6104-b456-c8466db39542 |
| Wix Stores             | 215238eb-22a5-4c36-9e7b-e7c08025e04e |
| Wix Subscriptions      | 8725b255-2aa2-4a53-b76d-7d3c363aaeea |
| Wix Video              | 14409595-f076-4753-8303-9a86f9f71469 |

