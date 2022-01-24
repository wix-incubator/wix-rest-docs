# Create an Editor Deep Link

### Authorization
This endpoint requires an authorization header. Pass the access token from the [OAuth installation flow](https://dev.wix.com/api/rest/getting-started/authentication).

<blockquote class='important'>
  <p>
    <strong>Permissions</strong><br/>
    This endpoint requires the Manage Your App <a href="https://devforum.wix.com/en/article/available-permissions">permission scope</a>).
  </p>
</blockquote>

### Syntax: REST

<span style="color:#fff;background-color:#46d895;">&nbsp;POST&nbsp;</span><span style="background-color:#fff;">&nbsp;http://www.wixapis.com/apps/v1/post-installation/editor-deep-link</span>

### Body Params

Name | Type | Description
---------|----------|---------
 custom_params | Array |Array of key-value pairs
 &nbsp;&nbsp;&nbsp;&nbsp;key | string |
 &nbsp;&nbsp;&nbsp;&nbsp;value | string |

### Response Object

Name | Type | Description
---------|----------|---------
url | URL | url that places App components on the page

### Example

```CURL
Curl -X  POST \
https://wixapis.com/apps/v1/post-installation/editor-deep-link \
-H 'Authorization: <AUTH>'

-data-raw '{
  "custom_params": [
    {
      "key1": "value1",
      "key2": "value2"
    }
  ]
}'
```

#### Response
```
{
   "url": <url>
}
```

### Status/Error Codes
The response will include an [HTTP status code](https://dev.wix.com/api/rest/getting-started/errors).
