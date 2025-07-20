# Sorting and Paging

_List_, _Query_ and _Search_ methods that return a list of entities
may allow you to specify sorting and paging options in the request.

This articles provides a general overview of sorting and paging.
The implementation syntax varies in REST
depending on whether a method is a GET or POST request.
Check your API's documentation for specific details,
including which fields are sortable.

## Sorting

Most APIs default to sorting by `createdDate` in `DESC` (descending) order,
although some APIs have a different default sort order.
You can often override the default sorting by specifying
a new field and order.

### Sorting _List_ methods

_List_ methods are designed to be lightweight requests.
For this reason, sorting is applied in REST through query parameters,
typically with sort field name and order fields.

For example, to list contacts by last name in ascending order:

::::tabs
:::REST_TAB
```txt
?sort.fieldName=info.name.last&sort.order=ASC
```
:::
:::SDK_TAB
```
const sort = [
  { fieldName: "info.name.last", order: "ASC" },
]
```
:::
::::


### Sorting _Query_ methods

_Query_ methods offer more robust filtering capabilities.
When working with a _Query_ method,
sorting is specified in REST in an array in the request body,
typically `query.sort`, and in the SDK with `.ascending()` and `.descending()` functions in the SDK's query chain. 
For each `query.sort` object,
sorting is typically applied with the `fieldName` and `order` parameters.

For example, to list payment links by created date in ascending order, and by status in descending order:

::::tabs
:::REST_TAB
```json
{
  "query": {
    "sort": [
      {
        "fieldName": "createdDate",
        "order": "ASC"
      },
{
        "fieldName": "status",
        "order": "DESC"
      }
    ]
  }
}
```
:::
:::SDK_TAB
```
import { paymentLinks } from "@wix/get-paid";

// ...
    const results = await paymentLinks.queryPaymentLinks()
      .ascending('_createdDate')        // Sort by created date ascending
      .descending('status')             // Then by status descending
      .find();
```
:::
::::

### Sorting _Search_ methods

When working with a _Search_ method,
sorting is specified in REST in an array in the request body,
typically `search.sort`, and in the SDK as an object defining the sort to the search function.

For example, to search payment links by created date in ascending order:

::::tabs
:::REST_TAB
```json
{
  "search": {
    "sort": [
      {
        "fieldName": "createdDate",
        "order": "ASC"
      }
    ]
  }
}
```
:::
:::SDK_TAB
```
import { paymentLinks } from "@wix/get-paid";

{
    const search = {
      // ...
      sort: {
        fieldName: "createdDate", order: "ASC"
    }
  }
};
```
:::
::::


## Paging

Paging allows you to control how many results are returned and where the result set starts. Wix APIs commonly support 1 or both of 2 paging strategies:

- **Offset-based** (includes `limit` and `skip`/`offset`): Specify the number of items to skip and the number to return. 
- **Cursor-based** (includes `nextCursor` and `prevCursor`): Use a token (cursor) to fetch the next or previous set of results.

### Paging _List_ methods

List endpoints typically support paging through query parameters in REST requests and `paging` objects in SDK calls.

For example, to list 100 contacts, starting from contact 21, with offset paging:

::::tabs
:::REST_TAB
```txt
?limit=100&offset=20
```
:::
:::SDK_TAB
```
{
    "options": {
       "paging": {
           "limit": 20,
           "offset": 0
       },
    }
 }
```
:::
::::

Should return items 21-120 in the results.


For calls that support cursor paging, after receieving a cursor in your first request, list the next set of entities with cursor paging:

::::tabs
:::REST_TAB
```txt
&cursorPaging.cursor=JWE.eyJhbGciOiJBMTI4S1ciLCJlbm
```
:::
:::SDK_TAB
```
{
    const options = {
      // ...
      paging: {
        cursor: JWE.eyJhbGciOiJBMTI4S1ciLCJlbm
    }
}
};
```
:::
::::

### Paging _Query_ methods

Query endpoints handle paging through the request body in REST and chainable methods in the SDK. Generally either offset-based or cursor-based strategies are supported, and occasionaly both are supported.

For example, to query 100 contacts, starting from contact 21, with offset paging:

::::tabs
:::REST_TAB
```json
"query": {
  "paging": {
    "limit": 100, 
    "offset": 20
    }
}
```
:::
:::SDK_TAB
```
import { contacts } from "@wix/crm";

// ...
const results = await contacts.queryContacts()               
  .limit(100)  
  .skip(20)
  .find()
```
:::
::::

Should return items 21-120 in the results.

To query 100 payment links with cursor paging:

::::tabs
:::REST_TAB
```json
"query": {
  "cursorPaging": {
    "cursor": JWE.eyJhbGciOiJBMTI4S1ciLCJlbm,
  }
}
:::
:::SDK_TAB
```
import { paymentLinks } from "@wix/get-paid";

// ...
const nextCursor = results.cursors.next;
return paymentLinks.queryPaymentLinks().skipTo(nextCursor).find();
}
```
:::
::::

### Paging _Search_ methods 

Search endpoints implement paging through the request body structure in REST and search configuration objects in SDK calls. Search methods typically use cursor-based paging to ensure consistent results even when the underlying data changes during pagination.

For example, to search for 10 payment links, and return a cursor for paging:

::::tabs
:::REST_TAB
```json
  "search": {
    "cursorPaging": {
      "limit": 10
  }
}
```
:::
:::SDK_TAB
```
import { paymentLinks } from "@wix/get-paid";

"search": {
// ...
    "cursorPaging": {
      "limit": 10
  }
}
```
:::
::::

Should return 10 items.


To retrieve the next 10 payment links with a cursor:

::::tabs
:::REST_TAB
```json
  "search": {
    "cursorPaging": {
      "cursor": JWE.eyJhbGciOiJBMTI4S1ciLCJlbm,
    }
```
:::
:::SDK_TAB
```
import { paymentLinks } from "@wix/get-paid";

// ...
const nextCursor = results.cursors.next;
return paymentLinks.queryPaymentLinks().skipTo(nextCursor).find();
}
```
:::
::::
