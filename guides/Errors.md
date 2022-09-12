# Errors

When you call an API, the response you'll receive will include a status code. If something went wrong, you'll receive an error code that defines the type of error that occurred. 

| HTTP Status Code | Description | 
| :-------------- | :------- |  
| 200 - OK | Success |
| 400 - Bad Request | One or more request parameters is wrong or missing, or you didn't pass validation |
| 401 - Unauthorized | The system was not able to authenticate you (missing or incorrect Authorization header, expired token, etc.) |
| 403 - Forbidden | The system authenticated you, but you don’t have permissions to call this API |
| 404 - Not found | Resource not found / doesn't exist |
| 409 - Conflict | The resource you are attempting to create already exists |
| 429 - Too many requests | Resource usage was exhausted (e.g., a previously used one-time-token) |
| 500 - Internal server error | An error occurred on Wix's server, try again later |
| 501 - Not implemented | The endpoint has not been implemented yet |
| 503 - Service unavailable | The service that you’re trying to access is temporarily unavailable. Try again later |
| 504 - Gateway timeout | The underlying service did not respond in a timely manner. Try again later |
