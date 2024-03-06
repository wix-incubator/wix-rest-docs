SortOrder: 2
# Registered Domains Errors

This articles outlines error messages that might be issued when calling endpoints of the Registered Domains API.

## Create Registered Domain errors

The [Create Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/create-registered-domain) endpoint might issue the following error messages:

| <div style="width:180px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| ------ | ------ | ------ | ------ |
| `INVALID_ARGUMENT (400)` | `INVALID_DOMAIN` | Domain `<domainName>` can't be registered. | Check that the TLD is supported by Wix and that the domain is still available for purchase. |
| `INVALID_ARGUMENT (400)` | `DOMAIN_TOO_LONG` | Domain `<domainName>` can't be registered because the domain name is too long. | Make sure that the domain name (excluding TLD) isn't longer than 63 characters. |
| `INVALID_ARGUMENT (400)` | `DOMAIN_TOO_SHORT` |  Domain `<domainName>` can't be registered because the domain name is too short. | Make sure that the domain name (excluding TLD) includes at least 3 characters. |
| `INVALID_ARGUMENT (400)` | `INVALID_TLD` | Product instance `<productInstanceId>` includes the benefit to register a domain with TLD `<TLD>`. You can't register a domain with another TLD using this product instance. | Check that the `<productInstanceID>` and the TLD are correct. Call [Adjust Product Instance Specifications](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/adjust-product-instance-specifications) to provide the missing benefit. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for details about the relevant `productID`. |
| `INVALID_ARGUMENT (400)` | `TLD_NOT_SUPPORTED` | Domain `<domainName>` can't be registered because the TLD `<tld>` isn't supported for Wix sites. | Contact the [Wix B2B sales team](mailto:bizdev@wix.com) to check which TLDs are supported. |
| `PERMISSION_DENIED (403)` | `PERMISSION_DENIED` | Permission denied for target account `<targetAccountId>`. | Make sure that the account ID is correct and that you have permissions to access the account. |
| `INVALID_ARGUMENT (400)` | `CANNOT_ASSIGN_DOMAIN_TO_FREE_SITE` | Domains can't be assigned to free Wix sites. | Make sure that the site you want to assign the domain to has an active [Premium plan](https://support.wix.com/en/article/upgrading-your-site-to-premium-3066683). You can use [Create Package](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2) to assign a Premium plan to your customer's site. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for information about the relevant `productID`. |
| `INVALID_ARGUMENT (400)` | `PRODUCT_INSTANCE_NOT_FOUND` | Subscription for product instance `<productInstanceId>` doesn't exist. | Check that the `productInstanceId` is correct. You can only register a domain to a Wix account that owns a [reseller product instance](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) for a domain with the specified TLD.|
| `INVALID_ARGUMENT (400)` | `INVALID_PRODUCT_INSTANCE` | Product instance `<productInstanceId>` doesn't include the benefit to register a domain. | Check that the `productInstanceId` is correct. You can call [Adjust Product Instance Specifications](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/adjust-product-instance-specifications) to provide the missing benefit. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for details about the relevant `productID`. |
| `INVALID_ARGUMENT (400)` | `PRODUCT_INSTANCE_NOT_ACTIVE` | Product instance `<productInstanceId>` has status `<status>`. You can only register a domain if the related product instance is `"ACTIVE"`. | You can only register a domain if the relevant Wix account or site has an active subscription for a Premium plan that supports domains of the specified TLD. Check that the `status` of the relevant product instance is `"ACTIVE"`. To check, call [Get Package](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/get-package). |
| `INVALID_ARGUMENT (400)` | `AWAITING_PRODUCT_ACTIVATION` | Product instance `<productInstanceId>` is `"ACTIVE"`, but you still need to wait before you can register a domain using it. | Try calling Create Registered Domain again in a couple of minutes. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) if the error persists. |
| `INVALID_ARGUMENT (400)` | `REGISTERED_DOMAIN_ALREADY_EXISTS` | Domain `<domainName>` has already a related `registeredDomain` object. | You can't call Create Registered Domain for a domain that's already registered or in the process of being registered. If the registration status is `"FAILED_REGISTRATION"`, you can call the endpoint again. |
| `INVALID_ARGUMENT (400)` | `DOMAIN_ALREADY_TAKEN` | Domain `<domainName>` has already been purchased. | You can only register domains that are still available for purchsase. You may call [Check Domain Availability](https://dev.wix.com/api/rest/account-level-apis/domain-search/check-domain-availability) or [Suggest Domains](https://dev.wix.com/api/rest/account-level-apis/domain-search/suggest-domains) to identify available domains. |
| `INVALID_ARGUMENT (400)` | `INVALID_BILLING_CYCLE` | Product instance `<productInstanceId>` from subscription `<subscriptionId>` has a billing cycle that doesn't support registering the domain. | Check that `<productInstanceID>` and the billing cycle are correct. You can use the Resellers API in case you need to [create](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) or [modfiy](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/adjust-product-instance-specifications) a subscription. |
| `INVALID_ARGUMENT (400)` | `SUBDOMAIN_NOT_SUPPORTED` | You can't register subdomains. | Make sure to register only root domains. |
| `INVALID_ARGUMENT (400)` | `SKU_NOT_FOUND` | Wix hasn't defined product instance `<productInstanceId>` properly. | Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for help. |

## Get Registered Domain errors

The [Get Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/get-registered-domain) endpoint might issue the following error messages:

| <div style="width:180px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| ------ | ------ | ------ | ------ |
| `INVALID_ARGUMENT (400)` | `REGISTERED_DOMAIN_NOT_FOUND` | Registered domain `<registeredDomainId>` doesn't exist. | Make sure that the ID of the registered domain is correct. |
