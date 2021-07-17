SortOrder: 3
Api supports context token flow.

https://github.com/wix-private/catalyst-server/blob/master/context-token/README.md

For backend integration SharedGalleryAccess payload must be set with appropriate authorized actions.

https://github.com/wix-private/catalyst-server/blob/master/photo-sharing-server/photo-sharing-api/src/main/proto/wix/sharedgallery/api/v1/items/shared-gallery-access.proto

All api methods accept `contextToken` parameter and if token gets refreshed - responds with `contextToken` in response.