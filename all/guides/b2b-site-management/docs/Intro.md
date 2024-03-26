SortOrder: 0
# About the B2B Site Management API


With the B2B Site Management API, strategic partners can transfer a Wix site 
from a source account to a target account. This allows their customers to have 
exactly the permissions they need, while the strategic partner retains access 
to the sites. Contact the Wix B2B sales team at bizdev@wix.com to learn how to 
become a strategic partner and which accounts are supported as source and 
target.

After transferring the site, strategic partners can use the 
[Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/introduction) 
to offer paid Wix services to their customers.


## Terminology


+ **Wix account**: A Wix account can have one or more users. Standard accounts 
  have one user, while team accounts can have multiple users. Each account can 
  hold multiple sites.
  + **Sub-account**: You can create sub-accounts for your customers. This 
    allows you to access your customers’ sites while customers have the 
    functionality and permissions they need. 
  + **Source account**: The account holding the site before the transfer. Not 
    all Wix accounts are supported as source accounts. Contact the 
    [Wix B2B sales team](mailto:bizdev@wix.com) for more information.
  + **Target account**: The account holding the site after the transfer. The 
    target account must be your main account or one of its sub-accounts.
+ **Wix site**: A website in an account. Sites are accessible to users 
  according to the specific permissions they hold on the site or the 
  entire account.
+ **Paid Wix service**: A service Wix offers site owners that isn’t free of 
  charge. For example, a `Website Plan`, `Business & eCommerce Plan`, or 
  `Ascend`. See 
  [Wix Premium Subscriptions](https://support.wix.com/en/article/choosing-a-premium-plan) 
  for more details.


## Limitations


+ Only strategic partners of Wix services can transfer sites. Contact the Wix 
  B2B sales team at bizdev@wix.com to learn how to become a strategic partner 
  and which accounts are supported as source and target.
+ You can transfer a site only to your main account or one of its sub-accounts. 
  It isn’t possible to transfer a site to an unrelated account. Contact the 
  [Wix B2B sales team](mailto:bizdev@wix.com) for more information.
+ Only sites that don’t include paid Wix services can be transferred. After 
  transferring the site, you can use the 
  [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/introduction) 
  to offer paid Wix services to your customers.
+ The ID of the target account can't be passed in the body of the 
  [Transfer Site](https://dev.wix.com/api/rest/account-level-apis/b2b-site-management/transfer-site) 
  call. It must be specified in the header.
  
