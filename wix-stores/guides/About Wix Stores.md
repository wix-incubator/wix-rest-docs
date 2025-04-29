# About Wix Stores
Wix enables site owners to quickly and easily create and manage an [online store](https://support.wix.com/en/article/about-wix-stores) for physical and/or digital products on their site. Read more about the [Wix Stores features](https://support.wix.com/en/article/wix-stores-features).

## About the Wix Stores catalog migration

Wix is introducing Catalog V3, a new set of APIs for the Wix Stores product catalog, set to roll out in Q2 2025. This upgraded catalog will empower Wix Store owners with enhanced tools to build more comprehensive product catalogs and streamline store management. Key improvements include more detailed management of product variants, advanced inventory capabilities, expanded customization options, and more.

Therefore, each site supports either [Catalog V1](https://dev.wix.com/docs/rest/business-solutions/stores/catalog/introduction) or [Catalog V3](https://dev.wix.com/docs/rest/business-solutions/stores/catalog-v3/introduction), but not both at the same time. Use the [Catalog Versioning API](https://dev.wix.com/docs/rest/business-solutions/stores/catalog-versioning/introduction) to determine the API version required for a given site.

Learn more in our [Catalog V1 to V3 conversion guide](https://dev.wix.com/docs/rest/business-solutions/stores/catalog-v3/catalog-v1-to-v3-conversion-guide).

## Terminology
- **The catalog** is a complete list of all the store’s products - compiled automatically. 
- **Collections** are themed groupings of items for purchase that a store owner can create to organize their products (e.g., Spring 2019, Running shoes, etc.). Products can belong to multiple collections.
- **Options** are property types that customers can select within the specific product - e.g., color and size. 
- **Selections** are the types available within each option - e.g., red and green selections under the Color option. 
- **Choices** are the specific choices the customer has made within a selection - e.g., choosing the red Selection triggers the red Choice.  
- **Variants** are combinations of  different product choices - e.g., a red shirt in size large.
A variant can override the following values from the parent product:
  - Price
  - SKU
  - Weight
  - Inventory
