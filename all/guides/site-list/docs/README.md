SortOrder: 0
# About the Site API

The Site API is a service that holds public information about Wix sites that is accessible to the site's owner, including the site's name, its URL, its publish status, its owner, display thumbnail, when it was created, if the site has a premium plan attached to it, and more.
Site owners can view their sites via the `My Sites` page, at https://manage.wix.com/account/sites.

Third party resellers, agencies and others can use the Site API to sync their external platform with Wix to allow customers to view and access their Wix sites.
Sites can be filtered by their folder ID, premium status, installed applications, domain connection status and more.

> **Important**: This API is accessible via API keys, which is currently available to selected beta users only. You will not be able to access this API with a standard Auth header.


## Terminology
* **Site**:  A website in the account. Sites are accessible to users according to the specific permissions they hold on a specific site or on the entire account.
* **Folder**: A grouping of sites that account users can create to organize their sites. Each site can only belong to one folder.
* **Account**: A Wix account can have one or more users. Standard accounts have one user while team accounts can have multiple users.
* **Trashed**: A Wix site can be "moved to trash", but not deleted. 


## User Flow
To show all the sites that belong to a specific client:

1. Get a list of sites by querying by site IDs.
2. Optional: you can sort by most recently updated.
3. For each site:  
   a. Show the site’s `displayName`.  
   b. Display the site’s snapshot using `thumbnail`.  
   c. Display the site’s URL using `viewURL`.  
   d. Enable navigation to the Editor by linking the `editUrl`.  
   e. Enable navigation to the site’s dashboard by concatenating "https://manage.wix.com/dashboard/" and the `id` field. Example: https://manage.wix.com/dashboard/412f6f5e-6c38-46df-aee1-66802a2001d1


## Limitations
* The maximum number of sites that can be retrieved by `QuerySites` is 1,000.  
* The Count Sites endpoint does not support `premium` and `appIds` filters.
