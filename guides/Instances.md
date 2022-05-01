# App Instances

The App Instance ID (instanceId) is the unique identifier of an app within a specific website.

When a site owner adds your app to their website, the Wix platform generates a new App Instance ID for that *instance* of your app on that site. 
It's always unique, fixed to a single website, and shared by all of your app endpoints (i.e., all of your app components will get the same App Instance ID).

It's persistent inside a website and will keep its value if the site owner decides to delete the app and add it again. 
This makes it ideal for identifying your users and their needs/requirements.

If your app follows the standard installation flow with [OAuth 2.0](https://dev.wix.com/api/rest/getting-started/authentication), 
this instanceId is embedded in the access token your app uses to access or modify site data.

If your app uses [API keys](https://dev.wix.com/api/rest/account-level-apis/about-api-keys), there is no instance embedded in the key, 
as they are based on accounts, not instances. To take any site-specific action, you will need to pass a site ID.
