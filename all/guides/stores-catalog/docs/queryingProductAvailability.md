SortOrder: 2
# Use Cases

In this example we will query a product variant: 
* The product is a shirt
* The shirt has 2 **options** - size and color
* The size option has 3 **choices** - S/M/L
* The color option has 3 **choices** - Red/Green/Blue
* The product **variant** S+Red is out of stock

**The product's options field**

```
curl 'https://www.wixapis.com/stores/v1/products/<product id>' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```
```json
{
  ...
  "productOptions": [
    {
      "optionType": "drop_down",
      "name": "Size",
      "choices": [
        {
          "value": "S",
          "description": "S",
          "inStock": true,
          "visible": true
        },
        {
          "value": "M",
          "description": "M",
          "inStock": true,
          "visible": true
        },
        {
          "value": "L",
          "description": "L",
          "inStock": true,
          "visible": true
        }
      ]
    },
    {
      "optionType": "color",
      "name": "Color",
      "choices": [
        {
          "value": "#FF0000",
          "description": "Red",
          "inStock": true,
          "visible": true
        },
        {
          "value": "#00FF00",
          "description": "Green",
          "inStock": true,
          "visible": true
        },
        {
          "value": "#00000FF",
          "description": "Blue",
          "inStock": true,
          "visible": true
        }
      ]
    }
  ]
}
```

**Now let's query the availability of S  **  
Notice in the response that:
1. Red is out of stock, because S+Red is out of stock
2. `availableForPurchase` is false, because both size and color must be given for this product

```
curl 'https://www.wixapis.com/stores/v1/products/<product id>/productOptionsAvailability' --data-binary '{"options": {"Size": "S"}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```
```json
{
  "productOptions": [
    {
      "optionType": "drop_down",
      "name": "Size",
      "choices": [
        {
          "value": "S",
          "description": "S",
          "inStock": true,
          "visible": true
        },
        {
          "value": "M",
          "description": "M",
          "inStock": true,
          "visible": true
        },
        {
          "value": "L",
          "description": "L",
          "inStock": true,
          "visible": true
        }
      ]
    },
    {
      "optionType": "color",
      "name": "Color",
      "choices": [
        {
          "value": "#FF0000",
          "description": "Red",
          "inStock": false,
          "visible": true
        },
        {
          "value": "#00FF00",
          "description": "Green",
          "inStock": true,
          "visible": true
        },
        {
          "value": "#00000FF",
          "description": "Blue",
          "inStock": true,
          "visible": true
        }
      ]
    }
  ],
  "availableForPurchase": false
}
```

**Now let's query the availability of S+Green  **  
Notice in the response that:
1. We get the selected variant, with proper values for price, weight, SKU and inventory 
2. `availableForPurchase` is true

```
curl 'https://www.wixapis.com/stores/v1/products/<product id>/productOptionsAvailability' --data-binary '{"options": {"Size": "S","Color": "Green"}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```
```json
{
  "selectedVariant": {
    "price": {
      "currency": "USD",
      "price": 81,
      "discountedPrice": 81,
      "formatted": {
        "price": "$81.00",
        "discountedPrice": "$81.00"
      }
    },
    "weight": 0,
    "sku": "364215376135191",
    "inStock": true,
    "visible": true
  },
  "productOptions": [
    {
      "optionType": "drop_down",
      "name": "Size",
      "choices": [
        {
          "value": "S",
          "description": "S",
          "inStock": true,
          "visible": true
        },
        {
          "value": "M",
          "description": "M",
          "inStock": true,
          "visible": true
        },
        {
          "value": "L",
          "description": "L",
          "inStock": true,
          "visible": true
        }
      ]
    },
    {
      "optionType": "color",
      "name": "Color",
      "choices": [
        {
          "value": "#FF0000",
          "description": "Red",
          "inStock": false,
          "visible": true
        },
        {
          "value": "#00FF00",
          "description": "Green",
          "inStock": true,
          "visible": true
        },
        {
          "value": "#00000FF",
          "description": "Blue",
          "inStock": true,
          "visible": true
        }
      ]
    }
  ],
  "availableForPurchase": true
}
```
