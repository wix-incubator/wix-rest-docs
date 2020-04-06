# About Carts
The Wix Stores Carts APIs provide your app with access to the site's customers' cart data.

<blockquote class='important'>
<p>
  <strong>Important:</strong><br/>
This Carts API will be deprecated in the second half of 2020, when a completely new version will be deployed.
</p>
</blockquote>

A cart is created the first time a visitor adds something to their cart.

A cart is considered abandoned once it has been idle for 1 hour.

The Abandoned Cart Webhook is triggered only for carts of site members who are logged in to the site, or for visitors who entered their email address in the checkout process before abandoning their cart.

## Use Case - Abandoned Cart Email Reminder
1. Listen to the [Cart Abandoned](https://dev.wix.com/api/wix-stores#carts.abandoned-carts.cartabandonedevent) and the [Cart Recovered](https://dev.wix.com/api/wix-stores#carts.abandoned-carts.cartrecoveredevent) webhooks.
<blockquote class='note'>
<p>
  <strong>Note:</strong><br/>
To ensure up-to-date information, you can also call the  <a href:"https://dev.wix.com/api/wix-stores#carts.abandoned-carts.get-abandoned-cart">Get Abandoned Carts</a> endpoint at regular intervals.
</p>
</blockquote>
2. When a cart status is changed to Abandoned (an hour after the last cart activity), call the [Get Cart Checkout URL](https://dev.wix.com/api/wix-stores#carts.carts.get-cart-checkout-url) and/or [Get Cart](https://dev.wix.com/api/wix-stores#carts.carts.get-cart) endpoints, as necessary.  
3. Enter the relevant cart information into the email to send to the customer reminding them to complete their order.
<blockquote class='note'>
<p>
  <strong>Note: </strong><br/>
If you receive a Cart Recovered webhook before the email is sent, cancel the email - the customer has already completed their order.
</p>
</blockquote>

## Testing 
Wix site owners can view all abandoned carts in their Wix Dashboard under Stores Orders > Abandoned Carts.
