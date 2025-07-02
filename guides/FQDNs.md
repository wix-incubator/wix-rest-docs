# About FQDNs

A Fully Qualified Domain Name (FQDN) is a unique identifier assigned to each Wix service entity.

The standard FQDN naming structure looks like: `wix.<domain?>.<product>.<version>.<entity>`.

For example:
- Wix eCommerce Cart ([REST](https://dev.wix.com/docs/rest/business-solutions/e-commerce/cart/introduction) | [SDK](https://dev.wix.com/docs/sdk/backend-modules/ecom/cart/introduction)) entity's FQDN is `wix.ecom.v1.cart`.
- Wix Multilingual's Machine Translation ([REST](https://dev.wix.com/docs/rest/business-management/multilingual/machine-translation/introduction) | [SDK](https://dev.wix.com/docs/sdk/backend-modules/multilingual/machine-translation/machine-translation/introduction)) entity's FQDN is `wix.multilingual.machine.v3.translatable_content`.

An entity's FQDN is returned in every webhook (except for [legacy webhooks](https://dev.wix.com/docs/rest/articles/getting-started/webhook-structure)) and may be required in endpoints that work with entities from other Wix services.
