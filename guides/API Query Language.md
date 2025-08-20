SortOrder: 3
# API Query and Search Language 

The query and search language described in this article is implemented partially or in full by many Wix APIs supporting query and search capabilities.
You may see some similarities between the Wix API Query Language and MongoQL, as the style of the Wix API Query Language is heavily influenced by MongoQL. 

> **Note:** Many query methods in the Wix JavaScript SDK handle filter and sort functionalities with chained functions. Learn more about Wix's [search](https://dev.wix.com/docs/rest/articles/get-started/search-query-and-list-methods#search-method-characteristics) and [query](https://dev.wix.com/docs/rest/articles/get-started/search-query-and-list-methods#query-method-characteristics) methods.

## Syntax

Query and Search objects consist of several optional parts:

* [`filter`](#filters):
  Which results to return.
* [`sort`](#sorting):
  In what order.
* [`paging`](#paging):
  Return only some of the matched entities.
* [`fields`](#fields):
  Field projection. Returns only part of each entity.
* [`fieldsets`](#fieldsets):
  Predefined, named sets of fields with common use cases.
  This is a shorthand provided by individual APIs.
* [`aggregations`](#aggregations-search-object-only)
  Search object only: Faceted search, a way to explore large amounts of data by displaying summaries about various partitions of the 
  data and later allowing to narrow the navigation to a specific partition.
* [`search`](#search-search-object-only)
  Search object only: Free text to match in searchable fields.
* [`timeZone`](#time-zones-search-object-only)
  Search object only: Time zone for aggregations and filters by date.

Each query is always a single JSON object.
An empty JSON object returns all records
according to the API's default paging and sort order.

The query object can define a key for each of the above parts:

```json
{
  "filter": { ... },
  "sort": [ ... ],
  "paging": { ... },
  "fields": [ ... ],
   "fieldsets": [ ... ],
   "aggregations": [ ... ],
  "search": [ ... ]
}
```

## Filters

The filter section is a single json object { } with the following rules:

### Equality

The format `{ "<field>": <value> }` specifies an equality condition.

For example, `{ "status": "DONE" }`
matches all entities where `status` is `"DONE"`.

### Operators

Operators use the format `{ "<field>": { "$<operator>": <value> } }`.

For example, `{ "status": { "$in": ["PENDING", "DONE"] } }`
matches all entities where status is `"PENDING"` or `"DONE"`.

The operators specified below are supported.

#### Comparison operators

* `$eq`: Matches values that are equal to a specified value.
* `$ne`: Matches all values that are not equal to a specified value.
* `$gt`: Matches values that are greater than a specified value.
* `$gte`: Matches values that are greater than or equal to a specified value.
* `$lt`: Matches values that are less than a specified value.
* `$lte`: Matches values that are less than or equal to a specified value.
* `$in`: Matches any of the values specified in an array.
* `$nin`: Matches none of the values specified in an array.
* `$startsWith`: Matches strings that start with a specified value. Not case-sensitive.
* `$isEmpty`: Matches strings or arrays that are empty or not empty,
  depending on whether the specified operand is `true` or `false`.

#### Logical operators

* `$and`: Joins query clauses with a logical _AND_
  and returns all items that match the conditions of both clauses.
* `$or`: Joins query clauses with a logical _OR_
  and returns all items that match the conditions of either clause.
* `$not`: Inverts the effect of a query expression
  and returns items that don't match the query expression.

#### Element operators

* `$exists`: Matches items where the specified field exists and has a non-null value.

#### Array operators

* `$hasAll`: Matches arrays that contain all elements specified in the query.
* `$hasSome`: Matches arrays that contain at least one element specified in the query.

### Sample queries

In the following example, the compound query returns all entities where the status equals `"A"` and either `qty` is less than `30` or `item` starts with the character `p`:

```json
{
  "status": "A",
  "$or": [
    {
      "qty": { "$lt": 30 }
    },
    {
      "item": { "$startsWith": "p" }
    }
  ]
}
```

The following example queries entities where the field `tags` value is an array with exactly two elements, `"red"` and `"blank"`, in the specified order:

```json
{
  "tags": [ "red", "blank" ]
}
```

The following example queries for all entities where `tags` is an array that contains the string `"red"` as one of its elements, or that `tags` is the string `"red"`:

```json
{
  "tags": "red"
}
```

The following query matches entities that do not contain the `item` field, or where the `item` field has no value:

```json
{
  "item": { "$exists": false }
}
```

## Sorting

The `sort` section is an array of field names and sort order.
If `order` is not specified for a field, the field is sorted in ascending order.
Sorting is applied to the first `sort` item, then the second, and so on:

```json
{
  "sort": [
    {
      "fieldName": "sortField1"
    },
    {
      "fieldName": "sortField2",
      "order": "DESC"
    }
  ]
}
```

## Paging

The `paging` section describes the size of the data set to return per response
and how many records to skip.
Each API can support **offset paging**, **cursor paging**, or both.
See your specific API for information on supported paging options.

### Offset paging

With offset paging, you provide a `limit` and `offset` with each request.
To retrieve additional pages,
submit subsequent requests with an increased `offset`
equal to the previous page's `limit` plus `offset`.

For example, this offset request returns records 41 through 60:

```json
{
  "paging": {
    "limit": 20,
    "offset": 40
  }
}
```

### Cursor paging

With cursor paging, each request returns a `cursors` object
that contains cursor strings that point to the next page, previous page, or both.
To retrieve either page, use the returned `next` or `prev` cursor
in the next request's `cursor` parameter.

Take this response object, for example:

```json
{
  "pagingMetadata": {
    "count": 10,
    "offset": 0,
    "cursors": {
      "next": "eyJmaWx0ZXIiOnsiJGFuZCI6W3sibGFuZ3VhZ2UiOnsiJGluIjpbImVuIiwiaGUiXX19LHsic3RhdHVzIjoicHVibGlzaGVkIn1dfSwidmFsdWUiOnsiaXNQaW5uZWQiOmZhbHNlLCJmaXJzdFB1Ymxpc2hlZERhdGUiOiIyMDIyLTA2LTAyVDA2OjQ2OjAyLjgwMloifSwib3JkZXIiOnsiaXNQaW5uZWQiOi0xLCJmaXJzdFB1Ymxpc2hlZERhdGUiOi0xLCJpZCI6LTF9fQ=="
    }
  }
}
```

You can use the returned `next` cursor to retrieve the next page of results
by forming your request like this:

```json
{
  "query": {
    "cursorPaging": {
      "cursor": "eyJmaWx0ZXIiOnsiJGFuZCI6W3sibGFuZ3VhZ2UiOnsiJGluIjpbImVuIiwiaGUiXX19LHsic3RhdHVzIjoicHVibGlzaGVkIn1dfSwidmFsdWUiOnsiaXNQaW5uZWQiOmZhbHNlLCJmaXJzdFB1Ymxpc2hlZERhdGUiOiIyMDIyLTA2LTAyVDA2OjQ2OjAyLjgwM1oifSwib3JkZXIiOnsiaXNQaW5uZWQiOi0xLCJmaXJzdFB1Ymxpc2hlZERhdGUiOi0xLCJpZCI6LTF9fQ"
    }
  }
}
```

## Fields

The `fields` section is an array of field paths to return.
If a field path points to an object, the entire sub-object is returned.
Subsets of sub-objects can be returned by using dot notation.
In this example,
the returned entities contain `firstName` from the `name` sub-object
and the entire `address` object:

```json
{
  "fields": [
    "name.firstName",
    "address"
  ]
}
```

## Fieldsets

An API may provide named projections to save clients from specifying individual fields in common cases.
For example,
the Contacts API implements a fieldset named `BASIC` that contains only
`id`, `revision`, `info.name.first`, `info.name.last`,
`primaryInfo.email`, and `primaryInfo.phone`.
To use a fieldset, specify its name in the `fieldsets` array.
If both `fieldsets` and `fields` sections exist, the union of both is returned.
For example:

```json
{
  "fieldsets": [
    "BASIC"
  ]
}
```

## Aggregations (Search object only)
Aggregation is a search method that groups data into different categories (called buckets) and generates summaries for each category (referred to as facets).
Supported aggregation types: 
- `DATE_HISTOGRAM`: Calculates the count of time values from the specified field in the dataset fall within the defined time interval (hour, day, week, etc.).  
- `NESTED`: Calculates multiple aggregations, of any type, nested within one aggregation, allowing you to first group data using one aggregation, and then apply another aggregation within each group.
- `RANGE`: Calculates the count of the values from the specified field in the dataset that fall within the range of each defined bucket.
  - `rangeBuckets`: categories for grouping data. Each bucket must have at least one range bound:
    - `from`: Inclusive lower bound of the range. 
    - `to`: Exclusive upper bound of the range.
- `SCALAR`: Calculates a single numerical value from a dataset, with the total count, sum, average, min, or max, summarizing the dataset into one key metric.
- `VALUE`: Calculates the distribution of a specific field's values within a dataset. 
  
## Search (Search object only)
With `search`, you can filter for specific text within any searchable field, using the following:
- `mode`: How to handle multiple words in the `expression`. Supported values: `AND`, `OR`. Default: `OR`.
- `expression`: Free text to search for.
- `fields`: Fields to search in. Use dot notation to specify json path. Default: All searchable fields.
- `fuzzy`: [Fuzzy search](https://www.techtarget.com/whatis/definition/fuzzy-search), enabling search including typos, by a managed proximity algorithm. Default: `false`. 

## Time zones (Search object only)
UTC offset or IANA time zone. Valid values are ISO 8601 UTC offsets, such as `+02:00` or `-06:00`, and IANA time zone IDs, such as `Europe/Rome`.
Affects all filters and aggregations returned values.
You may override this behavior in a specific filter by providing timestamps including time zone. For example, `"2023-12-20T10:52:34.795Z"`.
