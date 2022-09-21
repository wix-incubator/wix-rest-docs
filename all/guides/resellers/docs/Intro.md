SortOrder: 0
# About the Resellers API

With the Resellers API, strategic partners can offer Wix services to their 
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


> __Important__: This API is accessible via API keys, which are currently 
> available to selected beta users only. You won't be able to access this 
> API with a standard Auth header.  


## Terminology


+ __Reseller__: Strategic partner that offers Wix services to their customers.
+ __Product Instance__: Specific instance of a Wix service that the reseller 
  provides to one of their customers.
+ __Service Type__: Wix service types are groups of related services. For 
  example, the service type `Premium Plans` includes both the `Website Plan` and 
  `Business & eCommerce Plan` services.
+ __Voucher__: Time-limited benefit for non-Wix services that comes with some 
  products.
+ __Package__: Group of Wix services that the reseller offers to the customer 
  as part of a single transaction. 
+ __Site ID__: Unique identifier of a customer's Wix site. See the 
  [Sites API](https://dev.wix.com/api/rest/account-level-apis/sites/query-sites) 
  for more details.
+ __DIY__: Do-it-yourself business model. The resellers' customers actively 
  build and manage their sites in the Wix platform.
+ __DIFM__: Do-it-for-me business model. Only employees or agents of the 
  reseller have access to the Wix account.
+ __Account__: Wix account. In case of DIY, every customer has their own 
  account and actively build and manage their sites in the Wix platform. In 
  case of DIFM, the reseller uses a team account to manage their customers’ 
  sites.
+ __Adjust__: Resellers can up- or downgrade the Wix services that they're 
  offering to their customers. For example, you could upgrade a 
  `Business Basic` plan to `Business Unlimited`.


## Limitations


+ Only selected strategic partners are allowed to resell Wix services. Contact 
  the [Wix B2B sales team](mailto:bizdev@wix.com), if you’d like to become a 
  reseller.
+ Not all Wix services can be resold.
+ Resold Wix services won't have an expiration date. They are available to the 
  customer until the reseller actively cancels them.
+ Currently, you can't use the Resellers API to assign a service to a specific 
  Wix site after a package has been created.
+ Currently, there are no webhooks available for the Resellers API.

> __Note__: Contact the Wix B2B sales team at bizdev@wix.com about how to 
  become a reseller and which Wix services you could offer to your customers.
