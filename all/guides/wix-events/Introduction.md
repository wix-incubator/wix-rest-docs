SortOrder: 3
# Introduction

Wix Events will allow you to easily create and manage events, and enjoy many features, 
such as the ability to collect guest RSVPs, sell tickets, manage the guest list and check guests in.

### What can you do with it?

1. Create events (unlimited) by filling out the relevant event details.
2. Choosing between guests RSVPing to event or purchasing tickets.
3. Guests see the events, can read about them in dedicated event details page (optional) and signs up to the event. 
4. User manages guest list, can see who RSVPd and/or purchased tickets, and check them in as arrived, on the event day.

### What is an event?

Each event is defined by the user for his website and contains the following data properties:
1. General info: event title, description, rich text about section.
2. Scheduling information: start and end date times, time zone of the event etc.
3. Location (with assistance of map coordinates).
4. Customizable registration form (*).
5. Optional ticket selling (ticket definitions) (*).
6. External registration link

(*) customizable only in Wix Events dashboard

There are 3 types of events available:
 - **rsvp** - a response type (yes/no)
 - **tickets** - selling of the tickets
 - **external** - registration managed on external website

#### Registration (RSVP)

When a guest responds to a RSVP **Registration Form** then a new RSVP 
is created *and a confirmation email is sent*.

Rsvp registration settings can be configured in the dashboard.
Rsvp options can be Yes only or Yes and No. 

Limiting the number of guests is optional. Once the guest list is
full the registration is closed, unless Waitlist is enabled.

*If user RSVP to Waitlist, he will get a email once 
additional space in event is available*

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

