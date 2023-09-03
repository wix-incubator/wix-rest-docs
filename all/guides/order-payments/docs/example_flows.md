SortOrder: 1
# Example Flows

This article shares some examples of actions available with the Order Payments API.


## Getting an Order's Transaction Records

To retrieve a single order's transactions (both payments and refunds), pass the `orderId` to the [List Transactions For Single Order](hhttps://bo.wix.com/wix-docs/rest/ecommerce/order-payments/list-transactions-for-single-order) endpoint:

```sh
curl -X GET 'https://www.wixapis.com/ecom/v1/payments/orders/{orderId}' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>'
```

The response will contain the transactions associated with the order, including payment and refund details:

```json
{
  "orderTransactions": {
    "orderId": "4bab5870-7943-4a9e-8d4e-96719b3e4f38",
    "payments": [
      {
        "id": "7206d5d6-7479-4e5f-a12b-b43a36a52e71",
        "regularPaymentDetails": {
          "gatewayTransactionId": "777c7ce0-a045-4145-ab1f-176097db357c",
          "paymentMethod": "offline",
          "providerTransactionId": "842ac03f-3ef2-4bf7-90ac-19c9775b3ba6",
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
            "paymentId": "7206d5d6-7479-4e5f-a12b-b43a36a52e71",
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
  }
}
```

## Getting Transaction Records for Multiple Orders

To retrieve transaction details for several orders, pass the `orderIds` to [List Transactions For Multiple Orders](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments/list-transactions-for-multiple-orders):

```sh
curl -X POST 'https://www.wixapis.com/ecom/v1/payments/list-by-ids' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>'
    --data-binary '{
        "orderIds": [
            "ORDER_ID_1",
            "ORDER_ID_2"
        ]
    }'\
```

The response will contain an array of transactions associated with the specified orders, including payment and refund details:

```json
{
  "orderTransactions": [
    {
      "orderId": "4bab5870-7943-4a9e-8d4e-96719b3e4f38",
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
      "orderId": "6ae38b2e-455b-4e20-b418-01fca82edaa8",
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
      "refunds": [] // This order has no refunds
    }
  ]
}
```

## Getting an Order's Invoices

To retrieve a single order's invoice/s, pass the `orderId` to the [List Invoices For Single Order](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments/list-invoices-for-single-order) endpoint:

```sh
curl -X GET 'https://www.wixapis.com/ecom/v1/invoices/orders/{orderId}' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>'
```

The response will contain the invoices associated with the order:

```json
{
  "invoices": [
    {
      "id": "7c6109b5-259c-4378-ba62-d22bc56c9e93",
      "appId": "1380b703-ce81-ff05-f115-39571d94dfcd"
    }
  ]
}
```

## Getting Invoices for Multiple Orders

To retrieve invoices for several orders, pass the `orderIds` to [List Invoices For Multiple Orders](https://bo.wix.com/wix-docs/rest/ecommerce/order-payments/list-invoices-for-multiple-orders):

```sh
curl -X POST 'https://www.wixapis.com/ecom/v1/invoices' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>'
  --data-binary '{
        "orderIds": [
            "ORDER_ID_1",
            "ORDER_ID_2",
            "ORDER_ID_3"
        ]
  }'\
```

The response will contain an array of invoices coupled with their respective order IDs:

```json
{
  "invoicesForOrder": [
    {
      "orderId": "3dbebe78-1ce0-4a10-adc6-7300c10756a6",
      "invoicesInfo": [
        {
          "id": "7c6109b5-259c-4378-ba62-d22bc56c9e93",
          "appId": "1380b703-ce81-ff05-f115-39571d94dfcd"
        }
      ]
    },
    {
      "orderId": "fa734a26-5a0f-4d24-bc2f-8b8c0512fe1e",
      "invoicesInfo": [
        {
          "id": "e163ac7f-ecbc-4a12-bdcd-6971a52e1e12",
          "appId": "1380b703-ce81-ff05-f115-39571d94dfcd"
        }
      ]
    }
  ]
}
```