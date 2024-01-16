SortOrder: 0
# About Marketing Consent

When a visitor signs up for non-transactional content, such as a newsletter, they are consenting to receive marketing messages. This agreement is called a marketing consent. A marketing consent holds the visitor's sign-up details such as email address or phone number, the status of the consent, and more.

The Marketing Consent API allows your app to manage a site's marketing consents. With the Marketing Consent API, your app can:

+ Create and update a visitor's marketing consent. 
+ Get a visitor's marketing consent by ID or communication details. 
+ Query visitor marketing consents.
+ Cancel a visitor's marketing consent. 
+ Delete a visitor's marketing consent entirely.

Your app can also listen for events when a visitor's marketing consent is [created](https://dev.wix.com/api/rest/marketing/marketing-consent/marketing-consent-created-webhook), [updated](https://dev.wix.com/api/rest/marketing/marketing-consent/marketing-consent-updated-webhook), and [deleted](https://dev.wix.com/api/rest/marketing/marketing-consent/marketing-consent-deleted-webhook). 

## Terminology

+ **Visitor:** A visitor is any person who visits a site, including contacts, non-contacts, members, and non-members. 

+ **Communication channel:** Each marketing consent has a communication channel of either `email` or `phone`. A visitor can sign up multiple times using different email addresses and phone numbers, however, they can only create a single marketing consent per email and per phone number.

+ **State:** Different states of a marketing consent. 
  + `UNKNOWN_STATE`: State of the marketing consent is unknown.
  + `NEVER_CONFIRMED`: The visitor never confirmed to receive marketing messages.
  + `REVOKED`: The marketing consent has been removed, for example, when a visitor unsubscribes from a newsletter. 
  + `PENDING`: The marketing consent is pending confirmation. Relevant only for `{"optInLevel": "DOUBLE_CONFIRMATION"}`.
  + `CONFIRMED`: The site visitor has confirmed their marketing consent.

+ **Opt in level:** A marketing consent has an `optInLevel` of either single or double confirmation. Some countries require double confirmation for all marketing consents. With single confirmation, when a site visitor signs up, their marketing consent `state` is `CONFIRMED`. With double confirmation, when a site visitor signs up, their marketing consent `state` is `PENDING` until the visitor confirms their consent, for example, by clicking a link to verify their email address. When the visitor confirms their consent, the `state` is `CONFIRMED`. 

+ **Communication eligibility:** The [Get Marketing Consent By Identfier](https://dev.wix.com/docs/rest/internal-only/marketing/marketing-consent/get-marketing-consent-by-identifier) endpoint returns the `communicationEligibility.granted` boolean which determines whether the recipient of the marketing consent is eligible to receive marketing messages. Note that this only serves as a signal for your app to decide whether or not it should send marketing messages to the recipient's email address or phone number.

  For example:
  + If a visitor cancels their marketing consent, they are no longer eligible to receive communication, and`CommunicationEligibility.granted` is `false`. This applies to marketing consents made by both phone and email. 
  + If a marketing consent's `state` is `NEVER_CONFIRMED`, the visitor has never confirmed to receive communication, and `CommunicationEligibility.granted` is `false`. 
    >**Note:** This applies only to marketing consents made by **phone**. If a visitor made a marketing consent by **email** and the `state` is `NEVER_CONFIRMED`, the visitor can still receive communication, and `CommunicationEligibility.granted` is `true`. 