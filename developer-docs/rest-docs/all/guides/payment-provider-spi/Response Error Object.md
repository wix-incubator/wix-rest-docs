SortOrder: 3
# Error Responses
Our SPI describes only success flows, but in case something goes wrong, Wix will expect an error response.
In this section we will describe standard error responses from all SPI requests that you must implement on your side.

## Error object

```json
{
  "reasonCode": 1004,
  "errorCode": "ER23",
  "errorMessage": "Required fields: [email] are missing"
}
```

| Name | Type | Description |
|------|------|-------------|
| *reasonCode (required)*| int32 | `Wix` predefined [reasonCodes](reason-codes.md) that provide more detail about the error.|
| errorCode | string |  `Payment provider` error code. |
| errorMessage | string | `Payment Provider` error description. |

> ***Note**:
We suggest that you map your errors to our `reasonCode`, because in this case both merchants and buyers will get a proper localized error message using our UI design.
If you can't find an appropriate `reasonCode`, use `reasonCode: 6000`. In this case we will need your `errorCode` and `errorMessage`, so that a complaint and investigation can be communicated properly to our customers.  
