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
npm -i @wix/ambassador-contacts-labels-app
```

```typescript
import { ContactsLabelsApp } from '@wix/ambassador-contacts-labels-app/http';
import { appDefIds, getCurrentInstance } from '@wix/business-manager-api';

const contactLabelsServiceV4 = (instance: string) => {
    return ContactsLabelsApp('/_api/contacts/')
        .ContactLabelsServiceV4()({
            Authorization: instance,
        });
};

const listLabels = () => {
    const instance = getCurrentInstance(appDefIds.metaSite);
    return contactLabelsServiceV4(instance).listLabels({});
}
```