# End-of-Life Notices

This article contains the items being deprecated across Wix REST APIs.
Typically, deprecated items reach their planned end of life at the end of a calendar quarter,
at least 6 months after their announced deprecation.

## End of Life: March 31, 2023

- [List Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar/sessions/list-sessions)
  replaced by [Query Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar-v2/query-sessions).
  (Announced August 22, 2022)
  
- In Members API, the [Get Members](members/members/get-member),
  [List Members](members/members/list-members),
  and [Query Members](members/members/query-members)
  `fieldSet` parameter is replaced by `fieldsets`.
  (Announced September 1, 2022)

## End of Life: September 30, 2022

- [Order Created webhook](wix-restaurants/orders/order-created-webhook)
  replaced by [New Order](wix-restaurants/orders/new-order-webhook).
  (Announced April 18, 2022)
- [Wix Chat](wix-chat/wix-chat):
  The entire Wix Chat API is replaced by the [Inbox API](inbox/).
  (Announced March 1, 2022)

## End of Life: June 30, 2022

- [Wix Groups](wix-groups/wix-groups):
  - In the [Group Object](wix-groups/wix-groups/groups/group-object)
    (which is also embedded in the
    [Group Request Object](wix-groups/wix-groups/create-requests/group-request-object)):
    - `privacyLevel` replaced by `privacyStatus`.
    - `title` replaced by `name`.
    - `details` object: <br />
      `details.logo` replaced by `coverImage`,
      `details.membersTitle` replaced by `memberTitle`.
    - `createdBy` replaced by `ownerId`.
    - `recentActivityDate` replaced by `lastActivityDate`. <br />
  - [Group Member Object](wix-groups/wix-groups/members/group-member-object): `siteMemberId` replaced by `memberId`.
  - [Add Group Members](wix-groups/wix-groups/members/add-group-members): `siteMemberIds` replaced by `memberIds`.
  - [List Group Members](wix-groups/wix-groups/members/list-group-members): `siteMemberId` replaced by `memberId`.
  - [Remove Group Members](wix-groups/wix-groups/members/remove-group-members): `siteMemberIds` replaced by `memberIds`.
  - [Approve Join Group Requests](wix-groups/wix-groups/join-requests/approve-join-group-requests): `siteMemberIds` replaced by `memberIds` (will be a required field after June 30, 2022).
  - [Assign Role](wix-groups/wix-groups/roles/assign-role): `siteMemberIds` replaced by `memberIds`.
  - [Unassign Role](wix-groups/wix-groups/roles/unassign-role): `siteMemberIds` replaced by `memberIds`. <br />
    (Announced March 23, 2022)

- Forum [Category object](wix-forum/wix-forum/category/category-object):
  `postTypes` parameter deprecated without replacement.
  (Announced December 3, 2021)

- Forum [Post object](wix-forum/wix-forum/post/post-object):
  `postType` parameter deprecated without replacement.
  (Announced December 3, 2021)

- Member Authentication [Send Set Password Email](members/member-authentication/send-set-password-email):
  `requestedByMember` parameter replaced by `hideIgnoreMessage`.
  (Announced November 3, 2021)

- App Management - [Get App Instance](app-management/apps/app-instance/get-app-instance):`ownerEmail` field replaced by `ownerInfo` object.
  (Announced November 1, 2021)

## End of Life: March 31, 2022

- Contacts v4 [Update Contact](contacts/contacts/contacts-v4/update-contact)
  and [Bulk Update Contact](contacts/contacts/contacts-v4/bulk-update-contact):
  `fieldMask` parameter deprecated without replacement.
  (Announced September 13, 2021)

- [Contacts v1](contacts/contacts): All webhooks
  (Announced September 13, 2021)

- [Contacts v4 extended fields](contacts/contacts/sorting,-filtering,-and-searching#contacts_contacts_sorting,-filtering,-and-searching_extended-fields-filtering-sorting-and-searching):
  `contacts.displayByFirstName`, `contacts.displayByLastName`, `ecom.lastPurchaseDate`, `ecom.numOfPurchases`, `ecom.totalSpentAmount`, `ecom.totalSpentCurrency`, `members.mobile`
  (Announced September 13, 2021)

- [Contacts v4 contact attributes](contacts/contacts/contacts-v4/contact-object):
  `picture`, `source.wixAppId`
  (Announced September 13, 2021)

- Bookings: [List Resources](wix-bookings/resources/list-resources)
  (Announced August 1, 2021)

- Bookings: [List Bookings](wix-bookings/bookings/bookings-reader/list-bookings) 
  (Announced August 1, 2021)

- Bookings Service Catalog: [List services](wix-bookings/service-catalog/services/list-services)
  (Announced September 14, 2021)

## End of Life: July 2021

- [Contact Updated webhook](contacts/contacts/contacts-v4/contact-updated-webhook),
  [Marketing Tag Updated webhook](marketing/marketing-tags/marketing-tag-updated-webhook):
  `updatedEvent.previousEntity` no longer supported for 3rd-party apps.

## End of Life: June 30, 2021

- [Contacts v1](contacts/contacts): All endpoints

## Deprecated With Continued Support (No End of Life)

- Stores [Catalog Products](wix-stores/catalog/products/product-object): `price` parameter (replaced with `priceData`)  
- Stores [Catalog Products](wix-stores/catalog/products/product-object): `ribbons` parameter (replaced with `ribbon`)  
- Stores [Inventory](wix-stores/inventory/get-inventory-variants): `inventoryItem.externalId` parameter (replaced with `inventoryItem.productId`)  
- Stores [Orders](wix-stores/orders/order-object): `read` parameter  
- Stores [Orders](wix-stores/orders/order-object): `buyerInfo.type` parameter (replaced with `buyerInfo.identityType`)  
- Stores [Orders](wix-stores/orders/order-object): `billingInfo.externalTransactionId` parameter (replaced with `billingInfo.paymentProviderTransactionId`)  
- Stores [Orders](wix-stores/orders/order-object): `shippingInfo.shippingDetails.trackingInfo` parameter (replaced with `fulfillments.trackingInfo`)  
- Stores [Orders](wix-stores/orders/order-object): `shippingInfo.pickupDetails.buyerDetails` parameter (replaced with `buyerInfo`)  
- Stores [Orders](wix-stores/orders/order-object): `lineItems.price` parameter (replaced with `lineItems.priceData`)  
- Stores [Orders](wix-stores/orders/order-object): `lineItems.totalPrice` parameter (replaced with `lineItems.priceData`)  
- Stores [Orders](wix-stores/orders/order-object): `lineItems.taxIncludedInPrice` parameter (replaced with `lineItems.priceData`)  
- Stores [Orders](wix-stores/orders/order-object): `lineItems.mediaItem.mediaId` parameter (replaced with `lineItems.mediaItem.Id`)  
- Stores [Orders](wix-stores/orders/order-object): `discounts.value` parameter (replaced with `totals.discount`)  
