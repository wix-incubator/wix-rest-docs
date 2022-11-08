# Common Objects

Select objects are reused, as is or in part, across multiple Wix APIs for easier implementation/consumption.

For example, an API that implemented the full common query object will look like this:  

` '{
    "query": {
      "filter": {. 
        "info.name.last": "Smith"};  
         "sort": "[{\"dateCreated\"A: \"asc\"}]";  
        "fields": "email";  
        "fieldsets": "BASIC";  
        "paging": {
            "limit": 30,  
            "offset": 30
          };  
        "cursorPaging":  
      },  
      }' `  
      
An API that implemented a partial common query object might look like this:  

` '{
    "query": {
      "filter": {  
        "info.name.last": "Smith"};  
         "sort": "[{\"dateCreated\": \"asc\"}]";  
        "paging": {. 
            "limit": 30,  
            "offset": 30
          },  
      }' `

From January 2023, common objects will be documented as such.
