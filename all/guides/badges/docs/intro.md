SortOrder: 0
# Badges

The Badges API enables site owners to create badges on their website or Wix App, and assign them to site members, either from their site dashboard, or from their live site. Badges are set up by site owners in their site dashboard. Wix does not provide preset badges.

Badges assigned to specific site members help them stand out from other members. You can use badges to create specific categories of members within your site.

With the Badges API, third-party developers can customize how badges are created and assigned, including, for example, automating creation of specific categories of members who will recieve a given badge, or delegating assignment of badges to site members themselves.

For an overview of badges, see [About Member Badges](https://support.wix.com/en/article/about-member-badges).

## Terminology

 - **Badge:** a visible label to be displayed on a site member's profile. A badge has a name (mandatory), an icon, and a background color.

## Badge Permissions
Badges can grant site members special permissions to access specific pages.

Site owners can [set badge permissions](https://support.wix.com/en/article/setting-permissions-for-a-member-badge) in the Site Members area of the dashboard.

Badge permissions can't be set in the API.

Site members receive permissions once a permission-granting badge is assigned to them.

## Use cases

**Auto assign badges for the most active members.** A third party developer wants to create a loyalty program app that auto assigns badges to members, based on their activities.

   * Required information
        * Retrieve member IDs from the [Site members API](https://dev.wix.com/api/rest/members/members/about-wix-members), using the [List Members endpoint](https://dev.wix.com/api/rest/members/members/list-members) to get a full list of all members.
        * Select relevant members, based on e.g. activities, orders list / bookings etc. by looking up the member IDs in the [stores API](https://dev.wix.com/api/rest/wix-stores/about-wix-stores) / [bookings APIs](https://dev.wix.com/api/rest/wix-bookings/about-wix-bookings)):
        * To select members with a long store order history, you may wish to retrieve all orders with the [Query Orders endpoint](https://dev.wix.com/api/rest/wix-stores/orders/query-orders), filtering by `buyerInfo.id`. Retrieving a list of all orders, e.g. with an empty query filter, may include buyers who are site contacts, but not site members.
        * To select members who actively book services, you may wish to use the [Query Bookings endpoint](https://dev.wix.com/api/rest/wix-bookings/bookings/bookings-reader/query-bookings) and include the `contactId` of each member retrieved from the Site Members API.

  * Steps
    1. Define member group according to site owner's needs
    2. Get currently eligible members using other APIs
    3. Create badge using the [Create badge endpoint](https://dev.wix.com/api/rest/members/badges/create-badge)
    4. Assign badge using the [Assign badge to members endpoint](https://dev.wix.com/api/rest/members/badges/assign-badge-to-members)

**Allow site members to assign badges to other members.** A third party developer wants to create a community in which members can assign badges to one another and see available badges. For example, a site admin member may want to give certain site members access to a permissioned, "staff only" page on their site.

   * Required information
        * Member's details (Site members API)

  * Steps
    1. Get all available badges on site, to display to the user for assignment, using [List badges endpoint](https://dev.wix.com/api/rest/members/badges/list-badges)
    2. Select the permissioned, "staff only" badge from the list. The badge must already exist, created with permissions added by the site owner.
    3. Assign badge to selected members, based on user input, using the [Assign badge to members endpoint](https://dev.wix.com/api/rest/members/badges/assign-badge-to-members)
    4. Show updated listing of member's badges using the [List badges per member endpoint](https://dev.wix.com/api/rest/members/badges/list-badges-per-member)

## Limitations

Member permissions themselves cannot be managed via the badges API. They must be set by the site owner in the site's dashboard.
