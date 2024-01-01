SortOrder: 0
# restaurants-menus-menu

Responsible for managing a restaurant's menu
- A menu acts as a container for [sections](https://github.com/wix-private/restaurants-bazel/tree/master/restaurants-menus-section)
- Displayed by the [restaurants menus showcase livesite app](https://github.com/wix-private/restaurant-menus-showcase-livesite)
- Displayed and used by the future Restaurants Online-Ordering app

## Collaborators
- [Sections Service](https://github.com/wix-private/restaurants-bazel/tree/master/restaurants-menus-section)
    - Section deletion by the Sections Service triggers its deletion from all associated menus
    - Menu deletion triggers the deletion of its contained sections as long as those sections belong only for this menu
  
## Worth mentioning
- [Multilingual support](https://github.com/wix-private/server-infra/tree/master/framework/loom-prime/examples/prime-multilingual)

With the Menus menu API, you can:
* Create a menu
* Retrieve and query existing menus
* Update existing menu
* Delete existing menu

## Before you begin
This API requires that:
* The site owner installs the `Wix Restaurants Menus (New)` app.

