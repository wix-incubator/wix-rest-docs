SortOrder: 2
###### Upload Visual Media

Visual media upload happens in 3 phases:
  - start upload by getting upload url
  - upload to upload url
  - callback with upload response

You can initiate multiple media uploads with single request:

```
const response = await sharedGalleryApi.startVisualMediaUpload({
  actions: [{
    name: 'fileName',
    size: 123,
    parentAlbumId: null, // To upload to root
    actionId: 'clientgeneratedstring'
  }]
});

expect(response.urls).to.deep.equal([{
  actionId: 'actionId',
  requestParameters: {
    request: 'parameters'
  },
  url: 'uploadUrl'
}]);

```

You should not care what is in `requestParameters`. Just map it to `FormData` when performing upload.

Example of upload from browser:

```
<html>
  <body>
    <script>

      const uploadUrl = 'urlFrom_startFileUpload';
      const requestParameters = {}; // From startFileUpload

      async function uploadFile(e) {
        const file = e.elements[0].files[0];
        console.log('fileName', file.nane); //This name should be provided to startFileUpload, completeFileUpload

        //Populate form data with request parameters as is
        const formData = new FormData(e);
        Object.keys(requestParameters).forEach(key => formData.append(key, requestParameters[key]))

        const response = await fetch(uploadUrl, {
          method: 'POST',
          body: formData,
        });
        // this response must be provded to completeUpload
        console.log(await response.text());
      }
    </script>

    <form id="upload-form" enctype="multipart/form-data" action="" method="post" target="upload-result" onsubmit="uploadFile(this)">
        <input id="file" name="file" type="file" accept="image/*">
        <input id="submit" type="submit">
    </form>
  </body>
</html>
```

Complete upload by providing `uploadResponse`:
```
const response = await sharedGalleryApi.completeVisualMediaUpload({
  actions: [{
    uploadResponse: 'response body from upload url',
    actionId: 'clientgenerated'
  }]
});
```

Complete upload responds with newly created library items. You can complete upload of multiple files with single request.

ActionId can be used by client to map response to original files. 
For example when starting upload some files might be too big so response will contain list of failures.