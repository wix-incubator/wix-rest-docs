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

Now you should see the following form:
![](https://static.wixstatic.com/media/5cd5e7_05c9c3907be24a0ba55fdb428ee48d43~mv2.png)

You need to create a namespace for your app defined labels with display name for the UI (can be translated)
Under this namespace there are going to be system labels or app defined labels or both.

`System labels` are always part of the labels of the site, they cannot be deleted.

`App defined labels` can be modified, you can choose to restrict the modification permission to specific app, set a required permission, or both.

* In order to have system labels you must add them in the form.

* In order to allow creation of app defined labels - you must check the checkbox in the form.

Once you submit this form, the label app component is in `DRAFT` mode and waiting to be `APPROVED` by dev-center team to appear in production,
if you want to be able to see it in your site even when it's `DRAFT` read [specs](#specs)

### Specs 
To be able to easily test your app defined labels you can override the following specs: 
* Turn on [ContactsShouldUseAppDefinedExtensions][ContactsShouldUseAppDefinedExtensions] - for the app defined labels to be available
* Turn on [ContactsAppDefinedLabelsAllowDraft][ContactsAppDefinedLabelsAllowDraft] - in order to return also `DRAFT` app defined labels
* Turn on [ContactsAppDefinedLabelsNotInstalled][ContactsAppDefinedLabelsNotInstalled] - in order to show your app defined labels also on sites that don't have the app installed.
* New app defined labels will be shown after 15 minutes from creation time, Turn on [ContactsAppDefinedLabelsSkipCache][ContactsAppDefinedLabelsSkipCache] - to show it immediately.

### Translation
The default language supplied in the form is english,
currently the only way to supply additional languages is by submitting a PR to [contacts translation file][messages_en].  
You can translate namespace display name by adding a new row to the file with the following format:

`"label.namespace.[your_namespace_key]": "[your_namespace_display_name]"`

You can translate system label display name by adding a new row to the file with the following format:

`"label.namespace.[your_namespace_key].[your_system_label_key]": "[your_system_label_display_name]"`

[dev-center]: https://dev.wix.com
[messages_en]: https://github.com/wix-private/crm/blob/master/contacts/common/src/main/resources/contacts-app-translations/messages_en.json
[ContactsShouldUseAppDefinedExtensions]: https://bo.wix.com/petri/experiments/133332
[ContactsAppDefinedLabelsAllowDraft]: https://bo.wix.com/petri/experiments/133335
[ContactsAppDefinedLabelsNotInstalled]: https://bo.wix.com/petri/experiments/133336
[ContactsAppDefinedLabelsSkipCache]: https://bo.wix.com/petri/experiments/133333
