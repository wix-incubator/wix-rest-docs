SortOrder: 1
# Example Flows

This article shares some possible flows when using the Subscription Options API.

## Creating a subscription option and assigning it to a product

### Part 1: Creating a Subscription Option

For this use case we're creating an 8 week-long subscription that provides a 10% discount off the original price.
Using [Create Subscription Option](/docs/link), your request would look something like this:

  ```json
    {
      "subscriptionOption": {
        "title": "Weekly sub - 8 weeks",
        "description": "Save 10% on weekly subscription",
        "subscriptionSettings": {
          "frequency": "WEEK",
          "billingCycles": 8
        },
        "discount": {
          "type": "PERCENT",
          "value": 10
        }
      }
    }
```

The response is the newly created subscription option with its auto-generated ID:

 ```json
    {
      "subscriptionOption": {
        "id": "fb5f1365-472c-4445-bee0-1d3fb0591224",
        "title": "Weekly sub - 8 weeks",
        "description": "Save 10% on weekly subscription",
        "subscriptionSettings": {
          "frequency": "WEEK",
          "billingCycles": 8
        },
        "discount": {
          "type": "PERCENT",
          "value": 10
        }
      }
    }
```


### Part 2: Assigning the Subscription Option to a Product

Now that we've created the subscription option,
we can use [Assign Subscription Options To Product](/docs/link).
1. Pass the `productId` of the designated product for assignment as a path parameter in the url:
    ```
    https://www.wixapis.com/stores/v1/subscription-options/product/{productId}/assign
    ```

2. The request will contain one or more subscription option IDs to be assigned to the product,
    and whether to hide the subscription option from the product (default is `false` - not hidden).

    ```json
    {
      "assignedSubscriptionOptions": [
        {
          "id": "fb5f1365-472c-4445-bee0-1d3fb0591224",
          "hidden": false
        }
      ]
    }
    ```

   The response is an empty object.

### Part 3: Checking that the Subscription Option was assigned to the Product

To check that the subscription option has been assigned to the product, use the [Get Subscription Options For Product](/docs/link) endpoint.
1. Pass the same `productId` as the one used in part 2. To retrieve all the subscription options assigned to the product include the path parameter `includeHiddenSubscriptionOptions=true`:

    ```curl
    curl -X GET \
      'https://www.wixapis.com/stores/v1/subscription-options/byProduct/{productId}?        includeHiddenSubscriptionOptions=false' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>'
    ```
    The response is an array of the subscription options assigned to the product.

    ```json
    {
      "subscriptionOptions": [
        {
          "id": "475c6eff-6e2d-4a27-9b2b-ef096eacd56d",
          "hidden": false,
          "title": "Coffee of the Month",
          "description": "Subscribe and save 15%",
          "subscriptionSettings": {
            "frequency": "WEEK",
            "autoRenewal": false,
            "billingCycles": 6
          },
          "discount": {
            "type": "PERCENT",
            "value": 15
          }
        },
        {
          "id": "ab3b23a2-af20-4b63-9f30-fe7981029405",
          "hidden": false,
          "title": "Monthly for a Year",
          "description": "Annual Subscription",
          "subscriptionSettings": {
            "frequency": "MONTH",
            "autoRenewal": false,
            "billingCycles": 12
          },
          "discount": {
            "type": "PERCENT",
            "value": 20
          }
        }
      ]
    }
    ```
## Allowing a Product to be Sold as a One-Time Purchase
When a subscription option is assigned to a product, by default that product will only be available for purchase as a subscription. To allow for one-time purchase in addition to a subscription, you could use a flow like this:

1. Using [Get One Time Purchases Status](/docs/link), pass the `productId` of the product you'd like to check as a path parameter:

    ```curl
    curl -X GET \
      'https://www.wixapis.com/stores/v1/subscription-options/product/{productId}/oneTimePurchasesStatus' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>'
    ```

   The response is an object that holds a field with a boolean value:

    ```
    {"allowed": false}
    ```

2. Using [Allow One Time Purchases](/docs/link), pass the `productId` as a path parameter, and `"allowed": true` in the body

    ```curl
    curl -X PATCH \
      'https://www.wixapis.com/stores/v1/subscription-options/product/{productId}/allowOneTimePurchase' \
      --data-binary '{
        "allowed": true
      }'\
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>'
    ```

    The response is an empty object.