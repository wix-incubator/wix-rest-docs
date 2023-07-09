SortOrder: 3
# eCommerce Integration

Product details passed from the Stores catalog to an eCommerce cart, checkout, or order, must follow a certain structure in the form of the `catalogReference` object.

* `catalogItemId` - in the context of Wix Stores products, this is the `productId`
* `appId` - the Stores app ID. When using products from the Stores catalog, this must always be `"215238eb-22a5-4c36-9e7b-e7c08025e04e"`
* `options` - this field can hold different key-value pairs, depending on variant management and whether the product/variant has custom text fields.

Refer to the following `catalogReference` object examples for more detail:

## Managed Variants

When a product's variants are managed (`product.manageVariants: true`), the `options` object should hold the variant's `variantId`. In the following example, the variant also has `customTextFields`:

```json
{
  "catalogReference": {
    "catalogItemId": "5376f9ec-b92e-efa9-e4a1-f4f480aa0d3a",
    "appId": "215238eb-22a5-4c36-9e7b-e7c08025e04e",
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
    "appId": "215238eb-22a5-4c36-9e7b-e7c08025e04e",
    "options": {
      "options": {
        "Size": "Medium",
        "Color": "Red"
      }
    }
  }
}
```