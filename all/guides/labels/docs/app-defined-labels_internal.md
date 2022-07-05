SortOrder: 3
# App Defined Labels Integration

You can create app defined labels which are dedicated to your app (will be visible only on sites that have this app installed)
It can easily be done via [dev-center][dev-center].

The steps:
* Select the relevant App
* Click on Components
* Add Component
* Integration Component
* Contact Labels
* Add Component  

Now you should see the Contact Labels form,

before we start, you need to set a namespace for your app (if not already set),
this can be done in the following link:
https://pbo.wixpress.com/rpc-console-poc/app-service-webapp/sever_any/Apps/setAppNamespace

This namespace must represent your app, and should be written in `camelCase` convention.
The namespace you set, will be displayed in the UI as the namespace display name (which is not ideal), so you better set a namespace display name,
in order to do that, read [translation](#translation)

Under this namespace there are going to be system labels or app defined labels or both.

`System labels` are always part of the labels of the site, they cannot be deleted.

`App defined labels` can be modified, you can choose to restrict the modification permission for required permission.

* In order to have system labels you must add them in the form.

* In order to allow creation of app defined labels - you must check the checkbox in the form.

In order for the label app component to be in production, it needs to be whitelisted by the contacts team. 
That is done by adding it to FryingPan config of contacts-labels-app. In order to test it before its whitelisted, see [specs](#specs)

### Specs 
To be able to easily test your app defined labels you can override the following specs: 
* Turn on [ContactsAppDefinedLabelsTestMode][ContactsAppDefinedLabelsTestMode] - in order to return non whitelisted and not installed app defined labels

### Translation
The default language supplied in the form is english,
currently the only way to supply additional languages is by submitting a PR to [contacts translation file][messages_en].  
You can translate namespace display name by adding a new row to the file with the following format:

`"label.namespace.[your_namespace_key]": "[your_namespace_display_name]"`

You can translate system label display name by adding a new row to the file with the following format:

`"label.namespace.[your_namespace_key].[your_system_label_key]": "[your_system_label_display_name]"`

[dev-center]: https://dev.wix.com
[messages_en]: https://github.com/wix-private/crm/blob/master/contacts/common/src/main/resources/contacts-app-translations/messages_en.json
[ContactsAppDefinedLabelsTestMode]: https://bo.wix.com/petri/experiments/272685
