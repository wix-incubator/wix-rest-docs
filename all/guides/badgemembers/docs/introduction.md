SortOrder: 0
# BadgeMembers
Badge-Members-API works with the relationship of Badge and Member. 
The connection between the Badge and the Member 
is established by the relationship of their IDs. 

This service allows you to assign a Badge to a Member by creating a BadgeMember entity 
that contains both the Badge ID and the Member ID.
Methods for creating a single relationship, bulk creation, displaying all relationships with filtering and 
delete and bulk delete relationships are available.


## Terminology

- **Badge:** an entity you can get from [Badges-API]()
- **Badge-Member:** an entity representing relationship between Badge and Member only containing id's of both of them.


## Before you begin

Have a look at [Badges-API]() and [Members-API]() which are the core APIs for Badge-Members API

## Use cases

**Create a page where members will be listed with badge filtration.**
A third party developer wants to retrieve all the members of a specific Badge or all the Badges of a specific Member.
By utilizing the [Query BadgeMembers endpoint]() from the Badge-Members API, you can efficiently retrieve specific badge members relations based on Badge ID or Member ID. 

* Required information:
    * Badge-Members API details (Endpoint for Query BadgeMembers with filtering).

* Steps:
  1. Determine the filtering criteria you want to apply for querying badge members relations based on Badge ID or Member ID.
  2. Use the [Query BadgeMembers endpoint]() from the Badge-Members API, specifying the desired filtering parameters in request BODY:
     * For Badge title filtering: Provide the ID of the Badge.
     * For Member ID filtering: Provide the ID of the Member.
  3. Retrieve the list of Badge Members relations that match the specified filtering criteria.
  4. Display the results to the user, showing the members who hold the specified badge or the badges held by the specified member.

**Auto assign badges for the most active members.** A third party developer wants to create a loyalty program app that auto assigns badges to members, based on their activities.
The process involves the following steps, with utilizing the [Badge-Members API]():

* Required information
    * Retrieve member IDs from the [Site members API](https://dev.wix.com/api/rest/members/members/about-wix-members), using the [List Members endpoint](https://dev.wix.com/api/rest/members/members/list-members) to get a full list of all members.
    * Select relevant members, based on e.g. activities, orders list / bookings etc. by looking up the member IDs in the [stores API](https://dev.wix.com/api/rest/wix-stores/about-wix-stores) / [bookings APIs](https://dev.wix.com/api/rest/wix-bookings/about-wix-bookings)):
    * To select members with a long store order history, you may wish to retrieve all orders with the [Query Orders endpoint](https://dev.wix.com/api/rest/wix-stores/orders/query-orders), filtering by `buyerInfo.id`. Retrieving a list of all orders, e.g. with an empty query filter, may include buyers who are site contacts, but not site members.
    * To select members who actively book services, you may wish to use the [Query Bookings endpoint](https://dev.wix.com/api/rest/wix-bookings/bookings/bookings-reader/query-bookings) and include the `contactId` of each member retrieved from the Site Members API.
    * To create a relation between Badge and Member (Assign badge, Unassign badge) or retrieve information about Badges with their Members list use [Badge-Members API]().

* Steps
    1. Define member group according to site owner's needs
    2. Get currently eligible members using other APIs
    3. Create badge using the [Create badge endpoint](https://dev.wix.com/api/rest/members/badges/create-badge)
    4. Assign badge using the Badge-Members API [Create BadgeMember endpoint]().

**Allow site members to assign badges to other members.** A third party developer wants to create a community in which members can assign badges to one another and see available badges. For example, a site admin member may want to give certain site members access to a permissioned, "staff only" page on their site.

* Required information
    * Member's details (Site members API)

* Steps
    1. Get all available badges on site, to display to the user for assignment, using [List badges endpoint](https://dev.wix.com/api/rest/members/badges/list-badges)
    2. Select the permissioned - "staff only" badge from the list. The badge must already exist, created with permissions added by the site owner.
    3. Assign badge to selected members, based on user input, using the [Create Badge-Member endpoint]() from Badge-Members API
    4. Show updated listing of member's badges using the [List Badge-Members endpoint]() from Badge-Members API

**Member verification.** A third-party developer aims to enhance an online community by implementing a verification mechanism.
This feature ensures that members are legitimately approved by trusted parties, enhancing the credibility and authenticity of the community.
Through the integration of the Badge-Members API, members can query and display members with "verified" badges, allowing the community to easily identify and engage with trusted members.

* Required information
    * Badge (Badges API)
    * Member's details (Site members API)
    * BadgeMember (Badge-Members API)

* Steps
    1. Member makes a proper request which retrieves his id using [getMember() function](https://www.wix.com/velo/reference/wix-members-frontend/currentmember/getmember) and sends request to any pre-installed third party verification service.
    2. When member receives an approval, it triggers the AssignBadge endpoint from BadgeMembers API and assigns the "Verified" Badge to the member.
       The badge must already exist, created by the site owner or by the third part application.

**Badge import/export** A third-party developer wants to create a Badge definitions marketplace.
Similar to an online marketplace, this feature enables developers to store diverse badge definitions from various sites and allows to create a Badge based on information from third-party.

* Required information
    * To create a Badge use [Create badge endpoint](https://dev.wix.com/api/rest/members/badges/create-badge) from Badges API

* Steps
    1. Use a third party service that will allow to store the definitions of Badges (blueprints of information enough to perform a Badge creation)
    2. Allow member to view and choose the preferred Badge from third-party service Badge list
    3. Perform a request from third-party service to create a Badge
    4. Retrieve logged-in member ID using [getMember() function](https://www.wix.com/velo/reference/wix-members-frontend/currentmember/getmember)
    5. Assign a created Badge to member CreateBadgeMember from BadgeMembers API

**Open the content to a members who have specific badge** A third-party developer wants to integrate badges with permissions.
This integration enables the unveiling of specific content to members who possess designated badges.

* Required information
    * To create a Badge with specific permissions use CreateBadge endpoint from Badges API and [set badge permissions](https://support.wix.com/en/article/setting-permissions-for-a-member-badge)
      in the Site Members area of the dashboard.
    * To set a Badge to a specified member get his id using the GetMember endpoint from Site members API and create a relationship between Badge and Member using CreateBadgeMember endpoint from Badge-Members API
    * To set a Badge to multiple site members use the ListMembers from Site members API to show all site members or QueryMembers from Site members API to list the members with specific filtering.
      Then assign the Badge to multiple members using BulkCreateBadgeMember from Badge-Members API

* Steps
    1. Create a Badge
    2. Define a permissions for the Badge from dashboard
    3. Assign a badge to a single or multiple site members

**Allow members to perform badges self-assigning** A third-party developer wants to create a feature that allows members to self-assign badges through a dedicated button.
This feature empowers logged-in members to personally apply badges to their profiles.

* Required information
    * To retrieve an ID of logged-in member use [getMember() function](https://www.wix.com/velo/reference/wix-members-frontend/currentmember/getmember)
    * To allow a member to set a badges to himself or to another members - in Velo backend use the [assignMembers function](https://www.wix.com/velo/reference/wix-members-backend/badges/assignmembers) with an option:
      suppressAuth = true.
    * To view all available badges use ListBadges endpoint from Badges API
    * To set a Badge to Member use CreateBadgeMember endpoint from Badge-Members API

* Steps
    1. Create a button for self-assigning a badge to logged-in memeber
    2. Create a list of available badges
    3. Assign a badge


