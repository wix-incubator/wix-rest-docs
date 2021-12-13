SortOrder: 0
# Sites List Folders

The Folders API enables users to manage sites in an account by organizing them into folders. It enables users to query, create and update folders in an account, as well as to move sites and folders to other folders.
Users can also manage their sites and folders via the My Sites page, at https://manage.wix.com/account/sites.

## Objective
With the Wix Folders APIs you can query the list of folders in the account, update, delete and create new folders. 
You can also get a parent folder’s ID by site ID, and you can move sites and folders between folders.

## Target Audience
Channels would use this API for their internal workflows. For example:
- Have all sites waiting for QA in a designated folder
- Move all ‘suspended’ sites to a designated folder
- Create, update or delete folders to accommodate this workflow.

## Terminology
* **Site**:  a website in the account. Sites are accessible to users according to the specific permissions they hold on a specific site or on the entire account.
* **Folder**: grouping of sites that account users can create to organize their sites. A site can only belong to one folder.
* **Account**: a wix account can have one or more users. Standard accounts have one user while team accounts can have multiple users.
* **User**: a user represents a member of a Wix account. Each user has its own email and password that is used to access Wix.

## Limitations
* MoveSitesToFolder 
  * The metaSiteId list maximal length allowed is 500.
  * Single filter only is supported at the moment.