# Errors
Error messages are a fundamental component of Wix's APIs, providing critical information and guidance when something goes wrong. 
Most of Wix's errors follow a standardized format, as described below.

## Error properties
| Property | Description | 
| :-------------- | :------- |  
| Status code | See the HTTP status code table below. |
| `message` | Textual description that provides a brief explanation of the error. |
| `details` | Additional contextual information about the error, including either `validationError` or `applicationError`. See the tables below. |

## HTTP status codes
Every API call will return a status code. If something went wrong, you'll receive an error code that defines the type of error that occurred. 

| HTTP Status Code | Description | 
| :-------------- | :------- |  
| 200 - OK | Success. |
| 400 - Bad Request | One or more request parameters is wrong or missing, or you didn't pass validation. |
| 401 - Unauthorized | The system wasn't able to authenticate you (missing or incorrect Authorization header, expired token, etc.). |
| 403 - Permission denied | The system authenticated you, but you don’t have permissions to call this API. |
| 404 - Not found | Resource not found / doesn't exist. |
| 409 - Conflict | The resource you are attempting to create already exists. |
| 429 - Resource exhausted | Resource usage was exhausted (e.g., a previously used one-time-token, or too many requests). |
| 500 - Internal server error | An error occurred on Wix's server. Try again later. |
| 501 - Not implemented | The endpoint hasn't been implemented yet. |
| 503 - Service unavailable | The service that you’re trying to access is temporarily unavailable. Try again later. |
| 504 - Gateway timeout | The underlying service didn't respond in a timely manner. Try again later. |

## Validation error data
A validation error occurs when input data fails to meet predefined criteria or constraints set by the system. This type of error serves to enforce rules such as correct data formats, required fields, or value ranges. This will include rules like `OUT_OF_RANGE` and `INVALID_ARGUMENT`.

| Property | Description | 
| :-------------- | :------- |  
| `fieldViolations` | Array of validation issues found in individual fields. |
| `fieldViolations.field` | Field name. |
| `fieldViolations.description` | Detailed explanation of why the error occurred for the specified field. |
| `fieldViolations.violatedRule` | Specific rule or constraint that was violated by the input in the identified field. |
| `fieldViolations.ruleName` | Name of specific rule or constraint that was violated. For example, `"VALIDATION_ERROR"`  |
| `fieldViolations.data` | Additional contextual information related to the field violation.  |


### Example
```json
{
  "message": "Not really valid",
  "details": {
    "validationError": {
      "fieldViolations": [
        {
          "field": "fieldA",
          "description": "invalid music note. supported notes: [do,re,mi,fa,sol,la,ti]",
          "violatedRule": "CUSTOM",
          "ruleName": "INVALID_NOTE",
          "data": {
            "value": "FI"
          }
        },
        {
          "field": "fieldB",
          "description": "field value out of range. supported range: [0-20]",
          "violatedRule": "MAX",
          "data": {
            "threshold": 20
          }
        },
        {
          "field": "fieldC",
          "description": "invalid phone number. provide a valid phone number of size: [7-12], supported characters: [0-9, +, -, (, )]",
          "violatedRule": "FORMAT",
          "data": {
            "expected": "PHONE"
          }
        }
      ]
    }
  }
}
```

## Application error data
An application error occurs when the service business-logic decides to reject the request. This will include codes like `UNAUTHENTICATED`, `PERMISSION_DENIED`, `NOT_FOUND`, `ALREADY_EXISTS`, `ABORTED` and `RESOURCE_EXHAUSTED`.

| Property | Description | 
| :-------------- | :------- |    
| `code` | Identifier that categorizes and signifies the specific error. |
| `description` | Detailed explanation of why the error occurred. |
| `data` | Additional contextual information related to the error. |

### Examples
```json
{
  "message": "Payment failed",
  "details": {
    "applicationError": {
      "code": "NO_FUNDS",
      "description": "Payment declined due to insufficient funds",
      "data": {
        "availableFunds": 75.22
      }
    }
  }
}
```
```json
{
 "message": "Duplicate contact exists",
 "details": {
   "applicationError": {
     "code": "DUPLICATE_CONTACT_EXIST",
     "description": "Duplicate contact already exists",
     "data": {
       "duplicateContactId":"ca22360e-7f58-4613-bae6-a537f2791f84"
     }
   }
 }
}
```
## System errors
A system error occurs there's an exeption in the system, server is down, or some dependent service or database is down.  
These errors are sent empty by design.

### Example
```json
{
  "message": "",
  "details": {}
} 
```
