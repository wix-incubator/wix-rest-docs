SortOrder: 0
# Action SPI Provider

Here are the steps to create an automation action:

## Create application component
Each action must belong to some application in the form of an application component. Application may contain multiple actions (components). Each action must have a unique key in the related application.
ATM adding action to an application is done via direct [RPC call](https://pbo.wix.com/fire-console/?artifact=com.wixpress.devcenter.app-service-webapp&server=app-service-webapp-855777b7dd-mv2wh%3A8081&service=Components&method=create&body=eyJyZXF1ZXN0Ijp7ImFwcElkIjoiIn19)

Expected parameters:
- `appId` - ID of the application for which to create the component.
- `compData` - the app component's data. Select `automationsActionProvider` type and provide additional fields:
  - `actionsConfig`:
    - `outputSchema`, `inputSchema` - A schema that specifies which fields the action expects to get and which fields the action will emit. A JSON Schema (such as [this](http://json-schema.org/draft-07/schema)) should be used to describe the input and output schemas.  
    - `executionType` - `SYNC` or `ASYNC`. Please use `SYNC` unless you have a good use case such as an action that is executing some long 3rd party operation and that operation is not returning the response right away but instead should call us and notify us that the operation has ended. In the case you need to use `ASYNC` please contact us for further assistance. Note that using `SYNC` adds no performance penalty since the automations runtime engine is async by design.
    - `actionKey` - A unique key (name) of the action.
  - `baseUri` - URI of where the Action Provider service is deployed. For internal Wix service, the URI should be grpc://<artifact-id> ([More info](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/spi---service-provider-interface#platformization-guidelines_spi---service-provider-interface_wixspibase_uri)).
- `compType` - set it to `AUTOMATIONS_ACTION_PROVIDER`.
- `compName` - user-friendly name of the component.

Example [request](/docs/create-component-request-example.json).

After adding the action component via RPC we can see a new component is added in dev center.

Note: ATM there is no UI for creating and editing action components, but there is a UI option to delete components.

## Implement Action SPI Provider
Implement [this](https://github.com/wix-private/wix-automations/blob/master/action-spi-provider/src/main/proto/com/wixpress/esb/spi/action/v1/action_spi_provider.proto) SPI provider:

Implementation can be done using loom`, nodejs or any other way.

A single action SPI implementer should be created per application. Each action SPI implementer can handle all the actions (components) in the application. `action_key` field in the `InvokeRequest` message will indicate what the current action is.

There are the following endpoints:
- `Invoke` - This is where the action should be implemented:
  - `InvokeRequest` contains the following fields:
    - `action_key` - the key of the action as was defined in the component.
    - `execution_identifier` - some identifier of the currently invoked action.
    - `action_params` - object that contains all the relevant data that was collected from the trigger and from the event execution chain. The structure of this object is defined by the `input_schema` as was defined in the action component.
    - `request_context` - object that contains the context of the current request. Usually useful for advanced use cases or attribution.
  - `InvokeResponse` contains the following fields:
    - `result` - object that contains the output data of the action. The data structure should follow the definition in the `output_schema` field in the component.
- `ValidateConfiguration` - Called when the system has to validate the action config (user input..), for example in the Automation dashboard, so the user will be notified if the automation has a problem.
  When the Users click on an automation to see more information, they will be provided with information including the data returned by this method.

  * There is no need to do validations on JSON Schema types, we are validating the schema before calling validate config.
  * This method is optional - if not implemented by the provider, the action will be always considered to have valid configuration

Sample [implementation](https://github.com/wix-private/wix-automations/blob/master/actions/send-mail-provider/src/com/wixpress/automations/actions/v1/SendMailActionProvider.scala).

## Test Action:
There are 2 ways to test the action:
1. Use [this](https://pbo.wix.com/fire-console/?artifact=com.wixpress.esb.runtime.esb-runtime-engine&service=com.wixpress.esb.runtime.EsbRuntimeSpiActionTestService&method=TestAction) RPC to simulate a run of this action:
   - The parameters that we would use are:
     - `action_key` - the relevant action key as defined in the action component.
     - `user_action_config` - any payload, a valid JSON.
   - The call should be server signed with the following:
     - App ID of the application that contains the relevant action component. This app should have `ESB_RUNTIME.TEST_ACTION` permission.
     - Meta site ID.
2. Create a new automation that will use this action.
