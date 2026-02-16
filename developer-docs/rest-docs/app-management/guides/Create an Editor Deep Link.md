# Create an Editor Deep Link

<blockquote class='important' style="margin-bottom:20px">
  <p>
    <strong>Permissions</strong><br/>
    This endpoint requires the Manage Your App <a href="https://dev.wix.com/docs/build-apps/develop-your-app/access/authorization/about-permissions">permission scope</a>.
  </p>
</blockquote>

<span style="padding:6px;color:#fff;background-color:#46d895;">&nbsp;&nbsp;POST&nbsp;&nbsp;</span><span style="padding:6px;color:#000;background-color:#f2f3f4;font-size:12px;pointer-events:none;cursor:default;text-decoration:none;color:#000;">&nbsp;https://www.wixapis.com/apps/v1/post-installation/editor-deep-link</span>


### Body Params

 Name | Type | Description
---------|----------|---------
<svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24" data-hook="expand-button" class="_2rAFf" style="transform: rotate(90deg);vertical-align:middle;"><path d="M12,21 C7.02943725,21 3,16.9705627 3,12 C3,7.02943725 7.02943725,3 12,3 C16.9705627,3 21,7.02943725 21,12 C21,16.9705627 16.9705627,21 12,21 Z M12,20 C16.418278,20 20,16.418278 20,12 C20,7.581722 16.418278,4 12,4 C7.581722,4 4,7.581722 4,12 C4,16.418278 7.581722,20 12,20 Z M11.8535534,14.8496784 C11.6582912,15.0449406 11.3417088,15.0449406 11.1464466,14.8496784 C10.9511845,14.6544163 10.9511845,14.3378338 11.1464466,14.1425716 L13.2929623,11.9963306 L11.1464466,9.85355339 C10.9511845,9.65829124 10.9511845,9.34170876 11.1464466,9.14644661 C11.3417088,8.95118446 11.6582912,8.95118446 11.8535534,9.14644661 L14.7071758,11.9963306 L11.8535534,14.8496784 Z"></path></svg>&nbsp;&nbsp;**customParams** | object |Array of key-value pairs
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
https://www.wixapis.com/apps/v1/post-installation/editor-deep-link \
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
