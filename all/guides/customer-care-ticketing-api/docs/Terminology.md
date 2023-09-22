SortOrder: 1
## Terminology

### Topic

A topic entity represents the relevant Wix realm in which a user needs help. For example, Editor, Stores, Billing, Domains & Mailboxes and so on.
A topic must be specified in order to open a support request through the API, as it holds all the necessary data to route the created ticket to the relevant queue, assigned agents group and more in the support platform (Wix Answers).

Publicly, it holds:
- `id`
- `name`
- `languageCode`
  ISO 2 letter language code
- `description`
  The description of the topic
- `supportedChannels`
  Indicates wheter this topic is supported for phone callback, post ticket, or both
Internally, it holds:
- `postGroupId`
  The assigned agents group of the ticket used in the internal support platform
- `callbackQueueId`
  The matching phone callback queue, used for routing
- `callbackLineId`
  The mathcing phone callback line for outbound calls
- `skillId`
  The skill Id of the topic
- `createdDate`
- `updatedDate`

The available topics are accessible through the API. On top of that, it is possible (and recommended) to query the live availability of a topic before opening a support request for that topic. A topic is considered avilable for phone callbacks, for example, if the matching callback queue is opened. If a support request is made but the topic is unavailable at the time of the request - it will reject the action. See the Topic markdown for more details.

A complete mapping of the topic entities to the it's corresponding support platform entities is held internally as part of the service related database.
