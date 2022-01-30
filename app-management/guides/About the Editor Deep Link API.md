# About the Editor Deep Link API

This API generates a URL that will open the Editor and add an App's [Custom Element](https://devforum.wix.com/kb/en/article/create-a-custom-element) component to the user's page. If the App doesn't have a Custom Element component, the URL just opens the Editor.

> Note:
> The Custom Element is currently in beta testing, and is not available to all users. If you would like to request access, please submit a proposal.

## Terminology

- **Custom Element** - A website component that contains a custom script as well as custom parameters with UI control elements in a Settings panel.

- **Editor Deep Link** - A link that sends a user to the Editor, adding a Custom Element components directly to the page.

## Use Cases

The Editor Deep Link API generates a URL that opens the Editor and adds Custom Element components to a page. It can be used in the following ways.

### Use Case 1: Open the Editor

Calling the API for an App that doesn't have a Custom Element component generates a URL that just opens the Editor. It isn't nececasry to include any paramteters in the body of the request.

#### Request

```CURL
Curl -X  POST \
https://wixapis.com/apps/v1/post-installation/editor-deep-link \
-H 'Authorization: <AUTH>'
```

#### Response
```
{
   "url": <url>
}
```

### Use Case 2: Use the Deep Link to Add a Custom Element

Add a Custom Element component to your app. Edit the component, and enter the URL for your script in the **Basic Info** section. Click the **Settings Panel** tab and add custom  paramters to the Settings panel of the component, adding keys and values for each parameter. Values depend on the type of parameter - default text, toggle on/off, slider value and so on.

![Settings Panel](./../../media/custom-element-settings-panel.png)

Use the API to create a URL that will open the user's Editor and then add the Custom Element component to a page.

You can further customize each generated URL by adjusting the values of the custom parameters. This is done passing new values in the body of the request.

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

```JSON
{
   "url": <url>
}
```

> **Note:**
> Parameters passed in the body of the API request will only populate the Settings panel if their keys match the keys already present in the settings panel.

When users install your app they have access to the same settings panel. The values you set, either in the Settings panel or in the body of the API request, are presented to users as defaul or initial settings that can be changed by the user.

![Custom Element](./../../media/custom-plus-settings.png)
