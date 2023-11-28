SortOrder: 1
# Sample Use Cases and Flows
This article shares some possible use cases your app could support, as well as an example flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.

## Create a new Schema
1. Use [CreateSchema](/docs/<link_to_schemas>) in order to create a new schema.

## Update an existing Schema

As an app owner, you might want to update an existing Schema.

1. First, retrieve your Schema's id by using 
  [GetSchemaByKey](/docs/<link_to_Schemas>). You should know the SchemaKey of the Schema you wish to update.

2. Next, use [UpdateSchema](/docs/<link_to_Schemas>), with the id you retrieved in the previous step.

3. Add to the request all the information you wish to update, don't forget to list the fields you are updating in FieldMask.

## Querying existing Schemas

If your app handles translations of other apps, you might want to query the existing schemas.

1. Use [QuerySchemas](/docs/<link_to_Schemas>) with the available filters.
