SortOrder: 1
## Use cases

### Create a “most popular writers” widget for a blog or forum

Your app could help site owners add a widget of recommended blog, comment, or forum writers to follow based on their followers count.
 
1. Get all members of a site by calling the [List Members endpoint](https://dev.wix.com/api/rest/members/members/list-members).
2. For each member, get their followers from the [List Member Followers endpoint](https://dev.wix.com/api/rest/members/member-followers/list-member-followers), count them, and sort them by highest amount of followers.

 
### Add a “people you may know” widget based on second-degree connections of a specified member
 
Your app could help site owners add a widget showing connections of connections, and how many connections the specified member has in common with them.
 
1. Get the specified member's connections using the [List Member Followers endpoint](https://dev.wix.com/api/rest/members/member-followers/list-member-followers) and the [List Member Following endpoint](https://dev.wix.com/api/rest/members/member-followers/list-member-following).
2. For each direct connection, get _their_ connections in both directions, using the same endpoints as in step 1.
3. Using the list of indirect connections from step 2, query any existing relationships to the specified member, using the [List Member Connections endpoint](https://dev.wix.com/api/rest/members/member-followers/list-member-connections).
4. Sort the resulting list of potential connections into the following sets:

    - The specified member already follows the second-degree connection. Remove them from the suggestion list.
    - The second-degree connection follows the specified member. Add to a "follows you" sub-list.
    - There is not yet any direct connection to the second-degree connection. These are the members to use for the suggestion list.