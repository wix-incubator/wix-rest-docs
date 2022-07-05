SortOrder: 0
# About the Site Folders API

The Site Folders API enables the management of sites in an account by organizing them into folders. 

![Site Folders](https://s3.amazonaws.com/wixplorer-readme-images/site-folders%2FSiteFolders.jpg)


With the Folders APIs you can create folders, update folder names, and delete folders. 
You can also get a parent folder’s ID by site ID, and you can move folders and sites between folders.

> **Important**: This API is accessible via API keys, which are currently available to selected beta users only. You will not be able to access this API with a standard Auth header.  

Site owners and contributors can also manage their sites and folders via the [My Sites](https://manage.wix.com/account/sites) page.


## Terminology
* **Account**: A Wix account includes all the assets that site owners/contributors interact with: sites, folders, premium plans, domains, and more. An account can have one or more users. Standard accounts have one user while team accounts can have multiple users.
* **Site**:  A website in the account. Sites are accessible to site owners and contributors according to the specific permissions they hold on a specific site or on the entire account.
* **Folder**: A group of sites that account users can create to organize their sites. Each site can only belong to one folder.


## Sample User Flow

An agency that builds Wix sites for customers might set up their folders according to their internal workflow processes, and only share the site with the customer once it has reached a certain stage in the process. In such a situation the flow might look like this:

1. Call the [Create Folder](https://dev.wix.com/api/rest/drafts/site-folders/create-folder) endpoint as often as required to create folders with all your workflow process names, including “Design”, “QA”, “Suspended”, and “Live”.  
2. As the site moves along the workflow process, call the [Move Sites to Folder](https://dev.wix.com/api/rest/drafts/site-folders/move-sites-to-folder) endpoint to move the sites to the relevant folder, for example sites that have completed design and are waiting for QA into the designated "QA" folder.  
3. Periodically get all unpaid site IDs from an external list. 
4. Call the [Move Sites to Folder](https://dev.wix.com/api/rest/drafts/site-folders/move-sites-to-folder) endpoint to move all unpaid sites into the designated "Suspended" folder.  
5. If your process changes, call the [Update Folder](https://dev.wix.com/api/rest/drafts/site-folders/move-sites-to-folder) endpoint to rename a folder.


## Limitations
* Each site can only belong to one folder.
* Each account can have a maximum of 500 folders in the Wix account (not currently enforced via API).
* Up to 1,000 folders can be moved by `MoveFolders`.
* Up to 500 sites can be moved by `MoveSitesToFolder`.
* Up to 1,000 folders can be retrieved by `QueryFolders`.
