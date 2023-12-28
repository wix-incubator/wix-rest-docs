SortOrder: 0
# restaurants-menus-item

Responsible for managing a restaurant's menu item
- A menu item is attached to a [section](https://github.com/wix-private/restaurants-bazel/tree/master/restaurants-menus-section)
- Displayed by the [restaurants menus showcase livesite app](https://github.com/wix-private/restaurant-menus-showcase-livesite)
- Displayed and used by the future Restaurants Online-Ordering app

## Worth mentioning
- [Multilingual support](https://github.com/wix-private/server-infra/tree/master/framework/loom-prime/examples/prime-multilingual)

With the Menus Item API, you can:
* Read and manage items
* Retrieve and query existing items.
* Update existing items.
* Delete items.

## Before you begin
This API requires that:
* The site owner installs the `Wix Restaurants Menus (New)` app.

## Terminology
* **Item:** Anything that customers can buy in the restaurant.
* **Price:** The base cost of an item.
* **Price Variant:**  Different pricing options available for a menu item based on specific variations, such as size (small, medium, large), base ingredients (protein options), or preparation methods (thin/thick crust). An item can have either a Price or Price Variant.
