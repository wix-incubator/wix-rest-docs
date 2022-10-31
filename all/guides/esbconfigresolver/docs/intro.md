SortOrder: 0
# About the Triggers API and SPI

TODO

## Terminology

> This isn't final, but it's in a good enough state to capture in the internal docs

- __Automation__: Consists of a trigger and one or more actions.
- __Trigger__: Configuration that defines when an automation will be activated,
  as well as the expected payload (schema). Defined by an app.
- __Action__: What happens in response to a trigger.
  An action can be immediate, scheduled for a future datetime, or after a specified delay,
  depending on how the app configures the trigger
  and how the site collaborator configures their automation.
- __Event__: Activates automations with a specified trigger key.
  An event includes a payload that meet the schema requirements defined by the app that created the trigger.
  An event can be a realtime event or a scheduled event.
  - __Realtime event__: Event that happens at the time it's reported.
  - __Scheduled event__: Event that doesn't happen when it's reported,
    but rather at a future datetime as reported in a designated field in the payload.
- __Activation__: A discrete activation is generated for each automation where the activated trigger is used.

## Before You Begin

TODO