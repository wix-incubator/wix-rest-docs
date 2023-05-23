# About Custom Fields

The Custom Fields feature allows an app to extend the objects used by Wix's APIs with additional fields. You can use these fields to store information that isn't supported by the object's schema. Custom fields are added to an app in the Wix Dev Center. Once custom fields are added for a particular object, they can be read and written using that object's API endpoints. This article explains how to add custom fields to an app and the details of reading and writing custom fields using APIs.

> **Note:** Not all the API objects support custom fields. If an object or endpoint supports custom fields, the following message is displayed in the API Reference: `This API supports custom fields. To use this feature, set it up in the Wix Dev Center. ` <!--TODO - Finalize the snippet/tag with Wix Docs -->

## Add custom fields to an app

To add custom fields for an API object to an app, follow these steps:

1. Open the [Wix Dev Center](https://dev.wix.com/apps/) and select the app you want to add custom fields to.
1. In the sidebar on the left, click **Components**.
1. Hover over **Add Component** and select **Integration Component**.
1. Select **Data Extension** and click **Add Component**.
1. If this is the first time you're adding custom fields to the app, you're prompted to create a namespace for the app. This namespace is used when reading and writing any custom fields created for the app.  
   > **Note:** Once a namespace is created, it can't be changed.
1. Choose the object you want to add custom fields to and click **Choose Entity**.
1. Use the **JSON Editor** to define the custom fields you want to add the object in [JSON Schema](#json-schema) format.  
   The editor's linter indicates if there are any errors in the JSON Schema.
1. Once your custom fields are defined, click **Save**.  
   > **Important:** Once you add a custom field to an app, it can't be removed. You can [archive](#x-wix-archive) a custom field to prevent it from being read or written using the API.

## Read and write custom fields
Once you add custom fields to an app, you can read and write them using the API endpoints for the object. In both cases, custom fields are added to the main object using the `customFields` property. This property contains a `namespaces` object that contains the custom fields for each namespace. The namespace is the app's namespace that was created when the custom fields were added to the app. For example:
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

### Read
To read custom field data, use the same API endpoint used to retrieve object you extended. 

### Write
The endpoint used to write custom fields may be different depending on the object you extended. There are 2 possible options, unified endpoint and dedicated endpoint.

> **Note:** To delete the value of a custom field, set its value to `null`.

#### Unified Endpoint
If the object you extended has a unified endpoint, you can write custom field data using the same API endpoint used to write the object you extended. The custom fields are written to the `customFields` property of the object, as in the example above.

#### Dedicated Endpoint
In some cases, there is a dedicated API endpoint for updating custom fields. These endpoints may require a permission scope that's different from the scope required to update the object itself.

To check if there is a dedicated endpoint for updating your custom fields, see the API Reference for the object you are extending.


## JSON Schema
Custom fields are defined using a subset of [JSON schema](https://json-schema.org/). There are some general restrictions on the JSON schema to keep in mind when defining custom fields:
+ Max stored data size : 10000 Bytes
+ Custom field schemas can't contain more than 256 properties.
+ The maximum length of a property key is 64 characters.
+ Property keys must start with a letter and can contain only letters, bnubers, and underscores.
+ The maximum storage size for an individual custom field object is 10 KB. This size is calculated based on the properties defined in the object's schema including the maximum lengths of all strings and the maximum items of all arrays.

The custom fields feature supports all the basic JSON schema types with some restrictions, as follows:

### String
The `string` type is used to define a JSON schema [string](https://json-schema.org/understanding-json-schema/reference/string.html#string). Please note the following restrictions to the `string` definition:
+ [Length](https://json-schema.org/understanding-json-schema/reference/string.html#length): Strings must be between 1 and 10000 characters long. The maximum length of a custom string field must be defined.
+ [Format](https://json-schema.org/understanding-json-schema/reference/string.html#format): The following formats are supported:
    + [Hostnames](https://json-schema.org/understanding-json-schema/reference/string.html#hostnames)
    + [Resource identifiers](https://json-schema.org/understanding-json-schema/reference/string.html#resource-identifiers)
    + [Dates](https://json-schema.org/understanding-json-schema/reference/string.html#dates-and-times). Only `date`, `date-time`, and `time` values are supported.
    + `single-line`: A custom Wix value. By default, all `string` custom fields are considered multi-line text. This format indicates a field that can only contain a single line of text. The string must end with a newline character (`\n`).
       > **Note:** If a string is defined as `single-line`, the format can be removed later. However, if a string is created as multi-line text, the format can't be changed later to `single-line`.

### Numeric types
The `number` and `integer` types are used to define a JSON schema [numeric type](https://json-schema.org/understanding-json-schema/reference/numeric.html#numeric). The minimum value for a numeric custom field is -2^53 + 1 and the maximum value is 2^53 + 1.

### Object
The `object` type is used to define a JSON schema [object](https://json-schema.org/understanding-json-schema/reference/object.html#object). Please note the following restrictions to the `object` definition:
+ `object` fields must contain a `properties` object that defines the properties of the object. 
+ The items in the properties object must follow the all the restrictions of the other custom field types. 
+ There is maximum of 10 nesting levels for an object.

### Array
The `array` type is used to define a JSON schema [array](https://json-schema.org/understanding-json-schema/reference/array.html#array).  Please note the following restrictions:
+ `array` fields must contain an `items` object that defines the items in the array.
+ The items in the array must follow the all the restrictions of the other custom field types.
+ [Length](https://json-schema.org/understanding-json-schema/reference/array.html#length): The maximum length of an array is 100 items. The maximum number of items of an array field must be defined.
+ All the items in an array must be the same type.
+ Arrays can only contain items of these types: `string`, `number`, `integer`, and `boolean`.


### Boolean
The `boolean` type is used to define JSON schema [boolean](https://json-schema.org/understanding-json-schema/reference/boolean.html#boolean). There are no restrictions on the `boolean` type object.

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
This keyword is used to define the permissions required to read and write a custom field. This keyword is required for all custom fields. The value of this keyword is an object that defines read and write permissions separately. For example:
```json
"x-wix-permissions": {
  "read": ["apps", "users", "users-of-users"],
  "write": ["apps", "users"]
}
```
The supported permissions values are as follows:
+ `apps`: Other apps installed on a site together with the app that defines the custom field.
+ `users`: The owners of sites that have the app installed.
+ `users-of-users`: A site owner's site members.

#### `x-wix-archive`
This keyword is used to archive a custom field. The value of this keyword is a boolean. Once a custom field is archived, it can't be read or written using the API. If an archived custom has nested fields, the nested fields are also archived. To unarchive a custom field, change the value of this keyword to `false` or remove it from the schema. 

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

### Example custom field schema
Here is an example of a custom field schema that defines `firstName`, `lastName`, and `age` properties.
```json
{
  "firstName": {
    "type": "string",
    "description": "The person's first name.",
    "x-wix-permissions": {
      "read":["apps"],
      "write":["users"]
    },
    "title":"First Name",
    "maxLength": 20
  },
  "lastName": {
    "type": "string",
    "description": "The person's last name.",
    "x-wix-permissions": {
      "read":["apps"],
      "write":["users"]
    },
    "title":"Last Name",
    "maxLength": 20
  },
  "age": {
    "description": "Age in years which must be equal to or greater than zero.",
    "type": "integer",
    "minimum": 0,
    "x-wix-permissions": {
      "read":["apps"],
      "write":["users"]
    },
    "title":"Age",
    "maxLength": 20
  }
}
```