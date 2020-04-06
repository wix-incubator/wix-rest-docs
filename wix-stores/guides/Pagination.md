# Pagination

The standard Wix API pagination includes:

**limit:** amount of items per response (defaults will be defined per use case)   
**offset:** number of items to skip  

The following example:
```
"query": {
  "paging": { 
    "limit": 100, 
    "offset": 20 
  }
}
```

Should return items 21-120 in the collection.

Wix Stores query endpoints are designed to handle a max of 10k data items. Therefore, if a user's store includes ~10k relevant items (e.g., products, inventory items), limit and offset may fail.  
  
Instead, filter by numericId (query products, query inventory) or number (query orders) and sort in ascending order:
``` 
"query": { 
  "sort": [{"numericId": "asc"}],
} 
```

Then copy the last numericId/number sent in this call and call the endpoint again:
```
"query":{ 
  "sort": [{"numericId": "asc"}],
  "filter": {
    "numericId": {
      "$gt": <last numeric id>
    }
  }
}
```

Continue until you receive an empty JSON as a response.

<blockquote class='important'>
<p>
  <strong>Important:</strong><br/>
Escape the JSON strings in your query parameters.
</p>
</blockquote>
