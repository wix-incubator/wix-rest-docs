SortOrder: 3
# Use Cases

Third party apps can use coupons to help site owners improve brand loyalty, increase customer engagement and incentivize customer purchases on Wix sites. 
Coupons can be set to activate and expire automatically, and to deactivate after a maximum amount of uses, so that the entire coupon lifecycle is set during creation. 
Coupons can also be changed both before they become active and while they are active, including deactivation, or deleted.


This article shares possible use cases your app could support, as well as an example flow that could support each use case. 
You're certainly not limited to what's on this page, but it can be a helpful jumping off point as you plan your app.

## Create a "Buy X Get Y Free" coupon 

This use case describes creating a coupon that grants an extra 2 entities (products/services/events/tickets) for free when the customer purchases 3 of the same entity at the regular price.   
Coupon details include: coupon code: ABC, Active upon creation: true, Total usage limit: 10 uses, Valid from: `April 1, 2019 12:00:00 AM`, Valid until: `April 3, 2019 11:59:59 PM`.

- If the coupon should apply to any product in Wix Stores, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "BuyXGetY",
        "code": "ABC",
        "active": true,
        "startTime": 1554066000000,
        "usageLimit": 10,
        "expirationTime": 1554325199999,
        "scope": {
          "namespace": "stores"
        },
        "limitedToOneItem": true,
        "buyXGetY": {
          "x": 3,
          "y": 2
        }
      }
    }
    ```

- If the coupon should apply to a specific service in Wix Bookings, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "BuyXGetY",
        "code": "ABC",
        "active": true,
        "startTime": 1554066000000,
        "usageLimit": 10,
        "expirationTime": 1554325199999,
        "scope": {
          "namespace": "bookings",
          "group": {
            "name": "service",
            "entityId": "e599b709-1a8b-478a-ae80-26192944aef5"
          },
          "limitedToOneItem": true,
          "buyXGetY": {
            "x": 3,
            "y": 2
          }
        }
      }
    }
    ```

- If the coupon should apply to all tickets in Wix Events, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "BuyXGetY",
        "code": "ABC",
        "active": true,
        "startTime": 1554066000000,
        "usageLimit": 10,
        "expirationTime": 1554325199999,
        "scope": {
          "namespace": "events",
          "group": {
            "name": "ticket"
          }
        },
        "limitedToOneItem": true,
        "buyXGetY": {
          "x": 3,
          "y": 2
        }
      }
    }
    ```


## Create an "X Amount Off a Purchase" coupon 

This use case describes creating a coupon that grants a flat discount of 5 (currency is taken from the Wix site's settings) off a purchase.  
Coupon details include: coupon code: ABC, Active upon creation: true, Total usage limit: 10 uses, Valid from: `April 1, 2019 12:00:00 AM`, Valid until: `April 3, 2019 11:59:59 PM`.

- If the coupon should apply to all products in a specific Wix Stores collection, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "Discount",
        "code": "ABC",
        "active": true,
        "startTime": 1554126066895,
        "usageLimit": 10,
        "scope": {
          "namespace": "stores",
          "group": {
            "name": "collection",
            "entityId": "e599b709-1a8b-478a-ae80-26192944aef5"
          }
        },
        "limitedToOneItem": false,
        "moneyOffAmount": 5
      }
    }
    ```

- If the coupon should apply to all services in Wix Bookings, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "Discount",
        "code": "ABC",
        "active": true,
        "startTime": 1554126066895,
        "scope": {
          "namespace": "bookings"
        },
        "limitedToOneItem": false,
        "moneyOffAmount": 5
      }
    }
    ```

- If the coupon should apply to a specific ticket in Wix Events, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "Discount",
        "code": "ABC",
        "active": true,
        "startTime": 1554126066895,
        "scope": {
          "namespace": "events",
          "group": {
            "name": "ticket",
            "entityId": "e599b709-1a8b-478a-ae80-26192944aef5"
          }
        },
        "limitedToOneItem": false,
        "moneyOffAmount": 5
      }
    }
    ```

## Create a "Fixed Discount" coupon 

This use case describes creating a coupon that grants a special price of 5 (currency is taken from the Wix site's settings) to a specific entity (product/service/event/ticket).  
Coupon details include: coupon code: ABC, Active upon creation: true, Total usage limit: 10 uses, Valid from: `April 1, 2019 12:00:00 AM`, Valid until: `April 3, 2019 11:59:59 PM`.

If the coupon should apply to a specific product in Wix Stores, your request can look like this:

```json
{
  "specification": {
    "name": "SalePrice",
    "code": "ABC",
    "active": true,
    "startTime": 1554126541151,
    "scope": {
      "namespace": "stores",
      "group": {
        "name": "product",
        "entityId": "e599b709-1a8b-478a-ae80-26192944aef5"
      }
    },
    "limitedToOneItem": true,
    "fixedPriceAmount": 5
  }
}
```

## Create a "Percentage Discount" coupon

This use case describes creating a coupon that grants 5 percent off of a specific entity (product/service/event/ticket).  
Coupon details include: coupon code: ABC, Active upon creation: true, Total usage limit: 10 uses, Valid from: `April 1, 2019 12:00:00 AM`.

- If the coupon should apply to a specific collection in Wix Stores, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "111",
        "code": "ABC",
        "active": true,
        "startTime": 1554126716133,
        "scope": {
          "namespace": "stores",
          "group": {
            "name": "collection",
            "entityId": "e599b709-1a8b-478a-ae80-26192944aef5"
          }
        },
        "limitedToOneItem": true,
        "percentOffRate": 5
      }
    }
    ```

- If the coupon should apply to a specific ticket in Wix Events, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "111",
        "code": "ABC",
        "active": true,
        "startTime": 1554126716133,
        "scope": {
          "namespace": "events",
          "group": {
            "name": "ticket"
          }
        },
        "limitedToOneItem": true,
        "percentOffRate": 5
      }
    }
    ```

## Create a "Free Shipping" coupon that applies to a minimum subtotal

This use case describes creating a coupon that grants free shipping to a purchase requiring shipping, when a minimum subtotal is reached.  
Coupon details include: coupon code: ABC, Active upon creation: true, Total usage limit: 10 uses, Valid from: `April 1, 2019 12:00:00 AM`.

- If the coupon should apply to all namespaces (stores, bookings, and events) with physical products that require shipping, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "FreeShipping",
        "code": "ABC",
        "active": true,
        "startTime": 1554126275300,
        "minimumSubtotal": 5,
        "limitedToOneItem": true,
        "freeShipping": true
      }
    }
    ```

- If the coupon should apply to all Wix Stores purchases with physical products that require shipping, your request can look like this: 

    ```json
    {
      "specification": {
        "name": "FreeShipping",
        "code": "ABC",
        "active": true,
        "startTime": 1554126275300,
        "scope": {
          "namespace": "stores,"
        },
        "minimumSubtotal": 5,
        "limitedToOneItem": true,
        "freeShipping": true
      }
    }
    ```

## Invalidate a coupon 

This use case describes changing the coupon to make it inactive.

```json
{
  "specification": {
    "active": false
  },
  "fieldMask": {
    "paths": [
      "active"
    ]
  }
}
```

## Delete a coupon

This use case describes deleting a coupon.

```curl
curl 'https://www.wixapis.com/stores/v2/coupons/<couponId>' \
   -X DELETE \
   -H 'Authorization: <AUTH>'
```
