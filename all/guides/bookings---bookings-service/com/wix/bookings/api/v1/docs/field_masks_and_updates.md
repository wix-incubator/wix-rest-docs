SortOrder: 2
# Patch Endpoints and Field Masks in Update Requests
When updating a resource, the Resources API uses PATCH endpoints and field masks. A PATCH endpoint means that only the fields specified in the request will be updated.
Alternatively, a field mask explicitly lists the fields to update, regardless of which fields are specified in the request.
You must use a field mask if you want to clear the value from a field.

The example below uses a field mask. 
+ The value of the `phone` field is updated 
+ The value of the `email` field is cleared. 
+ The `name` field is not updated as it is not included in the field mask.

```JSON
{
    "resource": {
        "name": "John Smith",
        "phone": "5553456"
    },
    "fieldMask": {
        "paths": ["phone","email"]
    }
}
```
