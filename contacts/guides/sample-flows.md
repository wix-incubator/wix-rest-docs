# Sample Flows

This article shares some possible use cases your app could support,
as well as an example flow that could support each use case.
You're certainly not limited to these use cases,
but they can be a helpful jumping off point
as you plan your app's implementation.

## Periodically export new Wix contacts to an external CRM

If a site owner manages their contacts in an external CRM,
you can export new leads to their CRM.

To do this, your app can periodically bulk load new contacts:

1. For the first load after the app is installed, use
    [List Contacts][list-contacts] to get all contacts.
    Set `paging.limit` to `1000`.

    If you receive 1,000 contacts, there may be more contacts to retrieve.
    Run the request again, and increase `paging.offset` to `1000`.
    Keep running the request, each time increasing the offset,
    until all contacts are retrieved.

2. Upload the returned contacts to the external CRM.

3. Save the current datetime, and use it in the next request.
    Each subsequent request will need to use the datetime
    of the request that came before it.

4. For all subsequent loads, use [Query Contacts][query-contacts],
    and filter for new contacts created since the last load:

   ::::tabs
   :::REST_TAB
   ```json
        {
      "sort": {
        "fieldName": "createdDate",
        "order": "ASC"
      },
      "filter": {
        "createdDate": {
            "$gt": "<PREVIOUS_LOAD_DATETIME>"
        }
      }
    }
      ```
   :::
   :::SDK_TAB
   ```js
   const query = services.queryContacts().ascending("createdDate").gt("createdDate", "<PREVIOUS_LOAD_DATETIME>");
   ```
   :::
   ::::

5. Repeat steps 2 to 4 for each subsequent load.
    You can allow the site admin to configure the time interval in your app
    to fit their needs.

## Real-time 2-way sync with an external system

Site owners can use your app
to keep their external CRM or email marketing platform up to date
with their Wix contact list with a two-way sync.
To synchronize Wix and an external system,
think about how your app will handle these flows:

- [Initial setup][initial-setup]
- [Synchronize from Wix to the external system][sync-to-external]
- [Synchronize from the external system to Wix][sync-to-wix]

### Part 1: Initial setup

1. To ensure a 1:1 relationship with the external CRM contacts,
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

4. Prompt the site owner to choose a system of record
    (either Wix or the external CRM),
    and delete all the contacts from the other system.
    Be careful with this flow, however.
    Always warn your users when they're about to delete data.

    > **Note:**
    > If a contact in Wix is also a site member, the contact can't be deleted.

### Part 2: Synchronize to the external system

Listen for any changes to Wix contacts with these webhooks:

- [Contact Created Webhook][hook-contact-created]
- [Contact Deleted Webhook][hook-contact-deleted]
- [Contact Updated Webhook][hook-contact-updated]
- [Contacts Merged Webhook][hook-contacts-merged]

When one of the above webhooks is triggered,
you'll receive the contact in the payload.
You can bring those changes to the external CRM with a flow like this one:

1. Get the `slug` (which tells you what the event was),
    `entityId` (which is the contact ID),
    and any other relevant information from the payload data.

2. Use the mapping (from the [initial setup][initial-setup])
    to send the relevant information to the external CRM.

3. Ignore the resulting event from the external CRM
    so you don’t create an endless loop of updates.

### Part 3: Synchronize to Wix

Listen for contact events from the external CRM.
When your app receives a change it needs to synchronize,
follow this basic flow:

1. Use the mapping (from the [initial setup][initial-setup])
    to send the updated contact to the relevant endpoint
    ([Create Contact][create-contact], [Update Contact][delete-contact],
    or [Delete Contact][update-contact]).

2. Ignore the resulting event from Wix
    so you don’t create an endless loop of updates.

## Create new contacts from an external form

To create contacts using a form hosted in an external app,
capture the relevant form values, and follow this basic flow:

1. Filter for contacts by email address
    with [Query Contacts][query-contacts]
    to find out if the contact already exists.
2. If the contact already exists,
    update the contact with
    [Update Contact][update-contact].
3. If the contact doesn’t exist,
    create a new contact with
    [Create Contact][create-contact].

## Sync subscribed emails with an email delivery service

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
    Filter for contacts whose `subscriptionStatus` is `SUBSCRIBED`:

    ::::tabs
   :::REST_TAB
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
   :::
   :::SDK_TAB
   ```js
   const query = services.queryContacts().eq("info.extendedFields.emailSubscriptions.subscriptionStatus", "SUBSCRIBED");
   ```
   :::
   ::::

2. Create a mapping from the Wix fields to the email delivery service fields.
    Store this mapping on your app's server.

[list-contacts]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/list-contacts
[query-contacts]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/query-contacts
[find-create-field]: https://dev.wix.com/api/rest/contacts/extended-fields/find-or-create-extended-field
[create-contact]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/create-contact
[delete-contact]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/delete-contact
[update-contact]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/update-contact

[hook-contact-created]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-created-webhook
[hook-contact-deleted]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-deleted-webhook
[hook-contact-updated]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-updated-webhook
[hook-contacts-merged]: https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/contact-merged-webhook

[initial-setup]: #part-1-initial-setup
[sync-to-external]: #part-2-synchronize-to-the-external-system
[sync-to-wix]: #part-3-synchronize-to-wix
