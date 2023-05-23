# About Custom Fields

The Custom Fields feature allows an app to extend the objects used by Wix's APIs with additional fields. You can use these fields to store additional information that isn't supported by the object's schema. Custom fields are added to an app in the Wix Dev Center. Once custom fields are added for a particular object, they can be read and written using that object's API endpoints. This article explains how to add custom fields to an app and the details of reading and writing custom fields using APIs.

> **Note:** Not all the API objects support custom fields. If an object or endpoint supports custom fields, the following message is displayed in the API Reference: `This endpoint supports custom fields.` <!--TODO - Finalize the snippet/tag with Wix Docs -->

## Add custom fields to an app

You can add custom fields to your app in the Wix Dev Center. To do this, follow these steps:

1. Open the [Wix Dev Center](https://dev.wix.com/apps/) and select the app you want to add custom fields to.
1. In the sidebar on the left, click **Components**.
1. However over **Add Component** and select **Integration Component**.
1. Select **Data Extension** and click **Add Component**.
1. If this is the first time you're adding custom fields to the app, you're prompted to create a namespace for the app. This namespace is used to group all the custom fields for an app together in the extended object.  
   > **Note:** Once a namespace is created, it can't be changed.
1. Choose the object you want to add custom fields to and click **Choose Entity**.
1. Use the **JSON Editor** to define the custom fields you want to add the object in [JSON Schema](#json-schema) format.  
   The editor's linter indicates if there are any errors in the JSON Schema.
1. Once your custom fields are defined, click **Save**.  
   > **Important:** Once a custom field is added to an app, it can't be removed. You can archive a custom field, but it remains available to read using the API.

## Read and write custom fields
Once you add custom fields to an app, you can read and write them using the API endpoints for the object.

### Read
To read custom field data, use the same API endpoint used to retrieve object you extended. The custom fields appear in the objects `customFields` property. This propery has a property called `namespaces` which is an object containing keys corresponding to the namespaces of your apps that have custom fields defined for the object. The value of each key is an object containing the custom fields defined for that namespace. For example:
```json
{
    "customFields": {
        "namespaces": {
            "@my-name/app1": {
                "myCustomField": "my custom field value"
            },
            "@account-name/app2": {
                "myOtherCustomField": "my other custom field value"
            }
        }
    }
}
```

### Write
Two create or update custom fields, add the new field data using the following format:
```json
{
    "customFields": {
        "namespaces": {
            "@my-name/app1": {
                "myCustomField": "my new custom field value"
            },
            "@my-name/app2": {
                "myOtherCustomField": "my other new custom field value"
            }
        }
    }
}
```

The endpoint used to write custom fields may be different depending on the object you extended. There are 2 possible options, Unified Endpoint and Dedicated Endpoint.

#### Unified Endpoint
If the object you extended has a unified endpoint, you can write custom field data using the same API endpoint used to write the object. The custom fields are written to the `customFields` property of the object, as in the example above.

#### Dedicated Endpoint
In some cases, there is a dedicated API endpoint for updating custom fields. This endpoint is used to update the custom fields for an object without updating the object itself. These endpoints may require a permission scope that's different from the scope required to update the object itself.

To check if there is a dedicated endpoint for updating your custom fields, see the API Reference for the object.



## JSON Schema
Custom fields are defined using a subset of [JSON schema](https://json-schema.org/). Custom fields supports all the basic JSON schema types with some restrictions.

### String
The `string` type is used to define a custom field that contains a [JSON schema string](https://json-schema.org/understanding-json-schema/reference/string.html#string) value. Please note the following restrictions to the `string` type object:
+ [Length](https://json-schema.org/understanding-json-schema/reference/string.html#length): Strings must be between 1 and 10000 characters long. The maximum length of a custom string field must be defined.
+ [Format](https://json-schema.org/understanding-json-schema/reference/string.html#format): The following formats are supported:
    + [Hostnames](https://json-schema.org/understanding-json-schema/reference/string.html#hostnames)
    + [Resource identifiers](https://json-schema.org/understanding-json-schema/reference/string.html#resource-identifiers)
    + [Dates](https://json-schema.org/understanding-json-schema/reference/string.html#dates-and-times). Only `date`, `dater-time`, and `time` values are supported.
    + `single-line`: A custom Wix value. By default, all `string` custom fields are considered multi-line text. This format indicates a field that can only contain a single line of text. The string must end with a newline character (`\n`).
       > **Note:** If a string is defined as `single-line`, the format can be removed later. However, if a string is created as multi-line text, the format can't be changed later to `single-line`.

### Numeric types
The `number` and `integer` types are used to define a custom field that contains a [JSON schema numeric type](https://json-schema.org/understanding-json-schema/reference/numeric.html#numeric) value. Please note the following restrictions to the `number` and `integer` type ojbects:
+ [Range](https://json-schema.org/understanding-json-schema/reference/numeric.html#range): The minimum value for a numeric custom field is -2^53 + 1 and the maximum value is 2^53 + 1.

### Object
The `object` type is used to define a custom field that contains a [JSON schema object](https://json-schema.org/understanding-json-schema/reference/object.html#object) value. Custom fields that are defined as `object` must contain a `properties` object that defines the properties of the object. The items in the properties object must follow the all the restrictions of the other custom field types. There is maximum of 10 nesting levels for an object.

### Array
The `array` type is used to define a custom field that contains a [JSON schema array](https://json-schema.org/understanding-json-schema/reference/array.html#array) value. Custom fields that are defined as `array` must contain an `items` object that defines the items in the array. The items in the array must follow the all the restrictions of the other custom field types. Please note the following restrictions:
+ [Length](https://json-schema.org/understanding-json-schema/reference/array.html#length): The maximum length of an array is 100 items.
+ All the items in an array must be the same type.
+ Arrays can only contains items of these types: `string`, `number`, `integer`, and `boolean`.


### Boolean
The `boolean` type is used to define a custom field that contains a [JSON schema boolean](https://json-schema.org/understanding-json-schema/reference/boolean.html#boolean) value. There are no restrictions on the `boolean` type object.

### Global keywords
The following global JSON schema keywords are supported:
+ [Annotations](https://json-schema.org/understanding-json-schema/reference/generic.html#annotations)
+ [Enumerated values](https://json-schema.org/understanding-json-schema/reference/generic.html#enumerated-values)

The following global keywords aren't supported:
+ `required`
+ `$defs`
+ `$ref`
+ `readOnly`
+ `writeOnly`

### Wix-specific keywords
We extended the JSON schema to support the following Wix-specific keywords:

#### `x-wix-permissions`
This keyword defines the permissions required to read and write the custom field. The possible permissions values are `"apps"`, `"users"`, and `"user-of-users"`. This keyword is required for all custom fields. The value of this keyword is an object that defines read and write permissions separately. For example:
```json
"x-wix-permissions": {
    "read": ["apps", "users", "users-of-users"],
    "write": ["apps", "users"]
}
```
To learn more about permissions, see [Custom Field Permissions](#custom-field-permissions).

#### `x-wix-archive`
This keyword is used to archive a custom field. The value of this keyword is a boolean. Once a custom field is archived, it can't be read or written using the API. If an archived custom has nested fields, the nested fields are also archived. To un-archive a custom field, change the value of this keyword to `false` or remove it from the schema. 

For example:
```json
"myCustomField": {
    "x-wix-archive": true,
    "type": "string",
    "maxLength": 100,
    "x-wix-permissions": {
        "read": ["apps"],
        "write": ["apps"]
    },
}
```
#### `x-wix-display`

#### Other limitations
+ Max stored data size : 10000 Bytes
+ Max number of properties: 256
+ Proprty key max length: 64

## Custom field permissions
When defining a custom field, you must specify who has permission to read and write the field. This allows you to define who can see and define custom fields. The different permissions are:
+ `apps`: Other apps installed on a site together with the app that defines the custom field.
+ `users`: The owners of sites that have the app installed.
+ `users-of-users`: A site owner's site members.
