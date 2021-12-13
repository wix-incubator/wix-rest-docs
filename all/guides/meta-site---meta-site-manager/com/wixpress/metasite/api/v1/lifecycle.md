SortOrder: 2
## MetaSiteLifecycle

An [API](https://github.com/wix-private/meta-site/blob/master/meta-site-protos/msm-protos/src/main/proto/com/wixpress/metasite/api/v1/meta_site_lifecycle.proto) to manage the lifecycle of a MetaSite.

This API is exposed via Legacy JSON-RPC in `com.wixpress.metasite.wix-meta-site-manager-webapp`

### Consuming Via Legacy JSON-RPC

Add the following dependency: `@meta_site//meta-site-protos/msm-protos`

Use this erb-helper:
```
<%= rpc_service_url('com.wixpress.wix-meta-site-manager-webapp') %>
```
