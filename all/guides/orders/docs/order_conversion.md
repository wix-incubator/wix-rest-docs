SortOrder: 2
# Order Object Conversion Table

To help with migration to the eCommerce Orders API, refer to the table below for field changes in the new Order object.

| Stores Orders                                               | eCommerce Orders                                                          | Notes                                             |
| ------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------|
| `id`                                                        | `id`                                                                      |
| `number`                                                    | `number`                                                                  |
| `dateCreated`                                               | `createdDate`                                                             |
| `buyerInfo.id`                                              | `buyerInfo.contactId` & `buyerInfo.memberId`                              |
| `buyerInfo.id` && `buyerInfo.identityType: "MEMBER"`        | `buyerInfo.memberId`                                                      |
| `buyerInfo.id` && `buyerInfo.identityType: "CONTACT"`       | `buyerInfo.contactId`                                                     |
| `buyerInfo.firstName`                                       | `billingInfo.contactDetails.firstName`                                    |
| `buyerInfo.lastName`                                        | `billingInfo.contactDetails.lastName`                                     |
| `buyerInfo.phone`                                           | `billingInfo.contactDetails.phone`                                        |
| `buyerInfo.email`                                           | `buyerInfo.email`                                                         |
| `currency`                                                  | `currency`                                                                |
| `weightUnit`                                                | `weightUnit`                                                              |
| `totals.subtotal`                                           | `priceSummary.subtotal.amount`                                            |
| `totals.shipping`                                           | `priceSummary.shipping.amount`                                            |
| `totals.tax`                                                | `priceSummary.tax.amount`                                                 |
| `totals.discount`                                           | `priceSummary.discount.amount`                                            |
| `totals.total`                                              | `priceSummary.totalPrice.amount`                                          |
| `totals.weight`                                             | - | `(lineItems[0].physicalProperties.weight` X `lineItems[0].quantity)` + `(lineItems[1].physicalProperties.weight` X `lineItems[1].quantity)` and so on.
| `totals.quantity`                                           | -                                             | `lineItems[0].quantity` + `lineItems[1].quantity` and so on.
| `totals.refund`                                             | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
| `totals.giftCard`                                           | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
| `billingInfo.paymentMethod`                                 | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
| `billingInfo.paymentProviderTransactionId`                  | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
| `billingInfo.paymentGatewayTransactionId`                   | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
| `billingInfo.address`                                       | `billingInfo.address`                                                     | [Address object conversion table](https://bo.wix.com/wix-docs/rest/ecommerce/orders/address-object-conversion)
| `billingInfo.paidDate`                                      | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
| `billingInfo.refundableByPaymentProvider`                   | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
| `shippingInfo.code`                                         | `shippingInfo.code`                                                       |
| `shippingInfo.deliverByDate`                                | `shippingInfo.logistics.deliverByDate`                                    |
| `shippingInfo.deliveryOption`                               | `shippingInfo.title`                                                      |
| `shippingInfo.shippingRegion`                               | `shippingInfo.region.name`                                                |
| `shippingInfo.shippingDetails.address`                      | `shippingInfo.logistics.shippingDestination.address`                      | [Address object conversion table](https://bo.wix.com/wix-docs/rest/ecommerce/orders/address-object-conversion)
| `shippingInfo.shipmentDetails.discount`                     | `shippingInfo.cost.discount.amount`                                       |
| `shippingInfo.shipmentDetails.tax`                          | `shippingInfo.cost.taxDetails.totalTax.amount`                            |
| `shippingInfo.shipmentDetails.priceData.taxIncludedInPrice` | -                                                                         | If `shippingInfo.cost.price` == `shippingInfo.cost.totalPriceAfterTax` then tax is included in price
| `shippingInfo.shipmentDetails.priceData.price`              | `shippingInfo.cost.totalPriceAfterTax.amount`                             |
| `shippingInfo.pickupDetails.pickupAddress`                  | `shippingInfo.logistics.pickupDetails.address`                            | [Address object conversion table](https://bo.wix.com/wix-docs/rest/ecommerce/orders/address-object-conversion)
| `shippingInfo.pickupDetails.pickupInstructions`             | `shippingInfo.logistics.instructions`                                     |
| `shippingInfo.estimatedDeliveryTime`                        | `shippingInfo.logistics.deliveryTime`                                     |
| `buyerNote`                                                 | `buyerNote`                                                               |
| `archived`                                                  | `archived`                                                                |
| `paymentStatus`                                             | `paymentStatus`                                                           |
| `paymentStatus` == `PENDING`                                | `status` == `INITIALIZED`                                                 |
| `fulfillmentStatus`                                         | `fulfillmentStatus`                                                       | More info available with the [Order Fulfillments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-fulfillments)
| `fulfillmentStatus` == `CANCELED`                           | `status` == `CANCELED`                                                    | More info available with the [Order Fulfillments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-fulfillments)
| `lineItems.index`                                           | `lineItems.id`                                                            |
| `lineItems.quantity`                                        | `lineItems.quantity`                                                      |
| `lineItems.name`                                            | `lineItems.productName.original`                                          |
| `lineItems.translatedName`                                  | `lineItems.productName.translated`                                        |
| `lineItems.productId`                                       | `lineItems.catalogReference.catalogItemId`                                | [Stores Catalog eCommerce Reference](https://bo.wix.com/wix-docs/rest/stores/stores-catalog/ecommerce-integration)
| `lineItems.lineItemType`                                    | `lineItems.itemType.preset/custom`                                        |
| `lineItems.options`                                         | `lineItems.catalogReference.options`                                      | [Stores Catalog eCommerce Reference](https://bo.wix.com/wix-docs/rest/stores/stores-catalog/ecommerce-integration)
| `lineItems.customTextFields`                                | `lineItems.descriptionLines`                                              |
| `lineItems.weight`                                          | `lineItems.physicalProperties.weight`                                     |
| `lineItems.mediaItem.url`                                   | `lineItems.image.url`                                                     |
| `lineItems.mediaItem.height`                                | `lineItems.image.height`                                                  |
| `lineItems.mediaItem.width`                                 | `lineItems.image.width`                                                   |
| `lineItems.mediaItem.id`                                    | `lineItems.image.id`                                                      |
| `lineItems.mediaItem.altText`                               | `lineItems.image.altText`                                                 |
| `lineItems.sku`                                             | `lineItems.physicalProperties.sku`                                        |
| `lineItems.notes`                                           | `lineItems.descriptionLines.plainTextValue.original`                      |
| `lineItems.variantId`                                       | `lineItems.catalogReference.options`                                      | [Stores Catalog eCommerce Reference](https://bo.wix.com/wix-docs/rest/stores/stores-catalog/ecommerce-integration)
| `lineItems.fulfillerId`                                     | `lineItems.fulfillerId`                                                   |
| `lineItems.discount`                                        | `lineItems.totalDiscount.amount`                                          |
| `lineItems.tax`                                             | `lineItems.taxDetails.totalTax.amount`                                    |
| `lineItems.priceData.taxIncludedInPrice`                    | -                          | If `lineItems.price` equals `lineItems.totalPriceAfterTax` then tax is included
| `lineItems.priceData.price`                                 | `lineItems.price.amount`                                                  |
| `lineItems.priceData.totalPrice`                            | `lineItems.totalPriceAfterTax.amount`                                     |
| `activities.type`                                           | `activities.type`                                                         |
| `activities.TRACKING_LINK_WAS_SET`                          | `activities.TRACKING_LINK_SET`                                            |
| `activities.INVOICE_WAS_SET`                                | `activities.INVOICE_ADDED`                                                |
| `activities.INVOICE_WAS_SENT`                               | `activities.INVOICE_SENT`                                                 |
| `activities.author`                                         | `activities.authorEmail`                                                  |
| `activities.message`                                        | `activities.merchantComment.message`                                      | If `activities.type = "MERCHANT_COMMENT"`
| `activities.timestamp`                                      | `activities.createdDate`                                                  |
| `invoiceInfo`                                               | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
| `fulfillments`                                              | -                                                                         | Accessible via [Order Fulfillments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-fulfillments)
| `discount.appliedCoupon.couponId`                           | `appliedDiscounts.coupon.id`                                              | Search the `appliedDiscounts` array for populated `coupon` field; `couponId` is `coupon.id`
| `discount.appliedCoupon.name`                               | `appliedDiscounts.coupon.name`                                            | Search the `appliedDiscounts` array for populated `coupon` field; `name` is `coupon.name`
| `discount.appliedCoupon.code`                               | `appliedDiscounts.coupon.code`                                            | Search the `appliedDiscounts` array for populated `coupon` field; `code` is `coupon.code`
| `customField.value`                                         | `customFields.value.stringValue`                                          | Note: `customFields` is an array
| `customField.title`                                         | `customFields.title`                                                      |
| `customField.translatedTitle`                               | `customFields.translatedTitle`                                                 |
| `cartId`                                                    | -                                                                         | Replaced by `checkoutId`
| `buyerLanguage`                                             | `buyerLanguage`                                                           |
| `channelInfo.type`                                          | `channelInfo.type`                                                        |
| `channelInfo.externalOrderId`                               | `channelInfo.externalOrderId`                                             |
| `channelInfo.externalOrderUrl`                              | `channelInfo.externalOrderUrl`                                            |
| `enteredBy.id` $$ `enteredBy.identityType: "MEMBER"`        | `createdBy.memberId`                                                      |
| `enteredBy.id` $$ `enteredBy.identityType: "USER"`          | `createdBy.userId`                                                        |
| `enteredBy.id` $$ `enteredBy.identityType: "APP"`           | `createdBy.appId`                                                         |
| `enteredBy.id` $$ `enteredBy.identityType: "CONTACT"`       | `createdBy.visitorId` | Previously, for a buyer that is not logged in, `CONTACT` type and ID were returned. in the eCommerce API, `visitorId` is returned. Note: the ID itself will also be different.
| `lastUpdated`                                               | `updatedDate`                                                             |
| `numericId`                                                 | -                                                                         | Removed due to added cursor paging functionality
| `refunds`                                                   | -                                                                         | Accessible via [Order Payments API](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)

