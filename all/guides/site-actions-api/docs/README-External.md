SortOrder: 0
# About the Site Actions API

The Site Actions API allows you to manage the sites owned by a Wix account. 
  
With the Wix Site Actions API, your app can:
- Delete site in bulk.
- Publish sites.

## About publishing sites

If a site was built with any Wix editor, after calling the publish API for the first time anyone will be able to view the site on the internet. 
Calling the Publish endpoint after the initial publish will make any latest changes made in the Wix editor go live. (Site admins have access to view all changes made to the site in [Site History](https://support.wix.com/en/article/viewing-and-managing-your-site-history).)


## Before you begin
It’s important to note the following before starting to code:

- A maximum of 20 sites can be deleted each time the Bulk Delete Site endpoint is run.
