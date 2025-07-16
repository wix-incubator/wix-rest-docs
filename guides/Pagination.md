# Sorting and Paging

_List_ and _Query_ endpoints that return a list of entities
allow you to specify sorting and paging options in the request.

This articles gives a general overview of sorting and paging.
The implementation changes in REST
depending on whether an endpoint is a GET or POST request.
Check your API's documentation for specific details,
including which fields are sortable.

## Sorting

Most APIs default to sorting by `createdDate` in `DESC` (descending) order,
although some APIs have a different default sort order.
You can override the default sorting by specifying
a new field and order.

### Sort _List_ endpoints

_List_ endpoints are designed to be lightweight requests.
For this reason, sorting is applied through the query parameters,
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

Your API's _List_ method may support sorting by multiple fields.
This is done by adding new field name and order parameters
for each sort field:

::::tabs
:::REST_TAB
```txt
?sort.fieldName=info.name.last&sort.order=ASC&sort.fieldName=createdDate&sort.order=ASC
```
:::
:::SDK_TAB
```
const sort = [
  { fieldName: "status", order: "ASC" },
  { fieldName: "createdDate", order: "DESC" }
];

```
:::
::::


### Sort _Query_ endpoints

_Query_ endpoints offer more robust filtering capabilities.
When working with a _Query_ endpoint,
sorting is specified in REST in an array in the request body,
typically `query.sort`, and in the SDK within a .sort() function in the SDK's query chain. 
For each `sort` object,
sorting is applied with the `fieldName` and `order` parameters.

For example, to list payment links by created date in ascending order, and by status in descending order:

::::tabs
:::REST_TAB
```json
{
  "query": {
    "sort": [
      {
        "fieldName": "info.name.last",
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

export const queryPaymentLinksSorted = webMethod(
  async () => {
    try {
      const results = await paymentLinks.queryPaymentLinks()
        .ascending('_createdDate')        // Sort by created date ascending
        .descending('status')             // Then by status descending
        .find();

      console.log(`Found ${results.items.length} payment links`);
      console.log('Payment links:', results.items);
      
      return {
        success: true,
        paymentLinks: results.items,
        totalCount: results.totalCount,
        pageSize: results.pageSize,
        sortedBy: 'created date (oldest first), then status (descending)'
      };

      }
    }
);
```
:::
::::

## Paging

Paging allows you to control how many results are returned and where the result set starts. Wix APIs commonly support 1 or both of 2 paging strategies:

- **Offset-based** (includes `limit` and `skip`/`offset`): Specify the number of items to skip and the number to return.
- **Cursor-based** (includes `nextCursor` and `prevCursor`): Use a token (cursor) to fetch the next or previous set of results.

### Paging _List_ endpoints

For example, to list 100 contacts, starting from contact 20, with offset paging:

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

To list the next 100 contacts with cursor paging:

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
       cursorPaging {
            cursor: JWE.eyJhbGciOiJBMTI4S1ciLCJlbm,
    }
}
};
```
:::
::::

### Paging _Query_ endpoints

For example, to query 100 contacts, starting from contact 20, with offset paging:

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

const query = contacts.queryContacts()               
  .limit(100)  
  .skip(20)
  .find()
  .then(results => {
    console.log(results.items); // Sorted and filtered results
  })
  .catch(error => {
    console.error(error);
  });
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
```
:::
:::SDK_TAB
```
import { paymentLinks } from "@wix/get-paid";

  const nextCursor = results.cursors.next;
  return paymentLinks.queryPaymentLinks().skipTo(nextCursor).find();
}
```
:::
::::
