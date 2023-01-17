SortOrder: 0
# About Pro Gallery

The Pro Gallery API allows you to manage pro galleries on a Wix site's backend.

With the Pro Gallery API, you can:

+ Get, list, and update pro galleries created by a Wix site owner with the Editor.
+ Get, list, create, update, and delete items in a pro gallery.
+ Create or delete a pro gallery on a site's backend.

For the Pro Gallery API to synchronize with a site's frontend, a Wix site owner needs to [add a pro gallery](https://support.wix.com/en/article/wix-pro-gallery-adding-and-setting-up-your-gallery) to their site using the Editor. When you use the Pro Gallery API to create, update, or delete an item from a pro gallery created with the Editor, or to delete a pro gallery, the site's frontend updates automatically.

> **Note:** We do not recommend creating new pro galleries using the Pro Gallery API.
> When a Wix site owner adds a pro gallery to their site using the Editor, a corresponding pro gallery is created on the site's backend.
> You can then use the Pro Gallery API to manage items in this pro gallery or delete it, and all updates are reflected on the site's frontend.
> However, when you create a pro gallery using the Pro Gallery API, it's available only on the site's backend and doesn't appear on the live site.
> In order to display a backend pro gallery on a live site, the site owner needs to connect it manually to a gallery component using code.
> To learn more about how a site owner can do this using Velo, see [Displaying a Pro Gallery on Your Site Using the Pro Gallery Backend API](https://support.wix.com/en/article/velo-tutorial-displaying-a-pro-gallery-on-your-site-using-the-pro-gallery-backend-api).

## Before you begin

It's important to note the following points before starting to code:

+ We recommend using the Pro Gallery API for managing pro galleries that the site owner already created using the Editor.
+ Read more about how site owners can manage their [Pro Galleries](https://support.wix.com/en/article/wix-pro-gallery-about-the-wix-pro-gallery).
+ The [Gallery Created](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-created-webhook) and [Gallery Updated](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-updated-webhook) webhooks don't return the media items included in the gallery. To retrieve these items or their IDs, listen to the [Gallery Item Created](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-item-created-webhook) and [Gallery Item Updated](https://dev.wix.com/api/rest/site-content/pro-gallery/gallery-item-updated-webhook) webhooks.

## Terminology

+ **Pro Gallery:** A responsive and customizable gallery that displays media items.
+ **Gallery Items:** Media items in a pro gallery, such as images, videos, and text files. You can read more about [supported media](https://support.wix.com/en/article/wix-pro-gallery-adding-media-to-the-gallery). 
