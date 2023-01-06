SortOrder: 3
# Reporting and Canceling Events

Before diving in,
it's important to understand the difference between a trigger and an event
and what all this means for your users.

A **trigger** is the configuration you create for your app
in the Wix Developers Center.
On the other hand, an **event** is what takes place in your service,
which you then report to Wix.
(For more complete definitions, see
[Terminology](https://dev.wix.com/api/rest/wix-automations/introduction?branch=triggered-events#terminology)
in the introduction to this API.)

The distinction between triggers and events is hidden from your users.
From their perspective,they interact with triggers only.
Users who install your app
are able to use your triggers when they create new automations for their site.
When your app reports an event,
all site automations that use the specified trigger are activated.

## Event types

Wix Automations supports 2 types of events for triggers:
real-time events and scheduled events.

Each trigger can support either real-time events or scheduled events, but not both.
However, you can call [Report Event](/docs/../report-event/) multiple times
in response to a single business event in your system.

This table lays out the differences between real-time events and scheduled events:

| Real-time event                                                                                                            | Scheduled event                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Takes place the moment it's reported.                                                                                      | Takes place at a date and time specified in the payload.                                                                                                                                                                                                                                                |
| Supported by default in new triggers.                                                                                      | Supported only when your trigger meets both of these criteria: <ul> <li>A `date-time` property is specified in the trigger's [payload schema](./the-payload-schema.md).</li><li>You select the **Allow scheduled events with predefined date & time** option in your trigger configuration. </li> </ul> |
| Supports automation actions: <ul> <li>Immediately when the event is reported.</li><li>After the event is reported. </li> </ul> | Supports automation actions: <ul> <li>At the event time in the payload.</li><li>Before the event time in the payload.</li><li>After the event time in the payload. </li> </ul>                                                                                                                                  |

## About canceling events

Your users may configure actions to be carried out some time after you report an event.
If you create a trigger for something that could be canceled or deleted,
we strongly recommend canceling events when they're no longer relevant.
If your app doesn't cancel events,
your users' automations may carry out undesired actions,
like sending overdue notices for invoices after they've been paid.

Events are not cancelable by default.
To make an event cancelable,
you must first pass an `externalEntityId` and the applicable `triggerKey`to
[Report Event](https://dev.wix.com/api/rest/wix-automations/triggered-events/report-event).
When you call
[Cancel Event](https://dev.wix.com/api/rest/wix-automations/triggered-events/cancel-event)
with the same `externalEntityId` and `triggerKey`,
the event is canceled,
as are all other events that share the same `externalEntityId` and `triggerKey`.

### Choose the right `externalEntityId`

It's important to know that the Cancel Event endpoint cancels _all_ events
with the specified combination of `triggerKey` and  `externalEntityId`.
You must think through your implementation carefully
to make sure you don't pass an `externalEntityId`
that could cancel events you don't mean to cancel.

Consider what kind of relationship between entities you're trying to support.
These general guidelines might help you decide what ID to use
for `externalEntityId`:

* If you're supporting a one-to-many relationship,
  use the ID from the _many_ side of the relationship.

  For example, in a contact-to-invoices relationship:
  An invoice relates to a single contact,
  but a contact can relate to multiple invoices.
  The invoice ID is the appropriate `externalEntityId`.

* If you're supporting a many-to-many relationship,
  create a unique event ID for each reported event.

  For example, in a students-to-classes relationship:
  Each student relates to multiple classes,
  and each class relates to multiple students.
  A new event ID is the appropriate `externalEntityId`.

<blockquote class="important">

__Important:__
The scenarios here are for illustration only.
Always evaluate your implementation against your users' real-world requirements.

</blockquote>

### Scenario 1: One-to-many relationship

**The scenario**:
Customers can schedule appointments with site collaborators.

**Suggested value for `externalEntityId`**: Appointment ID

**Suggested triggers and how your users might use them**:

| Trigger key and description                                                                                   | How your users might use the trigger                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>`appointment_scheduled`</p> <p>Real-time event. Triggered when someone schedules an appointment.</p>       | <ul><li>Immediately send a confirmation email to the customer.</li> <li>Immediately send a notification to site collaborators.</li> </ul>                       |
| <p>`appointment_starting`</p> <p> Scheduled event. Triggered in relation to the appointment's start time.</p> | <ul> <li>Send a reminder email _x_ days before the appointment.</li> <li>Notify the applicable site collaborator _x_ minutes before the appointment.</li> </ul> |
| <p>`appointment_canceled`</p> <p>Real-time event. Triggered when someone cancels an appointment.</p>          | <ul> <li>Immediately send a cancellation email to the customer.</li> <li>Immediately notify site collaborators of the cancellation.</li> </ul>                  |

**Example logic for your app**:

| Business event                    | Your app's API calls                                                                                                                                  |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer schedules an appointment | <ol> <li>Report `appointment_scheduled` event.</li> <li>Report  `appointment_starting` event.</li> </ol>                                              |
| Customer cancels an appointment   | <ol> <li>Report `appointment_canceled` event.</li> <li>Cancel `appointment_scheduled` event.</li> <li>Cancel `appointment_starting` event.</li> </ol> |

### Scenario 2: Many-to-many relationship

**The scenario**:
Participants can enroll in multiple courses.
Each course can contain multiple participants.

**Suggested value for `externalEntityId`**:
A generated enrollment ID, unique to each student-class combination.

**Suggested triggers and how your users might use them**:

| Trigger key and description                                                                                 | How your users might use the trigger                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>`participant_enrolled_in_class`</p> <p>Real-time event. Triggered when someone signs up for a class.</p> | <ul> <li>Immediately send a confirmation email to the participant.</li> <li>Immediately send a notification to the site owner.</li> </ul>               |
| <p>`class_starting`</p> <p>Scheduled event. Triggered in relation to the class's start time.</p>            | <ul> <li>Send a reminder email _x_ days before the class.</li> <li>Notify the site owner _x_ minutes before the class.</li> </ul>                       |
| <p>`participant_left_class`</p> <p>Real-time event. Triggered when someone is unenrolled from a class.</p>  | <ul> <li>Immediately send a confirmation email to the participant.</li> <li>Immediately notify the site owner that someone left their class.</li> </ul> |
| <p>`class_canceled`</p> <p>Real-time event. Triggered when a class is canceled.</p>                         | <ul> <li>Immediately send a confirmation email to each participant.</li> <li>Immediately notify the site owner that a class is canceled.</li> </ul>     |

**Example logic for your app**:

| Business event                 | Your app's API calls                                                                                                                                      |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Participant enrolls in a class | <ol> <li>Report `participant_enrolled_in_class` event.</li> <li>Report `class_starting` event.</li> </ol>                                                 |
| Participant leaves  a class    | <ol> <li>Report `participant_left_class` event.</li> <li>Cancel `participant_enrolled_in_class` event.</li> <li>Cancel `class_starting` event.</li> </ol> |
| Class is canceled              | <ol> <li>Report `class_canceled` event.</li> <li>Cancel `participant_enrolled_in_class` event.</li> <li>Cancel `class_starting` event.</li> </ol>         |