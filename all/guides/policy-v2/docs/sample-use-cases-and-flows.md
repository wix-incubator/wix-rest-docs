SortOrder: 2
# Policies v2: Sample Use Cases & Flows

This article presents possible use cases and corresponding sample flows that your app can support. It provides a useful starting point as you plan your app's implementation. 

## Sync event policies with external ticketing system

If you're using a Wix site to manage events and another system to handle ticketing, you can synchronize policies between them whenever a policy is updated on the site. For instance, if the refund policies on the Wix site change, and now the policies guarantee a full refund up to only 5 days before the event, this change also needs to be reflected on your ticketing system for checkout purposes.

To upload and update all event policies defined on the Wix site to your external system for the first time, follow these steps:

1. Create a custom field in your system that stores the policy ID for a particular event to ensure a 1-to-1 relationship with the external ticketing system. Craft your code so that this ID won't be overwritten by future updates from your app.

2. Create a mapping from the site policies fields to the system fields that will be used whenever site policies and the external system are synchronized.

3. [Query Policies](https://dev.wix.com/api/rest/wix-events/policies-v2/query-policies) by `eventId` and send the relevant information to the external ticketing system.

4. On an ongoing basis, listen for changes to site policies with these webhooks:

    - [Policy Created Webhook](https://dev.wix.com/api/rest/wix-events/policies-v2/policy-created-webhook)
    - [Policy Updated Webhook](https://dev.wix.com/api/rest/wix-events/policies-v2/policy-updated-webhook)
    - [Policy Deleted Webhook](https://dev.wix.com/api/rest/wix-events/policies-v2/policy-deleted-webhook)
      
5. When one of the above webhooks is triggered, you'll receive the policy in the payload. You can bring those changes to the ticketing system by retrieving the relevant info from the payload, and use mapping to take action on the external system:

    - For updated policies retrieve the `updatedEvent.currentEntityAsJson.id`, `updatedEvent.currentEntityAsJson.body` and/or `updatedEvent.currentEntityAsJson.name` values.

    - For created policies retrieve the relevant info from the `createdEvent.currentEntityAsJson` object.

    - For deleted policies retrieve the `createdEvent.currentEntityAsJson.id` value.
