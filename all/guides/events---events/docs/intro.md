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

#### External

Registration button can be linked to an external website from 
the business manager. Once this option is selected event guest 
management (RSVP, tickets) is disabled. 

#### Registration Form

The Registration Form is customizable so the site visitor will
be able to fill in his details and RSVP to the event or purchase
tickets in check-out. Users are able to add custom form inputs
with free text and also pre-defined options (such as a drop-down
list and radio buttons). The only input fields which are fixed:
First name, Last name and Email.

![Events dashboard][events-dashboard] "Events dashboard"

#### Guest List

In the Guest List tab the user can find all of the guests that 
have RSVPd or purchased tickets to an event and also add guests 
manually. The "Check-in" Tab to mark guests that have arrived is 
easily accessed via the guest list.

### API

#### Event management

Currently event management supports event title, description, location, time and image. 
Other event data is available for configuration in site's dashboard.

* [EventManagement.Create][event-management-create] - creates a new event in scope of the site. 
Main event data such as title, description, location, time and image is supported. 
Currently **rsvp** events are available to be created. To change event to **external** or **tickets** please use dashboard. 
**Registration Form** has to be configured in dashboard too.
Supports multi-tenancy and tags.
* [EventManagement.Update][event-management-update] - updates event details with partial request.
* [EventManagement.List][event-management-list] - a lightweight event listing service with basic filter support.
* [EventManagement.Query][event-management-query] - a service for listing events with a support of structurized queries.
* [EventManagement.Get][event-management-get] - a service to get a single event by id.
* [EventManagement.Cancel][event-management-cancel] - a service to cancel event by id.
* [EventManagement.Delete][event-management-delete] - a service to delete event by id.

The [Event][event] entity contain data in the response based on the request fieldset.

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

![Registration Form configuration][reg-form-configuration] "Dashboard Registration Form configuration"

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

[cashier]: https://wixplorer.wixpress.com/cashier-pay/reference
[events-dashboard]: http://static.wixstatic.com/media/babf39_c057d8dfbe8c41a1a78bfa988734013a~mv2_d_3360_1792_s_2.png/v1/fit/w_2000,h_2000/babf39_c057d8dfbe8c41a1a78bfa988734013a~mv2_d_3360_1792_s_2.png
[reg-form-configuration]: https://static.wixstatic.com/media/babf39_af0806869d054c86a4bc58454062b61c~mv2_d_1924_1292_s_2.png/v1/fill/w_1760,h_1182,q_85,usm_0.66_1.00_0.01/babf39_af0806869d054c86a4bc58454062b61c~mv2_d_1924_1292_s_2.png

[event-management-create]: ../reference/event/.wix.events.-event-management.-create
[event-management-update]: ../reference/event/.wix.events.-event-management.-update
[event-management-list]: ../reference/event/.wix.events.-event-management.-list
[event-management-query]: ../reference/event/.wix.events.-event-management.-query
[event-management-get]: ../reference/event/.wix.events.-event-management.-get
[event-management-cancel]: ../reference/event/.wix.events.-event-management.-cancel
[event-management-delete]: ../reference/event/.wix.events.-event-management.-delete
[event]: ../reference/event
