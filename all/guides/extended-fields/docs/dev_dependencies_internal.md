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
npm -i @wix/ambassador-contacts-fields-app
```

```typescript
import { ContactsFieldsApp } from '@wix/ambassador-contacts-fields-app/http';
import { appDefIds, getCurrentInstance } from '@wix/business-manager-api';

const contactExtendedFieldsServiceV4 = (instance: string) => {
    return ContactsFieldsApp('/_api/contacts/')
        .ContactExtendedFieldsServiceV4()({
            Authorization: instance,
        });
};

const listFields = () => {
    const instance = getCurrentInstance(appDefIds.metaSite);
    return contactExtendedFieldsServiceV4(instance).listExtendedFields({});
}
```