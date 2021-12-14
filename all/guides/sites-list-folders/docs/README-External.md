SortOrder: 0
# About the Site Folders API

The Site Folders API enables the management of sites in an account by organizing them into folders. 

image

With the Wix Folders APIs you can query the list of folders in the account, update, delete and create new folders. 
You can also get a parent folder’s ID by site ID, and you can move sites and folders between folders.

Site owners and contributors can also manage their sites and folders via the [My Sites](https://manage.wix.com/account/sites) page.


## Terminology
* **Account**: A Wix account can have one or more users. Standard accounts have one user while team accounts can have multiple users.
* * **Site**:  A website in the account. Sites are accessible to site owners and contributors according to the specific permissions they hold on a specific site or on the entire account.
* **Folder**: A group of sites that account users can create to organize their sites. Each site can only belong to one folder.


## Limitations
* MoveSitesToFolder 
  * The metaSiteId list maximal length allowed is 500.
  * Single filter only is supported at the moment.
