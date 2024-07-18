# Webhook structure

Wix exposes webhooks for CUD actions and relevant additional actions in a standardized format. The data payload will always include the following fields:

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
| `actionEvent` | Data related to the non-standard action that was taken. For example, the [Contact Merged](https://dev.wix.com/docs/rest/crm/members-contacts/contacts/contacts/contact-v4/contact-merged) webhook returns the IDs of the source and target contact IDs in addition to the complete updated entity.|
| `deletedEvent` | ID of the entity that was deleted. |

