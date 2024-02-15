SortOrder: 2
# Orders: Supported Filters and Sorting

The following table shows field support for filters and sorting for the Order object:

| Field                                      | Supported Filtering                                | Sortable |
| -------------------------------------------| ---------------------------------------------------| -------- |
| `id`                                       | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `number`                                   | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`         | Sortable |
| `status`                                   | `$eq`, `$ne`, `$in`, `$nin`                        | Sortable |
| `archived`                                 | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith`      |          |
| `createdDate`                              | `$eq`, `$ne`, `$lt`, `$lte`, `$gte`, `$gt`, `$nin` | Sortable |
| `updatedDate`                              | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`         | Sortable |
| `lineItems.productName.original`           | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`, `$hasAll` |          |
| `lineItems.catalogReference.appId`         | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`, `$hasAll` |          |
| `lineItems.catalogReference.catalogItemId` | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`, `$hasAll` |          |
| `subscriptionInfo.id`                      | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `buyerInfo.email`                          | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith`      | Sortable |
| `buyerInfo.contactId`                      | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `buyerInfo.memberId`                       | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `paymentStatus`                            | `$eq`, `$ne`, `$in`, `$nin`                        | Sortable |
| `fulfillmentStatus`                        | `$eq`, `$ne`, `$in`, `$nin`                        | Sortable |
| `priceSummary.total.amount`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`         |          |
| `billingInfo.contactDetails.fullName`      | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith`      |          |
| `shippingInfo.title`                       | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `shippingInfo.logistics.deliveryTime`      | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith`      |          |
| `shippingInfo.region.name`                 | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `deliveryTimeSlotFromDate` (See notes)     | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith`      |          |
| `deliveryTimeSlotToDate` (See notes)       | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith`      |          |
| `createdBy.userId`                         | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `channelInfo.type`                         | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `channelInfo.externalOrderId`              | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `seenByAHuman`                             | `$eq`, `$ne`, `$in`, `$exists`, `$startsWith`      |          |
| `checkoutId`                               | `$eq`, `$ne`, `$in`, `$nin`                        |          |
| `paymentMethods` (See notes)               | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`, `$hasAll` |          |
| `fulfillmentStatuses` (See notes)          | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`, `$hasAll` |          |

<br />

> **Notes:**
> + `deliveryTimeSlotFromDate` - shorthand for the `shippingInfo.logistics.deliveryTimeSlot.from` field.
> + `deliveryTimeSlotToDate` - shorthand for the `shippingInfo.logistics.deliveryTimeSlot.to` field.
> + `paymentMethods` - aggregate of the `orderTransactions.payments.regularPaymentDetails.paymentMethod` field from the [Order Transactions API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/order-transactions/introduction).
> + `fulfillmentStatuses` - shorthand for the `fulfillmentStatusesAggregate` field.


__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Search Orders](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/search-orders)