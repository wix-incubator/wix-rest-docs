SortOrder: 0
# Introduction

The Site Media API allows you to manage media files and folders in a site's Media Manager.

With the Site Media API, you can:
* Manage files in the Media Manager.
* Manage folders in the Media Manager.
* Generate temporary URLS for:
  * Streaming video files from the Media Manager.
  * Downloading a folder and files from the Media Manager.

Learn more [about the Media Manager](https://support.wix.com/en/article/wix-media-about-the-media-manager) and how you can access it. 


## Before You Begin

Before using the Import File and Bulk Import Files endpoints, see the article on [Importing Files](https://dev.wix.com/api/rest/media/media-manager/importing-files).

## Terminology

* **Generate File Download Url** vs. **Generate Files Download Url**
  The Generate Files Download Url generates a permanent URL for downloading a compressed file containing specific files in the Media Manager. However, the [Generate File Download Url](https://dev.wix.com/api/rest/media/media-manager/files/generate-file-download-url) generates one or more temporary URLs for downloading a specific file in the Media Manager. You can use the `expirationInMinutes` parameter to set the URL expiration time, making it more secure than the [Generate Files Download Url](https://dev.wix.com/api/rest/media/media-manager/files/generate-files-download-url). Therefore, to download private files, use the Generate File Download Url for each private file that you want to generate a download Url for, instead of the Generate Files Download Url.

* **Generate File Resumable Upload Url** vs. **Generate File Upload Url**
  The Generate File Upload Url generates an upload URL to allow external clients to upload a file to the Media Manager. However, any interruption in the upload process stops the file upload. For files larger than 10MB, or when network connection is poor, use the [Generate File Resumable Upload Url](https://dev.wix.com/api/rest/media/media-manager/files/generate-file-resumable-upload-url) instead. With the resumable upload URL, any interruption in the upload process pauses the file upload, and resumes the file upload process after the interruption. 

  **Using the generated upload and resumable upload URLs**
  When you get the `uploadUrl` response from Generate File Upload Url, learn how you can use it to [upload a file to the Media Manager](https://dev.wix.com/api/rest/media/media-manager/upload-api). When you get the `uploadUrl` response from Generate File Resumable Upload Url, learn how you can use it to [resumably upload a file to the Media Manager](https://dev.wix.com/api/rest/media/media-manager/resumable-upload-api). 


* **System folders:** Folders in the Media Manager's file system directory. 
  There are 3 types of system folders:
  * **Root Folders:** Main categories of folders the Media Manager. 
    * `MEDIA_ROOT`: Contains all files and folders in the Media Manager's 'Site Files' tab in the UI.
      >**Note:** The `MEDIA_ROOT` system folder is different from the `media-root` folder of the Media Manager. The `MEDIA_ROOT` system folder contains all media in all levels of the 'Site Files' tab in the UI, while the `media-root` folder of the Media Manager only contains the media in the root level of the 'Site Files' tab in the UI.
    * `TRASH_ROOT`: Contains all files and folders in the Media Manager's 'Trash' tab in the UI.
    * `VISITOR_UPLOADS_ROOT`: Contains all files and folders created by site visitors or members. 
      >**Note:** The `VISITOR_UPLOADS_ROOT` folder is located in the 'Site Files' tab in the UI. However, it is its own root folder and doesn't return when searching in the `MEDIA_ROOT` folder. 
  * **Virtual Folders:** Special categories of folders in the Media Manager that are hidden from the UI and can't be deleted.
    * `MOBILE_UPLOADS`: Contains all media uploaded using mobile devices. 
    * `PURCHASED_ITEMS`: Contains all media imported using a purchase flow.
  * **Other Folders:** 
    * `VIDEO_MAKER`: Contains all videos created using Wix Video Maker. Located in the 'Site Files' tab in the UI.  

* **File Assets** Wix Media files are optimized for web use. When a file is imported or uploaded to the Media Manager, it is processed and may produce several variations of the file for use in different circumstances.    
  For example:   
    * A video file can have different resolutions and formats.
    * An audio file can have different formats and qualities.
    * Video or audio files can have a preview asset containing only a portion of the file.
  
  With the [Generate File Download Url](https://dev.wix.com/api/rest/media/media-manager/files/generate-file-download-url), you can use the `assetKeys` parameter to download different assets of a file.  

 