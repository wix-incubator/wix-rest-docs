SortOrder: 1
# Example Flows

This article shares some possible use cases for your app, as well as an example flow that could support each one. You're certainly not limited to these use cases, but they can be a helpful jumping-off point as you plan your app's implementation.

## Share a Pro Gallery on an External Platform

Your app can help the site owners upload media from a Pro Gallery to an external Social Media platform to increase their brand's popularity. You could retrieve the site's Pro Galleries, let the site owner select one, get the relevant media, and then upload the media items to the external platform.

1. Retrieve the site's Pro Galleries via the [List Galleries](https://dev.wix.com/api/rest/site-content/pro-gallery/list-galleries) endpoint.
2. Display the first image of each gallery to the site owners and let them select which Pro Gallery they want to upload to the external platform.
3. Retrieve the media items belonging to the relevant gallery using the [Get Gallery](https://dev.wix.com/api/rest/site-content/pro-gallery/get-gallery) endpoint.
4. Create a mapping for future syncs between the Pro Gallery and the external platform and store it on your servers.
5. Upload the media files to the external platform.

> **Note:** Make sure to include both the Wix media item IDs and the external media IDs in the mapping.

## Two-Way Sync a Pro Gallery with an External Gallery

### Part 1: Initial Setup

First, your app needs to create a mapping between the Wix media items and the external media. You can read about a possible way to do so in the [Share a Pro Gallery on an External Platform](#share-a-pro-gallery-on-an-external-platform "Share a Pro Gallery on an External Platform example flow") example flow.

### Part 2: Synchronizing to the External Gallery

1. Sign up for the following webhooks:
+ [Gallery Item Created Webhook](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-item-created-webhook)
+ [Gallery Item Deleted Webhook](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-item-deleted-webhook)
+ [Gallery Item Updated Webhook](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-item-updated-webhook)
2. Get notified when one of these webhooks is triggered and extract the item ID from the webhook data.
3. For the [Gallery Item Updated](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-item-updated-webhook) and [Gallery Item Created](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-item-created-webhook) webhooks, also extract the media URL, sort order, and other relevant information.
4. Identify the corresponding media item in your mapping and update the mapping accordingly.
5. Use the external platform's APIs to create, delete or update the media item there.

> **Note:** Ignore the resulting webhook, so you don’t create an endless loop of updates.

### Part 3: Synchronizing to a Pro Gallery

1. Listen to changes in the external gallery.
2. Update the mapping according to the changes.
3. Upload media to Wix Media using the [Media Manager API](https://dev.wix.com/api/rest/media/media-manager).
4. [Create](https://dev.wix.com/api/rest/site-content/pro-gallery/create-gallery-item), [update](https://dev.wix.com/api/rest/site-content/pro-gallery/update-gallery-item), or [delete](https://dev.wix.com/api/rest/site-content/pro-gallery/delete-gallery-item) the relevant media item in the Pro Gallery using the matching endpoint.
5. Ignore the resulting Wix webhook, so you don’t create an endless loop of updates.
