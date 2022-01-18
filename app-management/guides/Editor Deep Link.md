# About the Editor Deep Link API

This API generates a URL that you can use to add your app’s components to a user’s site directly in the Editor. The API can also be used to add a [Custom Element](https://devforum.wix.com/kb/en/article/create-a-custom-element) together with its Settings panel.

> **Note:**
> The Custom Element is currently in beta testing, and is not available to all users. If you would like to request access, please [submit a proposal](https://devforum.wix.com/kb/en/article/submit-an-app-proposal).

## Terminology

**Editor Deep Link** - A link that sends users directly to the Editor, in this case also adding an app’s components directly to the page.

**[Custom Element](https://devforum.wix.com/kb/en/article/create-a-custom-element)** - A website component that contains a custom script as well as custom parameters with UI control elements in a Settings panel.

## Use Cases

The Editor Deep Link API generates a URL that adds components to a site. It can be used in several ways.

### Use Case 1: Adding Components to a Page

In this first case, no parameters are sent in the body of the request and your app can have any type of components. The authorization token containing your App ID is used to generate a URL that adds the app’s components to a user’s page.

### Use Case 2: Using the Deep Link With a Custom Element

Parameters for the Custom Element are passed in the body of the request. They are added to the Custom Element’s Settings panel, described below, and the Custom Element is added to the page..

> **Note:**
> Parameters passed in the body of the API request will only populate the Settings panel if their keys match keys already defined in the settings panel.

### Use Case 3: Using the Custom Element’s Settings Panel

Each Custom Element web component has its own Settings panel. Parameters may be added to the panel using the tabbed layout and a variety of UI controls that make it easy for your users.

![Settings panel](./../../media/custom-element-settings-panel.png "Settings panel")

When users install your app and a Custom ElementEditor is added to their page, they have access to the same settings panel. Values set while developing the app are presented to users as default settings.

![Custom element on page](./../../media/custom-plus-settings.png "Custom element on page")

## An Example of Using the Custom Element

Consider an app that adds a lead generation form. Users create forms via the app's dashboard, and each form has a unique id. Next to each form in the dashboard the developer adds an “Add to Site'' button. It uses the Deep Link API together with the unique form id that is passed as a custom key-value pair into a Settings panel field with the same key. When users click the button, they are taken to the editor, and the component with that form id is added to the page.

## Editor Deep Link

### Authorization

This endpoint requires an authorization header. Pass the access token from the [OAuth installation flow](https://dev.wix.com/api/rest/getting-started/authentication).

> **Permissions:**
> This endpoint requires the Manage Your App [permission scope](https://devforum.wix.com/en/article/available-permissions).

### Request

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

### Response

```JSON
{
   "url": <url>
}
```

### Status/Error Codes

The response will include an [HTTP status code](https://dev.wix.com/api/rest/getting-started/errors).
