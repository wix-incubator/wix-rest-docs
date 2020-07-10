SortOrder: 0
# Contact Fields Service Metadata

## What is it?
The "Contact Fields" service is a tool to manage the the set of fields in the context of a given site

Contact List is the place where users can keep track of their leads, customers and anyone else interacting with their site and business, all in one place. 
Users can manually add anyone to their Contact List. These could be people they plan to do business with, subscribers for their newsletter or customers they meet in person.
When adding a contact, users can add their contact information by filling the contact's fields. Some of the fields are predefined and shown by default, while users can also use custom contact fields to collect additional information important to their business.
Custom fields can be either text, number, date or URL and can have any name they choose. Any custom field is added to all contacts in the Contact List (users do not have to fill this field in for every contact).
Check out this [article](https://support.wix.com/en/article/adding-custom-fields-to-contacts) to learn more about Adding Custom Fields to Contacts.

### The Contact Field Entity

A contact field can be used to add extended information on a contact. 
There is a set of built-in (system/predefined) fields, e.g. `TODO example1` or `TODO example2`, and there an option to create a custom (user-defined) field that will apply to each contact.

A custom field can be created by the owner in the contact dashboard (or via this API)

Contact field has the following properties:
- `key` - a read-only property that serves as a unique identifier of each contact field.
  - The key is a friendly id, auto-generated based on the first name of the field
  - User defined fields will be prefixed with "custom."
- `name` - field name - as user sees it. E.g. `First Name`, `E-mail`, etc. Read-only for SYSTEM fields.
- `dataType` - type of data that the fill can contain. Read-only for system fields. Can be one of the following:
    - `TEXT` - stands for textual data
    - `NUMBER` - stands for numeric data
    - `DATE` - stands to TimeStamp data - date only, does not support time resolution
    - `URL` - represents a Web Address
- `fieldType` - a read-only property that defines fields type, can be one of the following values:
  - `SYSTEM` - System predefined
  - `USER_DEFINED` - Defined by the user, i.e. custom fields.
- `namespace` - Defines the namespace for the fields's `key`. (Always `custom` for USER_DEFINED fields).
- `createdDate` - When the field was created.
- `updatedDate` - When the field was last updated.    
    
   

### Example

```json
   {
     "key": "custom.favorite-color",
     "name": "Favorite Color",
     "namespace" : "custom",
     "dataType": "TEXT",
     "fieldType" : "USER_DEFINED",
     "createdDate": "2019-10-10T12:30:56Z",
     "updatedDate": "2020-05-10T07:14:59Z"
   }
```

### Sample Usage
In a *Contact* object:

```json
{
  "id": "8046df3c-7575-4098-a5ab-c91ad8f33c47",
  ...
  "info": {
    ...
    "extendedFields": {
      "custom.favorite-color": "Blue"
    }
  }
}
```