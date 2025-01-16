SortOrder: 0

# About Wix Groups

With [Wix Groups](https://support.wix.com/en/article/wix-groups-about-groups), Wix users can offer their members places to participate in discussions, share media and more.

Media in Wix Groups is organized in a gallery.

Wix users can set whether members are allowed to create groups, or add new members to a group.

## Terminology

- **Group**: Place where members can connect with each other to get updates and share media.
- **Group Member**: Site member that has joined a group.

  > **Note:** The Wix Groups API doesn't assign group members a unique ID. Instead, it uses the `memberId` from the [Members API](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/introduction) for identification.

- **Group List**: List of groups displayed in the Wix Groups app home page.

  > **Note:** Depending on the viewer's role (see [Roles](https://dev.wix.com/docs/rest/crm/community/groups/introduction#roles)), not all groups will be displayed.

- **Group Privacy Level**: Defines the visibility of a group in the **Group List** and how a site member can join it.

  - **Public**: Anyone can see the group and its content. Anyone can join the the group.
  - **Private**: Anyone can see the group, but only group members can view its content. In order to join the group, site members must submit a **Join Group Request**.
  - **Secret**: Only group members and admins can see the group. It is not possible for site members to submit a **Join Group Request**. Instead, group members and admins can add new members.

- **Group Role**: Defines permissions. See [Roles](https://dev.wix.com/docs/rest/crm/community/groups/introduction#roles) for more details.
- **Join Group Request**: Request submitted by a site member to join a **private** group. Approved or rejected by a group admin.
- **Group Request**: When the Wix users have not given site members permission to create groups, they can submit a **Group Request** to do so. Approved or rejected by a group admin.
- **Membership Question**: Question asked to members when joining a group. Wix users can set whether it is required to answer the question in the dashboard.
- **Group Rule**: Guidelines ensuring that members post responsibly and respectfully. Wix users can set up **Group Rules** in the dashboard.
- **Group Settings**: Group specific settings. Including, whether members can see the full member list or invite new members. Available to Wix users under `Admin Tools` in the dashboard.

## Roles

- **Anonymous**: Site visitor that isn't logged in.
- **Site Member**: Site visitor that is logged in.
- **Group Member**: Site member that has joined a group.
- **Group Admin**: Group member with additional permissions.
  > **Notes:**
  >
  > - The creator of a group is automatically a **Group Admin**.
  > - A **Group Admin** always has permissions to create groups.
- **Wix Groups Manager**: Member, Wix user, or Wix app with full management permissions. Wix users are always **Wix Groups Managers**.
