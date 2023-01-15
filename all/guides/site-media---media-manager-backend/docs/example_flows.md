SortOrder: 1
# Example Flows

This article shares some possible use cases your app could support, as well as an example flow that could support each
use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your
app's implementation.

## Search and Delete Files  

A real estate agent has a Wix site for his property listings. Each property listing has a name, an image of the property, and a label representing whether the property has been sold. A real estate company can use the REST API to search the real estate agent's site for all property listings that have been sold. The real estate company can then remove all the sold property listings from the real estate agent's site. 

To do this, the real estate company can follow this basic flow. 

1. Use [Search Files](https://dev.wix.com/api/rest/media/files/search-files) to search for all the properties with the 'sold' label:

   ```json
   {
     "search": "abc-real-estate"
   }
   ```
   The response is an array of file objects containing information about the property listings that match the search term. Each file object has an `id`. These file IDs are needed for the next step.  

2. To delete these sold property listings from the real estate agent's site, the real estate company needs to take the file IDs returned in the previous step, and pass them in the `fileIds` parameter of the [Bulk Delete Files](https://dev.wix.com/api/rest/media/files/bulk-delete-files) endpoint. Deleting these property listings only move them to the Media Manager's trash bin. If the real estate company chooses to permanently delete these property listings from the Media Manager, they should set the `permanent` parameter to `true`.

   ```json
   {
     "fileIds": ["ab5499911fff444099", "3337f55vvv2222887"],
     "permanent": "true"
   }
   ```
