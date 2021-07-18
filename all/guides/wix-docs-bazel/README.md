SortOrder: 0
# Guilder

## ABOUT

Guilder is an internal service for Guild week management.
Once registered, Guilder will run weekly and send calendar invitations to the upcoming guild week participants, based on your own Guild week placement document. 

It also sends an email reminder, for every participant few days before the guild week starts and opens a slack channel for the relevant participants.

In order to register create Your own "Guild Week placement spreadsheet" - [How to create this spreadsheet](https://github.com/wix-private/automation-web-services/blob/master/guilder/CreatingSpreadsheet.md)

Contact the VI group.

## API

### Execute 
For all clients or using 'owner' for a specific client
```
@GET("/api/guilder/execute") execute(owner)
```
`owner` - client email, optional

**Usage:** `` GET /api/guilder/execute?owner=client_email ``

**Response:** `` {"data":"isSuccessful":true, "errorDescription":""} ``

### Execute Intro
For all clients or using 'owner' for a specific client
```
@GET("/api/guilder/executeIntro") executeIntro(owner)
```
`owner` - client email, optional

**Usage:** `` GET /api/guilder/executeIntro?owner=client_email ``

**Response:** `` {"data":"isSuccessful":true, "errorDescription":""} ``

## Development
Guilder Services web module is GAE based, and running on Java 8 environment 

### Running locally
Coming soon ...
 
### Deploying
* Secrets injection
* Use the IntelliJ App Engine Deployment configuration, or any other legacy equivalent GAE plugin

### Monitoring
[GAE Dashboard](https://console.cloud.google.com/appengine?project=guilder-web)

[Stackdriver](https://app.google.stackdriver.com/?project=guilder-web)

