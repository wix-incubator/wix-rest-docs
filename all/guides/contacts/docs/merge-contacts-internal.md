SortOrder: 9
# Merge Contacts

Nowadays, many site owners are suffering from duplicated contacts.
These duplications can happen for a number of different reasons.
Therefore we launched the `Contacts Merge` feature
to allow site owners and contributors to merge duplicate contacts.
Any contact that is not a site member can be merged into another contact.

## Merge in the Dashboard (UI)

In order to merge two or more contacts, go to Contacts List in the dashboard and select at least two contacts (up to 5). 
The _Merge Contacts_ will appear, click and follow the instructions.


## Merge endpoint

You can find `Merge Contacts` under the
[Contacts Service API][contacts-service-proto].

## Events

When some contacts are merged, the following events will be published:

* [Merged Contact Domain Event][contact-merged-event]
   *  (type = `Action`, slug = `merged`).
   *  Payload will contain the `targetContactId` and `sourceContactIds`.
  
  
* [Updated Contact Domain Event][contact-updated-event] for the target contact.
    * Payload will containt the updated info.


* [Deleted Contact Domain Event][contact-deleted-event] for all source contacts.
  *  (type = `Deleted`, originatedFrom = `merge`).



## Integration

If your vertical keeps track of the site's contact IDs,
you should listen to [Merged Contact Domain Event][contact-merged-event]
(type = `Action`, slug = `merged`).

In case you are using SDL please read [here](https://github.com/wix-private/server-infra/tree/master/iptf/simple-data-layer#contact-merged-events) for built-in support in this feature. 

The following code snippet illustrates a possible approach:

```scala
import com.wixpress.contacts.core.api.v4.events.ContactMerged
val domainEventConsumer = com.wixpress.greyhound.MessageHandler.aMessageHandler[DomainEvent]((msg: DomainEvent) => {

  implicit val mapper: JsonMapper = ProtobufIdlObjectMapper.configure(JsonMapper.objectMapperFromTemplate)

  (msg.body, msg.originatedFrom) match {
    case (Body.ActionEvent(event), _) => {
      msg.slug match{
        case "merged"=> {
          val contactMerged = event.bodyAsJson.as[ContactMerged]
          //your logic for contact merged
        }
        case _ => //doNothing
      }
    }
    case (Body.DeletedEvent(_), Some("merge")) =>
      //doNothing, keep this to skip Deleted as a result of Merge
    
    case (Body.DeletedEvent(_), originatedFrom) =>
      //your logic for contact deleted
    
    case _ => // doNothing
  }

}).withMapper(mapper).build

GreyhoundConsumerSpec.aGreyhoundConsumerSpec("domain_events_wix.contacts.v4.contact", domainEventConsumer).withGroup("grp")
```

Your task is to scan your database
and make sure all the `contactMerged.sourceContactIds`
are replaced with `contactMerged.targetContactId`.

Also, make sure, if you have any logic for deleted contacts, 
to skip it if the **DELETED** events have `originatedFrom="merge"`.

## Fallbacks

We will keep supporting the merged contact ids on GetById endpoint.
That means that if `Contact A` was merged to `Contact B`
The result of GetContact(`Contact A Id`) will be `Contact B`
You should be aware that this is the only endpoint that supports the merged IDs.
That means that QueryBy(`Contact A Id`) will not return `Contact B`

## GDPR consideration

Merged contact IDs (previous source contactId)
will be sent as part of UoU GDPR request.
This is in place to cover verticals that did not integrate
with the Contact Merged event above.

## Questions and to get help

For any questions,
feel free to contact us on [#contacts][slack-contacts] on Slack.

[contacts-service-proto]: https://github.com/wix-private/crm/blob/master/contacts/core/contacts-api/src/main/proto/v4/contacts_service.proto
[contact-merged-event]: crm.contacts.contacts-v4.contact-merged-domain-event
[contact-updated-event]: crm.contacts.contacts-v4.contact-updated-domain-event
[contact-deleted-event]: crm.contacts.contacts-v4.contact-deleted-domain-event
[slack-contacts]: https://wix.slack.com/archives/C3Y3H3RTL
