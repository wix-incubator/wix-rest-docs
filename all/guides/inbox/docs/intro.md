SortOrder: 0
# About Inbox

[Site contributors][kb-roles-permissions]
use Wix Inbox
to communicate with their visitors, members, and contacts
through Wix Chat, SMS, a Facebook business page, or other channels.
Visitor activities on the site and third party services
can also be displayed in Inbox conversations.

The Inbox API exposes functionality for working with a site's inbox.
With the Inbox API, your app can:

- Send messages on behalf of the site or a visitor.
- Retrieve a visitor's conversations with the site.
- Handle webhooks when incoming and outgoing messages are reported.

[Read more about how site contributors work with Wix Inbox][kb-inbox].

## Terminology

- A **message** is sent from the business to the visitor
  or from the visitor to the business.
  Messages can be one of these types: `PLAIN`, `TEMPLATE`, `MINIMAL`, `FORM`, `CUSTOM`.
  [Learn more about message types.][message-types]
- A **conversation** is a collection of messages that takes place between two or more participants.
  Conversations are displayed in the site's [Inbox][inbox-deeplink],
  one conversation per site visitor, contact, or member.
- A **participant** can be a site contributor (representing the business)
  or a site visitor.
  Site visitors could have a visitor ID, contact ID, or member ID.
  [Learn more about types of visitor IDs.][visitor-id-types]

[kb-inbox]: https://support.wix.com/en/article/wix-inbox-getting-started
[kb-roles-permissions]: https://support.wix.com/en/article/roles-permissions-overview
[inbox-deeplink]: https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Finbox
[message-types]: ./message-types.md
[visitor-id-types]: ./types-of-visitor-ids.md