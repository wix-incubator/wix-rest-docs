SortOrder: 3
# Types of Visitor IDs

The Inbox API uses the visitor's ID when
[sending][send-message-endpoint] or [listing][list-messages-endpoint] messages.
This visitor ID can be one of 3 possible values,
which relate to how Wix has identified the visitor:
[anonymous visitor](#anonymous-visitor-id), [contact](#contact-id), or [member](#member-id).

> **Note:**
> In cases where the ID always belongs to a visitor, contact, or member,
> the `visitorId` property is used.
> In cases where the ID could belong to a site contributor
> _or_ to a visitor, contact, or member,
> `participantId` is used.

The sections below tell you how your app can retrieve the relevant ID
to use the Inbox API.

## Anonymous visitor ID

Anonymous visitor IDs are available to your app
after the visitor sends a message to the business using the
[Message Sent To Business Webhook][message-sent-to-business-webhook].
The ID is available at `actionEvent.body.message.visitorId`.

## Contact ID

When a visitor provides contact details to the site,
they are converted to a contact.
Once this happens,
the ID used to access the visitor's conversations changes to the contact ID:

- Like the anonymous visitor,
  the contact ID is available when the contact sends a message to the business
  using the [Message Sent To Business Webhook][message-sent-to-business-webhook].
  The ID is available at `actionEvent.body.message.visitorId`.
- You can also use [Query Contacts][query-contacts] or [List Contacts][list-contacts]
  in the Contacts API to retrieve the contact.

## Member ID

If the visitor is a [site member][kb-members-area],
the conversation must be accessed using the member ID:

- Like the anonymous visitor and contact,
  the member ID is available when the contact sends a message to the business
  using the [Message Sent To Business Webhook][message-sent-to-business-webhook].
  The ID is available at `actionEvent.body.message.visitorId`.
- You can also use [Query Members][query-members] or [List Members][list-members]
  in the Members API to retrieve the member.

[kb-members-area]: https://support.wix.com/en/article/about-the-members-area
[inbox-deeplink]: https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Finbox
[send-message-endpoint]: https://dev.wix.com/api/rest/drafts/inbox/send-message
[list-messages-endpoint]: https://dev.wix.com/api/rest/drafts/inbox/list-messages
[message-sent-to-business-webhook]: https://dev.wix.com/api/rest/all-apis/inbox/message-sent-to-business-webhook
[query-contacts]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/query-contacts
[list-contacts]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/list-contacts
[query-members]: https://dev.wix.com/api/rest/members/members/query-members
[list-members]: https://dev.wix.com/api/rest/members/members/list-members