SortOrder: 3
# API Query Language 

The query language described in this article
is implemented partially or in full by Wix APIs supporting query capabilities.
You may see some similarities between the Wix API Query Language
and MongoQL.
This is because the style of the Wix API Query Language
is heavily influenced by MongoQL.

## Syntax

A query object consists of 5 optional parts:

* [`filter`](#the-filter-section):
  Which results to return.
* [`sort`](#the-sort-section):
  In what order.
* [`paging`](#the-paging-section):
  Return only some of the matched entities.
* [`fields`](#the-fields-section):
  Field projection. Returns only part of each entity.
* [`fieldsets`](#the-fieldsets-section):
  Predefined, named sets of fields with common use.
  This is a shorthand provided by individual APIs.

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
  "fieldsets": [ ... ]
}
```

## The `filter` section

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

## The `sort` section

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

## The `paging` section

The `paging` section describes the size of the data set to return per response
and how many records to skip.
The following returns records 41 through 60:

```json
{
  "paging": {
    "limit": 20,
    "offset": 40
  }
}
```

## The `fields` section

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

## The `fieldsets` section

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
