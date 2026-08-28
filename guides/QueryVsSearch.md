# Search, Query and List Methods

When working with Wix APIs, you'll notice that some APIs provide a mix of search, query, or list methods. Understanding the differences between these methods will help you choose the most appropriate one for your use case.

All three methods retrieve collections of items, but they're optimized for different scenarios:

* **Search methods** provide powerful text search functionality, aggregations, and result counting.
* **Query methods** are designed for efficient, low-latency data retrieval with predictable filtering and sorting capabilities.
* **List methods** provide simple, straightforward access to collections with basic pagination options. Generally only available for collections that are limited in size.

> **Note:** The Wix Data Items API has a dedicated Aggregate method.

## Key differences

| Feature | Search | Query | List |
|---------|------|-------|--------|
| Purpose | Discovery and exploration | Efficient filtered data access | Basic collection access |
| Complexity | Complex | Moderate | Simple |
| Consistency | Eventually consistent, higher latency for availability of created and updated records than list| Eventually consistent, higher latency for availability of created and updated records than list | Eventually consistent, lower latency |
| Result Count | Includes total count automatically in the first page | Not included; separate count endpoint may be available | Not included; separate count endpoint may be available  |
Filtering | Advanced text and field-based filtering | Extensive field-based filtering | Limited field-based filtering |
| Sorting | Flexible field-based sorting | Flexible field-based sorting | Limited, often predefined options |
| Aggregations | Supported | Not supported | Not supported |
| Free-text Search | Supported across multiple fields | Not supported | Not supported |
| Performance | Optimized for search capabilities  | Optimized for sorting and filtering | Good performance for simple queries |
| Pagination | Cursor-based for efficiency, offset/limit may be available | Cursor-based for efficiency, offset/limit may be available | Cursor-based for efficiency, offset/limit may be available |

## Search method characteristics
Search methods typically have these features:
- Advanced text search capabilities across multiple fields.
- Support for both structured filtering and free-text search.
- Fuzzy matching for spelling tolerance and typo forgiveness.
- Phrase matching for exact sequence detection.
- Field boosting to prioritize matches in specific fields.
- Automatic total result counting with the first page of results.
- Complex aggregation capabilities:
  - Count aggregations for faceted navigation.
  - Sum and average calculations on numeric fields.
  - Min/Max value detection.
  - Distinct count operations.
- Facet generation for filtered navigation interfaces.
- Higher latency compared to List methods.
- Designed for discovery-oriented user experiences.
- Suitable for building search boxes, filters, and exploratory interfaces.
- Often supports highlighting of matched text in results.
- REST: POST endpoints with comprehensive JSON configuration bodies.
- Support for complex filtering expressions with logical operators. Common operators include:  

  | Expression type | SDK & REST |  
  |----------------|------|  
  | Equal to | `$eq` |  
  | Not equal to |  `$ne`|
  | Greater than |  `$gt` |  
  | Greater than or equal to |  `$gte` |  
  | Less than |  `$lt` |  
  | Less than or equal to |  `$lte` |  
  | In a specified list |  `$in` |  
  | Field exists check |  `$exists` |  
  | String starts with |  `$startsWith` |  


## Query method characteristics

Query methods typically have these features:

- Field-specific sorting with direction control.
- Efficient cursor-based pagination for handling large datasets.
- Often allows multiple filter conditions to be combined.
- Optimized for low-latency data access patterns.
- No support for text search or aggregations.
- REST: HTTP POST endpoints with a JSON request body.
- Support for complex filtering expressions with logical operators. Common operators include:  

  | Expression type | SDK | REST |  
  |----------------|-----|------|  
  | Equal to | `eq()` | `$eq` |  
  | Not equal to | `ne()` | `$ne`|
  | Greater than | `gt()` | `$gt` |  
  | Greater than or equal to | `ge()` | `$gte` |  
  | Less than | `lt()` | `$lt` |  
  | Less than or equal to | `le()` | `$lte` |  
  | In a specified list | `in()` | `$in` |  
  | Field exists check | `exists()` | `$exists` |  
  | String starts with | `startsWith()` | `$startsWith` |  


## List method characteristics

List methods typically have these features:
* Basic field-based filtering.
* Usually have the simplest implementation requirements.
* Limited or no sorting capabilities beyond defaults.
* Suitable for dropdown menus, simple listings, and basic data display.
* REST: HTTP GET endpoints (though some use POST).

