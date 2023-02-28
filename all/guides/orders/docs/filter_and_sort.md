SortOrder: 1
# Filter and Sort

The [Query Orders](https://bo.wix.com/wix-docs/rest/ecommerce/orders/query-orders) endpoint allows for filtering and
sorting orders by field. Use `field:ASC` to sort results in ascending order, and `field:DESC` to sort in descending
order.

For example, to sort orders by number in descending order:

```json
{
  "sort": {
    "fieldName": "order.number",
    "order": "DESC"
  }
}
```

To query for paid and fulfilled orders with total prices less than or equal to 100 (currency is the store's default),
and sort them by full name in ascending order:

```sh
curl -X POST \
  'https://www.wixapis.com/ecom/v1/orders/query' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>' \
  --data-binary '{
    "query": {
      "filter": {
        "paymentStatus": "PAID",
        "fulfillmentStatus": "FULFILLED",
        "priceSummery.totalPrice": {
          "$lte": "100"
        }
      },
      "sort": [
        {
          "fieldName": "billingInfo.contactDetails.fullName",
          "order": "ASC"
        }
      ],
      "paging": {
        "limit": 2
      }
    }
  }'
```

The default sort is `createdDate:ASC`.

Refer to the table below to check which fields support sorting.

## Field Support for Filtering and Sorting

The table below shows field support for filters, sorting, and free-text searching. For more detailed field descriptions,
see the full [order object documentation](https://bo.wix.com/wix-docs/rest/ecommerce/orders/order-object).

| Field                        | Data Type/Format                                                                      | Supported Filters                                         | Sortable |
| ---------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------             | -------- |
| `id`                         | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `createdDate`                | UTC datetime string in either `YYYY-MM-DDThh:mm:ss.sss` (ISO 8601) or Unix formats    | `$eq`, `$ne`, `$hasSome`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `updatedDate`                | UTC datetime string in either `YYYY-MM-DDThh:mm:ss.sss` (ISO 8601) or Unix formats    | `$eq`, `$ne`, `$hasSome`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `number`                     | Number (as string)                                                                    | `$eq`, `$ne`, `$hasSome`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `priceSummery.totalPrice`    | String                                                                                | `$eq`, `$ne`, `$hasSome`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `fulfillmentStatus`          | String from supported enum values                                                     | `$eq`, `$ne`, `$hasSome`                                  | Sortable |
| `paymentStatus`              | String from supported enum values                                                     | `$eq`, `$ne`, `$hasSome`                                  | Sortable |
| `billingInfo.contactDetails.firstName` | String                                                                      | `$eq`, `$ne`, `$hasSome`, `$startsWith`      | Sortable |
| `billingInfo.contactDetails.lastName` | String                                                                       | `$eq`, `$ne`, `$hasSome`, `$startsWith`      | Sortable |
| `archived`                   | Boolean                                                                               | `$eq`, `$ne`                                              |          |
| `seenByAHuman`               | Boolean                                                                               | `$eq`, `$ne`                                              |          |
| `lineItems.catalogReference.catalogItemId` | GUID                                                                  | `$eq`, `$ne`, `$hasSome`, `$hasAll`                       |          |
| `lineItems.catalogReference.appId` | GUID                                                                  | `$eq`, `$ne`, `$in`, `$hasSome`, `$hasAll`, `$exists`                       |          |
| `lineItems.productName.original` | String                                                                            | `$eq`, `$ne`, `$hasSome`, `$hasAll`                       |          |
| `buyerInfo.memberId`         | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `buyerInfo.contactId`        | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `channelInfo.type`           | String                                                                                | `$eq`, `$ne`, `$hasSome`                                  |          |
| `channelInfo.externalOrderId`| String                                                                                | `$eq`, `$ne`, `$hasSome`                                  |          |
| `createdBy.userId`           | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `subscriptionInfo.id`        | GUID                                                                                  | `$eq`, `$ne`, `$hasSome`                                  |          |
| `shippingInfo.region.name`   | String                                                                                | `$eq`, `$ne`, `$hasSome`, `$startsWith`      |          |
| `shippingInfo.title`         | String                                                                                | `$eq`, `$ne`, `$hasSome`, `$startsWith`      |          |

## Examples

**Get orders billed to people named 'John'**

```sh
curl -X POST \
 'https://www.wixapis.com/ecom/v1/orders/query' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>' \
  --data-binary '{
    "query": {
      "filter":{
        "billingInfo.contactDetails.fullName": "John"
        }
      }
    }'
```

**Get paid orders, sorted by date of update**

```sh
curl -X POST \
 'https://www.wixapis.com/ecom/v1/orders/query' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>' \
  --data-binary '{
    "query": {
      "filter": {
        "paymentStatus": "PAID"
      },
      "sort": {
        "fieldName": "updatedDate",
        "order" : "ASC"
      }
    }
  }'
```

**Get orders by specific IDs**

```sh
curl -X POST \
 'https://www.wixapis.com/ecom/v1/orders/query' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>' \
  --data-binary '{
    "query": {
      "filter": {
        "id": {
          "$hasSome": ["ORDER_ID_1", "ORDER_ID_2"]
        }
      }
    }
  }'
```
