SortOrder: 1
# About Wix Restaurants Catalogs

With Wix Restaurants Catalogs, site owners can manage individual catalogs for each of their restaurant locations.

The Catalogs API allows your app to:

* Retrieve catalogs
* Read and manage menus, sections, dishes, variations, and discounts
* Use draft catalogs to synchronize updates

You can read more about setting up and managing multiple locations for a business with the [Locations API](https://dev.wix.com/api/rest/business-info/locations/introduction).


## Terminology


* **Catalog:** Collection of menus and discounts available in a specific location.
* **Draft Catalog:** Allows you to publish multiple changes to a catalog at the same time.
* **Menu:** Catalogs are made up of menus. For example "Breakfast", "Lunch", and "Dinner" menus.
* **Section:** Menus are made up of sections. For example "Appetizers", "Entrees", and "Desserts" sections.
* **Item:** Anything that customers can buy in the restaurant. Can be of type dish or variation.
    + **Dish:** Item that appears in a section of a menu.
    + **Variation:** Item that doesn't appear in a section on its own, only as a choice for a dish.
* **Choice:** Item that customers can choose to modify a dish. Both item types variation and dish are supported.
    + **Available Choices:** All possible choices for a dish.
    + **Default Choices:** The choices for a dish that are selected by default.
    + **Selected Choices:** The choices a customer has selected for a dish.
* **Dish Option:** Type of the choice. Can be an extra, selection, or deselection.
    + **Extra:** Item that customers can add to a dish. For example a topping. Customers can add multiple extras per dish.
    + **Selection:** Item that customers can select. For example a dish size. Customers can choose only a single selection per dish.
    + **Deselection:** Item that customers can remove from a dish. For example a specific ingredient. Customers can remove multiple deselections per dish.
* **Label:** Information about the ingredients and constituents of a dish. For example "spicy", "hot", "vegan", "gluten-free", or "organic".
* **Discount:** Can be an amount or percentage. Applies to a catalog, section, or dish. Customers may need to enter a coupon code to receive the discount.


## Limitations

* Each location has a single catalog.
* A section belongs to a single menu.
* You can create discounts for catalogs, sections, or dishes. You can't create a discount that applies to a menu.
* Currently, the [Catalog Changed](https://dev.wix.com/api/rest/wix-restaurants/catalogs/catalogs/catalog-changed-webhook) webhook doesn't return information about what has changed. In order to update an external POS upon changes to a Wix Restaurants catalog you may need to create your own logic to identify the changes.
