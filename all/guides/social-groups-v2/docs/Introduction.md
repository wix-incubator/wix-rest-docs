SortOrder: 0
# About Wix Groups

Wix Groups allows site owners to create a place where site members can join groups to participate in discussions, share media and more.

Media in groups is organized in a gallery.

Site owners can provide site members permissions to create groups, add members to groups, etc.


## Terminology
- **Group**: Place where group members can connect with each other, get updates and share media. Groups can always be created by a groups manager, and may be created by a site member depending on the site owner's discretion. (Permission to create groups is defined in the groups application settings in the Wix Business Manager.)
- **Group Member**: Site member that joined a group.
- **Groups List**: List of groups as displayed to members in the Wix Groups app home page. Groups displayed will vary based on the viewer's role (see **Group Role**).
- **Group Privacy Level**: Defines the visibility of a group in the groups list and how a site member can join the group:
  - **Public**: Anyone can see the group in the groups list and its content. Anyone can join the group.
  - **Private**: Anyone can see the group in the groups list, but only group members can view its content. In order to join the group, site members must submit a group join request.
  - **Secret**: Only group members and group managers can see the group in the groups list. New group members can only be added by other group members.
- **Group Role**: Roles of a group member in a group, that define their permissions:
  - **Member**: Regular group member.
  - **Admin**: Group administrator.
- **Group Join Request**: Request submitted by a site member to join a private group. The request can be approved or rejected by a group admin or groups manager (see **Roles**).
- **Group Request**: When a site member is not allowed to create a group, they can submit a request that may be approved or rejected by a groups manager.
- **Groups Application Settings**: Settings available in the Wix Business Manager that define the behavior of the Wix Groups app.

## Roles
- **Anonymous**: Site visitor that is not currently logged in.
- **Site Member**: Site visitor that is currently logged in.
- **Group Member**: Site member that joined a group.
- **Group Admin**: Group member that was assigned the 'group admin' role by the groups manager or another group admin. The creator of a group is automatically a group admin.
- **Groups Manager**: User, site member, Wix App or third party application with full management permissions. The site owner is automatically granted full management permissions.


## Use Cases

### Create a Group for a Predefined List of People
For example, create a group for each class at a school or each fitness class (yoga, TRX, etc) in a gym.

1. Create a list of site members to add to the relevant group, identified by one of the following: name, email address, phone number, contactId.
2. Create a group by calling the [Create Group](https://dev.wix.com/api/rest/community/social-groups/group/create-group) endpoint.
3. Call the [Query Members](https://dev.wix.com/api/rest/members/members/query-members) endpoint to get the site member data.
4. Map the site members to add to the group to their IDs as returned in step 3.
5. Add the site members to the group by calling the [Add Group Members](https://dev.wix.com/api/rest/community/social-groups/group-member/add-group-members) endpoint with the site member IDs collected above.

### Manage Bulk Emailing to Group Members
For example, send automated emails to group members.

1. Get all members of a group by calling the [List Group Members](https://dev.wix.com/api/rest/community/social-groups/group-member/list-group-members) endpoint.
2. From the response, collect the site member IDs.
3. Call the [Query Members](https://dev.wix.com/api/rest/members/members/query-members) endpoint, with site member IDs you collected, to get their email addresses.
4. Call the [Query Email Subscriptions](https://dev.wix.com/api/rest/marketing/email-subscriptions/query-email-subscriptions) endpoint to confirm that the members have agreed to receive emails from the site owner.
5. Prepare and send the automated emails.

### Provide Analytical Reports
For example, create a report including aggregated group info: total amount of groups created, the most popular groups by member count, idle groups;

1. Get the total amount of groups by calling the [List Groups](https://dev.wix.com/api/rest/community/social-groups/group/list-groups) endpoint.
2. From the response, collect the metadata total.
3. Get the most popular groups by calling the [Query Groups](https://dev.wix.com/api/rest/community/social-groups/group/query-groups) endpoint and sorting by group size.
Sample request body:
```json
{
    "query": {
        "sort": [
            {
                "fieldName": "membersCount",
                "order": "DESC"
            }
        ],
        "paging": {
            "offset": 0,
            "limit": 100
        }
    }
}
```
4. Get the idle groups (with the least recent activity) by calling the [Query Groups](https://dev.wix.com/api/rest/community/social-groups/group/query-groups) endpoint and sorting by date of most recent activity.
Sample request body:
```json
{
    "query": {
        "sort": [
            {
                "fieldName": "recentActivityDate",
                "order": "ASC"
            }
        ],
        "paging": {
            "offset": 0,
            "limit": 100
        }
    }
}
```
5. Prepare and display the report.

### Search members by provided membership answers

You can build an app that will search members by keywords in the answers given to membership questions.

1. Add membership questions that users have to answer before joining by calling the [Replace All Membership Questions](https://dev.wix.com/api/rest/community/social-groups/membership-questions/replace-all-membership-questions) endpoint.
2. Create answers by providing `membershipQuestionAnswers` either in [Join Group](https://dev.wix.com/api/rest/community/social-groups/group-member/join-group) endpoint.
3. List membership answers by calling [List Answers](https://dev.wix.com/api/rest/community/social-groups/membership-questions/list-answers) endpoint. You will get a map with provided answers.

### Enable weekly digest to improve retention for your users

You can change group settings to toggle different features such as a weekly digest with top posts. This digest will be send to group members weekly based on latest activities in the given group.

1. Check if digest is disabled by calling the [Get Settings](https://dev.wix.com/api/rest/community/social-groups/settings/get-settings) endpoint.
2. If it's disabled, update group setting with `{"emailDigestEnabled": true}` by calling the [Update Settings](https://dev.wix.com/api/rest/community/social-groups/settings/update-settings) endpoint.

## Copy group rules from one group and use them for all other groups on the website

Group rules can be seen in your group. You can apply rules from one group to all others with following:

1. Get the group rules by calling the [Get Group Rules](https://dev.wix.com/api/rest/community/social-groups/group-rules/get-group-rules) endpoint.
2. Save and update rules if needed.
3. Get the list of group ids you want to update by calling the [List Groups](https://dev.wix.com/api/rest/community/social-groups/group/list-groups) endpoint.
4. Iterate over all group ids and call the [Replace Group Rules](https://dev.wix.com/api/rest/community/social-groups/group-rules/replace-group-rules) endpoint for each group id.
