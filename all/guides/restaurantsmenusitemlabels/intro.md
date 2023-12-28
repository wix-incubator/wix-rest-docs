SortOrder: 0
# restaurants-menus-item-labels

Responsible for managing a restaurant's item labels
- An item label is attached to an [item](https://github.com/wix-private/restaurants-bazel/tree/master/restaurants-menus-item)
- Displayed by the [restaurants menus showcase livesite app](https://github.com/wix-private/restaurant-menus-showcase-livesite)
- Displayed and used by the future Restaurants Online-Ordering app

## Collaborators
- [Items Service](https://github.com/wix-private/restaurants-bazel/tree/master/restaurants-menus-item)
  - Label deletion by the Labels Service triggers its deletion from all associated items

## Worth mentioning
- [Multilingual support](https://github.com/wix-private/server-infra/tree/master/framework/loom-prime/examples/prime-multilingual)

## Before you begin
This API requires that:
* The site owner installs the `Wix Restaurants Menus (New)` app.

With the Menus Item Labels API, you can:
* Create a label
* Retrieve and query existing labels
* Update existing label
* Delete existing label

## Terminology
* **Label:** Information about the ingredients and constituents of a menu item. For example "spicy", "hot", "vegan", "gluten-free", or "organic".
