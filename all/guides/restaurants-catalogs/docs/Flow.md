SortOrder: 2
# Sample Use Case & Flow: Wix Restaurants Catalogs


This article shares possible use cases your app could support, as well as an example flow. 
You're certainly not limited to these use cases, but it can be a helpful jumping off point 
as you plan your app's implementation.


## Import a Catalog from an External POS


Your app could help site owners import a catalog from their external POS to Wix Restaurants. 
We recommend to use a [draft catalog](https://dev.wix.com/api/rest/wix-restaurants/catalogs/draft-catalogs) 
to update multiple entities of a catalog at once. This prevents customers from seeing partially updated menus.


1. Retrieve the external catalog.
1. Prepare a mapping to support future syncs and store it on your servers. Make sure to include all external IDs such as menu and dish IDs in the mapping.
1. Optional: Call the [List Locations](https://dev.wix.com/api/rest/business-info/locations/list-locations) endpoint. Identify and save the relevant location ID.
    > **Note:** You can skip this step if a restaurant has only a single location.
1. Retrieve all catalogs by calling the [List Catalogs](https://dev.wix.com/api/rest/wix-restaurants/catalogs/list-catalogs) endpoint. Identify the relevant catalog and save the corresponding catalog ID. If a restaurant has multiple locations, identify the relevant catalog by location ID.
1. [Create a draft catalog](https://dev.wix.com/api/rest/wix-restaurants/catalogs/draft-catalogs/create-draft-catalog) to synchronize your update.
1. Retrieve the existing menu IDs with the [List Menus](https://dev.wix.com/api/rest/wix-restaurants/catalogs/menus/list-menus) endpoint and save them.
1. Use the [Bulk Archive Menus](https://dev.wix.com/api/rest/wix-restaurants/catalogs/draft-catalogs/bulk-archive-menus) endpoint to archive all existing menus.
1. Add all variations to the draft catalog using the [Bulk Create Variations](https://dev.wix.com/api/rest/wix-restaurants/catalogs/draft-catalogs/bulk-create-variations) endpoint. Make sure to retrieve the item IDs and include them in your mapping.
1. Call the [Bulk Create Dishes](https://dev.wix.com/api/rest/wix-restaurants/catalogs/draft-catalogs/bulk-create-dishes) endpoint to add all dishes to the draft catalog. Make sure to retrieve the item IDs and include them in your mapping.
1. Use the [Bulk Create Sections](https://dev.wix.com/api/rest/wix-restaurants/catalogs/draft-catalogs/bulk-create-sections) endpoint to add all sections to the draft catalog. Make sure to retrieve the section IDs and include them in your mapping.
1. Add all menus to the draft catalog by calling the [Bulk Create Menus](https://dev.wix.com/api/rest/wix-restaurants/draft-catalogs/bulk-create-menus) endpoint. Make sure to retrieve the menu IDs and include them in your mapping.
1. Publish your changes to the live site using the [Publish Draft Catalog](https://dev.wix.com/api/rest/wix-restaurants/catalogs/draft-catalogs/publish-draft-catalog) endpoint.


## Update Wix Restaurants Catalogs According to Changes in an External POS


Your app can help site owners keep their Wix Restaurants catalogs up-to-date with changes to their external POS. Before you can start, you'll need to have a mapping between the two catalogs. You can read about one possible way to create such a mapping in the [Import a Catalog from an External POS](https://dev.wix.com/api/rest/wix-restaurants/catalogs/example-flow#wix-restaurants_catalogs_example-flows_import_a_catalog_from_an_external_pos) example flow above.

1. Listen to external webhooks for changes to the POS.
1. Update your mapping according to the changes.
1. Update the relevant Wix Restaurants catalog by calling the [Update Menu](https://dev.wix.com/api/rest/wix-restaurants/catalogs/menus/update-menu), [Update Section](https://dev.wix.com/api/rest/wix-restaurants/catalogs/sections/update-section), or [Update Item](https://dev.wix.com/api/rest/wix-restaurants/catalogs/items/update-items) endpoint. In case the update includes multiple changes, we recommend to use a [draft catalog](https://dev.wix.com/api/rest/wix-restaurants/catalogs/draft-catalogs).
