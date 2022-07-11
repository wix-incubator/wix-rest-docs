# Sorting and Paging

_List_ and _Query_ endpoints that return a list of entities
allow you to specify sorting and paging options in the request.

This articles gives a general overview of sorting and paging.
The implementation changes
depending on whether an endpoint is a GET or POST request.
Check your API's documentation for specific details,
including which fields are sortable.

## Sorting

Most APIs default to sorting by `createdDate` in `DESC` (descending) order,
although some APIs have a different default sort order.
You can override the default sorting by specifying
a new field and order.

### Sort _List_ endpoints

_List_ endpoints are designed to be lightweight HTTP GET requests.
For this reason, sorting is applied through the query parameters,
typically with `sort.fieldName` and `sort.order`.

For example, to list contacts by last name in ascending order,
append these query parameters to the request:

```txt
?sort.fieldName=info.name.last&sort.order=ASC
```

Your API's _List_ endpoint may support sorting by multiple fields.
This is done by adding a new `&sort.fieldName` and `&sort.order` parameter
for each sort field:

```txt
?sort.fieldName=info.name.last&sort.order=ASC&sort.fieldName=createdDate&sort.order=ASC
```

### Sort _Query_ endpoints

_Query_ endpoints offer more robust filtering capabilities.
When working with a _Query_ endpoint,
sorting is specified in an array in the request body,
typically `query.sort`.
For each `sort` object,
sorting is applied with the `fieldName` and `order` parameters.

For example, to list contacts by last name in ascending order,
include this structure in the request body:

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

## Paging

The standard Wix API pagination includes:

- **limit**: amount of items per response (default is `0`)

- **offset**: number of items to skip

The following examples:

```txt
?limit=100&offset=20
```

and

```json
    "limit": 100, 
    "offset": 20 
```

Should return items 21-120 in the results.
