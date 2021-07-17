SortOrder: 1
# Shared Gallery


## About Shared Gallery


With Wix Shared Gallery, site owners can create and manage a gallery that lets members upload media to their live site.

The Shared Gallery APIs allow your app to:

*   Query a Shared Gallery.
*   Get Media Display and Media Download URLs.

Read more about how site owners can manage their [Shared Galleries](https://www.wix.com/app-market/wix-shared-gallery).


## Terminology

*   **Media:** Site owners and their members can upload photos, videos, and GIFs to the Shared Gallery.
*   **Album:** Albums are folders in a Shared Gallery. Albums are only supported on the root level of a Shared Gallery, meaning you can not create an Album inside another Album.
*   **Likes:** Members can like media items.
*   **Views:** Represents the number of unique members who have viewed a specific media.
*   **Member Tags:** Members can tag themselves and other members in media items.


# Sample use cases & flows: Shared Gallery


This article shares a possible use case for your app, as well as an example flow that could support it. You're certainly not limited to this use case, but it can be a helpful jumping off point as you plan your app's implementation.


## Upload media from a Shared Gallery to an external platform.


The owners of a popular Gaming Blog also manage a Social Media feed. Now they want to increase their feed’s traffic by uploading media from their Shared Gallery to the external platform. Your app will query the Shared Gallery, create a Media Download URL, retrieve the relevant media, and finally upload it to the Social Media feed.

1. Query the desired media.

   For our example we want to identify the 5 most viewed media items that two specific members have uploaded to the Shared Gallery. You’ll use the [Query Items](http://QueryMediaAlbums.html) endpoint to get this info. Your app needs to pass the respective member IDs, in addition to the sort and paging info in the body of the request. Read more about how to get member IDs using the [Members API](http://MembersAPI.html).

    ``` sh
        curl -XPOST -H 'Authorization: npaIQ37TVGH1xdHDnfSWrt0AA4d4tkOUwGhuUy1y6Wk.eyJpbnN0YW5jZUlkIjoiMmQyYTcxYjMtZmYxNS00NGIwLWFhNTAtYTUyZjZiZWNiNWI0IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiMmQyYTcxYjMtZmYxNS00NGIwLWFhNTAtYTUyZjZiZWNiNWI0Iiwic2lnbkRhdGUiOiIyMDIxLTA1LTI3VDA5OjQzOjIxLjk2OVoiLCJ1aWQiOiIwYTVhNmVhNS1mY2RkLTQ4NWMtYjYxNC1jMDEyNzhmOTZkMzIiLCJwZXJtaXNzaW9ucyI6Ik9XTkVSIiwiZGVtb01vZGUiOmZhbHNlLCJzaXRlT3duZXJJZCI6IjBhNWE2ZWE1LWZjZGQtNDg1Yy1iNjE0LWMwMTI3OGY5NmQzMiIsInNpdGVNZW1iZXJJZCI6IjBhNWE2ZWE1LWZjZGQtNDg1Yy1iNjE0LWMwMTI3OGY5NmQzMiIsImV4cGlyYXRpb25EYXRlIjoiMjAyMS0wNS0yN1QxMzo0MzoyMS45NjlaIiwibG9naW5BY2NvdW50SWQiOiIwYTVhNmVhNS1mY2RkLTQ4NWMtYjYxNC1jMDEyNzhmOTZkMzIifQ'  -d '{
                     "filter": {
                        "created_by": [
                           "7e60dbb7-736e-4cb4-ac12-07301289fc42",
                           "2090bbca-4872-402b-a172-5b9b3146b892"
                        ],
                        "item_types": [
                           "VISUAL_MEDIA"
                        ]
                     },
                     "sort": {
                        "field": "LIKE_COUNT",
                        "order": "DESC"
                     },
                     "paging": {
                      "limit": 5
                     }
                  }' 'https://www.wixapis.com/shared-gallery/v1/items/query'
    ```

   > Note: Make sure to retrieve the item IDs from the response.

2. Create the Download URL.

   Then you’ll pass these IDs in the body of the [Get Media Download URL](http://GetDownloadURL.html) call to create the download URL.

    ``` sh
        curl -XPOST -H 'Authorization: npaIQ37TVGH1xdHDnfSWrt0AA4d4tkOUwGhuUy1y6Wk.eyJpbnN0YW5jZUlkIjoiMmQyYTcxYjMtZmYxNS00NGIwLWFhNTAtYTUyZjZiZWNiNWI0IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiMmQyYTcxYjMtZmYxNS00NGIwLWFhNTAtYTUyZjZiZWNiNWI0Iiwic2lnbkRhdGUiOiIyMDIxLTA1LTI3VDA5OjQzOjIxLjk2OVoiLCJ1aWQiOiIwYTVhNmVhNS1mY2RkLTQ4NWMtYjYxNC1jMDEyNzhmOTZkMzIiLCJwZXJtaXNzaW9ucyI6Ik9XTkVSIiwiZGVtb01vZGUiOmZhbHNlLCJzaXRlT3duZXJJZCI6IjBhNWE2ZWE1LWZjZGQtNDg1Yy1iNjE0LWMwMTI3OGY5NmQzMiIsInNpdGVNZW1iZXJJZCI6IjBhNWE2ZWE1LWZjZGQtNDg1Yy1iNjE0LWMwMTI3OGY5NmQzMiIsImV4cGlyYXRpb25EYXRlIjoiMjAyMS0wNS0yN1QxMzo0MzoyMS45NjlaIiwibG9naW5BY2NvdW50SWQiOiIwYTVhNmVhNS1mY2RkLTQ4NWMtYjYxNC1jMDEyNzhmOTZkMzIifQ'  -d '{
                        "item_ids": [
                           "28280b60-0e89-42c1-841d-a856350c6136",
                           "5ebf6908-ad87-43ef-882e-4d55af1d0862"
                        ]
                     }' 'https://www.wixapis.com/shared-gallery/v1/items/download-url'
    ```

3.   Download the relevant images.

   Now your app will retrieve the selected media by accessing the download URL. All media files are located on the root level of a zip archive. Your app will then extract the archive.

   > Note: A Media Download ULR is only valid for 15 minutes. Your app needs to create a new one after it has expired.

4. Upload the images to the external platform.

   Finally, you’ll upload the retrieved images to the external Social Media feed. 
