SortOrder: 0
# About Marketing Consent

When a visitor signs up to receive non-transactional content (for example, a newsletter), the sign-up is called a marketing consent. A marketing consent holds the visitor's sign-up details such as email address or phone number, the status of the consent, and more.

The Marketing Consent API allows you to manage marketing consents. With the Marketing Consent API, you can:

+ Create and update a visitor's marketing consent. 
+ Get a visitor's marketing consent by ID or communication details. 
+ Query visitor marketing consents.
+ Cancel a visitor's marketing consent. 
+ Delete a visitor's marketing consent entirely.

You can also listen for events when a visitor's marketing consent is [created](https://dev.wix.com/api/rest/marketing/marketing-consent/marketing-consent-created-webhook), [updated](https://dev.wix.com/api/rest/marketing/marketing-consent/marketing-consent-updated-webhook), and [deleted](https://dev.wix.com/api/rest/marketing/marketing-consent/marketing-consent-deleted-webhook). 

## Terminology

+ **Opt in level**: Marketing consents have an `optInLevel` of either single or double confirmation. With single confirmation, when a site visitor signs up, their marketing consent `state` is `CONFIRMED`. With double confirmation, when a site visitor signs up, their marketing consent `state` is `PENDING` until the visitor confirms their consent (for example, clicks a link to verify their email address). When the visitor confirms their consent (for exmple, verifies their email address), the `state` is `CONFIRMED`.

+ **CommunicationEligibility**: Details about whether the subject of the marketing consent is eligible to receive communication. If a visitor cancels their marketing consent, `CommunicationEligibility.granted` will be `false`.
