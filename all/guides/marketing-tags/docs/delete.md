SortOrder: 2
### In case you want to delete a tag

use [Delete Marketing Tag V2](https://www.wixapis.com/marketing/v2/tags)
```sh
curl -X DELETE \
    https://www.wixapis.com/marketing/v2/tags?tag_type=<TAG_TYPE>  \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>'
```