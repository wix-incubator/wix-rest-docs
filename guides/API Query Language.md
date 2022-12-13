SortOrder: 3
# API Query Language 

The query language described in this article is implemented partially or in full by Wix APIs supporting query capabilities.

You may see some similarities between the Wix API Query Language
and MongoQL.
The style of the Wix API Query Language is heavily influenced by MongoQL.

## Syntax

A query object consists of 5 optional parts:

* _Filter_: Which results to return.
* _Sort_: In what order.
* _Paging_: Return only some of the matched entities.
* _Fields_: Field projection. Returns only part of each entity.
* _Fieldsets_: Predefined, named sets of fields with common use.
  This is a shorthand provided by individual APIs.
  
Each query is always a single JSON object.
An empty JSON object returns records
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

### The Filter Section

The filter section is a single json object { } with the following rules:

#### Equality

The format `{<field>: <value>, ...}` specifies equality condition.
E.g. the query `{status: "X"}` will match all entities with a status equal to `"X"`

#### Operators

Operators use the following format: `{<field>: {<operator>:<value>}, ...}`.  
E.g. the query `{status: {$in: ["X", "Y"]}}` will match all entities that have status  set to `"X"` or `"Y"`  
The following operators are supported:

##### Comparison

* `$eq`: Matches values that are equal to a specified value.
* `$gt`: Matches values that are greater than a specified value.
* `$gte`: Matches values that are greater than or equal to a specified value.
* `$in`: Matches any of the values specified in an array.
* `$lt`: Matches values that are less than a specified value.
* `$lte`: Matches values that are less than or equal to a specified value.
* `$ne`: Matches all values that are not equal to a specified value.
* `$nin`: Matches none of the values specified in an array.
* `$startsWith`: Matches strings that start with a specified value. Not case-sensitive.

##### Logical

* `$and`: Joins query clauses with a logical AND, returns all documents that match the conditions of both clauses.
* `$not`: Inverts the effect of a query expression, returns documents that do not match the query expression.
* `$or`: Joins query clauses with a logical OR, returns all documents that match the conditions of either clause.

##### Element

* `$exists`: Matches documents that have the specified field.

##### Array

* `$all`: Matches arrays that contain all elements specified in the query.
* `$any`: Matches arrays that contain at least one element specified in the query

#### Sample queries

In the following example, the compound query returns all entities where the status equals `"A"` and either `qty` is less than `30` or `item` starts with the character `p`:

```json
{
  "status": "A",
  "$or": [
    {
      "qty": { "$lt": 30 }
    },
    {
      "item": { "$begins": "p" }
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

### The Sort Section
The sort section is an array of field names and sort order. If the order is not specified, it will be sorted in ascending order:

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

### The Paging Section
The paging section describes the size of the data set to return (i.e. page size), and how many "records" to skip. 
The following will return records 41-60. I.e. page number 3 with each page being 20 records:

```json
{
  "paging": {
    "limit": 20,
    "offset": 40
  }
}
```
### The Fields Section
The fields section is an array of field names/paths to return. 
If a pointed field of the DTO contains an object, the entire sub-object will be returned. 
Subset of sub-objects can be returned by using dot notation. 
In this example the returned entities will contain `first_name` from `name` sub-object and the entire `address` object

```json
{
  "fields": [
    "name.firstName",
    "address"
  ]
}
```

### The Fieldset Section
An API may provide named projections to save its clients the bother of writing the names of the fields in common cases.  
For example, Contacts can implement a fieldset named `common` that contains only first name, last name, primary email and phone number. 
To use fieldset, the client should specify its name. If both fieldset and fields sections exist, the union of both will take effect. 
For example:

```json
{
  "fieldset": [
    "COMMON"
  ]
}
```
