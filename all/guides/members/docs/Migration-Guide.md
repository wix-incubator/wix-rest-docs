SortOrder: 1
# Migration Guide

Migration guide to describe where what data goes to and where to get all the data you need.

## Bazel

For scala artifacts you need to add the required dependency: `@app_market//members/members-api:proto_scala`

It's a gRPC service, not JSON-RPC, so it needs to be initialized as gRPC service.

Example for Loom:

```scala
val membersNgClient = MembersWithCallScope.stub(grpcChannel, _.withAuthority("com.wixpress.members.members-ng-api"))
```

Example for bootstrap:

```scala
@Bean def membersNgClient(clients: Clients): MembersWithCallScope.MembersGrpcClient =
  MembersWithCallScope.stub(clients.grpcChannel(GrpcProxyUrl), _.withAuthority("com.wixpress.members.members-ng-api"))
```

## Node

For node artifacts you use:
 1. Ambassador `@wix/ambassador-members-ng-api`
 2. Directly `@wix/members-ng-api`


## RPC Endpoints

Table which describes how [v1.MembersService](https://github.com/wix-private/crm/blob/master/wix-site-members/wix-sm-platform-api/members-api/src/main/proto/MembersService.proto#L16) maps to [api.Members](https://github.com/wix-private/app-market/blob/master/members/members-api/proto/com/wixpress/members/api/members.proto#L20) PRC:

|wix.members.api.v1.MembersService|com.wixpress.members.api.Members|
|---|---|
|MembersService.Get|Members.GetMember|
|MembersService.GetCurrent|Members.GetMyMember|
|MembersService.Query|Members.QueryMembers|
|MembersService.List|Members.ListMembers|
|MemberAreaFacade.GetProfile|Members.GetMember|
|ProfileService.Query|Members.QueryMembers|
|HydraContactsFacade.FindMemberByContactId|Members.GetMember|
|MemberAreaFacade.CountActiveProfiles|Members.QueryMembers|
|HydraUsersFacade.getMemberStatusByMemberId|Members.GetMember & fieldSet=FULL to get the status|
|SiteMembersService.getMembersByUser|Members.QueryMembers & userId in the filter|
|SiteMembersService.GetMemberOrOwnerByIdWithRecovery|Members.GetMember|
|MembersService.BatchGet|Members.QueryMembers|
|SiteMembersService.GetMembersByUser|Members.QueryMembers with member ids from SiteMembersService.GetMembersByUser response if you need more than member ids|

## HTTP Endpoints

Table which describes how [v1.MembersService](https://github.com/wix-private/crm/blob/master/wix-site-members/wix-sm-platform-api/members-api/src/main/proto/MembersService.proto#L16) maps to [api.Members](https://github.com/wix-private/app-market/blob/master/members/members-api/proto/com/wixpress/members/api/members.proto#L20) Http:

|wix.members.api.v1.MembersService|com.wixpress.members.api.Members|
|---|---|
|`api/wix-sm/v1/members/{id}` <br /> `_api/wix-sm-webapp/v1/members/{id}`|`_api/members/v1/members/{id}`|
|`api/wix-sm/v1/members/current` <br /> `_api/wix-sm-webapp/v1/members/current`|`_api/members/v1/members/my`|
|`api/wix-sm/v1/members/query` <br /> `_api/wix-sm-webapp/v1/members/query`|`_api/members/v1/members/query`|
|`api/wix-sm/v1/members` <br /> `_api/wix-sm-webapp/v1/members`|`_api/members/v1/members`|
|`api/wix-sm/v1/profiles/query` <br /> `_api/wix-sm-webapp/v1/profiles/query`|`_api/members/v1/members/query`|
|`api/wix-sm/v1/profiles` <br /> `_api/wix-sm-webapp/v1/profiles/query`|`_api/members/v1/members`|

## Kafka

Table which describes how v1.MembersService CUD events map to api.Members domain events. Domain topic: `domain_events_wix.members.v1.member`

|Topic|Event|
|---|---|
|sm-created-members|CreatedEvent|
|sm-member-joined|CreatedEvent|
|sm-updated-members|UpdatedEvent|
|sm-profile-update|UpdatedEvent|
|sm-deleted-members|DeletedEvent|

## Cross-tenant requests

If you need to to cross-site requests, we're here to help you.
We're secretly supporting first-level `userId` filter in `Members.QueryMembers`.

When you send `userId` filter, we're switching the tenant from "meta site" bound to "user" bound under the hood, so security is not compromised. 
The response entity contains `contactId`, which we can use in order to figure our the meta site contexts for each of the records.
In order to find out the meta site contexts for each of the records, you need to call `MembersIdentity.GetContactMetaSites` from [members-identity-api](https://github.com/wix-private/app-market/blob/master/members/members-identity-api/proto/com/wixpress/members/identity/members_identity.proto#L14) service.
The response will contain the map of `contactId` to `metaSiteId`.


## Data

### Member data

Table which describes how [v1.Member](https://github.com/wix-private/crm/blob/master/wix-site-members/wix-sm-platform-api/members-api/src/main/proto/resources/Member.proto#L15) maps to [api.Member](https://github.com/wix-private/app-market/blob/master/members/members-api/proto/com/wixpress/members/api/member.proto#L13):

|wix.members.api.v1.Member|com.wixpress.members.api.Member|
|---|---|
| id | id |
| email_verified | - |
| role | - |
| login_email | login_email |
| member_name | contact.first\_name, contact.last_name |
| first_name | contact.first_name |
| last_name | contact.last_name |
| image_url | profile.photo.url | 
| nickname | profile.nickname |
| profile\_privacy_status | privacy_status | 
| slug | profile.slug |
| language | - |
| status | status |
| creation_date | created_date |
| last\_update_date | updated_date | 
| last\_login_date | - |
| emails | contact.emails |
| phones | contact.phones |
| addresses | - |
| labels | - |
| custom_fields | - |
| picture | profile.photo |
| user_id | - |
| groups | - |
| contact_id | contact.contact_id |

### Member status

Table which describes how [v1.SiteMemberStatus](https://github.com/wix-private/crm/blob/master/wix-site-members/wix-sm-platform-api/members-api/src/main/proto/resources/Member.proto#L126) maps to [api.AccessStatus](https://github.com/wix-private/app-market/blob/master/members/members-api/proto/com/wixpress/members/api/member.proto#L57):

|wix.members.api.v1.SiteMemberStatus|com.wixpress.members.api.AccessStatus|
|---|---|
|UNDEFINED_STATUS|UNKNOWN|
|APPLICANT|PENDING|
|ACTIVE|APPROVED|
|INACTIVE|PENDING|
|BLOCKED|BLOCKED|
|OFFLINE_ONLY|OFFLINE|


### Groups

Group data for each members can be fetched from [GroupsService.ListUsersGroups](https://github.com/wix-private/crm/blob/master/members-groups/api/src/main/proto/com/wixpress/members/groups/GroupsService.proto#L76).

### Identity

The `user_id`, `role` are data which will be served from Identity's side [MembersService.GetRole](https://github.com/wix-private/crm/blob/master/wix-site-members/wix-sm-platform-api/members-api/src/main/proto/MembersService.proto#L47).

### Contacts

The remaing contact data, which is not served from this API, must be queried from Contact's [ContactsService](https://github.com/wix-private/crm/blob/master/wix-contacts-server/wix-contacts-platform-api/wix-contacts-api/src/main/proto/com/wixpress/contacts/api/v3/contactsService.proto#L12)

## Member fieldset

Which fields will be returned using which fieldset property

|Public|Extended|Full|
|---|---|---|
|id|id|id|
| |login_email|login_email|
| |status|status|
|contact_id|contact_id|contact_id|
| | |contact.first_name|
| | |contact.last_name|
| | |contact.phones|
| | |contact.emails|
| | |contact.addresses|
|profile|profile|profile|
| |privacy\_status|privacy\_status|
| |activity\_status|activity\_status|
|created_date|created_date|created_date|
|updated_date|updated_date|updated_date|
| | |last_login_date|

## Member permission model

There are 3 levels of permisions for most of the endpoints:

- MEMBERS.MEMBER\_READ - allows to read PUBLIC member information for members who's privacy status is PUBLIC
- MEMBERS.MEMBER\_READ\_PRIVATE - allows to read PUBLIC member information for members who's privacy status is PUBLIC or PRIVATE
- MEMBERS.MEMBER\_READ\_FULL_SET - allows to read member data with FULL fieldSet.

The service will figure out what are the permissions of the caller identity and return the appropriate result.

## Member privacy status

This API respects member's privacyStatus. This means that only if the caller has required permissions to see members with PRIVATE privacy status - only then API will return member who's privacy status is PRIVATE.

If you have a flow where you *really* need to read members data with PRIVATE status, please let us know in #members.

# Good luck
