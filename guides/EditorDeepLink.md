# Deep Linking to the Editor

## Introduction

This API generates a link to a user’s Editor that then opens to your app.

### Authorization

This endpoint requires an authorization header - pass the access token from the [OAuth installation flow](https://dev.wix.com/api/rest/getting-started/authentication).

### Permissions

This endpoint requires the WIX_DEVELOPERS.GET_EDITOR_DEEP_LINK [permission scope](https://devforum.wix.com/en/article/available-permissions).

## Using the API

### Request

```curl
Curl -X  GET \
https://wixapis.com/apps/v1/editor-deep-link \
-H 'Authorization’ <AUTH>
```

### Response

```json
{
   "url": <url> 
}
```

* If successful, the response contains the url you need to send users to the your app in the editor.
* If not successful, the url returned is is just the string '1'.

