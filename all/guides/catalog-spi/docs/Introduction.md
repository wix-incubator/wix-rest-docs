SortOrder: 0
# About the eCommerce Catalog SPI

The Catalog SPI lets you become a Wix catalog provider. This means you can integrate any external repository of sellable items with the Wix eCommerce platform. Wix calls the Catalog SPI to get up-to-date information about items whenever a cart or checkout is updated, and when an item is added to an order.

With the Catalog SPI, you can:

+ Build a comprehensive business solution offering functionality that differs from Wix's in-house solutions like [Wix Stores](https://support.wix.com/en/article/wix-stores-about-wix-stores) or [Wix Bookings](https://support.wix.com/en/article/wix-bookings-about-wix-bookings), and integrate your solution with the Wix eCommerce platform to handle transactional capabilities. For example, develop an app to manage equipment rentals, online courses, subscriptions, or vouchers.
+ Integrate an externally managed repository of sellable items with the Wix eCommerce platform to meet specific business needs. For example, if your business handles pricing or availability in a unique way, or if you sell items that aren't easily categorized as physical or digital products or services.
+ Create a Wix app to integrate an existing eCommerce repository on a different platform with Wix's eCommerce platform.

## Why an external catalog?

The Catalog SPI enables you to maintain a complex and dynamic external catalog while being confident Wix can retrieve the latest information for every action.

For example, after a customer adds a particular item to their cart, one of the following details might change in your dynamic catalog:

+ The name of the item might be changed.
+ The price might be adjusted.
+ The item might go out of stock.

With the Catalog SPI, you can be sure that when the customer moves the item from their cart to their checkout, Wix will retrieve the updated details from your catalog automatically.

## Before you begin

It's important to note the following points before starting to code:

+ Existing solutions may already provide the catalog functionality that you need. Check out [Wix Stores](https://support.wix.com/en/article/wix-stores-about-wix-stores) and [Wix Bookings](https://support.wix.com/en/article/wix-bookings-about-wix-bookings), which provide built-in catalogs. If they cater to your needs, you probably don't need to implement the Catalog SPI.
+ For an overview of the Wix eCommerce platform and its capabilities, take a look at the [Wix eCommerce Platform Handbook](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/wix-e-commerce-platform-handbook/introduction).
+ We are constantly updating functionality. Check the documentation regularly to see the latest capabilities. Currently, external catalog integration has a few limitations:
    + Coupons and subscriptions aren't yet supported.
    + Preview mode in the Wix editor doesn't reflect full functionality.
    + Integration with external sales channels isn't yet available.

## Get started

To integrate an external catalog with the Wix eCommerce platform:

1. Create a database of items on the platform of your choice.
1. Learn how to [handle item variants](./Catalog-Reference.md) with the Catalog SPI.
1. Implement the [Get Catalog Items](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/catalog-spi/get-catalog-items) endpoint so Wix can retrieve the information it needs about specific items.
1. Create an app in the [Wix Developers Center](https://dev.wix.com/) and [add a catalog integration extension](#configuration).

## App Configuration

To enable your Wix app to communicate with your external catalog:

1. Open your app's page in the [Wix Developers Center](https://dev.wix.com/apps). 

1. Click **Extensions** in the left sidebar to open your app’s Extensions page.

1. Click **Create Extension**.

1. Scroll down to **Ecom Catalog** and click **Create**.

1. In the JSON editor, assign the URI where the Catalog SPI is implemented to `deploymentUri`. For example:

    ```json
    {
        "deploymentUri": "https://my-external-catalog.com"
    }
    ```

    **Note:** Other fields in the JSON editor are reserved for future functionality.

1. Click **Save**.

## Terminology

+ **Catalog:** A repository containing items for sale. Wix business solutions, such as Wix Bookings and Wix Stores, provide built-in catalogs. External business solutions can provide the Wix eCommerce platform with access to their catalogs via the Catalog SPI. This enables robust integration of the platform’s cart and checkout functionalities with diverse business types.
+ **Item:** An item in a catalog can be anything sellable, including physical products, services, gift cards, pricing plans, and custom items created for individual transactions like specialized project work.
+ **Cart:** A customer's cart holds information about a potential transaction, including details about selected items, prices, and discounts, as well as the potential buyer. Site visitors can see their cart on the cart page. Developers can access and manage a customer's cart with the [Cart API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/cart/introduction). When an item is added to a cart, Wix calls the Catalog SPI to retrieve current details for the item.
+ **Checkout:** Checkout is the page where a buyer finalizes a purchase. Each checkout holds information about the items to be purchased, price and tax summaries, shipping and billing information, any applied discounts, and more. Developers can access and manage checkout details and trigger checkout-related events with the [Checkout API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/checkout/introduction). When an item is added to a checkout, Wix calls the Catalog SPI to retrieve current details for the item.
+ **Order:** Once a customer has committed to a purchase, an order is created. An order holds information about purchased items, price and tax summaries, shipping and billing information, any applied discounts, and the status of payment and fulfillment. In the dashboard, business staff can create new orders, view and edit existing orders, track fulfillment, and manage the payments cycle. The [Orders API](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/orders/introduction) enables apps or site owners to customize management of the order lifecycle, including viewing, editing, approving, canceling, and charging. When an item is added to an order, Wix calls the Catalog SPI to retrieve current details for the item.
