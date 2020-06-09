SortOrder: 0
## Introduction

This API extends the Dealer API (https://bo.wix.com/wix-docs/rest/core-apis#dealer.introduction).

It enables tracking and querying data about how a user (or support agent) interacted with a dealer offer. This is important for example for the following use cases:
- Don’t show the user an offer that he previously skipped
- Show the offer only if the user has viewed it less than 5 times in the last month
- Mark that a Wix support agent has offered this offer to the user, but the user rejected it


### Using the API


Using this API usually involves 2 parts:
**Report Event** - Notifying the service that the user (or agent) has performed an interaction 


**List Events Summary** -  Getting a summary report of all previous interactions

### Types of Events


There are 3 types of events:
**Quantitative** - e.g. View, Interaction etc’. For this type of events the summary will include the count of events within a given time frame (from present time, backwards)


**User marked** - e.g. Skipped, Show Later etc’. These events represent a user action where the count doesn’t matter, but only whether they happened / when. 


**Agent marked** - e.g. Suggested, Rejected, Requested. These events represent a Wix employee, who made a mark on behalf of a user. For example the agent talked to a user and suggested him to add a product to his Wix Store.