SortOrder: 10
# Merge Contacts

Nowadays, many site owners are suffering from duplicated contacts.
These duplications can happen for a number of different reasons.
Therefore we launched the `Contacts Merge` feature
to allow site owners and contributors to merge duplicate contacts.
Any contact that is not a site member can be merged into another contact.

## Merge endpoint

You can find `Merge Contacts` under the
[Contacts Service API][contacts-service-proto].

## Integration

If your vertical keeps track of the site's contact IDs,
you should listen to [Merged Contact Domain Event][contact-merged-event]
(type = `Action`, slug = `merged`).

The following code snippet illustrates a possible approach:

```scala
import com.wixpress.contacts.core.api.v4.events.ContactMerged
val domainEventConsumer = com.wixpress.greyhound.MessageHandler.aMessageHandler[DomainEvent]((msg: DomainEvent) => {

  implicit val mapper: JsonMapper = ProtobufIdlObjectMapper.configure(JsonMapper.objectMapperFromTemplate)

  msg.body match {
    case Body.ActionEvent(event)=> {
      msg.slug match{
        case "merged"=> {
          val contactMerged = event.bodyAsJson.as[ContactMerged]
          //your logic
        }
        case _ => //doNothing
      }
    }
   case _ => // doNothing
  }

}).withMapper(mapper).build

GreyhoundConsumerSpec.aGreyhoundConsumerSpec("domain_events_wix.contacts.v4.contact", domainEventConsumer).withGroup("grp")
```

Your task is to scan your database
and make sure all the `contactMerged.sourceContactIds`
are replaced with `contactMerged.targetContactId`.

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
feel free to contact us on [#contacts-merge][slack-contacts-merge] on Slack.

[contacts-service-proto]: https://github.com/wix-private/crm/blob/master/contacts/core/contacts-api/src/main/proto/v4/contacts_service.proto
[contact-merged-event]: crm.contacts.contacts-v4.contact-merged-domain-event
[slack-contacts-merge]: https://wix.slack.com/archives/C019MHAFV50