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

The Resellers API allows you to:

+ Create, retrieve, and cancel packages of paid Wix services.
+ Manage product instances that are part of a package.

Learn more about the [Domain Search](https://dev.wix.com/api/rest/account-level-apis/domain-search/introduction),
[Registered Domains](https://dev.wix.com/api/rest/account-level-apis/registered-domains/introduction)
and [Domain Connections](https://dev.wix.com/api/rest/account-level-apis/domain-connections)
API to offer domains to your customers.

## Before you begin 

It’s important to note the following points before starting to code:

+ The Resellers API is accessible via API keys. You can't access this
  API with a standard Auth header. We recommend authenticating calls with an
  API key for your main account instead of using a key for the relevant
  sub-account. But the responses to calls remain consistent across API
  keys, provided you have the necessary permissions.
+ Only selected strategic partners are allowed to resell Wix services. Contact
  the [Wix B2B sales team](mailto:bizdev@wix.com), if you’d like to become a
  reseller.
+ Not all Wix services can be resold. Contact the
  [Wix B2B sales team](mailto:bizdev@wix.com) to learn more about which services
  you can resell.
+ Most resold Wix services don't have an expiration date. They're available to the
  customer until the reseller actively cancels them. Domains are an exception,
  since they're purchased by Wix, the reseller, or the customer through an
  external registrar. Resellers must actively extend access to domains.
  Currently, this isn't possible via APIs.
+ Some paid Wix services or products can't be resold to customers who don't
  have already access to another product. For example, you can resell domains only to
  Wix sites that have an active Premium plan. You must create a package
  containing the essential product first, before you can create a second
  package with the additional product.
+ When Wix customers purchase specific paid services or products, Wix may offer
  them time-limited free access to a different paid service or product. For
  example, customers get a voucher for a free 1-year domain registration when
  purchasing any Wix Premium plan. Resellers can also offer their customers the
  additional, associated product. To do so, create a package containing the original product
  first. Then, create a second package with the additional product. In this second
  [Create Package](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
  call, pass the instance ID of the original product as `referenceProductInstanceId`.
  This way, Wix doesn't charge you for the additional product.
+ Currently, there are no webhooks available for the Resellers API.

## Use Cases

+ [Set up a customer's site in your team account](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/sample-flows#set-up-a-customers-site-in-your-team-account)
+ [Reassign a paid service to a different site](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/sample-flows#reassign-a-paid-service-to-a-different-site)

## Terminology

+ __Reseller__: Strategic partner that offers Wix services to their customers.
+ __Customer__: Site owner who has purchased access to the Wix platform through a reseller.
+ __DIY__: Do-it-yourself business model. The customer actively
  builds and manages their site in the Wix platform.
+ __DIFM__: Do-it-for-me business model. Only employees or agents of the
  reseller have access to the Wix account.
+ __Package__: Group of product instances that the reseller offers to a customer
  as part of a single transaction.
+ __Product Instance__: Specific instance of a paid service or product that a
  reseller provisions to one of their customers.
+ __Reference product instance__: Product instance that you can use to offer
  your customers time-limited free access to an additional product or service.
  Not all products can be used as reference products. You can use each product
  instance only once as reference product instance.
+ __Floating__: A product instance that hasn't been assigned to a Wix site, but
  only a Wix account. Customers don't have access to floating instances,
  they or the reseller must assign the instance to a site before it can be used.
+ __Service Type__: Wix service types are groups of related services. For
  example, the service type `Premium Plans` includes both the `Website Plan` and
  `Business & eCommerce Plan` services.
+ __Feature__: Most granular capability or benefit that comes with a Wix service.  
+ __Adjust__: Resellers can up- or downgrade a product instance that they're
  offering to a customer. For example, you could upgrade a
  `Business Basic` plan to `Business Unlimited`.
+ __Voucher__: Time-limited benefit for non-Wix products that comes with some
  Wix services.
+ __Site ID__: Unique identifier of a Wix site. See the
  [Sites API](https://dev.wix.com/api/rest/account-level-apis/sites/query-sites)
  for more details.  
+ __Account__: Wix account that includes access to associated sites.
  + __Team account__: Account type that supports collaborative work by having
    multiple sets of login credentials. This is especially helpful for agencies
    and resellers when managing a large number of customer sites. In Wix Studio
    team accounts are called workspaces. An agency may have multiple workspaces
    in Wix Studio, while in Wix Editor they're limited to a single team account.
  + __Sub-account__: Account that's contained within another account, forming a
    hierarchical structure. The owners of the sub-account are only able to
    interact with sites that belong to the sub-account. This setup is
    particularly useful for agencies and resellers since it limits client access
    to relevant sites only.

> __Note__: Contact the Wix B2B sales team at bizdev@wix.com about how to become a reseller and which Wix services you could offer to your customers.