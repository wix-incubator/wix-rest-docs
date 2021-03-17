SortOrder: 3
# Example Flows

This article shares a possible use cases your app could support,
as well as an example flow that could support the use case.
You're certainly not limited to the use case,
but it can be a helpful jumping off point
as you plan your app's implementation.

## Importing Site Members

Your app can create site members
without the member signing up directly on the site.
This allows site owners to create members in bulk
or to import members from another site.

To do this, your app can follow this basic flow:

1. Create the list of members
    or get the list of members from the external site.
    Structure the list as an array of member objects,
    and make sure each member has a login email address:

    ```json
    {
      "member": {
        "loginEmail": "member_needs_an@email.com",
        "contact": { ... },
        "profile": { ... }
      }
    }
    ```

2. Iterate over the array, calling [Create Member][create-member] for each member.
    To keep below rate limits, set your requests at least 1 second apart.

3. To tell the members about their new accounts,
    use [Send Set Password Email][send-set-password-email]
    (in the Authorization API).
    Your app can trigger the email immediately after creating the member,
    or you can let the site owner choose to send the email later.
    If the email is triggered later,
    your app should iterate over an array of the member email addresses,
    calling [Send Set Password Email][send-set-password-email] for each email.

[create-member]: https://dev.wix.com/api/rest/members/members/create-member
[send-set-password-email]: https://dev.wix.com/api/rest/members/member-authentication/authentication