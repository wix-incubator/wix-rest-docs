SortOrder: 1

# Sample Use Cases & Flow: Social Groups

## Create a Group for a Predefined List of People

For example, create a group for each class at a school or each fitness class (yoga, TRX, etc) in a gym.

1. Create a list of site members to add to the relevant group, identified by one of the following: name, email address, phone number, contactId.
2. Create a group by calling [Create Group](https://dev.wix.com/docs/rest/crm/community/groups/groups/create-group).
3. Call [Query Members](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/query-members) to get the site member data.
4. Map the site members to add to the group to their IDs as returned in step 3.
5. Add the site members to the group by calling [Add Group Members](https://dev.wix.com/docs/rest/crm/community/groups/members/add-group-members) with the site member IDs collected above.

## Manage Bulk Emailing to Group Members

For example, send automated emails to group members.

1. Get all members of a group by calling [List Group Members](https://dev.wix.com/docs/rest/crm/community/groups/members/list-group-members).
2. From the response, collect the site member IDs.
3. Call [Query Members](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/query-members), with site member IDs you collected, to get their email addresses.
4. Call [Query Email Subscriptions](https://dev.wix.com/docs/rest/crm/communication/email-subscriptions/query-email-subscriptions) to confirm that the members have agreed to receive emails from the site owners.
5. Prepare and send the automated emails.

## Provide Analytical Reports

For example, create a report including aggregated group info: total amount of groups created, the most popular groups by member count, idle groups;

1. Get the total amount of groups by calling [List Groups](https://dev.wix.com/docs/rest/crm/community/groups/groups/list-groups).
2. From the response, collect the metadata total.
3. Get the most popular groups by calling [Query Groups](https://dev.wix.com/api/rest/community/wix-groups/groups/query-groups) and sorting by group size.
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

4. Get the idle groups (with the least recent activity) by calling [Query Groups](https://dev.wix.com/api/rest/community/wix-groups/groups/query-groups) and sorting by date of most recent activity.
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

## Send Promotional Emails Based on Members' Interests

Your can identify group members who are interested in a certain topic by searching for keywords in their answers to the membership questions.
Then, you can send emails to the identified members informing them about upcoming events or special offers.

1. Add membership questions by calling [Create or Replace All Membership Questions](https://dev.wix.com/docs/rest/crm/community/groups/membership-questions/create-or-replace-all-membership-questions).
2. At any time you want to send emails to selected members, call [List Answers](https://dev.wix.com/docs/rest/crm/community/groups/membership-questions/list-answers).
3. Identify the relevant members via a keyword search.
4. Call [Query Email Subscriptions](https://dev.wix.com/docs/rest/crm/communication/email-subscriptions/query-email-subscriptions) to confirm that the identified members have agreed to receive emails from the site owners.
5. Prepare and send the automated emails.

## Bulk Update Group Rules

When Wix users manually update the rules for one group, You can apply the new rules to other relevant groups.

1. Get the updated group rules by calling [List Rules](https://dev.wix.com/docs/rest/crm/community/groups/rules/list-rules).
2. Save the rules on your server and update them if needed by calling [Create or Replace Group Rules](https://dev.wix.com/docs/rest/crm/community/groups/rules/create-or-replace-all-rules).
3. Retrieve a list of all group IDs by calling [List Groups](https://dev.wix.com/docs/rest/crm/community/groups/groups/list-groups).
4. Iterate over the list of group IDs and update the rules for each relevant group by calling [Create or Replace All Rules](https://dev.wix.com/docs/rest/crm/community/groups/rules/create-or-replace-all-rules).
