SortOrder: 3
# About the Data Collections API

The Data Collections API enables your app to create, delete, and modify the structure of data collections in a Wix site.

## Data collections and their structure
Wix sites store data in collections.
A collection determines the structure of the data to be stored, defining the fields each item should contain and the data type of each field.
Site owners can [create and modify collections](https://support.wix.com/en/article/content-manager-creating-a-collection) for their site using the Content Manager.
With the Data Collections API, you can use code to create, modify, and delete collections in a Wix site.
You can then store and retrieve data in these collections using the [Data Items API](https://dev.wix.com/api/rest/wix-data/wix-data/data-items).

**Note:**
The structure you define for a data collection isn't enforced. This means that if you add or update an item containing a field or data type that doesn't match the collection's structure, your data is stored anyway.

## Permissions

Access to a data collection is controlled by its permissions. These permissions are defined in the collection object and they specify which types of user can perform actions on the data contained in the collection.

Wix Data recognizes 4 roles: 
* `ADMIN`: The site owner.
* `SITE_MEMBER_AUTHOR`: A signed-in user who has added content to the collection.
* `SITE MEMBER`: Any signed-in user.
* `ANYONE`: Any site visitor.

For each of the 4 basic actions (inserting, updating, removing, and reading content) the minimal role required must be set. For example, if you want to allow only site members to view data, and only the site owner to insert, update, and remove data, declare your permissions as follows:
* `insert`: `ADMIN`
* `update`: `ADMIN`
* `remove`: `ADMIN`
* `read`: `SITE_MEMBER`