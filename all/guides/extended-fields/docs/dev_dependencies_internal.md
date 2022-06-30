SortOrder: 1
# Dev Dependencies

### Bazel target
```
"@crm//contacts/fields/contact-fields-app:proto_scala",
```

### GRPC Client

In loom-prime app:
```build
prime_app(
   ...
   rpcs = [
       "com.wixpress.contacts.fields.v4.ContactExtendedFieldsServiceV4",
    ],
   ...
)
```

In Loom:
```scala
import com.wixpress.contacts.fields.v4.ContactExtendedFieldsServiceV4WithCallScope
import com.wixpress.grpc.Clients

object MyServer extends App {
  // given Config contains the erb value for the rpc service

  val contactFieldsService = ContactExtendedFieldsServiceV4WithCallScope
         .stub(Clients.grpcChannel(config.grpcProxy), 
               _.withAuthority("com.wixpress.contacts.contacts-fields-app")
         )
 
  /// ... do things with contactFieldsService!
}
```

In Bootstrap:
```scala
  @Bean
  def contactExtendedFieldsServiceV4(clients: Clients,
               csp: ThreadLocalCallScopeProducer): ContactExtendedFieldsServiceV4BlockingGrpcClient = {
    ContactExtendedFieldsServiceV4WithCallScope.blockingStub(
        clients.grpcChannel(ContactsServerConfig.topology.grpcProxy), 
        csp, 
        _.withAuthority("com.wixpress.contacts.contacts-fields-app")
    )
  }
```

### REST Client

```bash
npm i --save @wix/ambassador-contacts-v4-extended-field
```

```typescript
import { listExtendedFields } from '@wix/ambassador-contacts-v4-extended-field/http';
import { HttpClient } from '@wix/http-client';
import { appDefIds, getCurrentInstance } from '@wix/business-manager-api';


const doListExtendedFields = () => {
    const instance = getCurrentInstance(appDefIds.metaSite);
    const httpClient = new HttpClient({ getAppToken: () => instance });
  
    return httpClient.request(
      listExtendedFields({})
    );
}
