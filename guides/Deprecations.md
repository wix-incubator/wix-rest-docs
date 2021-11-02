# End-of-Life Notices

This article contains the items being deprecated across Wix REST APIs.
Typically, deprecated items reach their planned end of life at the end of a calendar quarter,
at least 6 months after their announced deprecation.

## End of Life: June 30, 2022

- App Management - [Get App Instance](https://dev.wix.com/api/rest/app-management/apps/app-instance/get-app-instance):
`ownerEmail` field, replaced by `ownerInfo`.
(Announced November 1, 2021)

## End of Life: March 31, 2022

- [Contacts v1](https://dev.wix.com/api/rest/contacts/contacts): All webhooks
  (Announced September 13, 2021)

- [Contacts v4 extended fields](https://dev.wix.com/api/rest/contacts/contacts/sorting,-filtering,-and-searching#contacts_contacts_sorting,-filtering,-and-searching_extended-fields-filtering-sorting-and-searching):
  `contacts.displayByFirstName`, `contacts.displayByLastName`, `ecom.lastPurchaseDate`, `ecom.numOfPurchases`, `ecom.totalSpentAmount`, `ecom.totalSpentCurrency`, `members.mobile`
  (Announced September 13, 2021)

- [Contacts v4 contact attributes](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-object):
  `picture`, `source.wixAppId`
  (Announced September 13, 2021)
  
- Bookings: [List Resources](https://dev.wix.com/api/rest/wix-bookings/resources/list-resources)
  (Announced August 1, 2021)


- Bookings: [List Bookings](https://dev.wix.com/api/rest/wix-bookings/bookings/bookings-reader/list-bookings) 
 (Announced August 1, 2021)
 
- Bookings Service Catalog: [List services](https://dev.wix.com/api/rest/wix-bookings/service-catalog/services/list-services)
(Announced September 14, 2021)

## End of Life: June 30, 2021

- [Contacts v1](https://dev.wix.com/api/rest/contacts/contacts): All endpoints


## Deprecated With Continued Support (No End of Life):  
- Stores [Catalog Products](https://dev.wix.com/api/rest/wix-stores/catalog/products/product-object): `price` parameter (replaced with `priceData`)  
- Stores [Catalog Products](https://dev.wix.com/api/rest/wix-stores/catalog/products/product-object): `ribbons` parameter (replaced with `ribbon`)  
- Stores [Inventory](https://dev.wix.com/api/rest/wix-stores/inventory/get-inventory-variants): `inventoryItem.externalId` parameter (replaced with `inventoryItem.productId`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `read` parameter  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `buyerInfo.type` parameter (replaced with `buyerInfo.identityType`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `billingInfo.externalTransactionId` parameter (replaced with `billingInfo.paymentProviderTransactionId`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `shippingInfo.shippingDetails.trackingInfo` parameter (replaced with `fulfillments.trackingInfo`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `shippingInfo.pickupDetails.buyerDetails` parameter (replaced with `buyerInfo`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `lineItems.price` parameter (replaced with `lineItems.priceData`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `lineItems.totalPrice` parameter (replaced with `lineItems.priceData`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `lineItems.taxIncludedInPrice` parameter (replaced with `lineItems.priceData`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `lineItems.mediaItem.mediaId` parameter (replaced with `lineItems.mediaItem.Id`)  
- Stores [Orders](https://dev.wix.com/api/rest/wix-stores/orders/order-object): `discounts.value` parameter (replaced with `totals.discount`)  
