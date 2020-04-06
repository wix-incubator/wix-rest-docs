SortOrder: 0
# Catalog Service

## About This API

Wix Stores creates a catalog of store owners’ items for purchase and allows store owners to  create smaller collections of products by type or theme. The catalog (known to Wix store owners as the "All Products Collection") organizes the store’s products and collections and facilitates inventory management. With the Wix Stores Catalog API you can query individual products, collections or the entire catalog.  

Querying the products and collections in the catalog enables you to coordinate a store’s inventory across other sales platforms (e.g., Facebook marketplace), or inventory management tools (e.g., NetSuite, TradeGecko), among other uses.  

## Limitations

Every product in a Wix site owner's store is limited to max 6 options (e.g., size, color, style) with max 30 choices (small, medium, blue, green, hipster, gangster) per option.
In addition, if the Wix site owner wants to manage variants (treat variants as separate products, with unique SKUs, prices and weights) they are limited to max 300 variants (combinations of product choices - e.g., a blue shirt in size medium) per product.
Every product is also limited to max 15 media items.

## Query language

For endpoints that allow querying, the format follows the following [guidelines](https://dev.wix.com/api/getting-started#api-query-language).  
