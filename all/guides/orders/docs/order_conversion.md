SortOrder: 3
# Stores to eCommerce Order Object Conversion

To help with migration to the eCommerce Orders API, refer to the table below for field changes between the [Stores order object](https://dev.wix.com/docs/rest/api-reference/wix-stores/orders/orders-object) and the [eCommerce order object](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-object).

Note that some fields are accessible via other eCommerce APIs like [Order Transactions](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction) or [Order Fulfillments](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-fulfillments/introduction). In these cases, the way to access the info is described in the third column.

The address object used in the eCommerce APIs is slightly different to the one used in the Stores APIs. For more details, refer to the [address object conversion table](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/address-object-conversion).

The eCommerce [Order Updated event](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-updated) fires when a Stores order and/or an eCommerce order is updated.
For more details on webhooks, refer to the [Webhook Conversion Table](#Webhook-Conversion-Table) below.

Fields marked with an asterisk (*) signify little to no change in semantics or access.

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
| `totals.weight`                                             | An order's total weight is equal to `(lineItems[0].physicalProperties.weight` X `lineItems[0].quantity)` + `(lineItems[1].physicalProperties.weight` X `lineItems[1].quantity)` and so on. |
| `totals.quantity`                                           | An order's total line item quantity is equal to `lineItems[0].quantity` + `lineItems[1].quantity` + `lineItems[2].quantity` and so on.    |
| `totals.refund`                                             | Available via the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).                                  | Pass the order ID to the [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) endpoint to retrieve this info.
| `totals.giftCard`                                           | Available via the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).                                  | Pass the order ID to the [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) endpoint to retrieve this info.
| `billingInfo.paymentMethod`                                 | Available via the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).                                  | Pass the order ID to the [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) endpoint to retrieve this info.
| `billingInfo.paymentProviderTransactionId`                  | Available via the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).                                  | Pass the order ID to the [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) endpoint to retrieve this info.
| `billingInfo.paymentGatewayTransactionId`                   | Available via the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).                                  | Pass the order ID to the [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) endpoint to retrieve this info.
| `billingInfo.paidDate`                                      | Available via the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).                                  | Pass the order ID to the [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) endpoint to retrieve this info.
| `billingInfo.refundableByPaymentProvider`                   | Available via the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).                                  | Pass the order ID to the [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) endpoint to retrieve this info.
| `billingInfo.address`*                                      | `billingInfo.address`                                                     | [Address object conversion table](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/address-object-conversion).
| `shippingInfo.code`*                                        | `shippingInfo.code`                                                       |
| `shippingInfo.deliverByDate`                                | `shippingInfo.logistics.deliverByDate`                                    |
| `shippingInfo.deliveryOption`                               | `shippingInfo.title`                                                      |
| `shippingInfo.shippingRegion`                               | `shippingInfo.region.name`                                                |
| `shippingInfo.shippingDetails.address`                      | `shippingInfo.logistics.shippingDestination.address`                      | [Address object conversion table](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/address-object-conversion).
| `shippingInfo.shipmentDetails.discount`                     | `shippingInfo.cost.discount.amount`                                       |
| `shippingInfo.shipmentDetails.tax`                          | `shippingInfo.cost.taxDetails.totalTax.amount`                            |
| `shippingInfo.shipmentDetails.priceData.taxIncludedInPrice` | `taxIncludedInPrices`                                                                         |
| `shippingInfo.shipmentDetails.priceData.price`              | `shippingInfo.cost.totalPriceAfterTax.amount`                             |
| `shippingInfo.pickupDetails.pickupAddress`                  | `shippingInfo.logistics.pickupDetails.address`                            | [Address object conversion table](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/address-object-conversion).
| `shippingInfo.pickupDetails.pickupInstructions`             | `shippingInfo.logistics.instructions`                                     |
| `shippingInfo.estimatedDeliveryTime`                        | `shippingInfo.logistics.deliveryTime`                                     |
| `buyerNote`*                                                | `buyerNote`                                                               |
| `archived`*                                                 | `archived`                                                                |
| `paymentStatus`*                                            | `paymentStatus`                                                           |
| `paymentStatus: PENDING`                                    | `status: INITIALIZED`                                                        |
| `fulfillmentStatus`*                                        | `fulfillmentStatus`                                                          | For more info, pass an order ID to the [List Fulfillments For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-fulfillments/list-fulfillments-for-single-order) endpoint.
| `fulfillmentStatus: CANCELED`                               | `status: CANCELED`                                                           |
| `lineItems[i].index`                                        | `lineItems[i].id`                                                            | While the `lineItems[i].index` in Stores Orders was an int32 type, the eCommerce Order's `lineItems[i].id` field is of type GUID.
| `lineItems[i].quantity`*                                    | `lineItems[i].quantity`                                                      |
| `lineItems[i].name`                                         | `lineItems[i].productName.original`                                          |
| `lineItems[i].translatedName`                               | `lineItems[i].productName.translated`                                        |
| `lineItems[i].productId`                                    | `lineItems[i].catalogReference.catalogItemId`                                | The `catalogReference` object links between eCommerce APIs and catalogs like Wix Stores. Learn more about [eCommerce integration for Wix Stores](https://dev.wix.com/docs/rest/api-reference/wix-stores/catalog/e-commerce-integration).
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
| `lineItems[i].variantId`                                    | `lineItems[i].catalogReference.options`                                      | The `catalogReference` object links between eCommerce APIs and catalogs like Wix Stores. Learn more about [eCommerce integration for Wix Stores](https://dev.wix.com/docs/rest/api-reference/wix-stores/catalog/e-commerce-integration).
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
| `invoiceInfo`                                               | Not available in eCommerce order object.                                     | Currently, this information is held in the Stores order object.
| `fulfillments`                                              | Not available in eCommerce order object.                                     | For more info, pass an order ID to the [List Fulfillments For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-fulfillments/list-fulfillments-for-single-order) endpoint.
| `discount.appliedCoupon.couponId`                           | `appliedDiscounts[i].coupon.id`   | Search the `appliedDiscounts` array for the `coupon` field; `couponId` is `coupon.id`
| `discount.appliedCoupon.name`                               | `appliedDiscounts[i].coupon.name` | Search the `appliedDiscounts` array for the `coupon` field; `name` is `coupon.name`
| `discount.appliedCoupon.code`                               | `appliedDiscounts[i].coupon.code` | Search the `appliedDiscounts` array for the `coupon` field; `code` is `coupon.code`
| `customField.value`                                         | `customFields[i].value.stringValue`                                       | Note: `customFields` is an array
| `customField.title`                                         | `customFields[i].title`                                                   |
| `customField.translatedTitle`                               | `customFields[i].translatedTitle`                                         |
| `cartId`                                                    | Not returned in the eCommerce order object.                               | Replaced by `checkoutId`
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
| `refunds`                                                   | Not available in eCommerce order object.                                  | Pass the order ID to the [List Transactions For Single Order](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/list-transactions-for-single-order) endpoint to retrieve this info.

*Fields marked with an asterisk signify little to no change in semantics or access.


## Webhook Conversion Table

The following table shows Stores Orders webhooks and their equivalents in the eCommerce Orders API that are triggered at the same time:

| Stores Orders API                                                                                        | eCommerce Orders API                                                                         |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [Order Paid Webhook](https://dev.wix.com/docs/rest/api-reference/wix-stores/orders/order-paid)           | [Payment Status Updated Webhook](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/payment-status-updated) sent with `order.paymentStatus = PAID` |
| [Order Created Webhook](https://dev.wix.com/docs/rest/api-reference/wix-stores/orders/order-created)     | [Order Approved Webhook](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-approved)  |
| [Order Canceled Webhook](https://dev.wix.com/docs/rest/api-reference/wix-stores/orders/order-canceled)   | [Order Canceled Webhook](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-canceled) |
| [Order Refunded Webhook](https://dev.wix.com/docs/rest/api-reference/wix-stores/orders/order-refunded)   | [Order Transactions Updated Webhook](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/order-transactions-updated) |


We've also updated the structure of the webhook/event payload. The event's order ID is now provided both at the top level as `entityId` and as `order.id` within the payload itself. The table below describes where to find the order ID or order entity in the new webhook payloads:

| Stores Webhooks                                    | eCommerce Webhooks                                                        |
| ---------------------------------------------------|---------------------------------------------------------------------------|
| Order ID - `order.id` / `orderId`                  | All order webhook payloads - `entityId`                                   |
| Order Created - the payload itself is the order    | Order Approved - `actionEvent.body.order`                                 |
| Order Paid/Canceled/Refunded - `order`             | Order Canceled/Approved - `actionEvent.body.order`                        |
| -                                                  | Order Updated - `updatedEvent.currentEntity`                              |