SortOrder: 1
# Member-to-Member Blocking Integration Guide

## Background
To meet the requirement of user blocks for Apple App-Store, the Members Area is introducing a feature called Member-to-Member Blocks. With it enabled, `member A` has to have a way to block `member B` and thus no longer see anything related to `member B`, except in a page displaying blocked member list, where `member A` could see and unblock `member B`, and thus see all their stuff again. After `member A` blocks `member B`, `member B` no longer sees anything related to `member A`. Also, `member B` is not notified about creation of this block and cannot remove it.


## Changes in Members Area
### A New Service: Member-to-Member Blocks API
Members Area are creating a service enabling member-to-member block data manipulation, data querying and publishing of related domain events. The current version of the proto documentation can be found here: https://bo.wix.com/wix-docs/rest/all-apis/membertomemberblocks

### Changes in Umbrella API (members-ng-api)
There will be certain changes in members-ng-api, as also illustrated by the flow diagrams specified below:
1. When calling `Umbrella API`'s endpoints `ListMembers` and `QueryMembers` with `SiteMember` identity (i.e. there's a current member that can be determined), these endpoints will return only those members that are not blocked by and not blocking the current member.
2. `Umbrella API` endpoint `GetMember` will do an additional check if the requested member is blocking or blocked by the current member and adjust the result according to that:
    - if the requested member is blocking the current member, an error with http status code `NOT_FOUND` will be returned
    - if the requested member is blocked by the current member, an error with http status code `NOT_FOUND` and application code `MEMBER_BLOCKED` will be returned.
    - if none of the above is true, the member info will be returned same as currently.

## Use Case Examples
Example flows are displayed below:
![Example Flows Image](https://s3.amazonaws.com/wixplorer-readme-images/member-to-member-blocks%2F2021-05-24_Integration_Example_Flows.png)

## Rollout Plan

### Phase 1
Both `Members` and all related `Verticals` have to perform the necessary actions:
1. `Members`: Release the Member-to-Member Blocks API
2. `Members`: Release the changes in Umbrella API
3. `Verticals`: Placeholder property values in the Verticals

### Phase 2
The related `Verticals` adapt their functionality to fully address block relationships between members, including,  but not limited to:
1. `Verticals`: Consumption of domain events upon block creation and/or removal, if applicable, e.g. to destroy existing relationships.
2. `Verticals`: Additional filtering and limiting of visibility and functionality between the members involved in a block relationship.

