SortOrder: 7
# Dev Dependencies

### Bazel target
```
"@crm//contacts/core/contacts-api/src/main/proto:proto_scala",
```

### GRPC Client

In loom-prime app:
```build
prime_app(
   ...
   rpcs = [
       "com.wixpress.contacts.core.api.v4.ContactsServiceV4",
    ],
   ...
)
```

In Loom:
```scala
import com.wixpress.contacts.core.api.v4.ContactsServiceV4WithCallScope
import com.wixpress.grpc.Clients

object MyServer extends App {
  // given Config contains the erb value for the rpc service

  val contactsServiceV4 = ContactsServiceV4WithCallScope
         .stub(Clients.grpcChannel(config.grpcProxy), 
               _.withAuthority("com.wixpress.contacts.contacts-app")
         )
 
  /// ... do things with contactsServiceV4!
}
```

In Bootstrap:
```scala
  @Bean
  def contactsServiceV4(clients: Clients,
               csp: ThreadLocalCallScopeProducer): ContactsServiceV4BlockingGrpcClient = {
    ContactsServiceV4WithCallScope.blockingStub(
        clients.grpcChannel(ContactsServerConfig.topology.grpcProxy), 
        csp, 
        _.withAuthority("com.wixpress.contacts.contacts-app")
    )
  }
```

### REST Client

```bash
npm i --save @wix/ambassador-contacts-v4-contact
```

```typescript
import { listContacts } from '@wix/ambassador-contacts-v4-contact/http';
import { HttpClient } from '@wix/http-client';
import { appDefIds, getCurrentInstance } from '@wix/business-manager-api';


const doListContacts = () => {
    const instance = getCurrentInstance(appDefIds.metaSite);
    const httpClient = new HttpClient({ getAppToken: () => instance });
  
    return httpClient.request(
      listContacts({})
    );
}
```
