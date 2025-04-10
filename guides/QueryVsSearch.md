# Query vs. Search Methods

When working with Wix APIs, you'll notice that some APIs provide both Query and Search methods. Understanding the differences between these methods will help you choose the most appropriate one for your use case.

Both Query and Search methods retrieve collections of items, but they're optimized for different scenarios:
- Query methods are designed for efficient, low-latency data retrieval with predictable filtering and sorting capabilities.
- Search methods provide powerful text search functionality, aggregations, and result counting.

## When to use Query methods
Query methods deliver structured data efficiently with consistent performance. Choose a Query method when:
- You need consistent, low-latency responses, even at the cost of some data freshness. For example, you're performing read operations immediately after write operations.
- Filtering or sorting based on structured fields is enough to meet your needs, without free text or aggregated data (counts, sums, and so on).


## When to use Search methods
Search methods provide more advanced functionality for complex data retrieval scenarios.  Choose a Search method when you need:
- Free-text searches across multiple fields.
- Aggregated data, such as counts, sums, and so on.
- Automatic counting of total results.
- More advanced filtering capabilities.

## Key differences
Understanding the technical distinctions between these methods helps you make informed implementation decisions:

|Feature | Query | Search |
|---|---|---|
|Consistency | Eventually consistent, lower latency compared to Search. | Eventually consistent, higher latency compared to Query.|
|Result count | Not included by default. A separate count method may be available. | Includes total count automatically for the first page of results.|
|Aggregations |Not supported. | Supported.|
|Free-text search | Not supported. | Supported across multiple fields.|
|Filter & sort | Supported on specific fields. | Supported, often with more field options. |

## Best practices
Follow these recommendations to get the most out of your API calls:

- Start with Query methods for simple data retrieval scenarios.
- Use Search methods when you need text search or aggregations.
- Check for a dedicated Count method if you only need to know the total results.
- Leverage both methods in your application when appropriate, for different user experiences.
- Remember to review each API's specific documentation for details about supported fields and features for both Query and Search methods.

## Example use cases
These examples illustrate common applications for both methods in the [Payment Links API](https://dev.wix.com/docs/rest/business-management/get-paid/payment-links/payment-links/introduction).

### Query example: Retrieve a list of payment links filtered by price and sorted by creation date
A business may want to review all payment links for premium offerings to ensure the most recent links reflect current marketing strategies.   
You can retrieve a list of payment links filtered by a specific price range and sorted chronologically by creation date with the following call:
```
curl -X POST \
  'https://www.wixapis.com/payment-links/v1/payment-links/query' \
  -H 'Authorization: <AUTH>' \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "query": {
      "filter": {
        "price": {
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

### Search example: Find all payment links containing "test" in their description, with aggregated counts by statuses
A business may want to identify all test payment links and check what types of tests were run.  
You can retrieve all test payment links, with aggregated counts for each status with the following call:
```
curl -X POST \
  'https://www.wixapis.com/payment-links/v1/payment-links/search' \
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
          "name": "statuses",
          "type": "VALUE",
          "fieldPath": "status",
          "value": {
            "sortType": "COUNT"
          }
        }
      ],
      "search": {
        "fuzzy": true,
        "expression": "Test",
        "fields": [
          "title"
        ]
      }
    }
  }'
```
