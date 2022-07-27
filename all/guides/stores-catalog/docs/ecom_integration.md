SortOrder: 3
# eCommerce Integration

Product details passed from the Stores catalog to an eCommerce cart, checkout, or order, must follow a certain structure in the form of the `catalogReference` object.

* `catalogItemId` - in the context of Stores, this is the `productId`
* `appId` - the Stores app ID. When using the Stores catalog, this must always be `"1380b703-ce81-ff05-f115-39571d94dfcd"`
* `options` - this field can hold different key-value pairs, depending on variant management and whether the product/variant has custom text fields.

Refer to the following `catalogReference` object examples for more detail:

## Managed Variants

When a product's variants are managed (`product.manageVariants: true`), the `options` object should hold the variant's `variantId`. In the following example, the variant also has `customTextFields`:

```json
{
  "catalogReference": {
    "catalogItemId": "5376f9ec-b92e-efa9-e4a1-f4f480aa0d3a",
    "appId": "1380b703-ce81-ff05-f115-39571d94dfcd",
    "options": {
      "variantId": "00000000-0000-0020-0005-ad9cdc10d3b8",
      "customTextFields": {
        "What would you like written on the custom label?": "Hope you enjoy the coffee! :)"
      }
    }
  }
}
```

## Non-Managed Variants

When a product's variants are not managed (`product.manageVariants: false`), the `options` object should hold the variant's options and choices

```json
{
  "catalogReference": {
    "catalogItemId": "4d93fb7e-e612-612f-5c27-81b35b503ad7",
    "appId": "1380b703-ce81-ff05-f115-39571d94dfcd",
    "options": {
      "options": {
        "Size": "Medium",
        "Color": "Red"
      }
    }
  }
}
```