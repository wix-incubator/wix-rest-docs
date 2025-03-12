SortOrder: 0
# About the Inbox API

The Inbox API allows you to
communicate with a site's visitors, contacts, and members
through Wix Chat, SMS, a Facebook business page, or other channels.
Visitor activities on the site and 3rd-party services
can also be displayed in Inbox conversations.

The Inbox API exposes functionality for working with a site's inbox.
With the Inbox API, you can:

- [Send messages](https://dev.wix.com/api/rest/inbox/messages/send-message) on behalf of the business or a visitor.
- [Retrieve conversations](https://dev.wix.com/api/rest/inbox/conversations/get-or-create-conversation) between a visitor and the business.
- Handle webhooks when messages are sent to [a visitor](https://dev.wix.com/api/rest/inbox/messages/message-sent-to-participant-webhook) or [the business](https://dev.wix.com/api/rest/inbox/messages/message-sent-to-business-webhook), when a [message button is clicked](https://dev.wix.com/api/rest/inbox/messages/button-interacted-webhook), or when [conversations are merged](https://dev.wix.com/api/rest/inbox/conversations/conversations-merged-webhook).

[Read more about how site contributors work with Wix Inbox][kb-inbox].

## Use case
+ [Sync messages from an external service](https://dev.wix.com/docs/rest/crm/communication/inbox/example-flows#sync-messages-from-an-external-service)
+ [Add contact activities from another service](https://dev.wix.com/docs/rest/crm/communication/inbox/example-flows#add-contact-activities-from-another-service)

## Terminology

- A **message** is sent from the business to the visitor
  or from the visitor to the business.
  Messages can be one of these types: `basic`, `minimal`, `template`, `form`, `system`.
  [Learn more about message types.][message-types]
- A **conversation** is a collection of messages that takes place between two or more participants.
  Conversations are displayed in the site's [Inbox][inbox-deeplink],
  one conversation per site visitor, contact, or member.
- A **participant** is the site visitor, contact, or member.
  [Learn more about types of participant IDs.][visitor-id-types]

[kb-inbox]: https://support.wix.com/en/article/wix-inbox-getting-started
[inbox-deeplink]: https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Finbox
[message-types]: https://dev.wix.com/api/rest/inbox/messages/message-types
[visitor-id-types]: https://dev.wix.com/api/rest/inbox/conversations/conversation-id
