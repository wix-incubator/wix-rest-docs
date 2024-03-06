SortOrder: 2
## About the Action SPI Input Schema

When an automation is triggered, Wix passes data from the trigger payload to your service so it can perform your action. You tell Wix exactly what data your action requires from the trigger by defining the input schema. The input schema is a [JSON Schema](https://json-schema.org/) object that allows you to define the data types your service needs to execute your action. You must provide the input schema for your action when you configure it in the Wix Developers Center.

By default, the fields defined by the schema are statically linked to a field in the trigger payload. This means the data from the payload passes to the input schema and does not require user input. However, you can allow users to input data into the schema by making the input fields dynamic. You can mark an input field as dynamic in the UI schema.

If the trigger payload fields do not match the fields in your input schema, your action will not run when the automation is triggered.

See the tables below for the expected input schema structure.

<blockquote class="tip">

__Tip:__ To create a starter schema using sample values and required properties, use the **Generate from Sample Data** option. You can then fill in the rest of the schema as needed.

</blockquote>

### Schema properties

These properties are at the schema's root level.

The input schema supports [schema composition](https://json-schema.org/understanding-json-schema/reference/combining.html#schema-composition) keywords such as `allOf`, `anyOf`, and `oneOf`. 

<blockquote class="important">

__Important:__
Be aware that Wix does not validate breaking changes to an input schema that uses composition. To ensure the user does not make errors when configuring an action that uses composition in its schema, we recommend performing the validation on your end.

</blockquote>

| Property | Data Type | Description |
| ------ |  ------ | ------ |
| `$schema` | string | When you save the action configuration, Wix overrides this property to set it to `"http://json-schema.org/draft-07/schema"`.
| `type` | string| _Required_. Must be `"object"`.|
| `properties` | object | _Required_. Object containing payload property metadata as key-object pairs. See the [properties](#the-properties-object) object below for details.|
| `required` | array | List of property keys that must be provided to the action service. |
| `additionalProperties` | boolean | When you save the action configuration, Wix overrides this property to set the value to `true`, which allows additional, unspecified properties to be sent in the payload.|

### The `properties` object

The `properties` object contains the key-object pairs that make up the bulk of the data passed to the action. The key name can include only alphanumeric characters or underscores (A-Z, a-z, 0-9, _). It cannot start with an underscore.

Each paired object contains display and validation metadata. This table gives the expected data structure for an object in `properties`:

| Property | Data Type | Description |
| ------ |  ------ | ------ |
| `type` | string | _Required_. Supported values: `"string"`, `"number"`, `"integer"`, `"boolean"`, `"array"`, `"object"`.<br /><br /> Expected data type of the payload property.|
| `title` | string | _Required_. Display name for the property. Shown to users when they create or edit an automation. |
| `examples` | array | Example values, displayed as placeholders when users test certain automation actions. Must be the same data type defined in `type`.|
| `format` | string | Validated string format. Used only when type is `"string"`. See [built-in formats](https://json-schema.org/understanding-json-schema/reference/string.html#built-in-formats) (from the JSON Schema 2020-12 docs) for supported formats.<br /><br />If set to `"uuid"`, the property can be connected to a site's contacts. |
| identityType | string | Supported values: `"contact"`, `"member"`, `"visitor"`.<br /><br />If you add this property to the input schema, the action becomes available for triggers that use `contactID`, and its icon appears in the list of actions available when such a trigger is selected. If you do not add this property, the action is not available for these triggers and does not appear in the possible list of actions. <br /><br />Max: 1 payload property. |
| `items` | object | Required if type is `"array"`. Omitted for other data types. <br /><br /> Object that contains a list of array items. <br /><br />  See the `items` object below for details. |
| `properties` | object | Required if type is `"object"`. Omitted for other data types.<br /><br />Object containing 2nd-level payload property metadata as key-object pairs. Accepts the same data as the 1st-level `properties` object and may contain strings, numbers, integers, booleans, or nested objects.|
| `required` | array | Used only when the type is `"object"` or `"array"`. <br /><br />  List of property keys that must be provided to the action service.|
| `enum` | array | Creates a dropdown list of options you define.|
| `uniqueItems` | boolean | Used only when the type is `"array"`. Allows a field to be added only once to the action configuration UI.|

### The `items` object

`items` is an object that contains an array schema.

| Property | Data Type | Description |
| ------ |  ------ | ------ |
| `type` | string | _Required_. Must be set to `"object"`.|
| `properties` | object | Object containing 2nd-level payload property metadata as key-object pairs. Accepts the same data as the 1st-level properties object, but can contain only strings, numbers, integers, or booleans. See the `properties` object above for details.|
| `required` | array | List of property keys that must be provided to the action service.|

### Editing a saved input schema

Once you publish the action with your app, Wix enforces the following limits on changes you can make to the action's input schema. Once the action is saved, you can't:

+ Add required fields to the schema.
+ Mark existing non-required fields as required.
+ Change a field’s type.
+ Change a field’s format.
+ Remove or change a field’s identity type.

