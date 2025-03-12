SortOrder: 1
# Example Flows

This article presents possible use cases and corresponding
sample flows that you can support. This can be a helpful jumping off point
as you plan your implementation.

## Sync messages from an external service

You can enable business owners to communicate with their customers on any platform
by syncing messages to Wix Inbox.
The scenario below covers chat messages,
but this flow could support integrating phone call logs, SMS services,
chat sessions, or any other online or offline communication.

To do this, you can follow this basic flow:

1. Set up the external service's webhooks.
    When a "message sent" or "message received" event is triggered,
    parse the event data for an email address.

2. Call [Query Contacts](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/query-contacts)
    to find a contact with the email address you extracted in step 1.
    You're looking for a contact ID here,
    so you can use the `fields` array to make sure the response only passes back `id`:

    ```json
    {
      "query": {
        "filter": {
          "info.emails.email": { "$eq": "<EMAIL_ADDRESS_FROM_INCOMING_MESSAGE>" }
        },
        "fields": [ "id" ]
      }
    }
    ```

    Any matching contacts are in the returned `contacts` array.
    An email address can belong to more than one contact,
    so you must handle situations when multiple contacts are returned.

3. Get the conversation ID with [Get or Create Conversation](https://dev.wix.com/api/rest/inbox/conversations/get-or-create-conversation).

    Set the `participantId.contactId` parameter to the `id` extracted in step 2:

    ```json
    {
      "participantId": { "contactId": "4e600edc-db48-5260-9d04-7ea5c3e5fffd" }
    }
    ```

    You can get the conversation ID from `conversation.id` in the response.

4. Call [Send Message](https://dev.wix.com/api/rest/inbox/messages/send-message)
    to add the new message to the contact's conversation.

    Set the `conversationId` parameter to `conversation.id` returned in step 3.

    In the body, pass the incoming message in a [`BASIC` message type](https://dev.wix.com/api/rest/inbox/messages/message-types#basic-messages):

    ```json
    {
      "message": {

        // Hides the message from the chat widget when the contact visits the site
        "visibility": "BUSINESS",

        "content": {
          "basic": {
            "items": [{ "text": "<INCOMING_MESSAGE_FROM_EXTERNAL_SERVICE>" }]
          }
        },

        // Indicates the message came from Facebook
        "badges": [{
          "text": "Facebook",
          "iconUrl": "https://static.wixstatic.com/media/aebe5b6fd55f471a936c72ff2c8289d7.png/v1/fill/w_43,h_43,al_c,q_85,usm_0.66_1.00_0.01/aebe5b6fd55f471a936c72ff2c8289d7.webp"
        }]
      },

      // Displays the message as if the contact sent it
      "direction": "PARTICIPANT_TO_BUSINESS"
    }
    ```

You can also send messages sent on behalf of the business
from the external chat tool.
In those cases, change the visibility settings to match your requirements,
and set `direction` to `BUSINESS_TO_PARTICIPANT`.

## Add contact activities from another service

You can capture contact activities from another platform
and display them in the contact's conversation in Wix Inbox.

To do this, you can follow this basic flow:

1. Set up the external service's events.
    When an event is triggered,
    parse the event data for an email address.

2. Call [Query Contacts](https://dev.wix.com/api/rest/contacts/contacts/contacts-v4/query-contacts)
    to find a contact with the email address you extracted in step 1.
    You're looking for a contact ID here,
    so you can use the `fields` array to make sure the response only passes back `id`:

    ```json
    {
      "query": {
        "filter": {
          "info.emails.email": { "$eq": "<CUSTOMER_EMAIL_ADDRESS>" }
        },
        "fields": [ "id" ]
      }
    }
    ```

    The response includes matching contacts in the returned `contacts` array.
    An email address can belong to more than one contact,
    so you must handle situations when multiple contacts are returned.

3. Get the conversation ID with [Get or Create Conversation][get-or-create-conversation].

    Set the `participantId.contactId` path parameter to the `id` extracted in step 2:

    ```json
    {
      "participantId": { "contactId": "4e600edc-db48-5260-9d04-7ea5c3e5fffd" }
    }
    ```

    You can get the conversation ID from `conversation.id` in the response.

4. Call [Send Message](https://dev.wix.com/api/rest/inbox/messages/send-message)
    to add the new message to the contact's conversation.

    Set the `conversationId` path parameter to `conversation.id` returned in step 3.

    In the body, pass the action in a [`MINIMAL` message type](https://dev.wix.com/api/rest/inbox/messages/message-types#minimal-messages):

    ```json
    {
      "message": {

        // Hides the message from the chat widget when the contact visits the site
        "visibility": "BUSINESS",

        "payload": {
          "type": "MINIMAL",
          "minimal": {
            "text": "Booked Spa Treatment",
            "iconUrl": "https://static.wixstatic.com/media/bd4a2aff643141cb8cbacde1a4007a2f.png/v1/fill/w_43,h_50,al_c,lg_1,q_85/bd4a2aff643141cb8cbacde1a4007a2f.webp"
          }
        }
      },

      // Displays the message as if the contact sent it
      "direction": "PARTICIPANT_TO_BUSINESS"
    }
    ```
