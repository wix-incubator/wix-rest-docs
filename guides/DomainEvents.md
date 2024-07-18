# Webhook structure

Wix exposes webhooks for CUD actions and relevant additional actions in a standardized format. 

The data payload will include the following as an encoded JWT:

| Field name | Description | 
| :-------------- | :------- |  
| `data` | |
| `data.eventType`| Webhook event type. For example: `wix.contacts.v4.contact_merged`. |
| `data.instanceId`| App instance ID, the identifier of the site where the event occurred. |
| `data.data`| Data payload as stringified JSON. See the **Data payload** table. |
| `data.identity` | Identity data as stringified JSON. | // Identity of what??
| `data.identity.identityType`| Identity type that triggered this event. Supported values: `ANONYMOUS_VISITOR`, `MEMBER`, `WIX_USER`, `APP`. See [Identities](https://dev.wix.com/docs/build-apps/develop-your-app/access/about-identities).|
| `data.identity.anonymousVisitorId` | Visitor ID. |
| `data.identity.memberId`|  Member ID. |
| `data.identity.wixUserId` | Wix User ID. | 
| `data.identity.appId` | App ID. | 
    

## Data payload
The `data.data` payload will always include the following fields:

| Field name | Description | 
| :-------------- | :------- |  
| `id` | Webhook event ID. Note that this ID is not related to the ID of the affected entity. |
| `slug` | Event type. Common values include: `created`, `updated`, and `deleted`. Non-CUD actions will return a slug that corresponds to the action taken. For example, the [Merge Contacts](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/contacts/contact-v4/merge-contacts) endpoint triggers a webhook with slug: `merge`. |
| `entityFqdn` | Fully qualified domain name of the entity associated with the event. |
| `entityId` | ID of the affected entity. For example, the affected contact ID. |
| `eventTime` | Timestamp when the webhook was triggered. |
| `triggeredByAnonymizeRequest` | Whether this change was triggered by a request to apply a privacy regulation. |
| `originatedFrom` | The slug of the action that triggered this change, when applicable. For example, when a contact is deleted due to merging of 2 contacts, this field will be populated with `merge`. |


In addition, each webhook will include one of the following fields with data specifc to the event:
| Field name | Description | 
| :-------------- | :------- |  
| `createdEvent` | Complete entity that was created. |
| `updatedEvent` | Complete entity that was updated. |
| `actionEvent` | Data related to the non-standard action that was taken, generally including the complete entity. For example, the [Contact Merged](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/contacts/contact-v4/contact-merged) webhook returns the IDs of the source and target contact IDs in addition to the complete updated entity.|
| `deletedEvent` | ID of the entity that was deleted. |

## Legacy webhooks
Wix also returns some legacy webhooks that don't follow the above standard.
For example, the legacy Wix Stores [Product Changed](https://dev.wix.com/docs/rest/business-solutions/stores/catalog/product-changed) webhook only returns the fields that were updated, and these fields are returned in a flat list, not according to the object structure returned in the calls.
We're working to replace these webhooks with new ones that align with the above standard, but in the meantime your may depend on a webhook that doesn't align with the standard structure.
