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
import { listContacts } from 'wix-crm-backend';

const sort = [
  { fieldName: "info.name.last", order: "ASC" },
];

listContacts({ sort })
  .then(results => {
    // results.items is sorted as requested
    console.log(results.items);
  })
  .catch(error => {
    console.error(error);
  });
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

listContacts({ sort })
  .then(results => {
    // results.items is sorted as requested
    console.log(results.items);
  })
  .catch(error => {
    console.error(error);
  });
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

For example, to list contacts by last name in ascending order,
include this structure in the request body:

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
import { contacts } from 'wix-crm-backend';

contacts.query()       
  .ascending('info.name.last')                 // Sort results by last name (A–Z)
  .descending('createdDate')                   // Then by creation date (newest first)
  .find()
  .then(results => {
    console.log(results.items); // Sorted and filtered results
  })
  .catch(error => {
    console.error(error);
  });
:::
::::

## Paging

The standard Wix API pagination includes:

- **limit**: amount of items per response (default is `0`)

- **offset**: number of items to skip. In legacy APIs **skip** is provided instead of **offset**.



### Paging _List_ endpoints

For example, to list 100 contacts, starting from contact 20:

::::tabs
:::REST_TAB
```txt
?limit=100&offset=20
```
:::
:::SDK_TAB
import { listContacts } from 'wix-crm-backend';

const sort = [
  { fieldName: "info.name.last", order: "ASC" },   
  { fieldName: "createdDate", order: "DESC" }      
];

listContacts({
  sort,     
  limit: 100, // Number of items to return
  skip: 20  // Number of items to skip (i.e., start with contact #101)
})
.then(results => {
  console.log(results.items);
})
.catch(error => {
  console.error(error);
});
:::
::::


### Paging _Query_ endpoints

For example, to query 100 contacts, starting from contact 20:

::::tabs
:::REST_TAB
```json
    "limit": 100, 
    "offset": 20 
```
:::
:::SDK_TAB
import { contacts } from 'wix-crm-backend'; 

contacts.query()                  
  .limit(100)  
  .offset(20)
  .find()
  .then(results => {
    console.log(results.items); // Sorted and filtered results
  })
  .catch(error => {
    console.error(error);
  });
:::
::::

Should return items 21-120 in the results.