## Method selection guide

When choosing between search, query, and list methods for your data retrieval needs, use decision tree below  to guide you to the most appropriate method based on your data retrieval needs, and your requirements for data freshness, filtering complexity, and caching.

![method decision tree](./SearchQueryList2.png)

<!-- remove temporarily until find samles that actually work
## Example use cases
These examples illustrate common applications for both methods in the [Payment Links API](https://dev.wix.com/docs/rest/business-management/get-paid/payment-links/payment-links/introduction).

### Search example: Finding Loyalty accounts containing "test" in the contact email address with aggregated counts by points balance

A business may want to identify all test loyalty accounts and check their point balances, sorted by latest created date.

::::tabs
:::REST_TAB
```
curl -X POST \
  'https://www.wixapis.com/loyalty-accounts/v1/accounts/search' \
  -H 'Authorization: <AUTH>' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "search": {
      "sort": [
        {
          "fieldName": "createdDate",
          "order": "DESC"
        }
      ],
      "aggregations": [
        {
          "name": "balances",
          "type": "VALUE",
          "fieldPath": "points.balance",
          "value": {
            "sortType": "COUNT"
          }
        }
      ],
      "search": {
        "fuzzy": true,
        "expression": "test",
        "fields": [
          "contact.email"
        ]
      }
    }
  }'
```
:::
:::SDK_TAB
```
import { accounts } from "@wix/loyalty";

export async function searchAccounts() {
  try {
    const response = await loyalty.searchAccounts({
      sort: [
          {
            fieldName: "createdDate",
            order: "DESC"
          }
        ],
        aggregations: [
          {
            name: "balances",
            type: "VALUE",
            fieldPath: "points.balance",
            value: {
              sortType: "COUNT"
            }
          }
        ],
        search: {
          fuzzy: true,
          expression: "test",
          fields: [
            "contact.email"
          ]
        },
    })
    return response
    }, catch (error) {
    console.error(error);
    },
     };

```
:::
::::




### Query example: Retrieve a list of Loyalty accounts filtered by points balances 
A business may want to review all Loyalty accounts and their current balance to send reminders to customers with high balances about ways to use their points.   
You can retrieve a list of Loyalty accounts filtered by a specific points balance range and sorted chronologically by creation date with the following call:

::::tabs
:::REST_TAB
```
curl -X POST \
  'https://www.wixapis.com/loyalty-accounts/v1/accounts/query' \
  -H 'Authorization: <AUTH>' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "query": {
      "filter": {
        "points.balance": {
          "$gt": 100,
        }
      },
      "sort": [
        {
          "fieldName": "createdDate",
          "order": "DESC"
        }
      ],
      "cursorPaging": {
        "limit": 1
      }
    }
  }'
```
:::
:::SDK_TAB
```
import { accounts } from "@wix/loyalty";

async function queryLoyaltyAccounts() {
    const { items } = await loyalty.queryLoyaltyAccounts().gt("points.balance", 100).descending("createdDate").find();
}
```
:::
::::


### List example: Retrieving Loyalty accounts for specific customers with basic pagination

A business needs to access a list of specific Loyalty accounts in a dashboard with page navigation. 
You can retrieve a list of specified Loyalty accounts with the deprecated List Accounts method.

::::tabs
:::REST_TAB
```
curl -X GET \
  'https://www.wixapis.com/loyalty-accounts/v1/accountscontactIds[]=88615e02-3e8a-4297-8939-5d0a432b322a&contactIds[]=fb8f125e-bfc3-4d9a-80c2-215494f24731' \
  -H 'Authorization: <AUTH>'
```
:::
:::SDK_TAB
```
import { accounts } from "@wix/loyalty";

export async function myListLoyaltyAccountsFunction() {
  try {
    const accountsList = await accounts.listAccounts(options);

    const firstAccountId = accountsList.accounts[0]._id;
    const firstAccountBalance = accountsList.accounts[0].points.balance;

    console.log(
      "Success! The ID and point balance for the first account in your list is: ",
      firstAccountId,
      " and ",
      firstAccountBalance,
    );

    return accountsList;
  } catch (error) {
    console.error(error);
  }
}

```
:::
::::
-->

