SortOrder: 2
# Ticket Definitions v3: Sample Use Cases & Flows

This article presents possible use cases and corresponding sample flows that your app can support. It provides a useful starting point as you plan your app's implementation. 

## Add a specific-price ticket counter for an event

This use case demonstrates how you can update your event site with a ticket counter for specific-price tickets. This counter provides real-time information on the availability of tickets for customers to see. For example, your page can have a counter that says "Only 3 tickets left for this price." By displaying the number of tickets remaining, you can motivate customers to buy tickets promptly. 

> **Note**: This flow assumes you have already created the UI component of the counter for your site.

To create a ticket counter, follow these steps:
    
1. Call [Get Ticket Definition](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/get-ticket-definition) and retrieve either:
 - The `salesDetails.unsoldCount` and `fixedPrice.value` values (for `fixedPrice` pricing method).
 - The `salesDetails.unsoldCount` and `pricingOptions.optionDetails.price.value` field values (for `optionalPrice` pricing method).

1. Pass these retrieved values in your app to initialize the counter on your website, displaying the number of available tickets at the specified price.

1. On an ongoing basis, listen for each new ticket purchase using the [Order Confirmed Webhook](https://dev.wix.com/api/rest/wix-events/wix-events/checkout/order-confirmed-webhook).

1. When the webhook is triggered, you'll receive an order in the payload. Retrieve the `ticketDefinitionId` value from the event data.

1. Send the extracted `ticketDefinitionId` value to your site and compare it with the ticket definition ID for which the counter is set. If they match, call [Get Ticket Definition](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/get-ticket-definition) again to retrieve the updated `salesDetails.unsoldCount` value. Send this new decreased value to your website to update the ticket counter.

## Sync ticket definitions with an external ticketing system

If you're using a Wix site to manage events and another system to handle ticketing, you can synchronize ticket definitions between them whenever a definition is updated on the site. This includes aspects such as ticket types, pricing, availability, and any other relevant ticket settings. This synchronization eliminates the need for manual updates and reduces the risk of discrepancies between systems.

To upload and update all ticket definitions defined on the Wix site to your external system for the first time, follow these flows:

- [Initial setup](events-services/events-ticket-definitions/proto/docs/sample-use-cases-and-flows.md#initial-setup)
- [Synchronize to the external system](events-services/events-ticket-definitions/proto/docs/sample-use-cases-and-flows.md#synchronize-to-the-external-system)

### Part 1: Initial setup

1. Create a custom field in your system that stores the ticket definition ID for a particular event to ensure a 1-to-1 relationship with the external ticketing system. Craft your code so that this ID won't be overwritten by future updates from your app.

1. Create a mapping from the site ticket definition fields to the system fields that will be used whenever site ticket definitions and the external system are synchronized.

1. [Query Ticket Definitions](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/query-ticket-definitions) by `eventId` and send the relevant information to the external ticketing system.

### Part 2: Synchronize to the external system

1. On an ongoing basis, listen for changes to site ticket definitions with these webhooks:

    - [Ticket Definition Created Webhook](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/ticket-definition-created-webhook)
    - [Ticket Definition Updated Webhook](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/ticket-definition-updated-webhook)
    - [Ticket Definition Deleted Webhook](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/ticket-definition-deleted-webhook)
      
1. When one of the above webhooks is triggered, you'll receive the ticket definition in the payload. You can bring those changes to the ticketing system by retrieving the relevant info from the payload, and use mapping to take action on the external system:

    - For created and updated ticket definitions retrieve the relevant info from the `createdEvent.currentEntity` object.

    - For deleted ticket definitions retrieve the `createdEvent.currentEntity.id` value.

## Notify customers when tickets go on sale 

Let customers know when ticket sales for an event begin. You can send automated notifications to customers with email or push notifications. These notifications make customers aware of ticket availability so they can secure their tickets promptly.

> **Note**: This flow assumes your customers already have the ability to subscribe to your newsletters.

To send notifications about the start of ticket sales, follow these steps:

1. [Get Ticket Definition](https://dev.wix.com/api/rest/wix-events/ticket-definitions-v3/get-ticket-definition).

2. Retrieve the `salePeriod.startDate` field value, and write your code so that the value can be passed to your marketing tool.

3. Request and filter the list of subscribers in your external marketing tool based on customers subscription status for the current event. 

4. When the ticket sale start date arrives, send notifications to your customers who have opted in to receive marketing emails.
