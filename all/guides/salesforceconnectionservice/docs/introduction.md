SortOrder: 0
# About Connections

This service is responsible for managing the connections between the Salesforce and the B2B system. It is responsible
for creating, updating, and deleting connections between the two systems. It also provides the ability to retrieve the
connection details.

## Connection

The connection object is the main object that is used to manage the connection between the two systems. It contains the
following fields:

- `id` (string): The unique identifier of the connection.
- `salesforce_instance_url` (string): The URL of the Salesforce instance.
- `salesforce_access_token` (string): The access token of the Salesforce instance.
- `salesforce_refresh_token` (string): The refresh token of the Salesforce instance.

## Endpoints
    


