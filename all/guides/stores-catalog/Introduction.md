SortOrder: 0
# Catalog Service

## About This API

Wix Stores creates a catalog of store owners’ items for purchase and allows store owners to create smaller collections of products by type or theme. A catalog organizes the store’s products and collections and facilitates inventory management. With the Wix Stores Catalog API you can query individual products, collections or the entire catalog, as well as create products and add their media. 

Querying the products and collections in the catalog enables you to coordinate a store’s inventory across other sales platforms (e.g., Facebook marketplace), or inventory management tools (e.g., NetSuite, TradeGecko), among other uses.

## Terminology
- **The catalog** is a complete list of all the store’s products. 
- **Collections** are themed groupings of items for purchase that a store owner can create to organize their products (e.g., Spring 2019, Running shoes, etc.). Products can belong to multiple collections.
- **Options** are property types that customers can select within the specific product - e.g., color and size. 
- **Choices** are the available selections within each option - e.g., red and green choices under the Color option.  
- **Variants** are combinations of different product options and choices - e.g., a red shirt in size large.
A variant can override the following values from the parent product:
  - Price
  - SKU
  - Weight
  - Inventory

## Error handling
| Status code | Description |
| --- | --- |
| 200 |Success|
| 400 |Invalid input (e.g., when the filter format is not valid or when providing invalid options when calling productOptionsAvailability)|
| 401 |Invalid authorization token, or Wix stores is not installed|
| 404 |Requested product or collection is not found|
| 500 |Unexpected error|
