# End of Life Notices

This article contains the items being deprecated across Wix REST APIs.
Typically, deprecated items reach their planned end of life at the end of a calendar quarter,
at least 6 months after their announced deprecation.




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
 
- Bookings Service Catalog: [List Bookings](https://dev.wix.com/api/rest/wix-bookings/service-catalog/services/list-serviceshttps://dev.wix.com/api/rest/wix-bookings/service-catalog/services/list-services)
(Announced September 14, 2021)


## End of Life: June 30, 2021

- [Contacts v1](https://dev.wix.com/api/rest/contacts/contacts): All endpoints


## Deprecated With Continued Support (No End of Life):
Stores Catalog Products: `price` parameter (replaced with `priceData`)
Stores Catalog Products: `ribbons` parameter (replaced with `ribbon`)
Stores Inventory: `inventoryItem.externalId` parameter (replaced with `inventoryItem.productId`)
Stores Orders: `read` parameter
Stores Orders: `buyerInfo.type` parameter (replaced with `buyerInfo.identityType`)
Stores Orders: `billingInfo.externalTransactionId` parameter (replaced with `billingInfo.paymentProviderTransactionId`)
Stores Orders: `shippingInfo.shippingDetails.trackingInfo` parameter (replaced with `fulfillments.trackingInfo`)
Stores Orders: `shippingInfo.pickupDetails.buyerDetails` parameter (replaced with `buyerInfo`)
Stores Orders: `lineItems.price` parameter (replaced with `lineItems.priceData`)
Stores Orders: `lineItems.totalPrice` parameter (replaced with `lineItems.priceData`)
Stores Orders: `lineItems.taxIncludedInPrice` parameter (replaced with `lineItems.priceData`)
Stores Orders: `lineItems.mediaItem.mediaId` parameter (replaced with `lineItems.mediaItem.Id`)
Stores Orders: `discounts.value` parameter (replaced with `totals.discount`)
