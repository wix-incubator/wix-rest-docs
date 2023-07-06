SortOrder: 1
# Services: Sample Use Cases and Flows

This article shares some possible use cases your app could support, as well as a sample flow that could support each use case. This can be a helpful jumping off point as you plan your app's implementation.

## Periodically export new Wix Bookings services to an external catalog

If a site owner manages their services in an external catalog, you can export new services to it. To do this, your app can periodically bulk load new services being offered:

1. For the first load after the app is installed and services are defined, use [Query Services](https://dev.wix.com/api/rest/wix-bookings/services-v2/query-services) to retrieve all services. By default the initial paging limit is 100.

1. If you receive 100 services, there may be more services to retrieve. Run the request again, and increase `paging.offset` to 100. Keep running the request, each time increasing the offset, until all services are retrieved.

1. Upload the retrieved services to the external catalog.

1. Save the current datetime, and use it in the next request. Each subsequent request will need to use the datetime of the request that came before it.

1. For all subsequent loads, use [Query Services](https://dev.wix.com/api/rest/wix-bookings/services-v2/query-services) , and filter for new services created since the last load:

    ```json
    {
      "sort": {
        "fieldName": "createdDate",
        "order": "ASC"
      },
      "filter": {
        "createdDate": {
            "$gt": "<PREVIOUS_LOAD_DATETIME>"
        }
      }
    }
    ```

1. Repeat steps 2 to 4 for each subsequent load. You can allow the site admin to configure the time interval in your app to fit their needs.