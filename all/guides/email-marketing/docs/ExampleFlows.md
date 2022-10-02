SortOrder: 1
## Example Flows

This article shares possible use cases your app could support, as well as example flows. You're certainly not limited to these use cases, but it can be a helpful jumping off point as you plan your app's implementation.


### Retrieve all of the email campaigns that a contact opened

Your app can help site owners check which emails a contact opened.

1. With a contact's email address, use [Query Contacts](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/query-contacts) to retrieve their Contact ID.
1. Use [List Campaigns](https://dev.wix.com/api/rest/marketing/email-marketing/campaign/list-campaigns) to retrieve all of the Campaign IDs for a site's campaigns.
1. For each of the retrieved Campaign IDs, use [List Recipients](https://dev.wix.com/api/rest/marketing/email-marketing/campaign/list-recipients) with the `activity=OPENED` query parameter.
1. Extract only those campaigns where recipients.contactId matches the selected Contact ID.


### Run an A/B test for a campaign's subject line

Your app can help a site owner run an A/B test on the subject of their new email campaign.

1. Divide a site's contacts into two segments and use [labels](https://dev.wix.com/api/rest/contacts/labels) to differentiate them.
1. Use the `labelIds` parameter in [Publish Campaign](https://dev.wix.com/api/rest/marketing/email-marketing/campaign/publish-campaign) to send 1 of the segments the new email campaign with 1 option for the `emailSubject`. Send the same email campaign with a different `emailSubject` to the other segment, also using `labelIds`.
1. Use [List Campaigns](https://dev.wix.com/api/rest/marketing/email-marketing/campaign/list-campaigns) to retrieve the Campaign IDs for both campaigns.
1. Use [List Statistics](https://dev.wix.com/api/rest/marketing/email-marketing/campaign/list-statistics) to receive the statistics for both campaigns.
1. Calculate and compare the `OPENED` rates for both campaigns.