SortOrder: 0
# Session Service
 
The session service is a Nile service which is in charge of managing sessions, including
creating, signing, updating (the expiration date), revoking and querying sessions.

### What is a session?
A session is a token which identifies a person (user, member, or visitor) or an application. 
A session may or may not have an expiration date.
The service can issue more than one session to the same identity (person or an application).

### What is the main purpose of this service?
The main purpose is to provide the ability to revoke sessions.
In the identification process we check that a session is not revoked.

### Which sessions does the service currently support?
The service currently support only Api Keys. 

### API
for more details see the [#proto files](https://github.com/wix-private/server-infra/tree/master/core-services/identity-session/identity-session-server/proto/com/wixpress/identification/session)
 - CreateSession
 - RevokeSession
 - GetSession
 - UpdateSessionExpirationDate
 - QuerySession

### How to call the API?
This service is available for internal calls only. 
It requires a service identity with the permissions listed in the [#proto file](https://github.com/wix-private/server-infra/blob/master/core-services/identity-session/identity-session-server/proto/com/wixpress/identification/session/session_service.proto)

#### managing Api Keys
Api Keys are account level tokens.
Make sure you have a targetAccountId in the callScope. It is used to determine the accountId of the Api Key. 
 
#### Managing other sessions - TBD  






