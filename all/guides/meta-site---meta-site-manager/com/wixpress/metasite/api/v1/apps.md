SortOrder: 1
## MetaSiteApps

An [API](https://github.com/wix-private/meta-site/blob/master/protos/msm-protos/src/main/proto/com/wixpress/metasite/api/v1/meta_site_apps.proto) to manage the lifecycle of TPAs.

This API is exposed via gRPC/REST in `com.wixpress.metasite.msm-writer`

### Consuming via gRPC

To consume this API via gRPC use `com.wixpress.metasite.msm-writer` authority.

Dependency: `@meta_site//meta-site-protos/msm-protos`

Example:

```scala
import com.wixpress.metasite.api.v1._
import com.wixpress.metasite.api.v1.ProvisionRequest.App
val channel = Clients.grpcChannel(config.grpcProxy)

val metaSiteApps = MetaSiteAppsWithCallScope.stub(
  channel,
  _
    .withAuthority("com.wixpress.metasite.msm-writer")
    .withDeadline(5, TimeUnit.SECONDS)
)

// ...
implicit val cs: CallScope = ... // metaSiteId OR signed instance is expected in Authorization header
for {
  response <- metaSiteApps.provision(ProvisionRequest().withApps(Seq(App("...")))
  metaSite = response.metaSite.getOrElse(throw new IllegalStateException("if meta site not found - future will be failed"))
} yield (metaSite.metaSiteId, metaSite.ownerId)
```
