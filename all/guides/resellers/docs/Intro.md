SortOrder: 0
# About the Resellers API

With the Resellers API, strategic partners can offer Wix services to their customers. You can contact the Wix B2B sales team at bizdev@wix.com to find out how to become a reseller and which services are available. Resellers are responsible for the complete purchase flow, including checkout experience, payment, and post-purchase management. The Wix services can be offered both as part of a do-it-yourself (DIY) or do-it-for-me (DIFM) flow, as described below. Resold Wix services will be available to the customer until the reseller actively cancels them.

> **Note:** Contact the Wix B2B sales team at bizdev@wix.com about how to become a reseller and which Wix services you could offer to your customers.  
> **Important**: This API is accessible via API keys, which are currently available to selected beta users only. You will not be able to access this API with a standard Auth header.  
> 
The Resellers APIs allow you to:

* Create, retrieve and cancel packages of Wix services
* Adjust and cancel product instances that are part of a package


## Terminology

* **Reseller:** Strategic partner that offers Wix services to their customers.
* **Product Instance:** Wix service that the reseller offers to their customers.
* **Service Type:** Wix service type. For example, `Website Plan`, `Business & eCommerce Plan`, or `Ascend`. See [Wix Premium Subscriptions](/docs/link) for more details.
* **Package:** Group of Wix services that the reseller offers to the customer as part of a single transaction. 
* **Site ID:** Unique identifier of a customer's Wix site. See the [Sites API](https://dev.wix.com/api/rest/account-level-apis/sites/query-sites) for more details.
* **DIY:** Do-it-yourself business model. The resellers' customers will actively build and manage their sites in the Wix platform.
* **DIFM:** Do-it-for-me business model. Only employees or agents of the reseller will have access to the Wix account.
* **Account:** Wix account. In case of DIY, every customer has their own account and will actively build and manage their sites in the Wix platform. In case of DIFM, the reseller uses a team account to manage their customers’ sites.
* **Adjust:** Resellers can up- or downgrade the Wix services that they are offering to their customers. For example, you could upgrade a `Business Basic` plan to `Business Unlimited`.


## Limitations

* Only selected strategic partners are allowed to resell Wix services. Contact the Wix B2B sales team, if you’d like to become a reseller.
* Not all Wix services can be resold.
* Resold Wix services will not have an expiration date. They will be available to the customer until the reseller actively cancels them.
* Currently, you cannot use the Resellers API to assign a service to a specific Wix site after a package has been created.
* Currently, there are no webhooks available for the Resellers API.

> **Note:** Contact the Wix B2B sales team at bizdev@wix.com about how to become a reseller and which Wix services you could offer to your customers.
