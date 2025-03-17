# Common Objects

Select objects are reused, in full or partially, across multiple Wix APIs for easier implementation/consumption.

Even when an object is reused, the root level name and any relevant value names (e.g., filterable field names, enum names) may have been customized.

## Common query object

For example, an API that implemented the full common query object will look like this:  

```json
'{ 
    "query": { 
      "filter": { 
        "info.name.last": "Smith";  
         "sort": "[{\"dateCreated\"A: \"asc\"}]";  
        "fields": "email";  
        "fieldsets": "BASIC";  
        "paging": {
            "limit": 30,  
            "offset": 30
          };  
        "cursorPaging":  
      },
    },  
  }' 
  ```  
      
An API that implemented a partial common query object might look like this:  

```json
'{
    "query": {
      "filter": {  
        "info.name.last": "Smith"};  
         "sort": "[{\"dateCreated\": \"asc\"}]";  
        "paging": { 
            "limit": 30,  
            "offset": 30
          },  
      }' 
```

## Common address object

For example, an API that implemented the common address object will look like this:  

```json
'{ 
    "address": { 
      "country": "USA";
      "subdivision": "LA";
      "subdivisionIso31662": "LA";
      "city": "Baton Rouge";  
      "postalCode": "70809";  
      "streetAddress": "7155 Exchequer Dr";
        OR
      "addressLine": "";
      "addressLine2": "";
      "formattedAddress": ""; 
      "hint": "entrance is around the corner";  
      "geocode": "";
      "countryFullname": "United States of America";
      "subdivisionFullname": "Louisiana";
      "subdivisions": "";

        },  
    }' 
  ```  


## Common image object
An API that implemented the full common image object will look like this:

```json
'{ 
    "image": { 
      "id": "123456789";
      "url": "";
      "height": "";
      "width": "";  
      "altText": "";  
      "urlExpirationDate": "";
      "filename": "";
      "sizeInBytes": "";
        },  
 }' 
  ```  
An API that implemented a partial common image object might look like this:

```json
'{ 
    "image": { 
      "id": "123456789";
      "height": "";
      "width": "";  
        },  
 }' 
  ```  

## Common video object

An API that implemented the full common image object will look like this:

```json
'{ 
    "video": { 
      "id": "123456789";
      "url": "";
      "resolutions": "";
      "filename": "";
      "posters": "";
      "urlExpirationDate": ""; 
      "sizeInBytes": "";
      "durationInMilliseconds": "";
        },  
 }' 
  ```

An API that implemented a partial common video object might look like this:

```json
'{ 
    "video": { 
      "id": "123456789";
      "resolutions": "";
        },  
 }' 
  ```  
