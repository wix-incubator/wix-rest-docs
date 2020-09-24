SortOrder: 0
# Overview

Use this API to trigger events about any changes to entities. For example:
- Transactions
- Refunds

Every time there is a change to a payment entity, send this as an event to Wix using the [Submit Event](link needed) method. 
If an event is accepted, the response will look like this:
```bash
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8
Transfer-Encoding: chunked

{}
```
In case of an error, Wix will respond with one of our [REST API error codes](https://dev.wix.com/api/rest/getting-started/errors).
