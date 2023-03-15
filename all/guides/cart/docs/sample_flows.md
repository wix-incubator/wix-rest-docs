SortOrder: 1
# Sample Flows

This article shares some possible use cases your app could support, as well as an example flow that could support each
use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your
app's implementation.

## Listen for a cart created by a site visitor

1. A site visitor adds an item to the cart.
2. Using the [Cart Created Webhook](https://dev.wix.com/api/rest/wix-ecommerce/cart/cart-created-webhook), listen for an event when a cart is created.

  ```js
  {
    "entityId" : "33d99986-63b0-4f0e-a549-33bda4bef756",
    "entityEventSequence" : "1",
    "slug" : "created",
    "id" : "09f3dfbf-f0c2-4276-9527-cc4af371125a",
    "createdEvent" : {
      "entity" : {
        "lineItems" : [ {
          "physicalProperties" : {
            "sku" : "364215376135191",
            "shippable" : true
          },
          "quantity" : 3,
          "paymentOption" : "FULL_PAYMENT_ONLINE",
          "couponScopes" : [ {
            "namespace" : "stores",
            "group" : {
              "name" : "collection",
              "entityId" : "00000000-000000-000000-000000000001"
            }
          }, {
            "namespace" : "stores",
            "group" : {
              "name" : "product",
              "entityId" : "df19c1f7-07d8-a265-42f8-e8dfa824cc6e"
            }
          } ],
          "url" : {
            "relativePath" : "/product-page/shoe",
            "url" : "https://example.wixsite.com/ep-tester"
          },
          "image" : {
            "id" : "3c76e2_bf235c38610f4d2a905db71095b351cf~mv2.jpg",
            "url" : "https://static.wixstatic.com/media/3c76e2_bf235c38610f4d2a905db71095b351cf~mv2.jpg",
            "height" : 1000,
            "width" : 1000
          },
          "price" : {
            "amount" : "85",
            "convertedAmount" : "85",
            "formattedAmount" : "$85.00",
            "formattedConvertedAmount" : "$85.00"
          },
          "availability" : {
            "status" : "AVAILABLE",
            "quantityAvailable" : 30
          },
          "priceBeforeDiscounts" : {
            "amount" : "85",
            "convertedAmount" : "85",
            "formattedAmount" : "$85.00",
            "formattedConvertedAmount" : "$85.00"
          },
          "id" : "00000000-0000-0000-0000-000000000001",
          "fullPrice" : {
            "amount" : "85",
            "convertedAmount" : "85",
            "formattedAmount" : "$85.00",
            "formattedConvertedAmount" : "$85.00"
          },
          "itemType" : {
            "preset" : "PHYSICAL"
          },
          "productName" : {
            "original" : "Shoe",
            "translated" : "Shoe"
          },
          "descriptionLines" : [ {
            "name" : {
              "original" : "Color",
              "translated" : "Color"
            },
            "colorInfo" : {
              "original" : "Black",
              "translated" : "Black",
              "code" : "#000"
            },
            "lineType" : "UNRECOGNISED"
          } ],
          "catalogReference" : {
            "catalogItemId" : "df19c1f7-07d8-a265-42f8-e8dfa824cc6e",
            "appId" : "1380b703-ce81-ff05-f115-39571d94dfcd",
            "options" : {
              "variantId" : "e62fee23-7878-437a-bf0e-292f17d11cb5"
            }
          }
        } ],
        "siteLanguage" : "en",
        "appliedDiscounts": [{
          "coupon":   {
            "id": "e463550b-220a-428f-82d9-8d11c3c1acd7",
            "code": "SUMMERSALE10"
          }
        }],
        "taxIncludedInPrices" : false,
        "weightUnit" : "KG",
        "id" : "33d99986-63b0-4f0e-a549-33bda4bef756",
        "buyerInfo" : {
          "visitorId" : "4c7ce95c-9fb3-417d-9f02-b41e82b841f7"
        },
        "currency" : "USD",
        "subtotal" : {
          "amount" : "255",
          "convertedAmount" : "255",
          "formattedAmount" : "$255.00",
          "formattedConvertedAmount" : "$255.00"
        },
        "updatedDate" : "2022-12-12T13:29:22.950Z",
        "conversionCurrency" : "USD",
        "buyerLanguage" : "en",
        "createdDate" : "2022-12-12T13:29:22.950Z"
      }
    },
    "entityFqdn" : "wix.ecom.v1.cart",
    "eventTime" : "2022-12-12T13:29:22.953616Z",
    "triggeredByAnonymizeRequest" : false
  } 
  ```
  Save the newly created cart's ID (`entityId` field in the above webhook's payload) for use in the flow below.

## Update a cart 

If a store owner wants to update a specific cart with a buyer note and remove a coupon, they can follow this basic flow. 

1. Pass the cart's ID (`entityId` field in the above webhook's payload) to the [Update Cart](https://dev.wix.com/api/rest/wix-ecommerce/cart/update-cart) endpoint to add a buyer note to the cart:

   ```js
   curl -X PATCH \
     'https://www.wixapis.com/ecom/v1/carts/33d99986-63b0-4f0e-a549-33bda4bef756' \
     -H 'Authorization: <AUTH>' \
     -H 'Content-Type: application/json' \
     -d '{
       "cartInfo": {
        "id": "33d99986-63b0-4f0e-a549-33bda4bef756",
        "buyerNote": "Please ship ASAP."
       }
     }'
   ```
   The response is the cart object containing the newly added buyer note.

2. Use [Remove Coupon](https://dev.wix.com/api/rest/wix-ecommerce/cart/remove-coupon) to remove a coupon from a cart.

   ```js
   curl -X POST \
     'https://www.wixapis.com/ecom/v1/carts/33d99986-63b0-4f0e-a549-33bda4bef756/remove-coupon' \
     -H 'Authorization: <AUTH>'
     -H 'Content-Type: application/json' \
   ```
