SortOrder: 0
# Orders Service

## About This API

Stores Orders allows third party apps to read orders for Wix store owners.

<blockquote class='note'>
<p>
<strong>Note:</strong><br/>
Write operations are not supported at this time.
</p>
</blockquote>

## Order Types

**Shipping orders**: Order and shipment of any selection of products from the store's catalog.  
**Pickup orders**: Order of any selection of products from the store's catalog for user pickup.  
**Point of Sale (POS) orders**: Sale consisting only of price and partial billing information, of products not included in the store's catalog.

## Query Language

For endpoints that allow querying, the format follows the following [guidelines](https://dev.wix.com/api/getting-started.html#api-query-language).

### Fields That Allow Filtering

| Field	                       | Operators                              |	Sorting Allowed |
| ---------------------------- | -------------------------------------- | --------------- |
| dateCreated                  | $eq,$ne,$hasSome,$lt,$lte,$gt,$gte     |	Allowed         |
| paymentStatus	               | $eq,$ne,$hasSome,$contains,$startsWith	| Allowed         |
| archived                     | $eq,$ne	                              |                 |
| read	                       | $eq,$ne	                              |                 |
| number	                     | $eq,$ne,$hasSome,$lt,$lte,$gt,$gte     |	Allowed         |
| id	                         | $eq,$ne,$hasSome,$contains,$startsWith	| Allowed         |
| lineItems.productId          | $eq,$ne,$hasSome,$hasAll               |                 |
| lineItems.name	             | $eq,$ne,$hasSome,$hasAll               |                 |
| billingInfo.address.fullName | $eq,$ne,$hasSome,$lt,$lte,$gt,$gte     |                 |
| buyerInfo.id	               | $eq,$ne,$hasSome,$lt,$lte,$gt,$gte     |                 |

** Note that "HasSome" is same as the operator "IN" in SQL
