SortOrder: 0
# About Email Subscriptions

The Email Subscriptions API is a service
that allows your app to create, view, and update email subscriptions
for a site's contacts.
Any changes made with the Email Subscriptions API
are reflected in the site's [Contact List][contact-list].

Wix keeps track of contacts' subscription and deliverability statuses.
These statuses are automatically updated by Wix,
although site contributors can
[change subscription status][change-subscription-status]
in the site Dashboard.

By using the Email Subscriptions API,
your app can keep subscription and deliverability statuses
in sync with an external email marketing tool.

The Email Subscriptions API allows your app to:

- Query existing email subscriptions
- Update or create subscriptions by email address
- Generate unsubscribe links for individual recipients
- Listen for changes to subscription or deliverability statuses
  for site contacts
  (coming soon)

## Terminology

- The **email subscription** object contains an email,
  subscription status, and deliverability status.
- **Subscription status** indicates a contact's opt-in or opt-out status
  for marketing emails.
- **Deliverability status** indicates if the emails were opened or bounced,
  if the contact marked an email as spam,
  or if no activity has been reported to Wix.

[contact-list]: https://support.wix.com/en/article/about-your-contact-list
[change-subscription-status]: https://support.wix.com/en/article/changing-the-subscription-status-of-a-contact