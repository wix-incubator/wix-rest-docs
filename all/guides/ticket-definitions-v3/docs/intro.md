SortOrder: 0
# About Ticket Definitions v3

With the Ticket Definitions API, you can create definitions for tickets. A definition includes the following ticket settings:

- Fee type. Determine whether the fee will be paid by a guest or a seller.
- Pricing. Define different ticket prices based on factors such as early bird discounts, VIP packages, group rates, or special promotions. Several pricing methods are available for you to select from: **Fixed price**, **Guest price**, **Free**. Additionally, you can customize prices for different groups of people using **Price options**.
- Availability. Set the ticket limit available to buy. Also, you are able to check number of purchased or reserved tickets.
- Sale period. Set the sale start and end dates. Also, when defining the sale period, it is possible to choose to display event tickets to customers even before the sale starts.

## Before you begin

It’s important to note the following points before starting to code:

- Install the **Wix Events & Tickets** app from [Wix App Market](https://www.wix.com/app-market/wix-events?referral=category&appIndex=5&referralTag=booking--events).
- Ticket definition is not the same as ticket. Ticket definitions are used to define settings for a set of tickets. After paying for selected tickets, the [Checkout API](https://dev.wix.com/api/rest/wix-events/wix-events/checkout/order-object) automatically generates the ticket.

## Use cases

- [Add a specific-price ticket counter for an event](events-services/events-ticket-definitions/proto/docs/sample-use-cases-and-flows.md#add-a-specific-price-ticket-counter-for-an-event)
- [Sync ticket definitions with external ticketing system](events-services/events-ticket-definitions/proto/docs/sample-use-cases-and-flows.md#sync-ticket-definitions-with-external-ticketing-system)
- [Notify when tickets go on sale](events-services/events-ticket-definitions/proto/docs/sample-use-cases-and-flows.md#notify-when-tickets-go-on-sale)

## Terminology

- **Pricing method**: Different pricing methods are available for an event:
    - **Fixed price**: All tickets in the same definition are sold at the exact same price, regardless of when they are purchased or other factors.
    - **Guest price**: A minimum price a guest must pay for a ticket. For example, money goes to donation.
    - **Price options**: All tickets in the same ticket definition are priced at different rates, such as different prices for adults, children, and students.
- **Ticket availability**: The status of ticket inventory, indicating whether tickets are available or sold out. This type can also include availability limits and timeframes for ticket sales.
- **Sale period**: Duration of time during which event tickets are available for purchase. 
- **Event Dashboard**: Control center in the Wix site UI for managing site event settings and features.