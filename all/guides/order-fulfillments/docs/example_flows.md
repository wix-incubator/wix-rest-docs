SortOrder: 1
# Sample Flow

This article presents a sample flow your app can support. You aren't limited to this exact flow, but it can be a helpful jumping off point as you plan your Wix eCommerce app.

## Listen for new orders and create a fulfillment for an order

1. A customer places an order.
2. Using the [Order Approved Webhook](https://dev.wix.com/api/rest/wix-ecommerce/orders/order-approved-webhook), listen for incoming approved orders.

    ```json
    {
      "id" : "520d5673-b7fb-4e7f-8e05-e6489a73d734",
      "slug" : "approved",
      "entityId" : "880fa895-dfd5-4d50-a2d4-971b03fd4b86",
      "entityFqdn" : "wix.ecom.v1.order",
      "eventTime" : "2022-12-21T13:30:45.872Z",
      "actionEvent" : {
        "body" : {
          "order" : {
            "id" : "880fa895-dfd5-4d50-a2d4-971b03fd4b86",
            "number" : "10002",
            "cartId" : "866a0cf8-d7ec-4ec5-b20f-08cf33d8ad74",
            "updatedDate" : "2022-12-21T13:30:39.075Z",
            "checkoutId" : "6f1204d5-3923-4709-869e-51680a1b5530",
            "buyerLanguage" : "en",
            "fulfillmentStatus" : "NOT_FULFILLED",
            "createdDate" : "2022-12-21T13:30:36.798Z"
            ...
          }
        }
      }
    }
    ```

3. Pass the new order's ID (`entityId` or `actionEvent.body.order.id` fields in the above webhook's payload) and the new fulfillment's info to the [Create Fulfillment](https://dev.wix.com/api/rest/wix-ecommerce/order-fulfillments/create-fulfillment) endpoint.

    ```bash
    curl -X POST \
      'https://www.wixapis.com/ecom/v1/fulfillments/orders/880fa895-dfd5-4d50-a2d4-971b03fd4b86/create-fulfillment' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>' \
      --data-binary '{
        "fulfillment": {
          "lineItems": [
            {
              "id": "00000000-0000-0000-0000-000000000001",
              "quantity": 1
            }
          ],
          "trackingInfo": {
            "trackingNumber": "12345",
            "shippingProvider": "fedex"
          }
        }
      }'
    ```
    The response will hold info about the newly created fulfillment and the ID of its associated order.

4. To retrieve the order's fulfillments, pass the order's ID to the [List Fulfillments For Single Order](https://dev.wix.com/api/rest/wix-ecommerce/order-fulfillments/list-fulfillments-for-single-order) endpoint:

    ```bash
    curl -X GET 'https://www.wixapis.com/ecom/v1/fulfillments/orders/880fa895-dfd5-4d50-a2d4-971b03fd4b86' \
        -H 'Content-Type: application/json' \
        -H 'Authorization: <AUTH>'
    ```

    The response will contain the fulfillments associated with the order, including the fulfillment ID and tracking info:

    ```json
    {
      "orderWithFulfillments": {
        "orderId": "880fa895-dfd5-4d50-a2d4-971b03fd4b86",
        "fulfillments": [
          {
            "id": "80f939c8-cdc4-44fe-a058-b54d506af170",
            "createdDate": "2021-05-25T13:55:26.458Z",
            "lineItems": [
              {
                "id": "00000000-0000-0000-0000-000000000001",
                "quantity": 1
              }
            ],
            "trackingInfo": {
              "trackingNumber": "12345",
              "shippingProvider": "fedex",
              "trackingLink": "https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber=12345"
            }
          }
        ]
      }
    }
    ```