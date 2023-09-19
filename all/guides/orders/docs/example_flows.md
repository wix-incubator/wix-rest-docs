SortOrder: 4
# Example Flows

This article shares some possible use cases for the Orders API, namely the flow from this API to
the [Order Payments](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments)
and [Order Fulfillments](https://bo.wix.com/wix-docs/rest/ecommerce/order-fulfillments) APIs. You're certainly not
limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.

The `order.id` is the key to getting and managing the order's payment and fulfillment information. This is done by
passing it to certain Order Payments and Order Fulfillments APIs. Follow these steps to retrieve multiple orders'
transaction records or fulfillment details.

## Querying orders and retrieving their transaction records

1. **Use [Query Orders](https://bo.wix.com/wix-docs/rest/ecommerce/orders/query-orders) to retrieve the relevant orders**

   In this example we've queried for orders that have been paid for, and have been fulfilled:

    ```sh
    curl -X POST \
      'https://www.wixapis.com/ecom/v1/orders/query' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>' \
      --data-binary '{
        "query": {
          "filter": {
            "paymentStatus": "PAID",
            "fulfillmentStatus": "FULFILLED"
          }
        }
      }'
    ```

   The response will contain the orders that pass the specified filters:

    ```json
    {
      "orders": [
        {
          "id": "265c7d98-a7c3-48c4-89cd-bbdc00921eab",
          "number": "10108",
          "createdDate": "2021-05-25T13:51:01.718Z",
          "updatedDate": "2021-05-25T13:55:55.130Z",
          "lineItems": [...],
          "buyerInfo": {...},
          "paymentStatus": "PAID",
          "fulfillmentStatus": "FULFILLED",
          ...
        },
        {
          "id": "d1748680-7fd5-401e-9f71-cd3b9ea70bdb",
          "number": "10109",
          "createdDate": "2021-06-22T11:47:15.134Z",
          "updatedDate": "2021-07-04T13:40:15.860Z",
          "lineItems": [...],
          "buyerInfo": {...},
          "paymentStatus": "PAID",
          "fulfillmentStatus": "FULFILLED",
          ...
        }
      ]
    }
    ```

2. **Pass the returned order IDs
   to [List Transactions for Multiple Orders](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments/list-transactions-for-multiple-orders):**

    ```sh
    curl -X POST \
      'https://www.wixapis.com/ecom/v1/payments/list-by-ids' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>' \
      --data-binary '{
        "orderIds": [
          "265c7d98-a7c3-48c4-89cd-bbdc00921eab",
          "d1748680-7fd5-401e-9f71-cd3b9ea70bdb"
        ]
      }'
    ```

   The response holds both payment and refund information for all `orderIDs` passed:

    ```json
    {
      "orderTransactions": [
        {
          "orderId": "265c7d98-a7c3-48c4-89cd-bbdc00921eab",
          "payments": [
            {
              "id": "b2215acc-4222-49a6-96ab-41f83272d603",
              "regularPaymentDetails": {
                "gatewayTransactionId": "777c7ce0-a045-4145-ab1f-176097db357c",
                "paymentMethod": "offline",
                "providerTransactionId": "234f46ee-923b-4ca5-9732-1f6588e1daf3",
                "offlinePayment": false,
                "status": "APPROVED"
              },
              "createdDate": "2021-07-01T16:36:32.510Z",
              "amount": {
                "amount": "13.0",
                "formattedAmount": "$13.00"
              },
              "refundDisabled": false
            }
          ],
          "refunds": [
            {
              "id": "39681184-254b-5fb6-0c94-320347576397",
              "transactions": [
                {
                  "paymentId": "b2215acc-4222-49a6-96ab-41f83272d603",
                  "amount": {
                    "amount": "13.0",
                    "formattedAmount": "$13.00"
                  },
                  "refundStatus": "SUCCEEDED",
                  "externalRefund": true
                }
              ],
              "details": {
                "items": [
                  {
                    "lineItemId": "2c204c9d-033c-c63c-9d7c-df791f553624",
                    "quantity": 1
                  }
                ],
                "shippingIncluded": true
              },
              "createdDate": "2021-07-01T16:36:38.532Z"
            }
          ]
        },
        {
          "orderId": "d1748680-7fd5-401e-9f71-cd3b9ea70bdb",
          "payments": [
            {
              "id": "a0275fed-84c0-44dc-9dcf-2d54bab53ad0",
              "regularPaymentDetails": {
                "gatewayTransactionId": "835477ca-5afd-4f78-bfb0-b52f064922e6",
                "paymentMethod": "offline",
                "providerTransactionId": "842ac03f-3ef2-4bf7-90ac-19c9775b3ba6",
                "offlinePayment": false,
                "status": "APPROVED"
              },
              "createdDate": "2021-06-28T10:23:36.473Z",
              "amount": {
                "amount": "21.0",
                "formattedAmount": "$21.00"
              },
              "refundDisabled": false
            }
          ],
          "refunds": []
        }
      ]
    }
    ```

## Querying orders and retrieving their fulfillment details

1. **Use [Query Orders](https://bo.wix.com/wix-docs/rest/ecommerce/orders/query-orders) to get the relevant orders**

   In this example we've queried for orders that have been paid for, and fulfilled:

    ```sh
    curl -X POST \
      'https://www.wixapis.com/ecom/v1/orders/query' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>' \
      --data-binary '{
        "query": {
          "filter": {
            "paymentStatus": "PAID",
            "fulfillmentStatus": "FULFILLED"
          }
        }
      }'
    ```

   The response will contain the orders that pass the specified filters:

    ```json
    {
      "orders": [
        {
          "id": "265c7d98-a7c3-48c4-89cd-bbdc00921eab",
          "number": "10107",
          "createdDate": "2021-05-05T11:34:05.079Z",
          "updatedDate": "2021-05-05T11:34:05.114Z",
          "lineItems": [...],
          "buyerInfo": {...},
          "paymentStatus": "PAID",
          "fulfillmentStatus": "FULFILLED",
          ...
        },
        {
          "id": "d1748680-7fd5-401e-9f71-cd3b9ea70bdb",
          "number": "10105",
          "createdDate": "2021-01-17T11:55:39.947Z",
          "updatedDate": "2021-01-17T11:56:03.631Z",
          "lineItems": [...],
          "buyerInfo": {...},
          "paymentStatus": "PAID",
          "fulfillmentStatus": "FULFILLED",
          ...
        }
      ]
    }
    ```

2. **Pass the returned order IDs
   to [List Fulfillments For Multiple Orders](https://bo.wix.com/wix-docs/rest/ecommerce/order-fulfillments/list-fulfillments-for-multiple-orders):**

    ```sh
    curl -X POST \
      'https://www.wixapis.com/ecom/v1/fulfillments/list-by-ids' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>' \
      --data-binary '{
        "orderIds": [
          "265c7d98-a7c3-48c4-89cd-bbdc00921eab",
          "d1748680-7fd5-401e-9f71-cd3b9ea70bdb"
        ]
      }'
    ```

   The response holds fulfillment details, including line items fulfilled and shipping tracking info for all `orderIDs`
   passed:

    ```json
    {
      "ordersWithFulfillments": [
        {
          "orderId": "265c7d98-a7c3-48c4-89cd-bbdc00921eab",
          "fulfillments": [
            {
              "id": "80f939c8-cdc4-44fe-a058-b54d506af170",
              "createdDate": "2021-05-25T13:55:26.458Z",
              "lineItems": [
                {
                  "id": "00000000-0000-0000-0000-000000000001",
                  "quantity": 2
                }
              ],
              "trackingInfo": {
                "trackingNumber": "12345",
                "shippingProvider": "ups",
                "trackingLink": "https://wwwapps.ups.com/WebTracking/track?track=yes&trackNums=12345"
              }
            },
            {
              "id": "eb9138ff-1490-4dbc-b053-743240b9ab8f",
              "createdDate": "2021-05-25T13:55:47.605Z",
              "lineItems": [
                {
                  "id": "00000000-0000-0000-0000-000000000002",
                  "quantity": 3
                }
              ],
              "trackingInfo": {
                "trackingNumber": "12345",
                "shippingProvider": "ups",
                "trackingLink": "https://wwwapps.ups.com/WebTracking/track?track=yes&trackNums=12345"
              }
            }
          ]
        },
        {
          "orderId": "d1748680-7fd5-401e-9f71-cd3b9ea70bdb",
          "fulfillments": [
            {
              "id": "9f6ff4c4-1fb2-4b0a-b433-32956052316c",
              "createdDate": "2021-07-04T13:40:15.860Z",
              "lineItems": [
                {
                  "id": "00000000-0000-0000-0000-000000000001",
                  "quantity": 1
                }
              ],
              "trackingInfo": {
                "trackingNumber": "102030",
                "shippingProvider": "dhl",
                "trackingLink": "https://www.logistics.dhl/global-en/home/tracking.html?tracking-id=102030"
              }
            }
          ]
        }
      ]
    }
    ```