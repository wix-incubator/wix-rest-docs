SortOrder: 1
My Test readme dummy change!


> Note: 
> It’s up to the Verticals to "protect" the users in regards to statuses of items being promoted in coupons. 
> For example, in stores, we don’t want to allow users make a product invisible, if it has a coupon attached to it. We added a logic that whenever a product is changed to invisible, we check if it has coupons attached, and if it does, we don’t allow to change to invisible ("One or more of these products has a promotion attached to it. You should close the promotion before you can set the product as Hidden.)
> fff--Ww'׳jk



![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)


![ScreenShot](https://s3.amazonaws.com/wixplorer-readme-images/wix-docs-bazel%2Fintellij.png)


![Dimetrodon](https://s3.amazonaws.com/wixplorer-readme-images/wix-docs-bazel%2Fdimetrodon.jpg)


<img src="../../readme/rial.png" style="vertical-align:bottom;"/>

Some tables:
| Code | HTTP Status | Meaning | 
 | :---- | :----------- | :------- | 
| OK   | 200         | Success !! |
| INVALID_ARGUMENT | 400 | Bad Request. The client sent malformed body (REST) or one of the arguments was invalid |
| OUT_OF_RANGE | 400 | Some argument was out of range |
| FAILED_PRECONDITION | 428 | Request cannot be executed in current system state such as deleting a non-empty folder |
| UNAUTHENTICATED | 401 | Identity missing (missing, invalid or expired oAuth token, signed instance or cookies) |
| PERMISSION_DENIED | 403 | Identity does not have the permission needed for this method / resource|
| NOT_FOUND |  404 | Resource does not exist |
| ALREADY_EXISTS | 409 | Concurrency conflict |
| ~~ABORTED~~ | 409 |  DO NOT USE IN WIX |
| RESOURCE_EXHAUSTED | 429 | Resource no longer usable |
| CANCELLED | 499 | Request cancelled by the client|
| ~~DEADLINE_EXCEEDED~~ | 504 | DO NOT USE IN WIX |
| ~~UNKNOWN~~ | 500 | DO NOT USE IN WIX |
| ~~DATA_LOSS~~ | 500 | DO NOT USE IN WIX |
| INTERNAL | 500 | Internal Server Error |
| ~~UNIMPLEMENTED~~ | 501 | DO NOT USE IN WIX |
| UNAVAILABLE | 503 | Come back later |

# Declare errors in Proto

| RPC code (HTTP error code) | HTTP error string | Description |
| :---- | :---- | :---- |
| INVALID_ARGUMENT (400) | Bad request | In case of bad parameters, the body will contain more data about which is the faulty param (see below) |
| UNAUTHENTICATED (401) | Unauthorized | The client could not be authenticated. This could be due to an expired token, missing authorization header or any other reason. Can be returned by the service if there's no identity, or even by apigateway |
| PERMISSION_DENIED(403) | Forbidden | The client does not have permission to call that endpoint |
| NOT_FOUND (404) | Not found | The resource requested was not found |
| RESOURCE_EXAUSTED (429) | Too many requests | The client has sent too many requests in a given amount of time (rate limit) |
| INTERNAL (500) |
| UNAVAILABLE (503) | Server error | Something bad happened on the server side. It is not the client's fault and there's nothing that the client can do to fix it. The client can try again later. |



| Verb   | Outcome                       | Idempotent              |
| ------ | ----------------------------- | ----------------------- |
| GET    | Get entity                    | Yes                     |
| POST   | Create new entity             | No                      |
| PUT    | Update full entity            | Yes                     |
| DELETE | Delete entity                 | Yes                     |
| PATCH  | Partial entity update by Id/s | Implementation Specific |



## Response Codes

Response codes allow developers to understand the API more easily.  
It is important to provide clear HTTP response codes and additional info.  
Codes we should support:

| Response Code | Meaning                 | Comment                                                                                                                                                                                                                   |
| ------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200           | OK                      | Request was handled successfully. Since we can't technically return other 2xx response codes, we return 200 for all success responses - Resource created (usually 201), Accepted (usually 202) and Mutli Response (usually 207). In case of batch operation that has multiple response codes, you should have an object in the response body with specific details |
| 400           | Bad request             | Format was wrong from client                                                                                                                                                                                              |
| 401           | Unauthorized            | Token did not pass gateway / framework                                                                                                                                                                                    |
| 403           | Forbidden               | Application denied request                                                                                                                                                                                                |
| 404           | Not found               | Resource not found                                                                                                                                                                                                        |
| 409           | Conflict                | The request cannot be processed because it conflicts with the server's state, e.g., trying to edit while not having the most recent version of the resource ([edit conflict](https://en.wikipedia.org/wiki/Edit_conflict)) |
| 500           | Internal Server Error   | Internal error (can provide additional internal code in response for debugging). Should only be used when it's not the client's fault, e.g., DB is not available.                                                           |
| 503           | Temporarily unavailable | Retry later - service is busy                                                                                                                                                                                             |




#### Common prefixes and suffixes
| Affix | Usage | example | Don't use |
| ----- | ----- | ------- | --------- |
| `xxxId` | When the value is an ID of __another__ entity |  An Order entity can have `ownerId` | The ID field of the entity itself should be named `id`. E.g. Order entity should have `id` and not `orderId`
| `xxxCount` | For items that increment | `likeCount`, `viewCount` | `xxxTimes`, `xxxNum`, `xxxTotal`
| `xxxInfo` | Added information on an entity | `userInfo`, `buyerInfo`, `couponInfo` | Don't use `xxxData`, `xxxDetails`, etc |
| `totalXxx` | Total number of items which is not incremented (see `xxxCount`) | `totalPages`, `totalValue` | Don't use `xxxCount`, `numXxx` |
| __DON'T USE__ `isXxx` | For boolean values, simply use the verb | `required`, `hidden` | Don't use `isRequired`, `isHidden` |
| `minXxx`, `maxXxx` | For min or max values | `minDate`, `maxValue` | Don't use full form `minimum` or `maximum` |
| `xxxDate` | For event timestamp. Use past tense for the verb | `createdDate`, `updatedDate`, `publishedDate` | __DON'T USE__ `date` as a prefix as in `dateUpdated`, don't use other tense like `createDate` |
| `xxxFields` | Fields in a form |`formFields`, `customFields` | `xxxData`, `xxxInfo` (Use `xxxInfo` for information not specific to a form) |


#### Common names
| Name | Usage | 
| ---- | ----- |
| lalalal| hey!|
| `email`, `phone`, `phones` | Don't use `emailAddress` or `phoneNumber` |
| `firstName`, `lastName` | First or Last name |
| `fullName` | First name and last name. Not name |
| `postalCode`  | Not `zipCode`|
| `revision` | Used for incremental update of existing data. E.g. `siteRevision` |
| `version` | Used for new variation (software version) |
| `required` | Element required to have value. For example, `$w("#myElement").required` |
| `send` | Send an entity, often to a user. e.g. `sendMessage`, `sendInvoice`. Not `post` |
| `submit` | Submit a form. For example, `onFormSubmit`. Not `post` |
