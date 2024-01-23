SortOrder: 3
# Best Practices

This article presents some best practices for designing your app and your database schema for integration with Wix.

## Recommended App Features

We recommend you do the following while implementing your app:

- Add forms/prompts for:
    - Mapping Wix location configurations with your POS locations. 
    - Synchronizing which menus to synchronize between the two systems per location. 
    - Entering order details on the Wix site. 
- Include feedback and notifications, some of which are for the site owner and some of which  the site owner will pass along to the customer. Examples are: 
    - A notification to the site owner that any existing catalogs (menus) for a location on the Wix site are disabled when synchronizing menus between the two systems.
    - A list of statuses and errors that your app might return, such as the status returned after order creation succeeded or failed. 
    - Feedback to the customer about their order, such as sending text message notifications that the order has been confirmed.
- Specify clear terms and conditions for orders to be accepted and processed. You want to make sure the site owner fills out all necessary legal and contractual agreements, and that you inform the site owner of pricing, fees, and payment terms.

## Database Schema Recommendations

When designing your database schema, you have a lot of flexibility. For example, you can decide how many database tables you want, name fields according to your business, and you can add fields as necessary to support your needs. Here are some recommendations that can help you plan ahead.

Consider making the following tables:

- [instances](#instances)
- [accounts](#accounts)
- [configurations](#configurations)
- [orders](#orders)
- [identifiers](#identifiers)
- [syncs](#syncs)

You can rename tables as long as you retain the associations between them.

![Table Relationships](https://s3.amazonaws.com/wixplorer-readme-images/point-of-sale-integration%2FPOS-SPI-Table-Relationships.png "Table Relationships")

### instances

The mandatory `instances` table represents the merchant's store, restaurant, or business. The table contains tokens for access.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| id | Yes | Instance ID. Primary key. |
| metaSiteId | Yes | Wix site ID. |
| accessToken | Yes | OAuth access token. |
| refreshToken | Yes | Refresh token. |

### accounts

The mandatory `accounts` table represents the accounts that exist between the merchant and the POS system. It also helps to reference between the `instances` table and the `configurations` table.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| id | Yes | Account ID. Primary key. |
| instanceId | Yes | Instance ID for the merchant's store, restaurant, or business. |
| posAuthorized | Yes | Whether the account is authorized by the POS system. |
| posMerchantId | No | ID of the merchant's store, restaurant, or business. on the POS system. Can be renamed, for example, to businessName. |

Other fields you might consider adding include: `posAccessToken`, `posRefreshToken`, `environment`, `createdDate`, and so on.

### configurations

The mandatory `configurations` table represents the Wix configurations (locations) and the locations on the POS system that they are associated with.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| id | Yes | Wix location configuration ID. Primary key. |
| accountId | Yes | Account ID. |
| locationName | No | Name of the configuration on the Wix site. Can be renamed. |
| posLocationId | No | ID for the corresponding location in the POS system. |
| enabled | No | Whether the configuration is currently enabled/connected. |
| catalogId | No | Catalog (menu) ID for the configuration. |
| status | No | When returned to Wix, must be sent as text. |

Other fields you might consider adding include: `createdAt`, `updatedAt`, and so on.

### orders

The optional `orders` table represents orders that have come through the POS system to the Wix site.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| id | Yes | Order ID. |
| configurationId | Yes | Configuration ID on the Wix site. Needed when creating an order. |
| externalId | Yes | POS provider ID. Can be renamed. Primary key. |
| orderId | Yes | Order ID on the Wix site. |
| status | Yes | Status of the order. |

Supported status values: `PENDING`, `NEW`, `ACCEPTED`, `CANCELED`, `FULFILLED`

### identifiers

The optional `identifiers` table maps Wix configurations (locations) to POS locations.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| wixId | Yes | ID of the Wix site. |
| configurationId | Yes | Configuration ID on the Wix sites. |
| externalId | Yes | POS provider ID. Can be renamed. |

### syncs

The optional `syncs` table contains details about each synchronization attempt and how it completed.

| Field | Required? | Description |
| ----- | --------- | ----------- |
| configurationId | Yes | Configuration ID on the Wix site. Primary key. |
| status | Yes | Sync status. |
| startedAt | No | When the sync started. |
| endedAt | No | When the sync ended. |
| successfullySyncedAt | No | When the sync successfully completed. |
| failureReason | No | Why the sync failed. |
| failureCode | No | Code for why the sync failed. |

Supported status values: `PENDING`, `IN_PROGRESS`, `SYNCED`, `FAILED`

> **Tip**: You might also consider adding a table for synchronization logs.