SortOrder: 0
# Virtual Numbers Manager

## What is it?
The service manages all entities of Virtual Numbers.

### The managed entities
#### [Agent](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/agent.proto)
An agent is a site level entity which describes a person whose communication channels can be configured as the agent's channels.
An agent can also be assigned to a [VirtualNumberAccount](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/virtual_number_account.proto) such that incoming calls to the account's business number will be redirected to the agent's configured communication channel.
The assigned agent can also make phone calls through the business number which will be redirected to the requested number.

#### [AssignedAgent](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/agent.proto)
An assigned agent is an entity representing the connection between [VirtualNumberAccount](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/virtual_number_account.proto)
 and an [Agent](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/agent.proto).
This entity holds the configuration of the agent's availability for receiving inbound calls from this account's business number.  

#### [PhoneNumber](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/phone_number.proto)
An entity representing a phone number that can be used as a business number and once purchased it is linked to a 
[VirtualNumberAccount](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/virtual_number_account.proto).
This entity specifies the type of the number along with its capabilities.

#### [CommunicationChannel](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/channel.proto)
An entity representing a channel to communicate with an agent.
This channel needs to be verified in order for the agent to be able to make and receive calls through it. 

#### [Schedule](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/schedule.proto)
An entity representing a time frame (single or recurring) which is being used to describe the availability time of an agent.

#### [VirtualNumberAccount](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/virtual_number_account.proto)
A VirtualNumberAccount is the main entity which wraps everything together.
An account can be linked to a certain business number, and can have a list of assigned agents which can communicate through this number.
This entity also holds the user preferences (settings) for the account usage.

#### [Voicemail](https://github.com/wix-private/crm/blob/master/virtual-numbers/backend/manager/manager-api/src/main/proto/com/wixpress/virtual/numbers/manager/api/v1/entities/voicemail.proto)
An entity representing a voicemail message that the account owner can configure in order to play for the caller when there's no answer.   
   
## Architecture

## The API 
