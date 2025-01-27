SortOrder: 1

# Terminology
The Groups APIs provide all the functionality required to create and manage groups. 

This article contains a comprehensive list of the various terms and concepts used in the Groups APIs.

## Create request
When a Wix user has not given site members permission to create groups, they can submit a request to create a group. The request can be approved or rejected by a group admin.

## Group
Place where members can connect with each other to get updates and share media.

## Group list
List of groups displayed in the Wix Groups app home page.

  > **Note:** Depending on the viewer's [role](#role), not all groups will be displayed.

## Group member
Site member that has joined a group. The Groups API doesn't assign group members a unique ID. Instead, it uses the `memberId` from the [Members API](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/introduction) for identification.

## Group privacy status
Defines the visibility of a group in a [group list](#group-list) and how a site member can join it.

  - **Public**: Anyone can see the group and its content. Anyone can join the group.
  - **Private**: Anyone can see the group, but only group members can view its content. In order to join the group, site members must submit a [join group request](#join-group-request).
  - **Secret**: Only group members and admins can see the group. It is not possible for site members to submit a [join group request](#join-group-request). Instead, group members and admins can add new members.

## Group settings
Group specific `settings`. Includes whether members can see the full group member list or invite new members. Wix users can also manage settings [in the dashboard](https://support.wix.com/en/article/wix-groups-managing-your-group).

## Join group request
Request submitted by a site member to join a private group. The request can be approved or rejected by a group admin.

## Membership question
A question asked to members when joining a group. Wix users can set whether it is required to answer the question in the dashboard.

## Role
Role a site visitor has in a group.

  - **Anonymous:** Site visitor that isn't logged in.
  - **Site member:** Site visitor that is logged in but not a group member.
  - **Group member:** Site member that has joined a group.
  - **Group admin:** Group member with additional permissions. The creator of a group is automatically a group admin.
  - **Wix Groups Manager:** Member, Wix user or Wix app with full management permissions. Site admins are always Wix Groups Managers.

## Rule
Guidelines ensuring that members post responsibly and respectfully. Wix users can set up group rules in the dashboard.
