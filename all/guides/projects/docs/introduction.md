SortOrder: 2
# Portfolio Projects

With Projects API, you can manage the Projects in Portfolio.

The Projects API allows your app to:

*   Create, Get, List, Query, Delete and Update Project
*   Query projects by Collection
*   Update the project sort order in Collection

## Sort Order
In order to preserve a defined order of Project in a Collection, Wix uses the sortOrder field.

* You can update the `sortOrder` field using your own logic using the **UpdateProjectOrderInCollection** endpoint.
* If sortOrder is not given on creation, the `sortOrder` field will automatically be populated with the current timestamp ([Epoch time](https://en.wikipedia.org/wiki/Unix_time)) * (-1), so the project will be first in the collection order.
* In order to prevent updating the all previous/next projects when reordering a single project, the Wix UI uses the following calculation:  
  `new_sortOrder = (next_project.sortOrder + previous_project.sortOrder)/2`

> **Note**: Your app can choose other forms of logic to reorder projects in collection.
> 
## Limitations

+ Only existing Collections in [Collections](https://bo.wix.com/wix-docs/rest/drafts/collections) can be assigned to Project.
