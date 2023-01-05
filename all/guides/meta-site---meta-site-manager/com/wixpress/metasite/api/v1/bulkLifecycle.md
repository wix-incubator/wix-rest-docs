SortOrder: 3
## BulkMetaSiteLifecycle

An [API](https://github.com/wix-private/meta-site/blob/master/protos/msm-protos/src/main/proto/com/wixpress/metasite/api/v1/bulk_meta_site_lifecycle.proto) to manage the lifecycle of a several MetaSites.

This API is exposed via gRPC in `com.wixpress.metasite.msm-writer`

### gRPC

To consume this API via gRPC use `com.wixpress.metasite.msm-writer` authority.

Add the following dependency: `@meta_site//meta-site-protos/msm-protos`

Example:

```scala
import com.wixpress.metasite.api.v1._
val channel = Clients.grpcChannel(config.grpcProxy)

val api = BulkMetaSiteLifecycleWithCallScope.stub(
  channel,
  _
    .withAuthority("com.wixpress.metasite.msm-writer")
    .withDeadline(10, TimeUnit.SECONDS)
)

// ...
implicit val cs: CallScope = ... 
val msIds = ...
for {
  response <- api.bulkMoveToTrash(BulkMoveToTrashRequest(msIds))
} yield response.results.partition(_.movedToTrash)
```
