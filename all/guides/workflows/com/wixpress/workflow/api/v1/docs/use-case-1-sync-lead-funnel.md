SortOrder: 2
# Example: Sync a Lead Funnel with an External CRM

This guide takes you through the actions your app can perform
to keep a Wix workflow in sync with a workflow in an external service.
Because each card in the Wix workflow needs to have a contact attached to it,
the external workflow should also be contact-based.

## Part 1: Setting Up the Wix Workflow

Before syncing,
create the workflow and phases in Wix as they exist on the external CRM.
In this example lead funnel,
the phases are **New Lead > Contacted > Qualified > Proposal Sent > Negotiating**.
The win phase is included in every Wix workflow and isn't created through an API call.

1. Request any applicable information from the external CRM, which could include:
    - External workflow ID and name
    - External phase IDs and names
    - External card IDs and names
    - External contact IDs and details

    Store this information on your server so you can map it
    to the workflow, phase, and card information you'll create in the next steps.

2. Create an empty workflow by calling [Create Workflow][create-workflow]:

    ```bash
    curl -X POST \
      'https://www.wixapis.com/workflows/v1/workflows' \
      -H 'Authorization: <AUTH>' \
      -H 'Content-Type: application/json' \
      -d '{
      "workflow": {
        "name": "Lead Funnel",
        "description": "Shows where contacts are in the lead funnel."
      }
    }'
    ```

    Capture the returned workflow `id`,
    which you'll need when creating phases in the next step:

    ```json
    {
      "id": "f4d11ab3-37ec-466b-affe-192689e5f40a"
    }
    ```

3. Set up the phases by calling [Create Phase][create-phase],
   using the workflow ID returned in step 2.
   The new workflow already contains a win phase,
   so you only need to set up the active phases.

    Run a separate request for each phase,
    setting `phase.name` in each request.
    In this example,
    the phases are "**New Lead**", "**Contacted**", "**Qualified**",
    "**Proposal Sent**", and "**Negotiating**".
    `position` can be omitted if you create the phases in order,
    from first to last:

    ```bash
    curl -X POST \
      'https://www.wixapis.com/workflows/v1/workflows/f4d11ab3-37ec-466b-affe-192689e5f40a/phases' \
      -H 'Authorization: <AUTH>' \
      -H 'Content-Type: application/json' \
      -d '{
      "phase": {
        "name": "New Lead"
      }
    }'
    ```

    Capture the returned phase `id` from each response,
    which you'll need when adding cards later on:

    ```json
    {
      "id": "da2d0644-4fd7-46bb-8dbb-d7f4ccdd1180"
    }
    ```

4. Retrieve the win phase ID by calling [Get Workflow][get-workflow] with the workflow ID:

    ```bash
    curl -X GET \
      'https://www.wixapis.com/workflows/v1/workflows/f4d11ab3-37ec-466b-affe-192689e5f40a' \
      -H 'Authorization: <AUTH>'
    ```

    Capture the returned win phase ID from the response at
    `workflow.winPhase.info.id`:

    ```json
    {
      "workflow": {
        "info": { ... },
        "winPhase": {
          "info": {
            "id": "0c1c9a05-dc8c-46f8-8e4b-7a31cfd9cbef",
            "name": "Win"
          },
          "cardsList": { ... }
        },
        "phasesList": { ... }
      }
    }
    ```

5. Use the [Contacts API][contacts-api]
   to create any necessary contacts.

6. Add cards in the applicable phases with [Create Card][create-card],
   using the following information:
    - Workflow ID from step 2
    - Phase IDs from steps 3 and 4
    - Contact IDs from step 5

    ```bash
    curl -X POST \
      'https://www.wixapis.com/workflows/v1/workflows/f4d11ab3-37ec-466b-affe-192689e5f40a/phases/da2d0644-4fd7-46bb-8dbb-d7f4ccdd1180/cards' \
      -H 'Authorization: <AUTH>' \
      -H 'Content-Type: application/json' \
      -d '{
      "card": {
        "name": "Ines Brunet",
        "primaryAttachment": {
          "contactId": "73904dbd-94ca-4ac1-a593-ef0627673e59"
        },
        "source": "My CRM"
      }
    }'
    ```

    Capture the returned card `id` from each response, which you'll add to your mapping in the next step:

    ```json
    {
      "id": "da2d0644-4fd7-46bb-8dbb-d7f4ccdd1180"
    }
    ```

7. Update the mapping on your server with the following information from the Wix site:
    - Workflow ID
    - Active phase IDs
    - Win phase ID
    - Card IDs
    - Contact IDs

## Part 2: Keeping the Wix Workflow in Sync

Listen for changes to cards from the external CRM.
When your app detects a change that it needs to synchronize,
use the Cards API to
[create][create-card], [move][move-card], or [archive][archive-card] a card.

[create-workflow]: https://dev.wix.com/api/rest/workflows/workflows/workflows/create-workflow
[create-phase]: https://dev.wix.com/api/rest/workflows/workflows/phases/create-phase
[get-workflow]: https://dev.wix.com/api/rest/workflows/workflows/workflows/get-workflow
[create-card]: https://dev.wix.com/api/rest/workflows/workflows/cards/create-card
[contacts-api]: https://dev.wix.com/api/rest/contacts/contacts/introduction
[move-card]: https://dev.wix.com/api/rest/workflows/workflows/cards/move-card
[archive-card]: https://dev.wix.com/api/rest/workflows/workflows/cards/archive-card