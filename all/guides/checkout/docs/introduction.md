SortOrder: 0
# About the eCommerce Checkout API

The checkout is the second stage of the eCommerce purchase flow: cart; checkout; order.

A checkout holds information about items to be purchased, price and tax summaries, shipping and billing info, any applied discounts, and more.

The eCommerce Checkout API currently provides functionality for [retrieving](https://dev.wix.com/api/rest/wix-ecommerce/checkout/get-checkout) checkouts and listening to events when a checkout is [created](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-created-webhook), [updated](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-updated-webhook), and [marked as completed](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-marked-as-completed-webhook).

To assist in migration from the Stores to eCommerce APIs, please refer to the [Stores Cart to eCommerce Checkout Conversion Table](https://dev.wix.com/api/rest/wix-ecommerce/checkout/stores-cart-to-ecommerce-checkout-object-conversion).

Future functionality includes creating and managing checkouts, as well as creating an order from a checkout.