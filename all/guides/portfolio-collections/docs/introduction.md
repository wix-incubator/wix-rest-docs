SortOrder: 0
# Portfolio Collections

With Collections API, you can manage the Collections in Portfolio.

Collections can be assigned to a Project using [Projects](https://bo.wix.com/wix-docs/rest/drafts/projects/introduction) API.\n
You can query projects by collection using [Query Project In Category](https://bo.wix.com/wix-docs/rest/drafts/projects/query-project-in-category) API.

The Collections API allows your app to:

*   Create, Get, List, Query, Delete and Update Collections.

## Sort Order
In order to preserve a defined order of the Collections in Portfolio, Wix uses the sortOrder field.

* You can update the `sortOrder` field using your own logic using the relevant **Update** endpoint.
* If sortOrder is not given on creation, the `sortOrder` field will automatically be populated with the current timestamp ([Epoch time](https://en.wikipedia.org/wiki/Unix_time)).
* In order to prevent updating the all previous/next collections when reordering a single collection, the Wix UI uses the following calculation:  
  `new_sortOrder = (next_collection.sortOrder + previous_collection.sortOrder)/2`

> **Note**: Your app can choose other forms of logic to reorder collections.
> 
