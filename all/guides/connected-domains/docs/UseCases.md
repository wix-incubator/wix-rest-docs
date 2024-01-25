SortOrder: 1
# Sample Use Cases & Flows: Connected Domains

This article shares a possible use case your app could support, as well as an example flow.
You're certainly not limited to this use case, but it can be a helpful jumping off point
as you plan your app's implementation.

## Connect an external domain using name servers

Your app could help site owners connect an external domain using name servers
to their Wix site.

To connect an external domain using name servers to a Wix site:

1. Optional: In case the relevant site is a free Wix site, use the
   [Resellers API](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
   to assign a Premium plan to it. Contact the
   [Wix B2B sales team](mailto:bizdev@wix.com) for details about supported
   product IDs.
1. Register the domain through an external provider.
1. Call [Create Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/create-connected-domain)
   to start the connection process. Make sure to use
   `{"connectionType": "NAMESERVERS"}`.
1. Use [Get Connected Domain Setup Info](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-setup-info-v1/get-connected-domain-setup-info)
   to retrieve the new DNS record values. You find them in
   `connectedDomainSetupInfo.pointingRecords.aRecord.values`
   and `connectedDomainSetupInfo.pointingRecords.cnameRecord.value`.
1. Use [Update Dns Zone](https://dev.wix.com/docs/rest/api-reference/account-level-apis/domain-dns/update-dns-zone)
   to change the A and CNAME records in Google's Cloud DNS.
1. Call [Get Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/get-connected-domain)
    to monitor the connected domain's `dnsPropagationStatus` and confirm that it changes to `"COMPLETED"`.

## Connect an external domain by pointing

Your app could help site owners connect an external domain by pointing
to their Wix site.

To connect an external domain by pointing to a Wix site:

1. Use [Create Package](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
    of the Resellers API to assign a Wix Premium plan to the Wix site. Contact the
    [Wix B2B sales team](mailto:bizdev@wix.com) for details about supported product IDs.
1. Call [Create Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/create-connected-domain).
1. Use [Get Connected Domain Setup Info](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-setup-info-v1/get-connected-domain-setup-info)
    to retrieve the new DNS record values. You find them in
    `connectedDomainSetupInfo.pointingRecords.aRecord.values` and
    `connectedDomainSetupInfo.pointingRecords.cnameRecord.value`.
1. Assist the site owners with setting up the new A and CNAME records. This can't be
    done using Wix APIs, you must use the infrastructure of the external domain
    registrar.
1. Call [Get Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/get-connected-domain)
    to monitor the connected domain's `dnsPropagationStatus` and confirm that it changes to `"COMPLETED"`.

## Connect a subdomain

Your app could help site owners connect a subdomain
to their Wix site.

To connect a subdomain to a Wix site:

1. Use [Create Package](https://dev.wix.com/docs/rest/api-reference/account-level-apis/resellers/packages-and-product-instances/create-package-v2)
    of the Resellers API to assign a Wix Premium plan to the Wix site. Contact the
    [Wix B2B sales team](mailto:bizdev@wix.com) for details about supported product IDs.
1. Call [Create Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/create-connected-domain).
1. Use [Get Connected Domain Setup Info](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-setup-info-v1/get-connected-domain-setup-info)
    to retrieve the new DNS record values. You find them in
    `connectedDomainSetupInfo.subdomainRecords.cnameRecords.value`.
1. Assist the site owners with setting up the new CNAME records. This can't be
    done using Wix APIs, you must use the infrastructure of the external
    domain registrar.
1. Call [Get Connected Domain](https://dev.wix.com/docs/rest/api-reference/account-level-apis/connected-domains/connected-domain-v1/get-connected-domain)
    to monitor the connected domain's `dnsPropagationStatus` and confirm that it changes to `"COMPLETED"`.