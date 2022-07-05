SortOrder: 3
# Best Practices

This article presents some best practices for designing your app and your database schema for integration with Wix.

## Recommended App Features

We recommend you do the following while implementing your app:

- Add forms/prompts for entering the estimated pickup time and the required delivery time.
- Include feedback and notifications, some of which the site owner will pass along to the customer. This includes feedback to the customer about their order. For example, sending text message notifications that the delivery driver is on the way, that the driver has arrived and dropped off the food, and so on.
- Specify clear terms and conditions for the merchant processing the delivery with you. You want to make sure the site owner fills out all necessary legal and contractual agreements, and that you inform the site owner of pricing, fees, and payment terms.

## Database Schema Recommendations

When designing your database schema, you have a lot of flexibility. For example, you can decide how many tables you want, name fields according to your business, and you can add fields as necessary to support your needs. Here are some recommendations that can help you plan ahead.

Consider making the following tables:

- [instances](#instances)
- [accounts](#accounts)
- [deliveries](#deliveries)
- [estimates](#estimates)

You can rename tables as long as you retain the associations between them.

![Table Relationships](https://s3.amazonaws.com/wixplorer-readme-images/local-delivery-integration-spi%2FLD-SPI-Table_Relationships.png "Table Relationships")

### instances

The mandatory `instances` table represents the merchant's store, restaurant, or business. The table contains tokens for access.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| id | Yes | Instance ID. |
| accessToken | Yes | OAuth access token. |
| refreshToken | Yes | Refresh token. |

### accounts

The mandatory accounts table represents the locations. It also helps to reference between the instances table and the deliveries table.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| accountId | Yes | Account ID for the location.  |
| instanceId | Yes | Instance ID for the merchant's store, restaurant, or business. |
| merchantId | No | ID of the Wix site for the merchant's store, restaurant, or business. Can be renamed, for example, to businessName. |
| externalId | No | ID for the local delivery service provider. |
| status | Yes | Status of the account. |

Other fields you might consider adding include: externalID, environment, createdDate, and so on.

### deliveries

The mandatory `deliveries` table represents the deliveries, including order information and any associated estimates. Delivery records are added to the table if the corresponding estimates are approved within 15 minutes of placing the order.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| id | Yes | Location ID. |
| accountId | Yes | Account ID. |
| externalId | Yes | Delivery ID. Can be renamed. |
| estimateId | No | Estimate ID. |
| orderId | No | Order ID. |
| status | Yes | When returned to Wix, must be sent as text. |

Supported values: “CREATED”, “ACTIVE”, or “INACTIVE”
Other fields you might consider adding include: creeatedAt, updatedAt, and so on.

### estimates

The optional `estimates` table represents the estimate, including whether the address is in range for deliveries and corresponding delivery fees. If the address is in range, we add a record to the estimates table.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| id | Yes | Estimate ID. Needed when creating an order. |
| accountId | Yes | Account ID. |
| externalId | Yes | Local delivery provider ID. Can be renamed. |
| orderId | Yes | Order ID on the Wix site. |
| fee | Yes | Delivery fee. |
| deliveryTime | Yes | Time at which to deliver the order.  |
| pickupTime | Yes | Time at which the order can be picked up. |
| currency | Yes | Currency of the fee. |
| deliveryAddress | Yes | Address to which to deliver the order. |
| pickupAddress | Yes | Address at which to pick up the order. |
| orderTotal | Yes | Cost of the order. |
| createdAt | Yes | The time the estimate was created. This time is used by the third-party app to determine if the estimate is still valid, because estimates expire after 15 minutes. |