SortOrder: 3
# API Query Language 

## General
The query language described in this document is implemented partially or in full by Wix APIs supporting query capabilities. 

The style of the QL is heavily influenced by MongoQL.

## Syntax
A query object consists of 5 (optional) parts:
* _Filter_ - which entities to return
* _Sort_ - in what order
* _Paging_ - return only part of the matched entities
* _Fields_ - return only part of each entity (a.k.a. projection)
* _Fieldset_ - a predefined set of fields with common use (i.e. named projection). This is a shorthand provided by the API for specifying each field name.
  
Each query is always a single JSON: `{ }`  
An empty json will return all records in no specific order. 
An application can decide to return a subset of the records (default paging behavior)  

The query object can define a key for each of the above parts:
```javascript
{
  filter: { … },
  sort: [ … ],
  paging: { … },
  fields: [ … ],
  fieldset: ["xx"…]
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
* _$eq_ - matches values that are equal to a specified value.
* _$gt_ - Matches values that are greater than a specified value.
* _$gte_ - Matches values that are greater than or equal to a specified value.
* _$in_ - Matches any of the values specified in an array.
* _$lt_ - Matches values that are less than a specified value.
* _$lte_ - Matches values that are less than or equal to a specified value.
* _$ne_ - Matches all values that are not equal to a specified value.
* _$nin_ - Matches none of the values specified in an array.
* _$begins_ - Matches strings that begin with a specified value (NOT case sensitive).

##### Logical
* _$and_ - Joins query clauses with a logical AND, returns all documents that match the conditions of both clauses.
* _$not_ - Inverts the effect of a query expression, returns documents that do not match the query expression.
* _$or_ - Joins query clauses with a logical OR, returns all documents that match the conditions of either clause.

##### Element
* _$exists_ - Matches documents that have the specified field.

##### Array
* _$all_ - Matches arrays that contain all elements specified in the query.
* _$any_ - Matches arrays that contain at least one element specified in the query

#### Sample Queries
In the following example, the compound query returns all entities where the status equals `"A"` and either `qty` is less than `30` or `item` starts with the character `p`:
```javascript
{
  status: "A",
  $or: [{qty: {$lt: 30}}, {item: {$begins: "p"}}]
}
```

The following example queries entities where the field `tags` value is an array with exactly two elements, `"red"` and `"blank"`, in the specified order:
```javascript
{ tags: ["red", "blank"] }
```

The following example queries for all entities where `tags` is an array that contains the string `"red"` as one of its elements, or that `tags` is the string `"red"`:
```javascript
{tags: "red" } 
```

The following query matches entities that do not contain the `item` field, or where the `item` field has no value:
```javascript
{item: {$exists: false }} 
```

### The Sort Section
The sort section is an array of field names and sort order. If the order is not specified, it will be sorted in ascending order:
```javascript
sort: [{"fieldName":"sortField1"},{"fieldName":"sortField2","order":"DESC"}]
```

### The Paging Section
The paging section describes the size of the data set to return (i.e. page size), and how many "records" to skip. 
The following will return records 41-60. I.e. page number 3 with each page being 20 records:
```javascript
paging: { limit: 20, offset: 40 }
```
### The Fields Section
The fields section is an array of field names/paths to return. 
If a pointed field of the DTO contains an object, the entire sub-object will be returned. 
Subset of sub-objects can be returned by using dot notation. 
In this example the returned entities will contain `first_name` from `name` sub-object and the entire `address` object
```javascript
fields: ["name.firstName", "address"]
```

### The Fieldset Section
An API may provide named projections to save its clients the bother of writing the names of the fields in common cases.  
For example, Contacts can implement a fieldset named `common` that contains only first name, last name, primary email and phone number. 
To use fieldset, the client should specify its name. If both fieldset and fields sections exist, the union of both will take effect. 
E.g. 
```javascript
fieldset: ["common"]
```

## Query Response
The response for a query request is an object with the following structure:
```javascript
{
  results: [...], //instead of 'results' you can use more explicit name like 'invoices'
  metadata: {  //this is page 2 
    items: 25,
    offset: 25
  },
  totalResults: 420
}
```
