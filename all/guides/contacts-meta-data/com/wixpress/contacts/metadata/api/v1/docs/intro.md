SortOrder: 0
# Contacts Metadata

## What is it?
The "Contacts Metadata" services set is a tool to manage both the contact schema and the set of labels in the context of a given site

## What can users do with it?
Site-Owner / Contributor can manage the contacts schema of the site, create new fields to include additional contact data. 
In addition, Site-Owner / Contributor can create new label in order to group contacts with respect to the Site-Owner considerations

## Contacts Schema Service
Contact List is the place where users can keep track of their leads, customers and anyone else interacting with their site and business, all in one place. 
Users can manually add anyone to their Contact List. These could be people they plan to do business with, subscribers for their newsletter or customers they meet in person.
When adding a contact, users can add their contact information by filling the contact's fields. Some of the fields are predefined and shown by default, while users can also use custom contact fields to collect additional information important to their business.
Custom fields can be either text, number, date or URL and can have any name they choose. Any custom field is added to all contacts in the Contact List (users do not have to fill this field in for every contact).
Check out this [article](https://support.wix.com/en/article/adding-custom-fields-to-contacts) to learn more about Adding Custom Fields to Contacts.

### The Contact Field Entity

A contact field is part of contact schema. There is a set of built-in (system/predefined) fields, e.g. `first_name` or `email`, and there an option to create a custom (user-defined) field that will apply to each contact.

A custom field can be created by the owner in the contact dashboard (or via this API)

Contact field has the following properties:
- `id` - a read-only property that serves as a unique identifier of each contact field.
  -  In the case of built-in fields it will be the same as name.
  - For custom fields it will a system generated random guid.
- `field_type` - a read-only property that defines fields type, can be one of the following values:
  - `BUILT_IN` - System predefined
  - `USER_DEFINED` - Defined by the user, i.e. custom fields.
- `details` - contains field details which are:
  - `name` - field name - as user sees it. E.g. `First Name`, `E-mail`, etc. Read-only for BUILT_IN fields.
  - `data_type` - type of data that the fill can contain. Read-only for system fields. Can be one of the following:
    - `Text` - stands for textual data
    - `Number` - stands for numeric data
    - `Date` - stands to TimeStamp data - date only, does not support time resolution
    
    
## Contacts Labels Service
Contacts Labels is the way  that Site-Owner can group contacts based on their relationships. Site-Owner can also use label to filter the contacts and perform more actions.
Check out the article regarding [contacts-labels relations](https://support.wix.com/en/article/adding-labels-to-contacts-in-your-contact-list).

### The Contact Label Entity

A contact label is way to group contact. There is a set of built-in (system/predefined) labels (see this [article](https://support.wix.com/en/article/predefined-contact-labels) for details), and there is an option to create new custom (user-defined) label.

A custom label  can be created by the owner in the contact dashboard (see [here](https://support.wix.com/en/article/creating-contact-labels) for details), or via this API.


Contact Label has the following properties:
- `id` - a read-only property that serves as a unique identifier of each contact label.
  -  In the case of built-in labels it will be the same as name.
  - For custom labels it will a system generated random guid.
- `type` - a read-only property that defines label's type, can be one of the following values:
  - `SYSTEM` - System predefined
  - `USER` - Defined by the user, i.e. custom labels.
- `details` - contains label details which are:
  - `name` - label name - as user sees it. E.g. `Customers`, `Frequent Flyers`, etc. Read-only for SYSTEM labels.