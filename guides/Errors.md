# Errors
Errors are a fundamental component of Wix's APIs, providing critical information and guidance when something goes wrong. 
Most of Wix's errors follow a standardized format, as described below.

## Error properties
| Property | Description | 
| :-------------- | :------- |  
| Status code | See the HTTP status code table below. |
| `message` | Textual description that provides a brief explanation of the error. |
| `details` | Additional contextual information about the error, including either `applicationError` or `validationError`. See the tables below. |

## HTTP status codes
Every API call will return a status code. If something went wrong, you'll receive an error code that defines the type of error that occurred. 

Status code types include:
- 2xx - Everything is OK.
- 4xx - There was a problem with the request. Usually you can fix the request and try again immediately.
- 5xx - There was a problem in Wix's service, there's nothing wrong with the request. Try again later.

| HTTP Status Code | Description | 
| :-------------- | :------- |  
| 200 - OK | Success. No error. |
| 400 - Bad Request | One or more request parameters is wrong or missing, or you didn't pass validation. |
| 401 - Unauthorized | The system wasn't able to authenticate you (missing or incorrect Authorization header, expired token, etc.). Occasionally returned when you don’t have permissions to call this API.|
| 403 - Permission denied | The system authenticated you, but you don’t have permissions to call this API. |
| 404 - Not found | Resource not found / doesn't exist. |
| 409 - Conflict | The resource you are attempting to create already exists or has a different revision than the one you're attempting to update, or another conflict with the server state. |
| 428 - Precondition required | Preconditions must be met for the request to be successful (for example, a required field wasn't passed, gift card is out of funds).
| 429 - Resource exhausted | Resource usage was exhausted (for example, a previously used one-time-token, or too many requests). |
| 500 - Internal server error | An error occurred on Wix's server. Try again later. |
| 501 - Not implemented | The endpoint hasn't been implemented yet. |
| 503 - Service unavailable | The service that you’re trying to access is temporarily unavailable. Try again later. |
| 504 - Gateway timeout | The underlying service didn't respond in a timely manner. Try again later. If you're trying to query for data, you may try a smaller page size or a simpler filter. |


## Application error data
An application error occurs when the service business-logic decides to reject the request. This includes codes like `UNAUTHENTICATED`, `PERMISSION_DENIED`, `NOT_FOUND`, `ALREADY_EXISTS`, `ABORTED` and `RESOURCE_EXHAUSTED`.

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
409 Conflict
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

## Validation error data
A validation error occurs when input data fails to meet predefined criteria or constraints set by the system. This type of error serves to enforce rules such as correct data formats, required fields, or value ranges. This includes rules like `OUT_OF_RANGE` and `INVALID_ARGUMENT`. Validation errors are 4xx types. Multiple violations may be returned in one response.

| Property | Description | 
| :-------------- | :------- |  
| `fieldViolations` | Array of validation issues found in individual fields. |
| `fieldViolations.field` | Field name. |
| `fieldViolations.description` | Detailed explanation of why the error occurred for the specified field. |
| `fieldViolations.violatedRule` | Specific rule or constraint that was violated by the input in the identified field. |
| `fieldViolations.ruleName` | Name of specific rule or constraint that was violated. For example, `"VALIDATION_ERROR"`.  |
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
          "description": "Invalid music note. Supported notes: [do,re,mi,fa,sol,la,ti]",
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

## System errors
A system error occurs when there's an exception in the system, server is down, or some dependent service or database is down.  
These errors are sent empty by design. System errors are 5xx types.

### Example
```json
500 Internal server error
{
  "message": "",
  "details": {}
} 
```
