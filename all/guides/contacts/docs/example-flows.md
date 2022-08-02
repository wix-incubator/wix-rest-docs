SortOrder: 1
# Example Flows

This article shares some possible use cases your app could support,
as well as an example flow that could support each use case.
You're certainly not limited to these use cases,
but they can be a helpful jumping off point
as you plan your app's implementation.

## Copying New Wix Contacts to an External CRM

If a site owner manages their contacts in an external CRM,
you can use the REST API to copy new leads to their CRM.

To do this, your app can follow this basic flow
to periodically bulk load contacts:

1. For the first request after the app is installed, use
    [List Contacts][list-contacts] to get all contacts.

    For all subsequent requests, use [Query Contacts][query-contacts],
    and filter for new contacts created since the last copy:

    ```json
    {
      "sort": {
        "fieldName": "createdDate",
        "order": "ASC"
      },
      "filter": {
        "createdDate": {
            "$gt": "<PREVIOUS_COPY_DATETIME>"
        }
      }
    }
    ```

    The response is an array of contacts.

2. Upload the returned contacts to the external CRM.

3. Save the current datetime, and use it in the next request.
    Each subsequent request will need to use the datetime
    of the request that came before it.

You can allow the site admin to configure the time interval in your app
to fit their needs.

## Two-Way Sync with an External System

Business owners can keep their external CRM or email marketing tool
updated with their Wix Contact List with a two-way sync.
To synchronize Wix and an external system,
think about how your app will handle these flows:

- [Initial setup][initial-setup]
- [Synchronizing from Wix to the external system][sync-to-external]
- [Synchronizing from the external system to Wix][sync-to-wix]

### Part 1: Initial Setup

1. To ensure a 1:1 mapping with the external CRM,
    create a custom field to hold the contact's external ID.
    You can do this with
    [Find or Create Extended Field][find-create-field]:

    ```json
    {
      "displayName": "externalCrmId",
      "dataType": "TEXT"
    }
    ```

2. The first time a contact is synchronized,
    populate the new field with the external ID.
    Craft your code so this ID won’t be overwritten
    by future updates from your app.

3. Create a mapping from the Wix fields to the external CRM fields,
    to be used whenever Wix and the external CRM are synchronized.
    Store this mapping on your app's server.

4. You'll soon see that this flow relies on webhooks to trigger syncs
    between Wix and the external CRM.
    To keep your app from getting caught in an endless loop,
    include logic that ignores a webhook that's triggered
    as the result of a sync.

### Part 2: Synchronizing to the External System

Listen for any changes to Wix contacts with these webhooks:

- [Contact Created Webhook][hook-contact-created]
- [Contact Deleted Webhook][hook-contact-deleted]
- [Contact Updated Webhook][hook-contact-updated]

<!-- TODO uncomment when v4 hooks are exposed
- [Contacts Merged Webhook][hook-contacts-merged] -->

<!-- TODO uncomment when v4 hooks are exposed
When one of these above webhooks is triggered, -->
When a webhook is triggered,
your endpoint will receive the contact in the payload.
You can bring those changes to the external CRM with a flow like this one:

<!-- TODO uncomment when v4 hooks are exposed
1. Get the `slug` (which tells you what the event was)
    and `entityId` (which is the contact ID) from the webhook data. -->

1. Get `contact.id` from the webhook data.
2. Parse the data object for any other relevant information.
3. Use the mapping (from the [initial setup][initial-setup])
    to copy the relevant information to the external CRM.
4. Ignore the resulting event from the external CRM
    so you don’t create an endless loop of updates.

### Part 3: Synchronizing to Wix

Listen for changes to contacts from the external CRM.
When your app detects a change that it needs to synchronize,
follow this basic flow:

1. Copy the relevant details using one of these CRUD endpoints.
    Use the endpoint that matches the event from the external CRM.

2. Ignore the resulting event from Wix
    so you don’t create an endless loop of updates.

## Creating New Contacts from an External Form

To create contacts using a form hosted in an external app,
capture the relevant form values, and follow this basic flow:

1. Filter for contacts with the same email
    with [Query Contacts][query-contacts]
    to find out if the contact already exists.
2. If the contact already exists,
    update the contact with
    [Update Contact][update-contact].
3. If the contact doesn’t exist,
    create a new contact with
    [Create Contact][create-contact].

## Sync Subscribed Emails with an Email Delivery Service

Some site owners communicate with their users
through an external email delivery service.
To comply with privacy regulations,
site owners need to ensure that only contacts
who have opted in to marketing emails will receive those emails.

Email subscription status is conveyed in the
`emailSubscriptions.subscriptionStatus` extended field.
To allow site owners to email opted-in contacts,
query contacts where `emailSubscriptions.subscriptionStatus` is `SUBSCRIBED`
with this basic flow:

1. Retrieve the filtered list of contacts with [Query Contacts][query-contacts].
    Filter for contacts whose `subscriptionStatus` is `SUBSCRIBED`,
    and return only the fields you need:

    ```json
    {
      "filter": {
        "info.extendedFields.emailSubscriptions.subscriptionStatus": {
          "$eq": "SUBSCRIBED"
        }
      },
      "fields": [
        "primaryInfo",
        "info.labelKeys",
        "info.extendedFields"
      ]
    }
    ```

2. Create a mapping from the Wix fields to the email delivery service fields.
    Store this mapping on your app's server.

[list-contacts]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/list-contacts
[query-contacts]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/query-contacts
[find-create-field]: https://dev.wix.com/api/rest/contacts/extended-fields/find-or-create-extended-field
[create-contact]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/create-contact
[delete-contact]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/delete-contact
[update-contact]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/update-contact
[add-labels]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/add-labels-to-contact
[remove-labels]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/remove-labels-from-contact

[hook-contact-created]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v1-(deprecated)/contact-created-webhook
[hook-contact-deleted]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v1-(deprecated)/contact-deleted-webhook
[hook-contact-updated]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v1-(deprecated)/contact-changed-webhook
[hook-contacts-merged]: crm.contacts.contacts-v4.contact-merged-domain-event

[initial-setup]: #part-1-initial-setup
[sync-to-external]: #part-2-synchronizing-to-the-external-system
[sync-to-wix]: #part-3-synchronizing-to-wix
