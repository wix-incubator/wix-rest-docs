SortOrder: 2
# The Payload Schema

When you configure your app's triggers, you must provide a payload schema.
The payload schema defines the required and validated fields
in your event payloads,
and it's used to display available options to your users
when they configure their automations.

A payload schema allows you to define scheduled events
and can give your users enriched payloads
by linking your trigger to a site contact.
Wix also uses the payload schema
to determine the available actions for a trigger.

The payload schema must be a
[JSON Schema](https://json-schema.org/) object.
See the tables below for the expected structure.

<blockquote class="tip">

__Tip:__
To create a starter schema with sample values and required properties,
use the **Convert from Payload** option.
You can then fill in the rest of the schema as needed.

![Screen shot of the "Configure the payload schema" section of the trigger configuration page. The "Convert from Payload" button is highlighted.](https://s3.amazonaws.com/wixplorer-readme-images/triggered-events%2Fautomations__json-schema-convert-from-payload.png)

</blockquote>

## Schema properties

These properties are at the schema's root level.

| Property               | Data type | Description                                                                                                                                                                 |
| ---------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$schema`              | string    | When you save the trigger configuration, Wix overrides this property to set it to `"http://json-schema.org/draft-07/schema"`.                                               |
| `type`                 | string    | _Required_. Must be `"object"`.                                                                                                                                             |
| `properties`           | object    | _Required_. Object containing payload property metadata as key-object pairs. See [the `properties` object](#the-properties-object) below for details.                       |
| `required`             | array     | List of property keys that are required to be present in the [reported event](https://dev.wix.com/api/rest/wix-automations/triggered-events/report-event) payload.          |
| `additionalProperties` | boolean   | When you save the trigger configuration, Wix overrides this property to set the value to `true`, which allows additional, unspecified properties to be sent in the payload. |

## The `properties` object

`properties` is an object that contains key-object pairs.

The key name can include only alphanumeric characters or underscores
(`A-Z`, `a-z`, `0-9`, `_`).
It cannot start with an underscore.

The paired object contains display and validation metadata.
This table gives the expected data structure:

| Property       | Data type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`         | string    | <p>Supported values: `string`, `number`, `integer`, `boolean`, `array`, `object`.</p> <p>_Required_. Expected data type of the payload property.</p> <p>**Note**: Only the 1st-level `properties` object supports `"object"` and `"array"` types.</p>                                                                                                                                                                                                                                                                                                         |
| `title`        | string    | _Required_. Display name for the property. Shown to users when they create or edit an automation.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `examples`     | array     | <p>Example values, displayed as placeholders when users test certain automation actions. Must be the same data type defined in `type`.</p> <p>Required in the 1st-level `properties` object. Omitted in the 2nd-level `properties` object.</p>                                                                                                                                                                                                                                                                                                                |
| `format`       | string    | <p>Validated string format. Used only when `type` is `"string"`. See [built-in formats](https://json-schema.org/understanding-json-schema/reference/string.html#built-in-formats) (from the JSON Schema 2020-12 docs) for supported formats.</p> <p>If set to `"uuid"`, the property can be connected to a site's contacts. This allows Wix to enrich the payload with contact data and allows the site owner to use actions that work with their contacts.</p> <p>If set to `"date-time"`, the property can be used to add support for scheduled events.</p> |
| `identityType` | string    | <p>Supported value: `contact`</p> <p>If the property is specified with **Connect a property to a contactId**, `identityType` is automatically set to `"contact"`. In all other cases, `identityType` is omitted.</p> <p>Limited to 1 payload property.</p>                                                                                                                                                                                                                                                                                                    |
| `futureDate`   | boolean   | <p>If the property is specified with **Allow scheduled events with predefined date & time**, `futureDate` is automatically set to `true`. In all other cases, `futureDate` is omitted.</p> <p>Limited to 1 payload property.</p>                                                                                                                                                                                                                                                                                                                              |
| `items`        | object    | <p>Object that contains a list of array items.</p> <p>Required if `type` is `"array"`. Omitted for other data types. See [the `items` object](#the-items-object) below for details.</p>                                                                                                                                                                                                                                                                                                                                                                       |
| `properties`   | object    | <p>Object containing 2nd-level payload property metadata as key-object pairs. Accepts the same data as the 1st-level `properties` object, but can contain only strings, numbers, integers, or booleans.</p> <p>Required if `type` is `"object"`. Omitted for other data types.</p>                                                                                                                                                                                                                                                                            |
| `required`     | array     | <p>List of property keys that are required to be present in the [reported event](https://dev.wix.com/api/rest/wix-automations/triggered-events/report-event) payload.</p> <p>Used only  when `type` is `"object"` or `"array"`.</p>                                                                                                                                                                                                                                                                                                                           |

## The `items` object

`items` is an object that contains an array schema.

| Property     | Data type | Description                                                                                                                                                                                                                                                                               |
| ------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`       | string    | _Required_. Must be set to `"object"`.                                                                                                                                                                                                                                                    |
| `properties` | object    | _Required_. Object containing 2nd-level payload property metadata as key-object pairs. Accepts the same data as the 1st-level `properties` object. See [the `properties` object](#the-properties-object) above for details. |
| `required`   | array     | List of property keys that are required to be present in the [reported event](https://dev.wix.com/api/rest/wix-automations/triggered-events/report-event) payload.                                                                                                                        |
