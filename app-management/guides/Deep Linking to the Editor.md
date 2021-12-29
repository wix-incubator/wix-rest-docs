# Deep Linking to the Editor

## Introduction

This API generates a link to the user’s Editor that adds a custom-element component to the stage.

### Authorization

This endpoint requires an authorization header - pass the access token from the [OAuth installation flow](https://dev.wix.com/api/rest/getting-started/authentication).

### Permissions

No special perimssion is required.

## Using the API

The API request does not require a body. If key-value pairs of data are included in a “custom_params” array, they will be added to a tab in the custom element’s Settings panel.

### Simple Request

```curl
curl -X  POST \
https://wixapis.com/apps/v1/post-installation/editor-deep-link \
-H 'Authorization: <AUTH>'
```

The simple request is used to place a custom element on the user’s stage along with its Settings panel, as described below. It is also possible to pass custom parameters by adding the parameters to the body of the request.

### Request with Custom Parameters

```curl
curl -X  POST \
https://wixapis.com/apps/v1/post-installation/editor-deep-link \
-H 'Authorization: <AUTH>' \
-header 'Content-Type: application/json' 

-data-raw '{
  "custom_params": [
    {
      "param1": "12345",
      "param2”: "abcde"
    }
  ]
}'
```

> Note:
> Custom parameters will be added to the Settings panel of a custom element.


### Response

```json
{
   "url": <url>
}
```

If the request is successful, a URL is returned that sends the user to the editor and adds a custom element to the stage.

If unsuccessful, the returned URL is '1'.

## Custom Element and its Settings Panel

The custom element is an app component that adds visual control objects as well as a settings panel. When an app with a custom element  is added to the editor, the settings are passed to the settings panel of the custom element.

A custom element is added to an app by selecting **Components > Website Component > Web component > Add Component**.

![Custom Element](./../choose-custom-element.png)

This adds a custom element, along with the settings panel, to the app. The Settings panel has many input and control widgets that can be added to it.

![Settings Panel](./../custom-settings-panel.png)

> Note:
> The Settings Panel passes default values that the user is free to adjust.

A deep link will send an app with a custom element to a user's stage together with its settings panel.

![Settings Panel](./../custom-element-on-stage.png)

Learn more about the custom element and its settings [here](https://devforum.wix.com/kb/en/article/create-a-custom-element).
