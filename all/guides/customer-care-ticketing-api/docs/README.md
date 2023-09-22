SortOrder: 0
# Customer Care Ticketing API

Customer Care service that exposes support actions for external or internal clients, specifically:
- Add a ticket on behalf of a user
- Request a callback on behalf of a user

The service hides any setup/implementation which is required when opening support requests within the suuport paltform (currently Wix Answers), and lets a client perform support requests without internal knowledge of callback queues, callback lines, assignee groups and more.

## Main use case:
External "channel" accounts transfer their user's support requests to Wix by selecting either a post ticket or a callback request on behalf of the user.
As the support tickets are handled internally by Wix experts, the channel is unaware of the mentioned platform specifics, and by providing the necessary payload to the API, they manage to transfer these requests to be handled by Wix.

## Relationship with Wix Answers API:
Wix Answers is the current choice to handle support tickets for Wix Customer Care. Thus, this API is built on top of Wix Answers API. In order to allow external vendors to easily connect, without the dependency of specific Answers knowledge, the API encapsulates this data and abstracts the fundamental requirements to open support requests. Besides authenticating the user within the platform (as a Wix x Partner user), the mentioned hidden internals include configuration details such as phone callback queues, ticket assignee groups, labels, internal agent notes and more.
