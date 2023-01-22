SortOrder: 3
# Address Object Conversion Table

The eCommerce APIs use a different `address` object. Notably, fields related to contact information have been moved
to an adjacent `contactDetails` object (for example, in `order.shippingInfo`).

To help with conversion and migration, refer to the table below to check which fields have changed and how.

> Note: in the eCommerce API, the buyer's email is only held in the `buyerInfo` field in the [eCommerce Order object](https://dev.wix.com/api/rest/wix-ecommerce/orders/order-object).

| Previous Address Object                         | eCommerce Address Field Location                                           | Change            |
| ------------------------------------------------|--------------------------------------------------------------|-------------------|
| `address.city`                                  | `address.city`                                               |
| `address.email`                                 | `buyerInfo.email`                                            |
| `address.zipCode`                               | `address.postalCode`                                         | Field name
| `address.country`                               | `address.country`                                            |
| `address.addressLine1`                          | `address.addressLine`                                        | Field name
| `address.addressLine2`                          | `address.addressLine2`                                       |
| `address.street`                                | `address.streetAddress`                                      | Field name
| `address.subdivision`                           | `address.subdivision`                                        |
| `address.fullName.firstName`                    | `contactDetails.firstName`                                   | Moved to `contactDetails` object
| `address.fullName.lastName`                     | `contactDetails.lastName`                                    | Moved to `contactDetails` object
| `address.phone`                                 | `contactDetails.phone`                                       | Moved to `contactDetails` object
| `address.company`                               | `contactDetails.company`                                     | Moved to `contactDetails` object
| `address.vatId`                                 | `contactDetails.vatId`                                       | Moved to `contactDetails` object