SortOrder: 11
# Picture Operations

The Contacts API allows you to update the contact's picture:

To update picture path you need to use id of uploaded picture

## Using id of uploaded picture
in order to use this method, you need to first upload the picture to the `wixmp` servers,
TODO: fix the url
this can be done using the [Get Picture Upload Token](https://bo.wix.com/wix-docs/rest/crm/contacts/contacts-v4/get-picture-upload-token) endpoint,
`GetPictureUploadToken` takes a `contactId` and the `file extension` of the soon to be upload picture,
the response of the endpoint has `path`, `uploadUrl` and `uploadToken`,
those params are used to upload the picture you want:

TODO: is this link public? (if not, need to copy the table from it)

https://support.wixmp.com/en/article/file-management#upload

Perform a `POST` multipart/form-data to the `uploadUrl` from the previous request, data of the request is:

`path`
`acl`
`uploadToken`
`file`

After uploading the picture you can update the contact's picture by calling `UpdateContactPicture` with the `contactId` and the file `id` you receive from the response of the `POST` operation.  
