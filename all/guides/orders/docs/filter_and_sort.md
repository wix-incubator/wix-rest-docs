SortOrder: 1
# Filter and Sort

_Query Orders_ endpoint allows sorting results by field.
Use `field:ASC` to sort results in ascending order,
and `field:DESC` to sort in descending order.

For example, to sort orders by number in descending order:

```json
{
  "sort": {
    "fieldName": "order.number",
    "order": "DESC"
  }
}
```

The default sort is `createdDate:ASC`.

Refer to the table below to check which fields support sorting.

## Field Support for Filtering and Sorting

The table below shows field support for filters, sorting,
and free-text searching. For more detailed field descriptions, see the full documentation.

| Field                        | Data Type/Format                                                                      | Supported Filters                                         | Sortable |
| ---------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------             | -------- |
| `id`                         | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `createdDate`                | UTC datetime string in either `YYYY-MM-DDThh:mm:ss.sss` (ISO 8601) or Unix formats    | `$eq`, `$ne`, `$hasSome`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `updatedDate`                | UTC datetime string in either `YYYY-MM-DDThh:mm:ss.sss` (ISO 8601) or Unix formats    | `$eq`, `$ne`, `$hasSome`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `number`                     | Number (as string)                                                                    | `$eq`, `$ne`, `$hasSome`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `priceSummery.totalPrice`    | String                                                                                | `$eq`, `$ne`, `$hasSome`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `fulfillmentStatus`          | String from supported enum values                                                     | `$eq`, `$ne`, `$hasSome`                                  | Sortable |
| `paymentStatus`              | String from supported enum values                                                     | `$eq`, `$ne`, `$hasSome`                                  | Sortable |
| `billingInfo.contactDetails.firstName` | String                                                                      | `$eq`, `$ne`, `$hasSome`, `$contains`, `$startsWith`      | Sortable |
| `billingInfo.contactDetails.lastName` | String                                                                       | `$eq`, `$ne`, `$hasSome`, `$contains`, `$startsWith`      | Sortable |
| `archived`                   | Boolean                                                                               | `$eq`, `$ne`                                              |          |
| `seenByAHuman`               | Boolean                                                                               | `$eq`, `$ne`                                              |          |
| `lineItems.catalogReference.catalogItemId` | String                                                                  | `$eq`, `$ne`, `$hasSome`, `$hasAll`                       |          |
| `lineItems.productName.original` | String                                                                            | `$eq`, `$ne`, `$hasSome`, `$hasAll`                       |          |
| `buyerInfo.memberId`         | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `buyerInfo.contactId`        | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `channelInfo.type`           | String                                                                                | `$eq`, `$ne`, `$hasSome`                                  |          |
| `channelInfo.externalOrderId`| String                                                                                | `$eq`, `$ne`, `$hasSome`                                  |          |
| `createdBy.userId`           | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `subscriptionInfo.id`        | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `shippingInfo.region.name`   | String                                                                                | `$eq`, `$ne`, `$hasSome`, `$contains`, `$startsWith`      |          |
| `shippingInfo.title`         | String                                                                                | `$eq`, `$ne`, `$hasSome`, `$contains`, `$startsWith`      |          |

## Examples

**Get orders billed to people named 'John'**

```sh
curl 'https://www.wixapis.com/ecom/v1/orders/query' \
  --data-binary '{"filter":{"billingInfo.contactDetails.fullName": "John"}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get paid orders, sorted by date of update**

```sh
curl 'https://www.wixapis.com/ecom/v1/orders/query' \
  --data-binary '{"filter": {"paymentStatus": "PAID"}, \
  "sort": {"fieldName": "updatedDate","order" : "ASC"}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get orders by IDs**

```sh
curl 'https://www.wixapis.com/ecom/v1/orders/query' \
  --data-binary '{"filter":{"id": {"$hasSome": ["ORDER_ID_1", "ORDER_ID_2"]}}}' \
  -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```