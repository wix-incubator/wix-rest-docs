SortOrder: 1
#  Using the Inventory API

## Step 1 - Query product variants ([Get Inventory Variants](https://dev.wix.com/api/rest/wix-stores/inventory/get-inventory-variants) endpoint)

```
curl 'https://www.wixapis.com/stores/v2/inventoryItems/product/{productId}/getVariants' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```

From the result, you can see whether inventory is being tracked for this product:
```json
{
  "inventoryItem": {
    "id": "f8753103-0b3a-b24a-4931-50de280ac31a",
    "externalId": "078acefc-f4c5-4db5-b6ce-af21d7f53ce5",
    "productId": "078acefc-f4c5-4db5-b6ce-af21d7f53ce5",
    "trackQuantity": true,
    "variants": [
      {
        "variantId": "00000000-0000-0000-0000-000000000000",
        "inStock": true,
        "quantity": 4
      }
    ],
    "lastUpdated": "2020-08-31T20:05:40.348Z",
    "numericId": "1598904314932014"
  }
}
```

## Step 2 - Update a specific variants on a product ([Update Inventory Status](https://dev.wix.com/api/rest/wix-stores/inventory/update-inventory-variants) endpoint)

Update whether the product inventory is tracked:
```
curl 'https://www.wixapis.com/stores/v2/inventoryItems/product/{productId}' -X PATCH --data-binary '{"inventoryItem": {"trackQuantity": false}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```

For a non-tracked product, you should update inStock:
```
curl 'https://www.wixapis.com/stores/v2/inventoryItems/product/{productId}' -X PATCH --data-binary '{"inventoryItem": {"trackQuantity": false,"variants": [{"variantId": "00000000-0000-0000-0000-000000000000","inStock": false}]}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```

For tracked products, you should update quantity:
```
curl 'https://www.wixapis.com/stores/v2/inventoryItems/product/{productId}' -X PATCH --data-binary '{"inventoryItem": {"trackQuantity": true,"variants": [{"variantId": "00000000-0000-0000-0000-000000000000","quantity": 4}]}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```