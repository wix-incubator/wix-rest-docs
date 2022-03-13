SortOrder: 1
# Dev Dependencies

### Bazel target
```
"@crm//contacts/labels/contact-labels-app:proto_scala",
```

### GRPC Client

In loom-prime app:
```build
prime_app(
   ...
   rpcs = [
       "com.wixpress.contacts.labels.v4.ContactLabelsServiceV4",
    ],
   ...
)
```

In Loom:
```scala
import com.wixpress.contacts.labels.v4.ContactLabelsServiceV4WithCallScope
import com.wixpress.grpc.Clients

object MyServer extends App {
  // given Config contains the erb value for the rpc service

  val contactLabelsService = ContactLabelsServiceV4WithCallScope
         .stub(Clients.grpcChannel(config.grpcProxy), 
               _.withAuthority("com.wixpress.contacts.contacts-labels-app")
         )
 
  /// ... do things with contactLabelsService!
}
```

In Bootstrap:
```scala
  @Bean
  def contactLabelsServiceV4(clients: Clients,
               csp: ThreadLocalCallScopeProducer): ContactLabelsServiceV4BlockingGrpcClient = {
    ContactLabelsServiceV4WithCallScope.blockingStub(
        clients.grpcChannel(ContactsServerConfig.topology.grpcProxy), 
        csp, 
        _.withAuthority("com.wixpress.contacts.contacts-labels-app")
    )
  }
```

### REST Client
```bash
npm i --save @wix/ambassador-contacts-v4-label
```

```typescript
import { listLabels } from '@wix/ambassador-contacts-v4-label/http';
import { HttpClient } from '@wix/http-client';
import { appDefIds, getCurrentInstance } from '@wix/business-manager-api';


const doListLabels = () => {
    const instance = getCurrentInstance(appDefIds.metaSite);
    const httpClient = new HttpClient({ getAppToken: () => instance });
  
    return httpClient.request(
      listLabels({})
    );
}
```
