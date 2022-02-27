SortOrder: 1
# Example Flow: Resellers API


This article shares a possible product flow you could implement. You're certainly not limited to this flow, but you might use it as inspiration for your design and development process.


## Resellers


Using the Resellers API, you can help your customers manage their Wix services. For example, you could identify relevant Wix site IDs, create a package of services, upgrade a service and get an overview about the services currently available to a specific customer.


* Step 1: Retrieve the relevant site IDs using the [Sites API](https://dev.wix.com/api/rest/account-level-apis/sites/query-sites).
* Step 2: Identify the relevant `catalogProductId` from the list of available Wix services you have received from the Wix B2B sales team.
* Step 3: [Create a package](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package) that includes the Wix services you want to offer the customer.
* Step 4: When it becomes necessary, upgrade or downgrade a product instance using the [Adjust Product Instance Specifications](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/adjust-product-instance-specifications) endpoint.
* Step 5: To get an overview of a customer’s available services, call the [Query Packages](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/query-packages) endpoint.
