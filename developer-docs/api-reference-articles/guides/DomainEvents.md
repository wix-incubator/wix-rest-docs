# Webhook structure

Wix exposes webhooks for create, update, and delete actions, and relevant additional actions.
Most webhooks are organized in a standardized format, as described below. Wix also has some legacy webhooks that don't comply with the standardized format.

## Standardized webhooks

The majority of webhooks exposed by Wix align with the standardized format described below.

The data payload consists of the following information encoded as a JWT:

| Field name | Description | 
| :-------------- | :------- |  
| `data` | |
| `data.eventType`| Webhook event type, as documented in each webhook. For example: `wix.contacts.v4.contact_merged`. |
| `data.instanceId`| App instance ID, the identifier of the site where the event occurred. |
| `data.data`| Data payload as stringified JSON. See the **Data payload** table. |
| `data.identity` | Identity data as stringified JSON. See the **Identity payload** table. | // Identity of what??

### Data payload
The `data.data` payload includes the following fields:

| Field name | Description | 
| :-------------- | :------- |  
| `id` | Webhook event ID. Note that this ID is not related to the ID of the affected entity. |
| `slug` | Event type. Common values include: `created`, `updated`, and `deleted`. Non-standard actions return a slug that corresponds to the action taken, as documented in each webhook. For example, the [Merge Contacts](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/contacts/contact-v4/merge-contacts) endpoint triggers a webhook with slug: `merge`. |
| `entityFqdn` | Fully qualified domain name (FQDN) of the entity associated with the event, as documented in each webhook. |
| `entityId` | ID of the affected entity. For example, the affected contact ID. |
| `eventTime` | Timestamp when the event was triggered, in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format and UTC time. |
| `triggeredByAnonymizeRequest` | Whether this change was triggered by a request to apply a privacy regulation. |
| `originatedFrom` | The slug of the action that triggered this change, when applicable, as documented in each webhook. For example, when a contact is deleted due to merging of 2 contacts, this field is populated with `merge`. |


In addition, each webhook includes one of the following fields with data specific to the event, based on the slug type:
| Field name | Slug | Description | 
| :-------------- | :------- |  :------- |  
| `createdEvent` | `created` | Complete entity that was created. |
| `updatedEvent` | `updated` | Complete entity that was updated. |
| `deletedEvent` | `deleted` | ID of the entity that was deleted. |
| `actionEvent` | Non-standard, as documented in each webhook. | Data related to the non-standard action that was taken, generally including the complete entity. For example, the [Contact Merged](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/contacts/contact-v4/contact-merged) webhook returns the IDs of the source and target contact IDs in addition to the complete updated entity.|



### Identity payload

The `data.identity` payload includes the type and ID of the identity that triggered the event:

| Field name | Description | 
| :-------------- | :------- |  
| `data.identity.identityType`| Identity type that triggered this event. Supported values: `ANONYMOUS_VISITOR`, `MEMBER`, `WIX_USER`, `APP`. See [Identities](https://dev.wix.com/docs/build-apps/develop-your-app/access/about-identities).|
| One of: |
| `data.identity.anonymousVisitorId` | Visitor ID. |
| `data.identity.memberId`|  Member ID. |
| `data.identity.wixUserId` | Wix User ID. | 
| `data.identity.appId` | App ID. | 

## Legacy webhooks
Wix also returns some legacy webhooks that don't follow the above standard.
For example, the legacy Wix Stores [Product Changed](https://dev.wix.com/docs/rest/business-solutions/stores/catalog/product-changed) webhook only returns the fields that were updated, and these fields are returned in a flat list, not according to the full object structure.
We're working to replace these webhooks with new ones that align with the above standard, but in the meantime you may depend on a webhook that doesn't align with the standard structure.
