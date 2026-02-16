SortOrder: 2
# Importing Files

To import files using the [`Import File`](https://dev.wix.com/api/rest/media/media-manager/files/import-file) or [`Bulk Import Files`](https://dev.wix.com/api/rest/media/media-manager/files/bulk-import-files) endpoints, you need to do one of the following: 

1. Pass each file's [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) in the `mimeType` parameter of the request.  For example, 'image/png'.

2. Pass each file's name and extenstion. For example, 'my-image.png'. 

3. If you don't know a file's extension or MIME type, pass its media type in the `mediaType` parameter of the request. For example, 'IMAGE'. Note that this option only works if the server hosting the media allows a "HEAD" request.