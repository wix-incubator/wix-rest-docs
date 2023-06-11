SortOrder: 2
# Stores to eCommerce Cart Conversion Table

To help with migration from the [Stores Cart API](https://dev.wix.com/api/rest/wix-stores/carts/cart-object) to the eCommerce [Cart](https://dev.wix.com/api/rest/wix-ecommerce/cart/cart-object) and [Checkout](https://dev.wix.com/api/rest/wix-ecommerce/checkout/introduction) APIs, refer to the table below for field changes in name and/or location.

Certain information that used to be held in the Cart, is now kept in the Checkout object. These fields are marked in the table below, with more information available in the [Stores Cart to eCommerce Checkout Conversion Table](https://dev.wix.com/api/rest/wix-ecommerce/checkout/stores-cart-to-ecommerce-checkout-object-conversion).

The address object used in the eCommerce APIs is slightly different to the one used in the Stores APIs. For more details, refer to the [address object conversion table](https://dev.wix.com/api/rest/wix-ecommerce/cart/address-object-conversion).

Fields marked with an asterisk (*) signify little to no change in semantics or service location.


| Stores Cart                                        | eCommerce Cart                                              |
| ---------------------------------------------------|-------------------------------------------------------------|
| `id`*                                              | `id`                                                        |
| `status`                                           | All carts in the eCommerce Cart API have a status value of `INCOMPLETE`. After a purchase, the cart is deleted and the [Cart Deleted Webhook](https://dev.wix.com/api/rest/wix-ecommerce/cart/cart-deleted-webhook) is triggered. Any attempt to retrieve it via the [Get Cart](https://dev.wix.com/api/rest/wix-ecommerce/cart/get-cart) endpoint will yield a 404 error code. In the Stores Cart API, the cart's status would change to `COMPLETE` after a purchase. |
| `weightUnit`*                                      | `weightUnit`                                               |
| `buyerNote`*                                       | `buyerNote`                                               |
| `currency.code`                                    | `currency`                                    |
| `currency.symbol`                                  | No longer returned. Instead, for every price returned, we also provide the formatted price.                                          |
| `convertedCurrency.code`                           | `conversionCurrency`                          |
| `convertedCurrency.symbol`                         | No longer returned. Instead, for every converted price returned, we also provide the formatted converted price.                                             |
| `billingAddress`                                   | Billing address is no longer kept in the Cart. This information is only kept in [Checkout](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object).   |
| `appliedCoupon.couponId`                           | `appliedDiscounts[i].coupon.id` - The coupon is now an item in the `appliedDiscounts` array. To get it, search the `appliedDiscounts` array for the only populated `coupon` field.                                               |
| `appliedCoupon.code`                               | `appliedDiscounts[i].coupon.code` - The coupon is now an item in the `appliedDiscounts` array. To get it, search the `appliedDiscounts` array for the only populated `coupon` field.                                               |
| `appliedCoupon.name`                               | This field is held only in the [Checkout object](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object) under `appliedDiscounts[i].coupon.name`.                                               |
| `appliedCoupon.discountValue`                      | This field is held only in the [Checkout object](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object) under `appliedDiscounts[i].coupon.amount.amount`.                                 |
| `appliedCoupon.convertedDiscountValue`             | This field is held only in the [Checkout object](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object) under `appliedDiscounts[i].coupon.amount.convertedAmount`.                               |
| `appliedCoupon.couponType`                         | No longer returned.                                         |                            |
| `totals`                   | Future functionality will see this information made available in the eCommerce Cart API.                                               |                                             |
| `convertedTotals`          | Future functionality will see this information made available in the eCommerce Cart API.                                                   |
| `shippingInfo`        | Shipping information is now only kept in [Checkout](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object).                                              |
| `buyerInfo.id` and `buyerInfo.identityType: CONTACT`| `buyerInfo.contactId` only.                                               |
| `buyerInfo.id` and `buyerInfo.identityType: VISITOR`| `buyerInfo.visitorId` only.                                              |
| `buyerInfo.id` and `buyerInfo.identityType: MEMBER` | `buyerInfo.memberId` only.                                               |
| `buyerInfo.email`     | Buyer email is now only kept in [Checkout](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object).                                               |
| `buyerInfo.phone`     | Buyer phone is now only kept in [Checkout](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object).                                               |
| `buyerInfo.firstName` | Buyer first name is now only kept in [Checkout](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object).                                               |
| `buyerInfo.lastName`  | Buyer last name is now only kept in [Checkout](https://dev.wix.com/api/rest/wix-ecommerce/checkout/checkout-object).                                               |
| `lineItems[i].id`                                | `lineItems[i].id` - **Note:** this `id` is of type GUID. In the Stores Cart API, the `lineItem.id` is of type Int32.                                              |
| `lineItems[i].productId`                         | `lineItems[i].catalogReference.catalogItemId` - See [Stores Catalog eCommerce Integration](https://bo.wix.com/wix-docs/rest/stores/stores-catalog/ecommerce-integration) for more information. |
| `lineItems[i].name`                              | `lineItems[i].productName.original`                          |
| `lineItems[i].quantity`                          | `lineItems[i].quantity`                          |
| `lineItems[i].weight`                            | `lineItems[i].physicalProperties.weight`                  |
| `lineItems[i].sku`                               | `lineItems[i].physicalProperties.sku`                                               |
| `lineItems[i].lineItemType: "PHYSICAL"`          | `lineItems[i].itemType.preset: "PHYSICAL"`                                |
| `lineItems[i].lineItemType: "DIGITAL"`           | `lineItems[i].itemType.preset: "DIGITAL"`                               |
| `lineItems[i].lineItemType: "CUSTOM_AMOUNT_ITEM"`| `lineItems[i].itemType.custom` and `lineItems[i].catalogReference` is empty.                               |
| `lineItems[i].notes`                             | `lineItems[i].descriptionLines[i].plainText.original`                                               |
| `lineItems[i].customTextFields`                  | `lineItems[i].descriptionLines`                                             |
| `lineItems[i].mediaItem.mediaType`               | All line item media in the Cart API are images. |
| `lineItems[i].mediaItem.url`                     | `lineItems[i].media.url`                                               |
| `lineItems[i].mediaItem.width`                   | `lineItems[i].media.width`                                               |
| `lineItems[i].mediaItem.height`                  | `lineItems[i].media.height`                                               |
| `lineItems[i].options`                           | `lineItems[i].descriptionLines` - See [Stores Catalog eCommerce Integration](https://bo.wix.com/wix-docs/rest/stores/stores-catalog/ecommerce-integration) for more information.
| `lineItems[i].priceData.price`                   | `lineItems[i].price.amount`                                               |
| `lineItems[i].priceData.totalPrice`              | `lineItems[i].price.amount` X `lineItems[i].quantity`                                 |
| `lineItems[i].convertedPriceData.price`          | `lineItems[i].price.convertedAmount`                                               |
| `lineItems[i].convertedPriceData.totalPrice`     | `lineItems[i].price.convertedAmount` X `lineItems[i].quantity`                            |