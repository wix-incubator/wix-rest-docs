SortOrder: 9
# About Domain Events

As of V4 Contacts Service, we started to use Domain Events.
Those events replace the previous events sent by contacts service.
All consumers but move to those events, all the older ones will be deprecated.

The existing domain events are:

- Contact Created Domain Event
- Contact Updated Domain Event
- Contact Deleted Domain Event
- Contact Merged Domain Event

You can read about each of those events in a dedicated section.
The topic of those new events is `domain_events_wix.contacts.v4.contact`.
The `entityId` field on the event body is the `contact id`,
and for each type of event there is a field for the slug (String)
and info of the event:

- Contact Created: slug is `created` and the info is the field `createdEvent`
- Contact Updated: slug is `updated` and the info is the field `updatedEvent`
- Contact Deleted: slug is `deleted` and the info is the field `deletedEvent` (which is empty)
- Contact Merged: slug is `merged` and the info is the field `actionEvent`
- Contact Submitted: slug is `submitted` and the info is the field `actionEvent`

For each contact domain event, there are also:

- `eventTime` field, which is a string with the event timestamp
- boolean `triggeredByAnonymizeRequest` — whether this event was triggered
  as a result of a privacy regulation application
- `entityFqdn`, which equals `wix.contacts.v4.contact`

## Legacy events 

The topics that will be deprecated:
- `crm-contacts-events`. With the respective [payload][v1-events] of each events (`Created, Updated, Deleted`)

- `contacts-changed-events`. With message [ContactChangedEvent][bootstrap-events-1].

- `contacts-update`. With message [UpdateContactMessage][bootstrap-events-2]

[v1-events]: https://github.com/wix-private/crm/blob/master/contacts/core/contacts-api/src/main/proto/v1/webhooks/contact_events.proto
[bootstrap-events-1]: https://github.com/wix-private/crm/blob/master/wix-contacts-server/wix-contacts-server-api/src/main/scala/com/wixpress/contacts/api/greyhound/ContactChangedEvent.scala
[bootstrap-events-2]: https://github.com/wix-private/crm/blob/master/wix-contacts-server/wix-contacts-server-api/src/main/scala/com/wixpress/contacts/api/greyhound/UpdateContactMessage.scala