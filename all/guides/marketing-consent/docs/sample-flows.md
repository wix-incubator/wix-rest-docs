SortOrder: 1
# Marketing Consent: Sample Use Cases & Flows

This article shares some possible use cases your app could support, as well as an example flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your
app's implementation.

## Confirm a marketing consent with double confirmation

A visitor signs up on your app to receive non-transactional content. If the visitor is from a country where the opt in level is double confirmation, follow this flow to create the marketing consent and update the visitor's marketing consent state.

To confirm the marketing consent:

1. Use [Upsert Marketing Consent](https://dev.wix.com/docs/rest/api-reference/marketing/marketing-consent/upsert-marketing-consent) to create a marketing consent with a double confirmation opt in level.

2. Notice the returned `state` property of the response is `PENDING` until the visitor confirms the sign up. 

3. When the visitor confirms the sign up on your app, use [Update Marketing Consent](https://dev.wix.com/api/rest/marketing/marketing-consent/update-marketing-consent) to update a marketing consent's state from `PENDING` to `CONFIRMED`.

