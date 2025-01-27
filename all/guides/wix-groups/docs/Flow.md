SortOrder: 2

# Sample Use Cases & Flows: Groups
This article presents possible use cases and corresponding sample flows that you can support. This can be a helpful jumping off point as you plan your implementation.

## Create a group for a predefined list of people

To create a group for each class at a school or each fitness class (yoga, TRX, etc) in a gym:

1. Create a list of site members to add to the relevant group, identified by one of the following: name, email address, phone number, contact ID.
2. Create a group with [Create Group](https://dev.wix.com/docs/rest/crm/community/groups/groups/create-group).
3. Call [Query Members](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/query-members) to get the site member data.
4. Map the site members for the group by their IDs as returned in step 3.
5. Add the site members to the group by calling [Add Group Members](https://dev.wix.com/docs/rest/crm/community/groups/members/add-group-members) with the site member IDs collected above.

## Manage bulk emailing to group members

To send automated emails to group members:

1. Call [List Group Members](https://dev.wix.com/docs/rest/crm/community/groups/members/list-group-members) to get all members of a group.
2. From the response, collect the site member IDs.
3. Call [Query Members](https://dev.wix.com/docs/rest/crm/members-contacts/members/members/query-members), with the site member IDs you collected, to get their email addresses.
4. Call [Query Email Subscriptions](https://dev.wix.com/docs/rest/crm/communication/email-subscriptions/query-email-subscriptions) to confirm that the members have agreed to receive emails from the Wix user.
5. Prepare and send the automated emails.

## Provide analytical reports

To create a report including aggregated group information, such as, the total amount of groups created, the most popular groups by member count, and idle groups:

1. Call [List Groups](https://dev.wix.com/docs/rest/crm/community/groups/groups/list-groups) to retrieve the total amount of groups.
2. From the response, collect `metadata.total`.
3. Retrieve the most popular groups by calling [Query Groups](https://dev.wix.com/docs/rest/crm/community/groups/groups/query-groups) and sorting by `membersCount`.

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

4. Retrieve idle groups with the least recent activity by calling [Query Groups](https://dev.wix.com/docs/rest/crm/community/groups/groups/query-groups) and sorting by `recentActivityDate`.

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

## Send promotional emails based on members' interests

You can identify group members who are interested in a certain topic by searching for keywords in their answers to the membership questions.
Then, send emails to the identified members informing them about upcoming events or special offers.

1. Add membership questions with [Create or Replace All Membership Questions](https://dev.wix.com/docs/rest/crm/community/groups/membership-questions/create-or-replace-all-membership-questions).
2. Call [List Answers](https://dev.wix.com/docs/rest/crm/community/groups/membership-questions/list-answers) to retrieve members' answers to the membership questions.
3. Identify the relevant members via a keyword search.
4. Call [Query Email Subscriptions](https://dev.wix.com/docs/rest/crm/communication/email-subscriptions/query-email-subscriptions) to confirm that the identified members have agreed to receive emails from the Wix user.
5. Prepare and send the automated emails.

## Bulk update group rules

If the rules are updated for one group, you can apply the new rules to other, relevant groups.

1. Listen to [Rules Updated](https://dev.wix.com/docs/rest/crm/community/groups/rules/group-rules-updated), and/or regularly get the updated group rules by calling [List Rules](https://dev.wix.com/docs/rest/crm/community/groups/rules/list-rules).
2. Save the rules on a server and update them if needed by calling [Create or Replace All Rules](https://dev.wix.com/docs/rest/crm/community/groups/rules/create-or-replace-all-rules).
3. Call [List Groups](https://dev.wix.com/docs/rest/crm/community/groups/groups/list-groups) to retrieve a list of all group IDs.
4. Iterate over the list of group IDs and update the rules for each relevant group with [Create or Replace All Rules](https://dev.wix.com/docs/rest/crm/community/groups/rules/create-or-replace-all-rules).
