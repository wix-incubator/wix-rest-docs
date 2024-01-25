SortOrder: 2
# Sample Use Cases & Flows: Domain DNS

This article shares a possible use case your implementation could support, as
well as a sample flow. You're not limited to this use case, but it can be a
helpful jumping off point for your planning.

## Update DNS records for a registered domain

You could purchase a domain through Wix and then update the MX and TXT records.
This allows you to connect the domain to a website that isn't build on Wix.

To update the DNS records for a registered domain:

1. Optional: In case the relevant site is a free Wix site, use the
   [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to assign a Premium plan to it. Make sure to save the `productInstanceId`.
1. Use the [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to create a product instance for the relevant domain TLD and privacy. Don't
   assign the product instance to a site, but keep it floating in the relevant
   account.
1. Call [Create Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/create-registered-domain)
   to start the domain registration process through Wix.
1. Use [Get Registered Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/registered-domains/registered-domain-v1/get-registered-domain)
   to confirm that the `status` has changed to `"PENDING_REGISTRATION"`.
1. Call [Update Dns Zone](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/update-dns-zone)
   to change the MX and TXT records in Google's Cloud DNS.
1. Connect the domain to the external site.

## Connect an external domain by nameservers to a Wix site

You could help Wix site owners connect an external domain by nameservers to
their site. Note that you can't use
[Update DNS Zone](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/update-dns-zone)
for external domains that are connected by pointing.

To connect an external domain by nameservers to a Wix site:

1. Optional: In case the relevant site is a free Wix site, use the
   [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to assign a Premium plan to it.
1. Register the domain through an external provider.
1. Call [Create Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/create-connected-domain)
   to start the connection process. Make sure to use
   `{"connectionType": "NAMESERVERS"}`.
1. Use [Get Connected Domain Setup Info](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-setup-info-v1/connected-domain-setup-info-object)
   to retrieve the new DNS record values. You find them in
   `connectedDomainSetupInfo.pointingRecords.aRecord.values`
   and `connectedDomainSetupInfo.pointingRecords.cnameRecord.value`.
1. Use [Update Dns Zone](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/update-dns-zone)
   to change the A and CNAME records in Google's Cloud DNS.
1. Call [Get Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/get-connected-domain)
   to monitor the connected domain's `dnsPropagationStatus` and confirm that it
   changes to `"COMPLETED"`.