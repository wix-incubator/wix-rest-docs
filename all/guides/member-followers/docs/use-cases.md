SortOrder: 1
## Use cases

### Create a “Most popular writers” widget on a blog/forum site home page.
 For example, a developer wants to add a widget of recommended blog, comment, or forum writers to follow, and expose it on the home page.
 
 
 1. Get all members of a site by calling [the List Members endpoint](https://dev.wix.com/api/rest/members/members/list-members)
 2. For each member, get their followers from [the List Member Followers endpoint](https://dev.wix.com/api/rest/members/member-followers/list-member-followers) and count them
 3. For the members with the most followers, provide "Follow this Member" links using [the Follow Member endpoint](https://dev.wix.com/api/rest/members/member-followers/follow-member)

 
### Add a “people you may know” widget based on second-degree connections of a specified member
 
 For example, a developer wants to add a widget showing connections of connections, and how many connections the specified member has in common with them.
 
 1. Get the specified member's connections using [the List Member Followers](https://dev.wix.com/api/rest/members/member-followers/list-member-followers) and [the List Member Following](https://dev.wix.com/api/rest/members/member-followers/list-member-following)
 2. For each direct connection, get _their_ connections in both directions, using the same endpoints as in step 1.
 3. Using the list of indirect connections from step 2., query any existing relationships to the specified member, using [the List Member Connections endpoint](https://dev.wix.com/api/rest/members/member-followers/list-member-connections).
 4. Sort the resulting list of potential connections into sets:
  - The specified member already follows the second-degree connection. Remove them from the suggestion list.
  - The second-degree connection follows the specified member. Add to a "follows you" sub-list.
  - There is not yet any direction connection to the second-degree connection suggestion. Keep them on the suggestion list.
 5. For each remaining suggestion use [the List Members endpoint](https://dev.wix.com/api/rest/members/members/list-members) to display details to the specified member, and provide "Follow this Member" links using [the Follow Member endpoint](https://dev.wix.com/api/rest/members/member-followers/follow-member)
 
