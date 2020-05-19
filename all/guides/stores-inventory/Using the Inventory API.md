SortOrder: 1
#  Using the Inventory API

## Step 1 - Get the product ID ([Get Product](https://dev.wix.com/api/rest/wix-stores/catalog/product/get-product) endpoint)

```
curl 'https://www.wixapis.com/stores/v1/products/{productId}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```
From the response, take the inventoryItemId. You will use this ID to query the inventory system.

## Step 2 - Update the inventory item's status ([Update Inventory Status](https://dev.wix.com/api/rest/wix-stores/inventory/get-inventory-variants) endpoint)

```
curl 'https://www.wixapis.com/stores/v1/inventoryItems/{inventoryItemId}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```

From the result, you can see whether inventory is being tracked for this product:

```json
{
  "item": {
    "id": "4d55c9b5-7f00-1dd8-c213-272615328354",
    "externalId": "b2aa364a-80ff-e227-3dec-d8d9eacd7cab",
    "trackInventory": false
  }
}
```

Or change the product to track or not track inventory:

```
curl 'https://www.wixapis.com/stores/v1/inventoryItems/{inventoryItemId}' -X PATCH --data-binary '{"item": {"trackInventory": true}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```

## Step 3 - Query the product variants ([Query Inventory](https://dev.wix.com/api/rest/wix-stores/inventory/query-inventory) endpoint) - inventory is trakced per variant

This query will return all variants, unless you filter for specific ones.

```
curl 'https://www.wixapis.com/stores/v1/products/{productId}/variants/query' --data-binary '{}' -H 'Content-Type: application/json' -H 'Authorization: XXXX'
```

This is an example for what the result would be like for a product that has no options.
From the below response, you can extract the variant ID - 00000000-0000-0000-0000-000000000000

```json
{
  "variants": [
    {
      "id": "00000000-0000-0000-0000-000000000000",
      "choices": {
        
      },
      "variant": {
        "price": {
          "currency": "USD",
          "price": 0.0,
          "discountedPrice": 0.0,
          "formatted": {
            "price": "$0.00",
            "discountedPrice": "$0.00"
          }
        },
        "sku": "",
        "visible": true
      }
    }
  ],
  "metadata": {
    "items": 1,
    "offset": 0
  }
}
```

## Step 4 - Use variant ID to get or update the variant inventory ([Get Inventory Variants](https://dev.wix.com/api/rest/wix-stores/inventory/get-inventory-variants) endpoint)

```
curl 'https://www.wixapis.com/stores/v1/inventoryItems/{inventoryItemId}/variant/{variantId}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```

From the result, you can see whether the variant is in stock or not.
If inventory is being tracked, you can get the exact quantity

```json
{
  "variant": {
    "itemId": "4d55c9b5-7f00-1dd8-c213-272615328354",
    "variantId": "00000000-0000-0000-0000-000000000000",
    "inStock": true,
    "quantity": 5
  }
}
```

And you can also update the inventory. For a non-tracked product, you should update inStock:

```
curl 'https://www.wixapis.com/stores/v1/inventoryItems/{inventoryItemId}/variant/{variantId}' -X PATCH --data-binary '{"variant": {"inStock": true}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```

For tracked products, you should update quantity:

```
curl 'https://www.wixapis.com/stores/v1/inventoryItems/{inventoryItemId}/variant/{variantId}' -X PATCH --data-binary '{"variant": {"quantity": 5}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```





