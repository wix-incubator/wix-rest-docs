SortOrder: 0
# Introduction

The Activity Counters service allows site owners and third-party developers to keep track of Wix site members' activity. See "Integrations" below for  Wix App activities that are already counted.

The service allows public and private counters: 
 - Public counters can be read by any site member.
 - Private counters can only be accessed by the site member who owns the counter.

The Activity Counters API gives third-party developers access to the counters on a site at a per-member, per-app level.

Counters are only activated when a site member actually performs the activity the counter tracks.

This means that the query and list endpoints for this API may return a large number of results, for sites with many members.

## Integrations

Activity Counters is currently integrated with these Wix apps and features:

### Wix Blog

Wix Blog counts blog posts, comments, and likes.

 - [Blog (API documentation)](https://dev.wix.com/api/rest/wix-blog/blog/introduction)

### Wix Forum

Wix Forum counts forum posts, comments, likes, and views.
 - [About Wix Forum](https://support.wix.com/en/article/wix-forum-about-wix-forum)

### Wix Members Area

Wix Members Area counts followers in both directions (followed by / following).
 - [Followers (Members Area feature)](https://support.wix.com/en/article/about-the-members-area)


## Access

Third-party developers can
 - read (but not set) public counts from any apps.
 - read **and** set all counts for their own apps.

## Initializing a counter

To create a new counter for a third-party app, use the [Set Activity Counters
 endpoint.](https://dev.wix.com/api/rest/members/activity-counters/set-activity-counters)

## Use cases

**Most active writer widget.** 
A developer wants to add a "most active writer" widget to their home page, based on the number of posts each member creates.

1. Get per-member post numbers for blog or forum app using the [Get Activity Counters endpoint.](https://dev.wix.com/api/rest/members/activity-counters/get-activity-counters)
2. Process counts and display in widget.
 
**Most influential member widget.** 
A developer wants to add a "most influential members" widget to his community, based on how many likes and comments each member's posts get.

1. Get per-member reaction numbers for blog/forum app using [Get Activity Counters endpoint.](https://dev.wix.com/api/rest/members/activity-counters/get-activity-counters)
2. Process counts and display in widget.
