SortOrder: 3
# Creating and Updating Coupons - Examples


## Create a "buyXGetY" coupon that applies to all the store's products

```
curl 'https://www.wixapis.com/stores/v2/coupons' --data-binary '{"specification":{"name":"BuyXGetY","code":"ABC","active":true,"startTime":1554066000000,"usageLimit":10,"expirationTime":1554325199999,"scope":{"namespace":"stores"},"limitedToOneItem":true,"buyXGetY":{"x":3,"y":2}}}' -H 'Content-Type: application/json' -H 'Authorization: XXX' 
```

## Create a "moneyOffAmount" coupon that applies to all the bookings services

```
curl 'https://www.wixapis.com/stores/v2/coupons' --data-binary '{"specification":{"name":"Discount","code":"ABC","active":true,"startTime":1554126066895,"scope":{"namespace":"bookings"},"limitedToOneItem":false,"moneyOffAmount":5}}' -H 'Content-Type: application/json' -H 'Authorization: XXX' 
```

## Create a "freeShipping" coupon that applies to a minimum subtotal

```
curl 'https://www.wixapis.com/stores/v2/coupons' --data-binary '{"specification":{"name":"FreeShipping","code":"ABC","active":true,"startTime":1554126275300,"minimumSubtotal":5,"limitedToOneItem":true,"freeShipping":true}}' -H 'Content-Type: application/json' -H 'Authorization: XXX' 
```

## Create a "fixedPriceAmount" coupon that applies to a specific product

```
curl 'https://www.wixapis.com/stores/v2/coupons' --data-binary '{"specification":{"name":"SalePrice","code":"ABC","active":true,"startTime":1554126541151,"scope":{"namespace":"stores","group":{"name":"product","entityId":"e599b709-1a8b-478a-ae80-26192944aef5"}},"limitedToOneItem":true,"fixedPriceAmount":5}}' -H 'Content-Type: application/json' -H 'Authorization: XXX' 
```

## Create a "percentOffRate" coupon that applies to all event tickets

```
curl 'https://www.wixapis.com/stores/v2/coupons' --data-binary '{"specification":{"name":"111","code":"ABC","active":true,"startTime":1554126716133,"scope":{"namespace":"events","group":{"name":"ticket"}},"limitedToOneItem":true,"percentOffRate":5}}' -H 'Content-Type: application/json' -H 'Authorization: XXX' 
```

## Update a coupon - invalidate the coupon so it can't be used any longer

```
curl 'https://www.wixapis.com/stores/v2/coupons/2baa30ad-e70e-4293-9562-7f8e46baa4d5' -X PATCH --data-binary '{"specification":{"active":false},"fieldMask":{"paths":["active"]}}' -H 'Content-Type: application/json' -H 'Authorization: XXX' 
```

## Delete a coupon

```
curl 'https://www.wixapis.com/stores/v2/coupons/2baa30ad-e70e-4293-9562-7f8e46baa4d5' -X DELETE --data-binary '{"specification":{"active":false},"fieldMask":{"paths":["active"]}}' -H 'Content-Type: application/json' -H 'Authorization: XXX' 
```
   
