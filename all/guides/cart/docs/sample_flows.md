SortOrder: 1
# Sample Flows

This article shares some possible use cases your app could support, as well as an example flow that could support each
use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your
app's implementation.

## Update a cart 

If a store owner wants to update a specific cart with a buyer note and remove a coupon, they can follow this basic flow.

1. Use [Update Cart](https://dev.wix.com/api/rest/wix-ecommerce/cart/update-cart) to add a buyer note to a specific cart:

   ```js
   curl -X PATCH \
     'https://www.wixapis.com/ecom/v1/carts/f97a2939-b1f3-41f2-9fc5-7ecea2060991' \
     -H 'Authorization: <AUTH>' \
     -H 'Content-Type: application/json' \
     -d '{
       "cartInfo": {
        "id": "a97a2939-b1f3-41f2-9fc5-7ecea2060974",
        "buyerNote": "Please ship ASAP."
       }
     }'
   ```
   The response is the cart object containing the newly added buyer note.

2. Use [Remove Coupon](https://dev.wix.com/api/rest/wix-ecommerce/cart/remove-coupon) to remove a coupon from a cart.

   ```js
   curl -X POST \
     'https://www.wixapis.com/ecom/v1/carts/a97a2939-b1f3-41f2-9fc5-7ecea2060974/remove-coupon' \
     -H 'Authorization: <AUTH>'
     -H 'Content-Type: application/json' \
   ```
