SortOrder: 0
## MetaSiteReadApi

This [API](https://github.com/wix-private/meta-site/blob/master/protos/msm-protos/src/main/proto/com/wixpress/metasite/api/v1/meta_site_api.proto) aims to be the single read API for `wix-meta-site-manager-webapp`, it is a platformized API such that it:

* Uses API GW client to implicitly take identity (MSID/appDefId+instanceId).
* Is Protobuf based.
* Supports `FieldMask` based projections, please **avoid** sending an empty `FieldMask` as the entire DTO will be returned in that case.
* Is a joint effort with platformization team.

This API currently exposes only a part of the entire MetaSite object, this is done on purpose to avoid exposing internal implementation details and to replace old abstractions. If you feel you want to use this API but are missing some information please feel free to contact us via `#meta-site-republic` on Slack.

### gRPC

To consume this API via gRPC use `com.wixpress.metasite.msm-server` authority.

Dependency: `@meta_site//meta-site-protos/msm-protos`

Example:

```scala
import com.wixpress.metasite.api.v1._
val channel = Clients.grpcChannel(config.grpcProxy)

val metaSiteReadApi = MetaSiteReadApiWithCallScope.stub(
  channel,
  _
    .withAuthority("com.wixpress.metasite.msm-server")
    .withDeadline(3, TimeUnit.SECONDS)
)

// ...
implicit val cs: CallScope = ... // metaSiteId OR signed instance is expected in Authorization header
for {
  response <- metaSiteReadApi.get(GetRequest().withResponseData(FieldMask(Seq("metaSiteId", "ownerId"))))
  metaSite = response.metaSite.getOrElse(throw new IllegalStateException("if meta site not found - future will be failed"))
} yield (metaSite.metaSiteId, metaSite.ownerId)
```

### Legacy JSON-RPC

Use this erb-helper:
```
<%= rpc_service_url('com.wixpress.wix-meta-site-manager-webapp') %>
```

Notice, that it's not a desired way of consumption of this API. gRPC is a preferred way.

### Utils

To resolve EditorType:

```
@meta_site//scala/com/wixpress/metasite/api/v1/util
```

```
import com.wixpress.metasite.api.v1.util.MetaSiteUtils

implicit val cs: CallScope = ... // metaSiteId OR signed instance is expected in Authorization header
for {
  response <- metaSiteReadApi.get(GetRequest().withResponseData(FieldMask(MetaSiteUtils.editorTypeFields)))
  metaSite = response.metaSite.getOrElse(throw new IllegalStateException("if meta site not found - future will be failed"))
} yield MetaSiteUtils.editorType(metaSite)
```
