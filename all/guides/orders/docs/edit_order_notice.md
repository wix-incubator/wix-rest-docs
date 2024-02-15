SortOrder: 5
# Edit Order/Draft Orders API Migration Guide

> **Notes:**
>
> + This migration is relevant for all apps that currently use the Stores Orders API.
> + The Stores Orders API will soon be deprecated in favor of the eCommerce Orders API.

We’re introducing a new Wix eCommerce Orders API that enables business owners to meet new customer needs and provide better customer service. This will eventually replace the existing Stores Orders API. This quick guide will help you to make sure your app is ready for the migration.

## New object and webhook structures

The structure of the eCommerce Order object is different from the Stores Order object. You can learn more about these structural changes [here](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-object-conversion).

The webhook payload structure has also changed. To facilitate your move to these webhooks, have a look at the [webhook conversion table](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-object-conversion#webhook-conversion-table).

## Users can now edit orders

Customers occasionally make mistakes when placing an order, or they might simply want to make a change to an existing order. This could include adding items, updating prices, revising customer details, and more.

The new eCommerce service includes functionality that lets users edit existing orders. **This will be known as Draft Orders when using our REST APIs, and as Edit Order in the dashboard.**

When an existing order is edited, the [Order Updated Webhook](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-updated) is triggered. This webhook returns the whole order object in the eCommerce order structure, but you can still pass the edited order’s ID to the Stores Orders endpoints if you’d like to fetch the order in the Stores structure.

## Impact examples

If a Wix user edits an existing order, depending on your app type you might need your app to be aware of the change. Here are some examples:

- A user changes the quantity of a product item in an existing order. As a result, the number of items to be shipped has changed.
- A user changes the shipping address in an existing order.
- A user adds a new item to an existing order. As a result, the amount to be paid changes.
- A user changes the price of an item in an existing order. As a result, the total payable amount of the order, as well as the payment status can change.

## How to add the new Order Updated webhook

1. Go to your app in the [Wix Developers Center](https://dev.wix.com/).
2. Go to the **Webhooks** tab in the side menu.
3. Click **+ Add Webhook**.
4. Select an **API Category** > **Wix eCommerce**
5. Find and select the [Order Updated Webhook](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/order-updated)
6. Add a **Callback URL**.
7. Click **Save**.

## How to test the impact on your app

Edit Order is not yet available publicly, but if you’d like to test the feature yourself and understand any implications it may have for your app, follow these steps:

1. Install the [EditThisCookie Chrome extension](https://chromewebstore.google.com/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?pli=1).
2. Click + to add a new cookie, select `petri-ovr` and fill out the following fields:
- Value: `specs.stores.OrderEditPageComponent#true`
- Domain: `.wix.com`
- Secure: Check the box
- HttpOnly: Check the box

![editorder](https://s3.amazonaws.com/wixplorer-readme-images/orders%2Fedit-order.jpg)

3. Create a new Wix website with Wix Stores installed (testing this change only works on **new sites**).
4. Refresh the **Orders** page.
5. Navigate to an [unfulfilled order in the dashboard](https://support.wix.com/en/article/wix-stores-fulfilling-store-orders).
6. Click on the **More Actions** button in the top right corner.
7. Click on **Edit Order**.

> **Note:**
>
> All orders, including changes committed by Edit Order, are still available in the Stores Orders APIs and webhooks. However, we highly recommend planning your transition to eCommerce Orders and Edit Order/Draft Orders, as the Stores Orders API will be deprecated in the coming months.
