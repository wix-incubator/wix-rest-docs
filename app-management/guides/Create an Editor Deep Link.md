# Create an Editor Deep Link

### Authorization

This endpoint requires an authorization header. Pass the access token from the [OAuth installation flow](https://dev.wix.com/api/rest/getting-started/authentication).

<blockquote class='important' style="margin-bottom:20px">
  <p>
    <strong>Permissions</strong><br/>
    This endpoint requires the Manage Your App <a href="https://devforum.wix.com/en/article/available-permissions">permission scope</a>.
  </p>
</blockquote>

<span style="padding:6px;color:#fff;background-color:#46d895;">&nbsp;&nbsp;POST&nbsp;&nbsp;</span><span style="padding:6px;color:#000;background-color:#f2f3f4;font-size:12px;pointer-events:none;cursor:default;text-decoration:none;color:#000;">&nbsp;https://www.wixapis.com/apps/v1/post-installation/editor-deep-link</span>

### Body Params

Name | Type | Description
---------|----------|---------
 <img src="./../../media/arrow-down.png" width=20 style="vertical-align:middle">&nbsp;&nbsp;**customParams** | object |Array of key-value pairs
 <span style="margin-left:25%">&vert; **key** | string |</span>
 <span style="margin-left:25%">&vert; **value** | string |</span>

### Response Object

Name | Type | Description
---------|----------|---------
**url** | URL | Deep Link URL

### Example

#### Request

```CURL
Curl -X  POST \
https://wixapis.com/apps/v1/post-installation/editor-deep-link \
-H 'Authorization: <AUTH>'

-data-raw '{
  "customParams": [
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
   "url": "https://www.wix.com/editor/8d157c7a-2cb8-4ea9-bf6f-3039e30099a3?appMarketParams=eyJraWQiOiJ5R0xVRVlVTiIsImFsZy.."
}
```

### Status/Error Codes

The response will include an [HTTP status code](https://dev.wix.com/api/rest/getting-started/errors).
