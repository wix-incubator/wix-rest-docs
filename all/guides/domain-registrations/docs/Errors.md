SortOrder: 4
# Error messages


This articles outlines error messages that might be issued when calling endpoints of the Domain Registration API.


## Register Domain Errors


The [Register Domain](https://dev.wix.com/api/rest/account-level-apis/domains/register-domain) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `INVALID_ARGUMENT (400)` | `INVALID_DOMAIN` | Domain `<domainName>` can't be registered. | Check that the TLD is supported by Wix and that the domain is still available for purchase. |
| `INVALID_ARGUMENT (400)` | `DOMAIN_TOO_LONG` | Domain `<domainName>` can't be registered because the domain name is too long. | Make sure that the domain name (excluding TLD) doesn't include more than 63 characters. |
| `INVALID_ARGUMENT (400)` | `DOMAIN_TOO_SHORT` |  Domain `<domainName>` can't be registered because the domain name is too short. | Make sure that the domain name (excluding TLD) includes at least 3 characters.  |
| `INVALID_ARGUMENT (400)` | `TLD_NOT_SUPPORTED` | Domain `<domainName>` can't be registered because the TLD `<tld>` isn't supported for Wix sites. | Contact the [Wix B2B sales team](mailto:bizdev@wix.com) to check which TLDs are supported for Wix sites. |
| `PERMISSION_DENIED (403)` | `PERMISSION_DENIED` | Permission denied for target account `<targetAccountId>`. | Make sure that you have permissions to access the account. |
| `INVALID_ARGUMENT (400)` | `PRODUCT_INSTANCE_NOT_FOUND` | Subscription for product instance `<productInstanceId>` doesn't exist. | Check that the `productInstanceID` is correct. You can only register a domain if the site owners have a Wix Premium plan that includes registering a domain. If it's missing, you can use the [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) to create such a subscription. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for details about the relevant `productID` in the Create Package call for different domain TLDs. |
| `INVALID_ARGUMENT (400)` | `DOMAIN_REGISTRATION_ALREADY_EXISTS` | Domain `<domain>` has already a related `domainRegistration` object. | You can't call Register Domain for a domain that's already registered or in the process. You can call Register Domain again, if the registration status is `FAILED`. |
| `INVALID_ARGUMENT (400)` | `DOMAIN_ALREADY_TAKEN` | Domain `<domainName>` has already been purchased. | You can register only domains that are still available for purchsase. You may use the [Check Domain Availability](https://dev.wix.com/api/rest/account-level-apis/domain-search/check-domain-availability) and [Suggest Domains](https://dev.wix.com/api/rest/account-level-apis/domain-search/suggest-domains) endpoints to identify domains available for purchase. |
| `INVALID_ARGUMENT (400)` | `INVALID_PRODUCT_INSTANCE` | Product instance `<productInstanceId>` doesn't include the benefit to register a domain. | Check that the `productInstanceId` is correct. You can use the [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) to create a new package or [adjust a product instance](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/adjust-product-instance-specifications) to allow the site owners to register the domain. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for details about the relevant `productID`. |
| `INVALID_ARGUMENT (400)` | `INVALID_BILLING_CYCLE` | Product instance `<productInstanceId>` from subscription `<subscriptionId>` has a billing cycle that doesn't support registering the domain. | Check that the `<productInstanceID>` and the billing cycle are correct. You can use the [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) to create a new Wix Premium plan for the site owners if needed. |
| `INVALID_ARGUMENT (400)` | `INVALID_TLD` | Product instance `<productInstanceId>` includes the benefit to register a domain with TLD `<TLD>`. You can't register a domain with another TLD using this product instance. | Check that the `<productInstanceID>` and the TLD are correct. You can use the [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/introduction) to [create a package](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/create-package-v2) or [adjust a product instance](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/adjust-product-instance-specifications) to allow the site owners to register a domain with this TLD. Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for details about the relevant `productID`. |
| `INVALID_ARGUMENT (400)` | `SUBDOMAIN_NOT_SUPPORTED` | You can't register subdomains. | Make sure to register only root domains. |
| `INVALID_ARGUMENT (400)` | `SKU_NOT_FOUND` | Wix hasn't defined product instance `<productInstanceId>` properly. | Contact the [Wix B2B sales team](mailto:bizdev@wix.com) for help. |
| `INVALID_ARGUMENT (400)` | `PRODUCT_INSTANCE_NOT_ACTIVE` | Product instance `<productInstanceId>` has status `<status>`. You can only register a domain if the related product instance is `ACTIVE`. | You can only register a domain if the relevant Wix account has an active subscription for a Premium plan that supports domains of the specified TLD. Check that the product instance related to your domain registration is `ACTIVE`. You can do so with the [Get Package](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/get-package) endpoint of the [Resellers API](https://dev.wix.com/api/rest/account-level-apis/resellers/product-instances/product-instance-object). |
| `INVALID_ARGUMENT (400)` | `AWAITING_PRODUCT_ACTIVATION` | Product instance `<productInstanceId>` is `ACTIVE`, but you still need to wait before you can register a domain using it. | Try calling Register Domain again in a couple of minutes. If it's still not working contact the [Wix B2B sales team](mailto:bizdev@wix.com) for help. |

## Get Domain Registration Domain Errors


The [Get Domain Registration](https://dev.wix.com/api/rest/account-level-apis/domains/get-domain-registration) endpoint might issue the following error messages:

| <div style="width:200px">HTTP status</div> | <div style="width:250px">Error code</div> | <div style="width:280px">Error message </div> | <div style="width:300px">Troubleshooting </div> |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| `INVALID_ARGUMENT (400)` | `DOMAIN_REGISTRATION_NOT_FOUND` | Domain registration `<domainRegistrationID>` doesn't exist. | Make sure that the ID of the domain registration is correct. |