Payment collection is provided by [Cashier](https://wixplorer.wixpress.com/cashier-pay/reference)

#### External

Registration button can be linked to an external website from 
the dashboard. Once this option is selected event guest 
management (RSVP, tickets) is disabled. 

#### Registration Form

The Registration Form is customizable so the site visitor will 
be able to fill in his details and RSVP to the event or purchase 
tickets in check-out. Users are able to add custom form inputs 
with free text and also pre-defined options (such as a drop-down 
list and radio buttons). The only inputs fields which are fixed: 
First name, Last name and Email.

![Events dashboard](http://static.wixstatic.com/media/babf39_c057d8dfbe8c41a1a78bfa988734013a~mv2_d_3360_1792_s_2.png/v1/fit/w_2000,h_2000/babf39_c057d8dfbe8c41a1a78bfa988734013a~mv2_d_3360_1792_s_2.png) "Events dashboard"

#### Guest List

In the Guest List tab the user can find all of the guests that 
have RSVPd or purchased tickets to an event and also add guests 
manually. The "Check-in" Tab to mark guests that have arrived is 
easily accessed via the guest list.

### API

#### Event management

Currently event management supports event title, description, location, time and image. 
Other event data is available for configuration in site's dashboard.

* [EventManagement.Create](../reference/event/.wix.events.-event-management.-create) - creates a new event in scope of the site. 
Main event data such as title, description, location, time and image is supported. 
Currently **rsvp** events are available to be created. To change event to **external** or **tickets** please use dashboard. 
**Registration Form** has to be configured in dashboard too.
Supports multi-tenancy and tags.
* [EventManagement.Update](../reference/event/.wix.events.-event-management.-update) - updates event details with partial request.
* [EventManagement.List](../reference/event/.wix.events.-event-management.-list) - a lightweight event listing service with basic filter support.
* [EventManagement.Query](../reference/event/.wix.events.-event-management.-query) - a service for listing events with a support of structurized queries.
* [EventManagement.Get](../reference/event/.wix.events.-event-management.-get) - a service to get a single event by id.
* [EventManagement.Cancel](../reference/event/.wix.events.-event-management.-cancel) - a service to cancel event by id.
* [EventManagement.Delete](../reference/event/.wix.events.-event-management.-delete) - a service to delete event by id.

The [Event](../reference/event) entity contain data in the response based on the request fieldset.

| Fieldset     | Comment                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------- |
| DETAILS      | Includes event description, calendar links and main image                                   |
| TEXTS        | Rich texts of the event. This may dramatically increase size of the response                |
| REGISTRATION | Calculates registration (RSVP/tickets) to event state and includes in the response          |
| URLS         | Resolves site urls for each of the event. This adds extra latency to the request            |
| FORM         | Includes event **Registration Form** used for RSVP or tickets checkout                      |
| DASHBOARD    | Calculates event registration (RSVP/tickets) summary and includes in the response. Authorized for site contributors only |

**Registration Form** contains a meta data of field controls how the form has to be rendered in UI. 
The *Form response* has to be sent according to *Registration Form* input fields when creating RSVP or at checkout.

![Registration Form configuration](https://static.wixstatic.com/media/babf39_af0806869d054c86a4bc58454062b61c~mv2_d_1924_1292_s_2.png/v1/fill/w_1760,h_1182,q_85,usm_0.66_1.00_0.01/babf39_af0806869d054c86a4bc58454062b61c~mv2_d_1924_1292_s_2.png) "Dashboard Registration Form configuration"

The form definition in JSON:

```json
{
  "controls": [
    {
      "type": "NAME",
      "system": true,
      "name": "name",
      "inputs": [
        {
          "name": "firstName",
          "label": "First Name"
        },
        {
          "name": "lastName",
          "label": "Last Name"
        }
      ],
      "label": "First Name, Last Name"
    },
    {
      "system": true,
      "name": "email",
      "inputs": [
        {
          "name": "email",
          "label": "Email"
        }
      ],
      "label": "Email",
      "orderIndex": 1
    },
    {
      "name": "phone",
      "inputs": [
        {
          "name": "phone",
          "label": "Phone Number"
        }
      ],
      "label": "Phone Number",
      "orderIndex": 2
    },
    {
      "type": "CHECKBOX",
      "name": "custom-1643bc21138",
      "inputs": [
        {
          "name": "custom-1643bc21138",
          "array": true,
          "label": "Pick colours you like",
          "options": [
            "Red",
            "Green",
            "Blue",
            "Yellow"
          ]
        }
      ],
      "label": "Pick colours you like",
      "orderIndex": 3
    }
  ]
}
```

Example of *Form response*:

```json
{
  "inputValues": [
    {
      "inputName": "firstName",
      "value": "John"
    },
    {
      "inputName": "lastName",
      "value": "Smith"
    },
    {
      "inputName": "email",
      "value": "joh****@***.com"
    },
    {
      "inputName": "phone",
      "value": "+1-***-***-****"
    },
    {
      "inputName": "custom-1643bc21138",
      "values": [
        "Red",
        "Blue"
      ]
    }
  ]
}
```

#### RSVP management

* [RsvpManagement.Create](../reference/rsvp/.wix.events.rsvp.-rsvp-management.-create) - creates RSVP and associates a contact of the site.
The *Form response* has to be sent according to *Registration Form* input fields when creating RSVP or at checkout.
If site member is creating a RSVP the site member id is associated.  
To change existing RSVP - use dashboard.
* [RsvpManagement.List](../reference/rsvp/.wix.events.rsvp.-rsvp-management.-list) - a lightweight RSVPs listing service with basic filter support.
* [RsvpManagement.Query](../reference/rsvp/.wix.events.rsvp.-rsvp-management.-query) - a service for listing RSVPs supporting structurized queries.
* [RsvpManagement.Get](../reference/rsvp/.wix.events.rsvp.-rsvp-management.-get) - a service to get a single rsvp.
* [RsvpManagement.Update](../reference/rsvp/.wix.events.rsvp.-rsvp-management.-update) - a service to update rsvp.
* [RsvpManagement.Delete](../reference/rsvp/.wix.events.rsvp.-rsvp-management.-delete) - a service to delete rsvp.
* [RsvpManagement.CheckIn](../reference/rsvp/.wix.events.rsvp.-rsvp-management.-check-in) - a service to check-in rsvp.
* [RsvpManagement.DeleteCheckIn](../reference/rsvp/.wix.events.rsvp.-rsvp-management.-delete-check-in) - a service to delete rsvp check-in.

#### Order management

* [OrderManagement.List](../reference/order/.wix.events.ticketing.-order-management.-list) - a lightweight orders listing service with basic filter support. Includes tickets in the response.
* [OrderManagement.Get](../reference/order/.wix.events.ticketing.-order-management.-get) - a service to get a single order with it's tickets.
* [OrderManagement.Update](../reference/order/.wix.events.ticketing.-order-management.-update) - a service to partially update order
* [OrderManagement.Complete](../reference/order/.wix.events.ticketing.-order-management.-complete) - a service to complete order.
Changes order status from "INITIATED, "PENDING", "OFFLINE_PENDING" to "PAID".
Already completed orders (with status "PAID" or "FREE") are unchanged.

The [Order](../reference/order) entity contains a link to ticket PDF. 
To check-in the ticket the organiser of the event has to use Wix mobile app and scan the QR code of the ticket.

![Ticket example](https://static.wixstatic.com/media/babf39_1dcf46d9715a4c92979eb44c4a8e7277~mv2_d_1636_1348_s_2.png/v1/fill/w_1636,h_1348,q_85,usm_0.66_1.00_0.01/babf39_1dcf46d9715a4c92979eb44c4a8e7277~mv2_d_1636_1348_s_2.png)

#### Ticket management

* [TicketManagement.List](../reference/ticket/.wix.events.ticketing.-ticket-management.-list) - a ticket listing service with basic filter support.
* [TicketManagement.Get](../reference/ticket/.wix.events.ticketing.-ticket-management.-get) - a service to get a single ticket.
* [TicketManagement.CheckIn](../reference/ticket/.wix.events.ticketing.-ticket-management.-check-in) - a service to check-in ticket.
* [TicketManagement.DeleteCheckIn](../reference/ticket/.wix.events.ticketing.-ticket-management.-delete-check-in) - a service to delete ticket check-in.

#### Ticket definition management

* [TicketDefinitionManagement.Create](../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-create) - a service to create ticket definition and start selling tickets.
* [TicketDefinitionManagement.List](../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-list) - a ticket definition listing service with basic filter support.
* [TicketDefinitionManagement.Get](../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-get) - a service to get a single ticket definition.
* [TicketDefinitionManagement.Update](../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-update) - a service to update ticket definition.
* [TicketDefinitionManagement.Delete](../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-delete) - a service to delete ticket definition.
* [TicketDefinitionManagement.ChangeCurrency](../reference/ticket-definition/.wix.events.ticketing.-ticket-definition-management.-change-currency) - a service to change currency for all tickets.
