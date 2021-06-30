SortOrder: 0
# About Members Follow

Members Follow service enables site members to follow and unfollow one another.

API allows for site members:
* Follow or Unfollow site member
* List followers
* List followings

API allows for visitors:
* List followers
* List followings

## Use cases

**1. Creating a “Most popular writers” widget** on a blog/forum site home page.
 A developer wants to add a widget of recommended writers to follow and expose it on the home page
 
 The required info:
 - Members info (Site Members API)
 - Followers list
 
**2. Add a “people you may know” widget** based on members you are following that are following other members
 
 The required info:
 - Members info (Site Members API)
 - Following list
 - Followers list
