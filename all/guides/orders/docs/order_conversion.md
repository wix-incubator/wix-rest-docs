SortOrder: 2
# Stores to eCommerce Order Object Conversion

To help with migration to the eCommerce Orders API, refer to the table below for field changes between the [Stores order object](https://dev.wix.com/api/rest/wix-stores/orders/order-object) and the [eCommerce order object](https://dev.wix.com/api/rest/wix-ecommerce/orders/order-object).

Note that some fields are accessible via other eCommerce APIs. In these cases, the field in the 2nd column refers to its
location in the other API, which is specified in the 3rd column.

The address object used in the eCommerce APIs is slightly different to the one used in the Stores APIs. For more details, refer to the [address object conversion table](https://dev.wix.com/api/rest/wix-ecommerce/orders/address-object-conversion).

Fields marked with an asterisk (*) signify little to no change in semantics or access.

For details on webhooks, refer to the [Webhook Conversion Table](#Webhooks-Conversion-Table) below.

## Order Object Conversion Table
| Stores Order Object                                         | eCommerce Order Object                                                    | Notes                                             |
| ------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------|
| `id`*                                                       | `id`                                                                      |
| `number`*                                                   | `number`                                                                  |
| `dateCreated`                                               | `createdDate`                                                             |
| `buyerInfo.id`                                              | `buyerInfo.contactId` & `buyerInfo.memberId`                              |
| `buyerInfo.id` and `buyerInfo.identityType: "MEMBER"`       | `buyerInfo.memberId`                                                      |
| `buyerInfo.id` and `buyerInfo.identityType: "CONTACT"`      | `buyerInfo.contactId`                                                     |
| `buyerInfo.firstName`                                       | `billingInfo.contactDetails.firstName`                                    |
| `buyerInfo.lastName`                                        | `billingInfo.contactDetails.lastName`                                     |
| `buyerInfo.phone`                                           | `billingInfo.contactDetails.phone`                                        |
| `buyerInfo.email`*                                          | `buyerInfo.email`                                                         |
| `currency`*                                                 | `currency`                                                                |
| `weightUnit`*                                               | `weightUnit`                                                              |
| `totals.subtotal`                                           | `priceSummary.subtotal.amount`                                            |
| `totals.shipping`                                           | `priceSummary.shipping.amount`                                            |
| `totals.tax`                                                | `priceSummary.tax.amount`                                                 |
| `totals.discount`                                           | `priceSummary.discount.amount`                                            |
| `totals.total`                                              | `priceSummary.total.amount`                                               |
| `totals.weight`                                             | An order's total weight equals `(lineItems[0].physicalProperties.weight` X `lineItems[0].quantity)` + `(lineItems[1].physicalProperties.weight` X `lineItems[1].quantity)` and so on. |
| `totals.quantity`                                           | An order's total line item quantity equals `lineItems[0].quantity` + `lineItems[1].quantity` + `lineItems[2].quantity` and so on.    |
| `totals.refund`                                             | Not available in eCommerce order object.                                  | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `totals.giftCard`                                           | Not available in eCommerce order object.                                  | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `billingInfo.paymentMethod`                                 | Not available in eCommerce order object.                                  | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `billingInfo.paymentProviderTransactionId`                  | Not available in eCommerce order object.                                  | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `billingInfo.paymentGatewayTransactionId`                   | Not available in eCommerce order object.                                  | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `billingInfo.paidDate`                                      | Not available in eCommerce order object.                                  | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `billingInfo.refundableByPaymentProvider`                   | Not available in eCommerce order object.                                  | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `billingInfo.address`*                                      | `billingInfo.address`                                                     | [Address object conversion table](https://bo.wix.com/wix-docs/rest/ecommerce/orders/address-object-conversion).
| `shippingInfo.code`*                                        | `shippingInfo.code`                                                       |
| `shippingInfo.deliverByDate`                                | `shippingInfo.logistics.deliverByDate`                                    |
| `shippingInfo.deliveryOption`                               | `shippingInfo.title`                                                      |
| `shippingInfo.shippingRegion`                               | `shippingInfo.region.name`                                                |
| `shippingInfo.shippingDetails.address`                      | `shippingInfo.logistics.shippingDestination.address`                      | [Address object conversion table](https://bo.wix.com/wix-docs/rest/ecommerce/orders/address-object-conversion).
| `shippingInfo.shipmentDetails.discount`                     | `shippingInfo.cost.discount.amount`                                       |
| `shippingInfo.shipmentDetails.tax`                          | `shippingInfo.cost.taxDetails.totalTax.amount`                            |
| `shippingInfo.shipmentDetails.priceData.taxIncludedInPrice` | `taxIncludedInPrices`                                                                         |
| `shippingInfo.shipmentDetails.priceData.price`              | `shippingInfo.cost.totalPriceAfterTax.amount`                             |
| `shippingInfo.pickupDetails.pickupAddress`                  | `shippingInfo.logistics.pickupDetails.address`                            | [Address object conversion table](https://bo.wix.com/wix-docs/rest/ecommerce/orders/address-object-conversion).
| `shippingInfo.pickupDetails.pickupInstructions`             | `shippingInfo.logistics.instructions`                                     |
| `shippingInfo.estimatedDeliveryTime`                        | `shippingInfo.logistics.deliveryTime`                                     |
| `buyerNote`*                                                | `buyerNote`                                                               |
| `archived`*                                                 | `archived`                                                                |
| `paymentStatus`*                                            | `paymentStatus`                                                           |
| `paymentStatus: PENDING`                                | `status: INITIALIZED`                                                 |
| `fulfillmentStatus`*                                        | `fulfillmentStatus`                                                       | Future functionality will see more information made available in the eCommerce API.
| `fulfillmentStatus: CANCELED`                           | `status: CANCELED`                                                    | Future functionality will see more information made available in the eCommerce API.
| `lineItems[i].index`                                        | `lineItems[i].id`                                                            | While `lineItems[i].index` was an int32 type, the eCommerce Order's `lineItems[i].id` field is of type GUID.
| `lineItems[i].quantity`*                                    | `lineItems[i].quantity`                                                      |
| `lineItems[i].name`                                         | `lineItems[i].productName.original`                                          |
| `lineItems[i].translatedName`                               | `lineItems[i].productName.translated`                                        |
| `lineItems[i].productId`                                    | `lineItems[i].catalogReference.catalogItemId`                                | See [Stores Catalog eCommerce Integration](https://bo.wix.com/wix-docs/rest/stores/stores-catalog/ecommerce-integration) for more information.
| `lineItems[i].lineItemType: "PHYSICAL"`                     | `lineItems[i].itemType.preset: "PHYSICAL"`                                   |
| `lineItems[i].lineItemType: "DIGITAL"`                      | `lineItems[i].itemType.preset: "DIGITAL"`                                    |
| `lineItems[i].lineItemType: "CUSTOM_AMOUNT_ITEM"`           | `lineItems[i].itemType.custom` and `lineItems[i].catalogReference` is empty.                                     |
| `lineItems[i].options`                                      | `lineItems[i].descriptionLines`                                      |
| `lineItems[i].customTextFields`                             | `lineItems[i].catalogReference.options`                                      | Within the `catalogReference.options` look for the `customTextFields` key.
| `lineItems[i].weight`                                       | `lineItems[i].physicalProperties.weight`                                     |
| `lineItems[i].mediaItem.url`                                | `lineItems[i].image.url`                                                     |
| `lineItems[i].mediaItem.height`                             | `lineItems[i].image.height`                                                  |
| `lineItems[i].mediaItem.width`                              | `lineItems[i].image.width`                                                   |
| `lineItems[i].mediaItem.id`                                 | `lineItems[i].image.id`                                                      |
| `lineItems[i].mediaItem.altText`                            | `lineItems[i].image.altText`                                                 |
| `lineItems[i].sku`                                          | `lineItems[i].physicalProperties.sku`                                        |
| `lineItems[i].notes`                                        | `lineItems[i].descriptionLines[i].plainText.original`                   |
| `lineItems[i].variantId`                                    | `lineItems[i].catalogReference.options`                                      | See [Stores Catalog eCommerce Integration](https://bo.wix.com/wix-docs/rest/stores/stores-catalog/ecommerce-integration) for more information.
| `lineItems[i].fulfillerId`*                                 | `lineItems[i].fulfillerId`                                                   |
| `lineItems[i].discount`                                     | `lineItems[i].totalDiscount.amount`                                          |
| `lineItems[i].tax`                                          | `lineItems[i].taxDetails.totalTax.amount`                                    |
| `lineItems[i].priceData.taxIncludedInPrice`                 | `taxIncludedInPrices`                                                        |
| `lineItems[i].priceData.price`                              | `lineItems[i].price.amount`                                                  |
| `lineItems[i].priceData.totalPrice`                         | `lineItems[i].totalPriceAfterTax.amount`                                     |
| `activities[i].type`*                                       | `activities[i].type`                                                         |
| `activities[i].TRACKING_LINK_WAS_SET`                       | `activities[i].TRACKING_LINK_SET`                                            |
| `activities[i].INVOICE_WAS_SET`                             | `activities[i].INVOICE_ADDED`                                                |
| `activities[i].INVOICE_WAS_SENT`                            | `activities[i].INVOICE_SENT`                                                 |
| `activities[i].author`                                      | `activities[i].authorEmail`                                                  |
| `activities[i].message`                                     | `activities[i].merchantComment.message`                                      | If `activities.type = "MERCHANT_COMMENT"`
| `activities[i].timestamp`                                   | `activities[i].createdDate`                                                  |
| `invoiceInfo`                                               | Not available in eCommerce order object.                                     | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `fulfillments`                                              | Not available in eCommerce order object.                                      | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.
| `discount.appliedCoupon.couponId`                           | `appliedDiscounts[i].coupon.id`   | Search the `appliedDiscounts` array for the `coupon` field; `couponId` is `coupon.id`
| `discount.appliedCoupon.name`                               | `appliedDiscounts[i].coupon.name` | Search the `appliedDiscounts` array for the `coupon` field; `name` is `coupon.name`
| `discount.appliedCoupon.code`                               | `appliedDiscounts[i].coupon.code` | Search the `appliedDiscounts` array for the `coupon` field; `code` is `coupon.code`
| `customField.value`                                         | `customFields[i].value.stringValue`                                       | Note: `customFields` is an array
| `customField.title`                                         | `customFields[i].title`                                                   |
| `customField.translatedTitle`                               | `customFields[i].translatedTitle`                                         |
| `cartId`                                                    | No longer returned.                                                                         | Replaced by `checkoutId`
| `buyerLanguage`*                                            | `buyerLanguage`                                                           |
| `channelInfo.type`*                                         | `channelInfo.type`                                                        |
| `channelInfo.externalOrderId`*                              | `channelInfo.externalOrderId`                                             |
| `channelInfo.externalOrderUrl`*                             | `channelInfo.externalOrderUrl`                                            |
| `enteredBy.id` and `enteredBy.identityType: "MEMBER"`       | `createdBy.memberId`                                                      |
| `enteredBy.id` and `enteredBy.identityType: "USER"`         | `createdBy.userId`                                                        |
| `enteredBy.id` and `enteredBy.identityType: "APP"`          | `createdBy.appId`                                                         |
| `enteredBy.id` and `enteredBy.identityType: "CONTACT"`      | `createdBy.visitorId` | Previously, for a buyer that is not logged in, `CONTACT` type and ID were returned. in the eCommerce API, `visitorId` is returned. Note: the ID itself will also be different.
| `lastUpdated`                                               | `updatedDate`                                                             |
| `numericId`                                                 | -                                                                         | Removed due to added cursor paging functionality
| `refunds`                                                   | Not available in eCommerce order object.                                  | Currently, this information is held in the Stores order object. Pass `order.id` to the [Stores Get Order](https://dev.wix.com/api/rest/wix-stores/orders/get-order) endpoint. Future functionality will see this information made available in the eCommerce API.

*Fields marked with an asterisk signify little to no change in semantics or access.


## Webhooks Conversion Table

The following list shows Stores Orders webhooks and the eCommerce webhooks (across Orders, Order Payments, and Order Fulfillments) that are triggered at the same time:

| Stores Orders API                                                                         | eCommerce Orders API                                                         |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [Order Paid Webhook](https://dev.wix.com/api/rest/wix-stores/orders/order-paid-webhook) | Orders - [Payment Status Updated Webhook](https://dev.wix.com/api/rest/wix-ecommerce/orders/payment-status-updated-webhook) sent with `order.paymentStatus = PAID` |
| [Order Created Webhook](https://dev.wix.com/api/rest/wix-stores/orders/order-created-webhook) | Orders - [Order Approved Webhook](https://dev.wix.com/api/rest/wix-ecommerce/orders/order-approved-webhook)  |
| [Order Canceled Webhook](https://dev.wix.com/api/rest/wix-stores/orders/order-canceled-webhook) | Orders - [Order Canceled Webhook](https://dev.wix.com/api/rest/wix-ecommerce/orders/order-canceled-webhook) |
| Fulfillment [Created](https://dev.wix.com/api/rest/wix-stores/orders/fulfillment-created-webhook) / [Updated](https://dev.wix.com/api/rest/wix-stores/orders/fulfillment-updated-webhook) / [Deleted](https://dev.wix.com/api/rest/wix-stores/orders/fulfillment-deleted-webhook) Webhooks | [Fulfillment Status Updated Webhook](https://dev.wix.com/api/rest/wix-ecommerce/orders/fulfillment-status-updated-webhook) |