# Query vs. Search Methods

When working with Wix REST APIs, you'll notice that some endpoints provide both Query and Search methods. Understanding the differences between these methods will help you choose the most appropriate one for your use case.

Both Query and Search methods retrieve collections of items, but they're optimized for different scenarios:
- Query methods are designed for efficient, low-latency data retrieval with predictable filtering and sorting capabilities
- Search methods provide powerful text search functionality, aggregations, and result counting

## When to use Query methods
Choose a Query method when:
- You need consistent, low-latency responses, even at the cost of some data freshness. For example, you're performing read operations immediately after write operations.
- You need predictable performance for displaying paginated data.
- Filtering or sorting based on structured fields is enough to meet your needs, without free text or aggregated data (counts, sums, and so on).


## When to use Search methods
Choose a Search method when you need:
- Free-text searches across multiple fields
- Aggregated data (counts, sums, etc.)
- Automatic counting of total results
- More advanced filtering capabilities

## Key Differences
|Feature | Query | Search |
|---|---|---|
|Consistency | Generally lower latency but may sacrifice immediate consistency | Eventually consistent|
|Result count | Not included by default; separate count endpoint may be available | Usually includes total count automatically|
|Aggregations |Not supported |Supported (sum, count, etc.)|
|Free-text search | Not supported |Supported across multiple fields|
|Filter & sort | Supported on specific fields | Supported, often with more options |

## Practical Considerations
Keep these issues in mind while making your decision:

- **API-specific differences**: Always check the specific API documentation as available fields and capabilities may vary
- **Performance**: Query methods generally provide more predictable performance for simple retrievals
- **Complexity**: Search methods offer more power but may have more complex syntax
- **Result limits**: Both methods typically support pagination, but may have different default and maximum values

## Example use cases

### Query example: Retrieving a list of payment links filtered by price and sorted by creation date
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

### Search example: Finding all payment links containing "test" in their description, with aggregated counts by statuses
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
## Best Practices

- Start with Query methods for simple data retrieval scenarios.
- Use Search methods when you need text search or aggregations.
- Check for a dedicated Count method if you only need to know the total results.
- Leverage both methods in your application when appropriate, for different user experiences.
- Remember to review each API's specific documentation for details about supported fields and features for both Query and Search methods.

