SortOrder: 12
# Uploading a picture

After calling generatePictureUploadUrl (TODO explain and give example)

## Two possible ways to upload file, need to check:

### Axios

```javascript
import axios from 'axios';

async function uploadFile(uploadUrl, stream) {   
     const { data } = await axios.put(uploadUrl, stream, {
      headers: { 'content-type': 'application/octet-stream', 'origin': 'yourdomain.com' },
      responseType: 'json',
      params: {},
    });
    return data;
}
```
taken from: https://github.com/wix/media-platform-js-sdk/blob/df0b5ebe881f0f42b24e734046ad0c8ef06e2ec7/src/platform/http/http-client.ts#L137

For stream we need something like the normalizeStream in https://github.com/wix/media-platform-js-sdk/blob/df0b5ebe881f0f42b24e734046ad0c8ef06e2ec7/src/platform/management/file-uploader.ts#L221

### XMLHttpRequest

```javascript
function uploadFile(uploadUrl, file) {
    const onLoad = event => {
      console.log("onLoad", event)
    };
    
    const formData = new FormData();
    formData.append('file', this.file);
    //formData.append('acl', "private");
    
    const request = (this.request = new XMLHttpRequest());
    
    request.addEventListener('load', onLoad);
    request.open('POST', uploadUrl);
    request.withCredentials = true;
    request.responseType = 'json';
    request.send(formData);
}
```
Thaken from here:
https://github.com/wix/media-platform-js-sdk/blob/3b93affc817be972e589f58ae887480272d6d0d8/src/public/platform/uploader/upload-job.ts#L151

## Notes
* This is a private URL, https://support.wixmp.com/en/article/file-management#upload
* The explanation in there is confusing and maybe outdated
* Pending CORS problem, should be able to upload from anywhere
* Need to verify we can upload without sending the path
* Need to verify we if we don't send acl the file is indeed private (as requested by the server)
