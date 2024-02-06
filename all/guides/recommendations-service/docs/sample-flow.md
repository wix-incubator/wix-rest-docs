SortOrder: 1
# Sample Flows
This article shares a possible use case your app could support, as well as an example flow that could support the use case. You're certainly not limited to this use case, but it may be a helpful jumping-off point as you plan your app's implementation.


## Show bestselling products from a Wix site in your app
In this scenario, you are selling products through multiple channels, one of which is a website using Wix Stores. You want your app to showcase the bestselling items from each of your channels. To show the bestselling items from the Wix Stores catalog in your app, follow this basic flow:

1. Call [`List Available Algorithms`](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/recommendations/list-available-algorithms) to get the `algorithmId` of the "Best sellers" algorithm.
2. Call [`Get Recommendation`](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/recommendations/get-recommendation) with the `algorithmId` from step 1. Use the Wix Stores app ID (`215238eb-22a5-4c36-9e7b-e7c08025e04e`) in the algorithm object.
3. For each item in the object returned by `Get Recommendation`, call [`Get Product`](https://dev.wix.com/docs/rest/api-reference/wix-stores/catalog/get-product) in the Wix Stores Catalog API using the recommended item’s `catalogItemId`.
4. Using the product information in the responses from `Get Product`, display the bestselling items in your app.
