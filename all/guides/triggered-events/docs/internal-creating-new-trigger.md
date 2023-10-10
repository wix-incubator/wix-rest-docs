SortOrder: 1
# Creating a New Automations Trigger in the Dev Center

[New doc](https://docs.google.com/document/d/1mSX6ufmSlQXCunb2yOuXXN6nEw2qMk8DbO5hChdb_Yo/edit)

> **TODO:** Add general information about automations and the general flow:

To learn more about Wix Automations please review this KB and our documentation

## Recommended: Prerequisites before creating a new trigger

1. Implement a call to `[reportEvent](https://bo.wix.com/wix-docs/rest/drafts/esbconfigresolver)` in your app, whenever your trigger event occurs.

    For non-wix apps, use this url:

    ```txt
    ​​​​https://wixapis.com/automations/v1/events/report
    ```

    If wix apps, you can find the `reportEvent` call under this ambassador package:

    `​​@wix/ambassador-automations-esb-v1-report-event-result`.

    Please note that you will need to sign with your appDefId and with the metaSiteId of the site where the event has happened.

    > __Important__:
    > Please note that your app must have this permission (Can be added in Dev Center): `​​AUTOMATIONS.REPORT_EVENT`

2. Have an SPI implementation for [TriggerProviderService](https://bo.wix.com/wix-docs/rest/drafts/trigger-spi-provider/)

    If you’re not familiar with SPI implementations in Wix - general information about SPIs can be found [here](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/spi---service-provider-interface).

    Please note that if your project is a loom-prime project,
    `@wix_automations//trigger-spi-provider/src/main/proto`
    should be added in the `proto_deps` in `BUILD.bazel`.

    The relevant endpoints to implement in TriggerProviderService are `validateConfiguration` and `getDynamicSchema`.

    - `validateConfiguration`:
      The purpose of validateConfiguration is to have the ability to alert users with wrong trigger configuration.

      For example - if a trigger should be fired whenever a purchase is being made, and a user adds a filter so that an automation with this trigger will run only when a **specific** product is purchased - We will want to verify this specific selection is valid whenever the user enters his automations page.
      but that product does not exist anymore - validateConfiguration should return ‘false’ and Automations will alert the user that their automation will always fail to run.
      If your trigger does not have any dynamic filters - You can safely return ‘true’ for every input.
    - `getDynamicSchema`: More information about this endpoint can be found in the [Trigger Filters](#trigger-filters) section

3. Make sure your app / product has a logo

    When opening your app in the dev center, you will need to add your logo. This logo will be used in the automation wizard, recipes, preview panel and more.   
    For general guidelines on [App Market Listing](https://devforum.wix.com/kb/en/article/create-your-app-market-listing#app-icon)

    - **For non-wix apps**:
      Upload a square, 1000 x 1000 px icon in JPG or PNG format.
    - **For Wix apps**:
      If you don’t already have a logo, you will need to submit [this form](https://forms.monday.com/forms/77008a2b0a92868ea48fdc4869bcb4ef?r=use1) to Wix design system.

To view your triggers and create a new one, use this link:

```txt
https://dev.wix.com/apps/{YourAppId}/automations
```

## Shorter version: Step-by-step guide for creating a new automation trigger

- Before starting - please make sure that your Dev Center app has a logo - as it will be used in our automations page. 
- Enter this url (replace `{YourAppId}` with your appId:

  ```txt
  https://dev.wix.com/apps/{YourAppId}/automations
  ```

- ‘Create a Trigger’

### Enter your trigger details

- Trigger Name and Description will be shown to site owners when creating new automations.
- Trigger key is your trigger identifier. It must be a lower case slug, unique per app. It will be used when reporting the trigger in `reportEvent`. (//TODO: Add link to docs)
- Your SPI baseUrl - Please make sure you have an implementation for [TriggerProviderService](https://github.com/wix-private/wix-automations/blob/master/trigger-spi-provider/src/main/proto/com/wixpress/esb/spi/trigger/v1/trigger_spi_provider.proto).

### Test your trigger & auto-generate a json schema for your trigger payload

- To test your trigger, please select a site in which your app is installed, and ‘Start Listening’. Go and trigger your event (Wix apps can use [Fire Console](https://pbo.wix.com/fire-console/?artifact=com.wixpress.automations.esb.resolver.esb-config-resolver&service=wix.automations.esb.resolver.v1.EsbConfigResolver&method=ReportEvent&body=eyJ0ZW5hbnRfaWQiOiIiLCJ0cmlnZ2VyX2tleSI6IiJ9) to mock your call. Don’t forget to sign with your appDefId and the msid of the selected site.)
- You will be able to see your trigger payload and create a json schema that represents your payload. Please make sure that all of the information you want to be available for actions, is part of your payload.

### Create a payload json schema for your trigger payload

- Whether you start from scratch or use our auto-generated payload json schema, please note that we expect a v7 json schema, all properties must have titles, the only complex type allowed is an array of objects, where all of the objects contain only primitive values. 
- If you want to pass an identity uuid, please make sure that the field type is marked as ‘string’, and the format is ‘uuid’.
- If your trigger refers to a [future event](#bookmark=id.ms2spcr1p7my), please mark the relevant dateTime field as a future date.
- To prevent breaking changes, not all trigger details are editable. For more information, please read [this section](#bookmark=id.kfgneryjezfd).

### If needed - set possible filters for your trigger

Let your users set filters for specific properties from your schema. A filter example could be - trigger this automation only when the ‘formId’ property from the payload is ‘form-id-123’. For more information please read the [trigger filters section](#bookmark=id.8gpx0qzibq11).

## Longer version: Creating the trigger in Dev Center

### General trigger settings to configure:

When creating a new trigger, these are the details you’ll be required to fill:

- Trigger Name - The display name that will be shown to users as the trigger identifier. Max length - 50 characters. 
- Trigger Description - A description of the trigger event. Max length - 250 characters.
- Trigger Key - Not visible to users. Can only be a slug with lower letters, numbers, _, or -. This is the identifier of the trigger that would be sent in the `reportEvent` request. The same application cannot have 2 triggers with the same trigger key. Cannot be edited after the trigger is created.
- SPI Base URI - The uri under which `validateConfiguration` is implemented, for more details please read [this](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/spi---service-provider-interface#platformization-guidelines_spi---service-provider-interface_wixspibase_uri) documentation. Cannot be edited after the trigger is created.
- ‘Don’t let users create…’ checkbox - In case your want your trigger to be hidden from all users (For example if its only used in some hidden Application Automation), please check this checkbox.

### Configuration test (Recommended but not mandatory)

After filling in the basic details, you’re advised to visit the test section, the test has 2 purposes:

- Verify that your trigger is being reported correctly.
- Build a [trigger schema](#bookmark=id.cv268fp0crg6) out of your payload.

To test your trigger, you’ll first need to select a site that has your app installed,
and ‘Start Listening’ to your event.

After that, you’ll have to trigger your trigger (reportEvent) in your application, in the context of the site you’ve selected.

(Wix apps only) - In case the call to reportEvent is not yet implemented, you can use [Fire Console](https://pbo.wix.com/fire-console/?artifact=com.wixpress.automations.esb.resolver.esb-config-resolver&service=wix.automations.esb.resolver.v1.EsbConfigResolver&method=ReportEvent&body=eyJ0ZW5hbnRfaWQiOiIiLCJ0cmlnZ2VyX2tleSI6IiJ9) to mock your call. Don’t forget to sign with your appDefId and the msid of the selected site.

If all is well - you should see your requests in the table, with all of the different payloads you might have sent. Choose an entry with a payload that represents what will be sent for all triggers and press ‘Convert to Schema’ to proceed to the final stage.

After you convert to a schema, please go over the auto-generated schema and make sure all types, titles, and other information are correct and as you expected. 

### Building your trigger payload schema

The payload schema is the json that represents the payload that will be sent every time the trigger is triggered. It is written in [jsonSchema](https://json-schema.org/) format - if you’re not familiar with it, it’s recommended to read the docs.

It is important that you declare all relevant payload properties when creating the trigger, as the editing capabilities of this schema are limited (Read more [here](#bookmark=id.kfgneryjezfd)).

If you’ve used the configuration test section, a skeleton of your payload json schema should already exist in the json editor, if not - you’ll need to provide one from scratch.

> __Important:__  
> It is expected that the schema will be written in [draft-07](https://json-schema.org/draft-07/json-schema-release-notes.html) version, Please make sure that the `"$schema"` property has the following value:
> 
> ```txt
> "[http://json-schema.org/draft-07/schema](http://json-schema.org/draft-07/schema)"
> ```

The most important part of the payload schema is the `properties` property, which gives information on all properties sent in the trigger payload. Each property has the following information:

- **Property key**: The property key must include only english letters (lower/upper), numbers, or an underscore (‘_’). The key must not start with an underscore.
- **Type**: should be either a primitive type (string, number, integer) or an **array**. If the type is an array - all of its items should be on type **object**, and inside that object, all types should be primitives. This field is mandatory.
- **Format**: when your property is of type ‘string’, you can specify further what kind of string is it - options include but not limited to - `email`, `uuid`, `date-time` and `uri`
- **Title**: The visible name of the property, shown to users when defining automations. This field is mandatory.
- **Default**: default value to if the property is not sent.
- **Example**: An example of the value, may be shown to users. This field is mandatory.
- **identityType**: If one of your payload fields represents a Wix identity, you can mark it using this property. **It is important to specify your entities** as it enriches the payload with relevant information and enables more actions to be connected with your trigger.

    > __Important:__
    > You can only specify identityType for properties that are of type ‘string’ and of format ‘uuid’.

    The valid values for identityType are ‘contact’/’visitor’/’member’.

    If you mark one of your fields as ‘contact’ - The payload that would be passed to the action will include all of that contact’s information - Including name, mail, and address.

    As for now, there is now special enrichment for visitors and members.

- **futureDate**: For more information about this property, please read the
  [Future Events](#future-events) section.

Another important property is the **required** property. Here we specify all property keys that are required for the trigger to be active, meaning that if one of them is not sent - **the automation will not run.**

additionalProperties - is the option to send unknown properties with the payload, that are not defined in this schema. This is always enabled.

Example:

If the payload that is being sent when you reportEvent for your trigger is:

```json
{
  "formId": "60d2cd50-1047-4164-884d-8c24fbda84bb",
  "formName": "My Cool Form",
  "submitterId": "1234-abcd-1234-abcd"
}
```

The corresponding payload schema could be:

```jsonc
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "type": "object",
  "title": "Visitor submits a form Payload Schema",
  "description": "The schema of the payload that is part of the triggered event",
  "default": {},
  "examples": [{
    "formId": "60d2cd50-1047-4164-884d-8c24fbda84bb",
    "formName": "My Cool Form",
    "submitterId": "1234-abcd-1234-abcd"
  }],
  "properties": {
    "formId": {
      "$id": "#/properties/formId",
      "type": "string",
      "format": "uuid",
      "title": "Form ID",
      "description": "The form identifier",
      "default": "",
      "examples": ["60d2cd50-1047-4164-884d-8c24fbda84bb"]
    },
    "formName": {
      "$id": "#/properties/formName",
      "type": "string",
      "title": "Form Name",
      "description": "The form display name",
      "default": "",
      "examples": ["My Form"]
    },
    "submitterId": {
        "$id": "#/properties/submitterId",
        "type": "string",
        "format": "uuid",
        "title": "Submitter Id",
        "description": "The Id of the contact which submitted the form",
        "default": "",
        "identityType": "contact", // can be contact, visitor, user limited to 1 type per identity
      }
  },
  "required": ["formId", "formName", "submitterId"],
  "additionalProperties": true
}
```

//TODO: Replace with new naming once it’s decided

### Future events

A future event is an event that is **reported** at a specific point in time, but **triggered** at another point in the future.

An example for this use case is a trigger called ‘Invoice is overdue’ - a trigger that is sent to a UoU whenever an invoice is overdue (Usually shortly before - this is configurable by the user).

The reportEvent for this trigger would happen whenever an invoice is **created**, but the actual activation of the automation would be whenever the invoice is overdue.

To achieve that - You’re required to mark a specific field in the payload schema as a ‘futureDate’ - in our example that field would be the overdue date of the invoice. This date is the date that will be referred to when the automation is created.

This is how it would look in your payload json schema:

```json
"overdueDate": {
    "$id": "#/properties/overdueDate",
    "type": "string",
    "futureDate": true,
    "format": "date-time",
    "title": "Overdue Date",
    "default": "",
    "examples": ["2023-07-12T16:06:37+0000"],
},
```

> __Important:__
>
> - The property that is defined as a future date must be of type ‘string’ and format ‘date-time’.
> - There can only be one future date per trigger.
> - To cancel a future event (For example - the invoice from our example was **paid**, making the ‘invoice overdue’ trigger not relevant), please use `[cancelEvent](https://bo.wix.com/wix-docs/rest/drafts/esbconfigresolver/cancel-event)`.

### Trigger Filters

Note - Currently the only way to create filters is registering as a Pikachu provider. For more information please read [Pikachu’s docs.](https://github.com/wix-private/pikachu/blob/master/docs/business_manager_providers.md)

Trigger filters are predefined conditions for on your payload properties that will be suggested to your users upon Automation creation. These filters allow the user to choose which specific cases (Currently - on what specific entities) the automation will run in.

For example, for the ‘User submits a form’ trigger, we could define a filter based on the ‘formId’ property, that will allow users to enable the Automation only for specific forms.

Information needed to define a trigger filter:

Item selection label - The label presented to the user while creating an automation with your trigger. For example ‘Select which forms activate this automation’ (It is recommended to keep this format). This label is translatable. 

Selection method - Multi/single select.

Item FQDN - The entity id that is correlated with the property the trigger should be filtered by. (When integrating with Pikachu - this is the id you set as the provider.) 

Item property from schema - Each filter is linked to a specific property from your payload (In our example - formId). Please make sure that you select the correct property (The one correlated to your item FQDN), or else your filter will not work properly.

Reevaluate the schema for dynamic properties - Check this checkbox if your payload contains dynamic properties based on the filter selection.

For example - if for specific forms, you also want to include form fields in the trigger payload, check this checkbox, and whenever the user makes a filter selection, the `getDynamicSchema` SPI endpoint will be called and we will receive an additional json-schema representing the new dynamic payload fields. For more information, please review [`getDynamicSchema` documentation.](https://bo.wix.com/wix-docs/rest/drafts/trigger-spi-provider/get-dynamic-schema)

### Testing your trigger in the dashboard

After you’ve configured your payload schema, you can now create your trigger and test it E2E. Find the relevant trigger in the triggers table and press ‘Test’ - choose a site where you have your app installed, and you’ll be redirected to the Automations wizard, and will be able to create a new automation with your newly created trigger.

- Please use this experiment - `specs.crm.AutomationsUseV2API`
- (This part is only relevant for non Wix apps) To test your trigger, you’ll first need to have your app installed in ‘test’ mode. To do that, use the ‘Test your app’ button in the Dev Center. You can either choose to create a test site with your app installed, or to install your app in test mode in some specific site.

### Editing your trigger

After you’ve created and published your trigger, you are able to edit some parts of it. (Before publishing - you  are still able to edit all of the trigger configuration)

Things that **you will be able to change** in edit mode are:

- Trigger name.
- Hidden trigger - Make a hidden trigger visible.
- Hidden trigger - Make a visible trigger hidden. (This will **deprecate **your trigger)
- Payload schema - add a new **non required** field.
- Payload schema - change a field's display name.
- Payload schema - change a field's description.
- Payload schema - add a new identityType - if that identityType isn’t already assigned to another property.
- Payload schema -  Render a field that was required -> **non-required.**
- Payload schema -  Render a field that was non-required -> **required.**
- Trigger filters - add filters to triggers.
- Trigger filters - Change filter label.
- Trigger filters - Change filter identifier (FQDN).
- Trigger filters - Change ‘Reevaluate Schema’ checkbox.

Things that **you won’t be able to change** in edit mode are:

- Trigger key.
- SPI base url.
- Payload schema -  delete an existing field.
- Payload schema -  change a field’s id.
- Payload schema -  change a field’s type.
- Payload schema -  change a field’s format.
- Payload schema -  remove / switch an identityType.
- Payload schema -  remove / add a futureEvent indication.
- Trigger filters - remove filters from triggers.
- Trigger filters - change filter property.
- Trigger filters - change multi select to specific select and vice versa.

### Summary of when each endpoint is being called

We will differentiate between **edit time** and **run time**.

- **Edit time**: The point in time where a user is within Automations page in BM, and creates/edits his automations.

  Whenever a user focuses on an automation that has your trigger in it - **validateConfiguration** will be called with the automation configuration (For trigger that means - all the filter selections the user has made).

  Whenever a user makes a selection of a trigger filter, **getDynamicSchema** will be called (Assuming the filter has ‘Reevaluate schema’ checkbox checked in its definition).

- **Run time**: After an Automation was created - this is the point in time where a trigger is being fired, and an action is being invoked.

  This whole process starts when an application calls us with **reportEvent**.

-->
