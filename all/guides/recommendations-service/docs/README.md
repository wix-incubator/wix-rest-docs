SortOrder: 0
# Introduction
The Recommendations API allows users to promote and recommend items to their customers.  Users can get item recommendations from catalogs on their site using algorithms provided by installed apps. 

>**Note:** Currently, the Recommendations API is for use with Wix Stores only.

With the Recommendations API, you can:
* Get a [list of algorithms](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/recommendations/list-available-algorithms) available for use on your site.
* Get a [list of recommended items](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/recommendations/get-recommendation) suggested by a given algorithm.


## Algorithms
Algorithms are programs that identify and return a set of item recommendations based on a catalog. There are different types of algorithms, identified by their `algorithmType` that calculate different kinds of recommendations. For example, Algorithms with the `algorithmType` of `RELATED_ITEMS` also take a list of items as input and use those to calculate recommendations.

For example, Wix Stores provides the following algorithms:
| Name                         | Description                                                                        | Algorithm Type  |
|------------------------------|------------------------------------------------------------------------------------|-----------------|
| “From the same categories”   | Returns items that share the most categories with items in the list provided.      | `RELATED_ITEMS` |
| “Frequently bought together” | Returns items that are frequently bought together with the first item in the list provided. | `RELATED_ITEMS` |
| “Frequently viewed together” | Returns items that are frequently viewed together with the first item in the list provided. | `RELATED_ITEMS` |
| “Best sellers”               | Returns the items from the catalog with the highest number of sales.               | `GLOBAL`        |



## Before you begin
* You must have a Wix app that provides algorithms installed on your site, and you must have a Wix app whose catalogs are supported by those algorithms installed on your site. For more information see the [List Available Algorithms](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/recommendations/list-available-algorithms) method. Currently, the only app providing algorithms and their supported catalogs is Wix Stores.
* No caching is implemented, so repeat calls take the same time to complete as the first call.

## Use cases
[Show bestselling products from a Wix site in your app.](https://dev.wix.com/docs/rest/api-reference/wix-e-commerce/recommendations/sample-flow)

## Terminology
* **Catalog:** A set of products or services available for purchase in a Wix app. For example, a set of products in Wix Stores.
* **Algorithm:** A program implemented by a Wix app, such as Wix Stores, which returns a list of item recommendations.
