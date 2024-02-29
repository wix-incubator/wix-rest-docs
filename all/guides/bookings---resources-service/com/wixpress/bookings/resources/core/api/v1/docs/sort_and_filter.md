SortOrder: 1
# Query Syntax: Filters, Sorting, Fields and Paging.



## Filters
The filter section allows you to retrieve a specified subset of the available data.

The filter section is a single JSON object with the following rules:

**Equality**  
Use the following format to specify an equality condition:
```JSON
{ 
  "query": {
      "filter":{
           "<field>":"<value>"}
      }
  }
}
```

**Operators**  
Use operators in the following format: 
```JSON
{ 
  "query": {
      "filter":{
          "<field>": {"<operator>":"<value>"},
      ...
      }
  }
}
```
For example, the following query will match all entities that have `status` set to `"CREATED"` or `"UPDATED"`:

```JSON  
{ 
  "query": {
      "filter":{"status": {"$in": ["CREATED", "UPDATED"]}
      }
  }
} 
```

Each endpoint supports a subset of the following operators. See the specific endpoint's reference documentation for a list of supported operators.  

- Comparison
  + `$eq` - Matches values that are equal to a specified value.
  + `$ne` - Matches all values that are not equal to a specified value.
  + `$lt` - Matches values that are less than a specified value.
  + `$lte` - Matches values that are less than or equal to a specified value.
  + `$gt` - Matches values that are greater than a specified value.
  + `$gte` - Matches values that are greater than or equal to a specified value.
  + `$in` - Matches any of the values specified in an array.
  + `$hasSome` - Matches an array that contains at least one of the specified values.
  + `$hasAll` - Matches an array that contains all of the specified values.
  + `$startsWith` - Matches strings that start with a specified value. Case insensitive.
  + `$endsWith` - Matches strings that end with the specified value. Case insensitive.
  + `$contains` - Matches strings that contain the specified value. Case insensitive.
- Logical
  + `$and` - Joins query clauses with a logical AND, and returns all documents that match the conditions of all clauses.
  + `$not` - Inverts the effect of a query expression and returns documents that do not match the query expression.
  + `$or` - Joins query clauses with a logical OR, and returns all documents that match the conditions of at least one of the clauses.
- Element
  + `$exists` - Matches objects that have the specified field.
- Array
  + `$hasSome` - Matches an array that contains at least one element specified in the query.
  + `$hasAll` - Matches arrays that contain all elements specified in the query



**Sample Queries**  
The following example shows a compound query that returns all entities where `status` is `"NEW"` and either `Quantity` is less than `30` or `itemName` starts with the character `P`:

```JSON
{ 
  "query": {
      "filter":{
        "status": "NEW",
        "$or": [{"Quantity": {"$lt": 30}}, {"itemName": {"$startsWith": "P"}}]
      }
  }
}    
```

The following example queries entities where the field tags value is an array with exactly two elements, "red" and "blank", in the specified order:

```JSON
{ 
  "query": {
      "filter":{ "tags": ["red", "blank"] }
  }
}  
```

The following example queries for all entities where tags is an array that contains the string "red" as one of its elements, or that tags is the string "red":

```JSON 
{ 
  "query": {
      "filter":{"tags": "red" } 
  }
}      
```

The following query matches entities that do not contain the item field, or where the item field has no value:

```JSON
{ 
  "query": {
      "filter":{"item": {"$exists": false } }
  }
}     
```
## Sort 
The sort section is an array of field names and sort direction. If the direction is not specified, it will be sorted in ascending order:

```JSON
{ 
  "query": {
      "sort": [{"fieldName":"sortField1"},{"fieldName":"sortField2","order":"DESC"}]
  }
}      
```

## Paging
The paging section describes the size of the data set to return, and how many items to skip. For example, the following will return items 41-60. In other words, page number 3,with each page being 20 items:

```JSON
{ 
  "query": {    
    "paging": { "limit": 20, "offset": 40 }
  }
}  
```

## Fields
The fields section is an array of field names and paths to return. Subsets of sub-objects can be returned by using dot notation. The following example returns `firstName` from `name` sub-object and the entire `address` object

```JSON
{ 
  "query": {    
      "fields": ["name.firstName", "address"]
  }
}  
```
## Fieldsets
An API may provide named projections to save its clients from specifying the names of the fields in common use-cases.
For example, Contacts includes a fieldset named `common` that contains only first name, last name, email, and phone number. If both fieldset and fields sections are specified, the returned items will include the fields specified in the `fields` array and those defined in the fieldset.

```JSON
{ 
  "query": {    
    "fieldset": ["common"]
  }
}    
```
## Query Response
The response for a query request should be an object with the following structure:

```JSON
{
  "result-object": [...], //Array of the result object
  "pagingMetadata": {
     "count": 33, // Number of items in the result-object array
     "offset": 3, // Offset of the first item in the result-object array
     "total": 36 // Total number of result-objects that match the specified filters.
  }
 
}
```
