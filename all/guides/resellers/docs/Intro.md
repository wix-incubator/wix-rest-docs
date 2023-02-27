SortOrder: 0
# About the Resellers API

With the Resellers API, strategic partners can offer paid Wix services to their
customers. You can contact the Wix B2B sales team at bizdev@wix.com to find
out how to become a reseller and which services you could offer to your
customers. Resellers are responsible for the complete purchase flow, including
checkout experience, payment, and post-purchase management. The Wix services
can be offered both as part of a do-it-yourself (DIY) or do-it-for-me (DIFM)
flow, as described below. Resold Wix services are available to the customer
until the reseller actively cancels them.

 
The Resellers APIs allow you to:

+ Create, retrieve, and cancel packages of Wix services.
+ Adjust and cancel product instances that are part of a package.

Learn more about the [Domain Search](https://dev.wix.com/api/rest/account-level-apis/domain-search/introduction)
and [Domain Connections](https://dev.wix.com/api/rest/account-level-apis/domain-connections)
API to offer domains to your customers.

## Before you begin 


+ The Resellers API is accessible via API keys. You can't access this
  API with a standard Auth header. We recommend to authenticate calls of the
  Resellers API with an API key for your main account instead of setting up
  API keys for all of your customers' sub-accounts. But the response of any
  endpoint in Resellers API doesn't vary depending on whether you use an API
  key for an account or sub-account, as long as you have the required
  permissions for the call.
+ Only selected strategic partners are allowed to resell Wix services. Contact
  the [Wix B2B sales team](mailto:bizdev@wix.com), if you’d like to become a
  reseller.
+ Not all Wix services can be resold. Contact the
  [Wix B2B sales team](mailto:bizdev@wix.com) to learn more about which services
  you can resell.
+ Resold Wix services don't have an expiration date. They're available to the
  customer until the reseller actively cancels them.
+ Currently, you can't use the Resellers API to assign a product instance to a
  specific Wix site after a package has been created. But resellers and
  customers can assign floating product instances to sites from their dashboard.
+ Currently, there are no webhooks available for the Resellers API.


## Terminology


+ __Reseller__: Strategic partner that offers Wix services to their customers.
+ __Product Instance__: Specific instance of a Wix service that the reseller
  provides to one of their customers.
+ __Package__: Group of product instances that the reseller offers to a customer
  as part of a single transaction.
+ __Floating__: A product instance that hasn't been assigned to a Wix site, but
  only a Wix account. Currently, you can't assign a floating product
  instance to a site using the Resellers API after you've created a package.
  But customers or agents can assign a floating instance to a site from their
  account's dashboard.
+ __Feature__: Most granular capability or benefit that comes with a Wix service.
+ __Service Type__: Wix service types are groups of related services. For
  example, the service type `Premium Plans` includes both the `Website Plan` and
  `Business & eCommerce Plan` services.
+ __Voucher__: Time-limited benefit for non-Wix products that comes with some
  Wix services.
+ __Site ID__: Unique identifier of a Wix site. See the
  [Sites API](https://dev.wix.com/api/rest/account-level-apis/sites/query-sites)
  for more details.
+ __DIY__: Do-it-yourself business model. The resellers' customers actively
  build and manage their sites in the Wix platform.
+ __DIFM__: Do-it-for-me business model. Only employees or agents of the
  reseller have access to the Wix account.
+ __Account__: A Wix account includes all the assets that site owners interact
  with: sites, folders, Premium plans, domains, and more. An account can have
  one or more users. Standard accounts are for a single user, while team
  accounts allow multiple users to collaborate. Standard and team accounts
  are the same in all other ways. In case of DIY, every customer has their own
  account and actively builds and manages their sites in the Wix platform. In
  case of DIFM, the customer doesn't have their own Wix account.
+ __Sub-account__: Resellers can create sub-accounts for their DIY customers.
  This allows the reseller to access the sites of all their customers while
  customers can only access their own sites.
+ __Adjust__: Resellers can up- or downgrade a product instance that they're
  offering to a customer. For example, you could upgrade a
  `Business Basic` plan to `Business Unlimited`.


> __Note__: Contact the Wix B2B sales team at bizdev@wix.com about how to become a reseller and which Wix services you could offer to your customers.
