SortOrder: 1
# **Use Cases**
In this example we'll provide few basic examples that will show some usages of our API.

## 1. Creating a new "Mega Gallery" 
In this example we will: create a new gallery in the Editor segment, which contains all of the items in all of the other galleries in the site, and then publish it.
#### Flow Overview
1. Fetch all of the galleries in the site
2. Create a New Gallery with all of the items of all of the galleries
3. Publish the Gallery

#### Using The API
- In order to fetch all the galleries for a site in the Editor segment we need to use ListGalleries method with SAVED state:

```
curl -X GET \
         'https://progallery.wixapps.net/pro-gallery-webapp/v1/galleries?state=SAVED' \
         -H 'Authorization: XXX
```
**Please note that the authorization must contain the InstanceId of ProGallery on this site, otherwise our service will not know which galleries to fetch.**

Let's say we created an array ITEMS which contains all of the itmes of all of the galleries

- Now we'll create a new gallery which contains ITEMS:

```$xslt
 curl -X POST \
   'https://progallery.wixapps.net/pro-gallery-webapp/v1/galleries' \
   --data-binary '{
                  	"gallery": {
                  		"name": "Mega Gallery",
                  		"items": ITEMS
                  	},
                  	"state": "SAVED"
                  }' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```
 Let's say the response had the galleryId: GALLERY_ID

- Now we'll publish the gallery:

```$xslt
 curl -X PATCH \
   'https://progallery.wixapps.net/pro-gallery-webapp/v1/galleries/GALLERY_ID' \
   -H 'Authorization: <AUTH>'
```

## 2. Gallery For UoU Media 
In this example, we'll allow to Users of Users to add Items to a single Gallery which its purpose is to allow users to share their experiences. 

#### Flow Overview

We'll just use CreateGalleryItem method, but with PUBLISHED state, because we want to apply the changes directly to the LiveSite

Nothing to fancy here, we just wanted to show an example of editing a gallery in PUBLISHED state 

#### Using The API

```$xslt
 curl -X POST \
   'https://progallery.wixapps.net/pro-gallery-webapp/v1/galleries/e481d9b4-14b9-4a98-ae52-67f4170e3a63/items' \
   --data-binary '{
                    "item": {
                      "orderIndex": 1597671468.749,
                      "title": "UoU's Image!",
                      "mediaUrl": "https://static.wixstatic.com/media/nsplsh_215a426736346c6e443551~mv2.jpg",
                      "dataType": "Photo",
                      "photoMetadata": {
                        "height": 4898,
                        "width": 3265
                      },
                      "name": "Image by UoU",
                      "tags": [
                        "_unsplash",
                        "_unsplash_qWBg64lnD5Q"
                      ],
                      "mediaOwner": "Wix"
                    }
                  }' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```