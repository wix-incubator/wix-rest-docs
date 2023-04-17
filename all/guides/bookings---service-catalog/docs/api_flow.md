SortOrder: 0
# Service Catalog API

 > **Deprecation Notice**
 >   
 > **The Service Catalog API has been replaced with [Services V2 APIs](https://dev.wix.com/api/rest/wix-bookings/services-v2) and will be removed on December 31, 2023. If your app uses this API, we recommend updating your code as soon as possible.**

The service catalog is a detailed list of all the services this business provides.
The Catalog API enables you to showcase services by staff member, theme or type.

Retreive extended information for each service, including information about its payment options, associated resources and more.

The Catalog API allows robust querying, enabling you to showcase services in different places based on different needs. 

The returned data for each service will include:
- **Service entity**
- **Pricing Plans** - A list of Wix Paid Plans (e.g., membership plans or pre-paid packages for sessions) which can be used to book this service, when relevant.
- **Resources** - The resources which are associated with this service.
- **Form** - The booking form used to collect the customer's input while booking the service.
- **Schedules** - The details of the schedules associated with this service.
- **Category** - The category to which the service belongs.
- **URL addresses** - URL addresses to directly access the service's information page, and the service's booking page in Wix Bookings.
- **Slugs** - The slug name of the service. This combined with the URL provides the full path to the service's page and booking page.
- **Service status** - A service can have a status of `ACTIVE` or `DELETED`.
