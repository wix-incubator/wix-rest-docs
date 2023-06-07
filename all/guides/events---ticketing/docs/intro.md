SortOrder: 0
# Introduction

#### Tickets

To start selling tickets, the user needs to set the ticket definition 
(title, price, amount of tickets available, currency and an optional 
short description).

Once the first is ticket defined, the event becomes a ticketed event 
(event type **tickets**).

To register to the event: the guest has to choose the tickets, 
fill out the **Registration Form** and checkout. An order is created
and if tickets are not free then payment has to be made. *Once payment
is received the confirmation email with attached tickets PDF is sent to
the guest.*

Payment collection is provided by [Cashier][cashier]

### API

#### Order management

* [OrderManagement.List][order-management-list] - a lightweight orders listing service with basic filter support. Includes tickets in the response.
* [OrderManagement.Get][order-management-get] - a service to get a single order with its tickets.
* [OrderManagement.Update][order-management-update] - a service to partially update order
* [OrderManagement.Complete][order-management-complete] - a service to complete order.
Changes order status from "INITIATED, "PENDING", "OFFLINE_PENDING" to "PAID".
Already completed orders (with status "PAID" or "FREE") are unchanged.

The [Order][order] entity contains a link to ticket PDF. 
To check-in the ticket the organiser of the event has to use Wix mobile app and scan the QR code of the ticket.

![Ticket example][ticket-example]

#### Ticket management

* [TicketManagement.List][ticket-management-list] - a ticket listing service with basic filter support.
* [TicketManagement.Get][ticket-management-get] - a service to get a single ticket.
* [TicketManagement.CheckIn][ticket-management-check-in] - a service to check-in ticket.
* [TicketManagement.DeleteCheckIn][ticket-management-delete-check-in] - a service to delete ticket check-in.

#### Ticket definition management

* [TicketDefinitionManagement.Create][ticket-def-management-create] - a service to create ticket definition and start selling tickets.
* [TicketDefinitionManagement.List][ticket-def-management-list] - a ticket definition listing service with basic filter support.
* [TicketDefinitionManagement.Get][ticket-def-management-get] - a service to get a single ticket definition.
* [TicketDefinitionManagement.Update][ticket-def-management-update] - a service to update ticket definition.
* [TicketDefinitionManagement.Delete][ticket-def-management-delete] - a service to delete ticket definition.
* [TicketDefinitionManagement.ChangeCurrency][ticket-def-management-change-currency] - a service to change currency for all tickets.

[cashier]: https://wixplorer.wixpress.com/cashier-pay/reference

[order-management-list]: ../reference/order/.wix.events.ticketing.-order-management.-list
[order-management-get]: ../reference/order/.wix.events.ticketing.-order-management.-get
[order-management-update]: ../reference/order/.wix.events.ticketing.-order-management.-update
[order-management-complete]: ../reference/order/.wix.events.ticketing.-order-management.-complete
[order]: ../reference/order

[ticket-example]: https://static.wixstatic.com/media/babf39_1dcf46d9715a4c92979eb44c4a8e7277~mv2_d_1636_1348_s_2.png/v1/fill/w_1636,h_1348,q_85,usm_0.66_1.00_0.01/babf39_1dcf46d9715a4c92979eb44c4a8e7277~mv2_d_1636_1348_s_2.png
[ticket-management-list]: ../reference/ticket/.wix.events.ticketing.-ticket-management.-list
[ticket-management-get]: ../reference/ticket/.wix.events.ticketing.-ticket-management.-get
[ticket-management-check-in]: ../reference/ticket/.wix.events.ticketing.-ticket-management.-check-in
[ticket-management-delete-check-in]: ../reference/ticket/.wix.events.ticketing.-ticket-management.-delete-check-in

[ticket-def-management-create]: ../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-create
[ticket-def-management-list]: ../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-list
[ticket-def-management-get]: ../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-get
[ticket-def-management-update]: ../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-update
[ticket-def-management-delete]: ../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-delete
[ticket-def-management-change-currency]: ../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-change-currency