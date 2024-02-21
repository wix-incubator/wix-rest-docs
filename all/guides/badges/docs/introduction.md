SortOrder: 0
# Badges API

The Badges API enables site owners to create badges on their website or Wix App, and assign them to site members, either from their site dashboard, or from their live site. Badges are set up by site owners in their site dashboard. Wix does not provide preset badges.

Badges assigned to specific site members help them stand out from other members. You can use badges to create specific categories of members within your site.

With the Badges API, third-party developers can customize how badges are created and assigned, including, for example, automating creation of specific categories of members who will recieve a given badge, or delegating assignment of badges to site members themselves.

For an overview of badges, see [About Member Badges](https://support.wix.com/en/article/about-member-badges).

To use all the functions related to the connection between Badges and Members,
such as:
- Assign Badge to one or multiple Members
- Unassign Badge from one or multiple Members
- Query Badges with their Members (with filters)

you should use a separate [Badge-Members API]().


## Terminology

- **Badge:** a visible label to be displayed on a site member's profile. A badge has a name (mandatory), an icon, and a background color.

## Badge Permissions
Badges can grant site members special permissions to access specific pages.

Site owners can [set badge permissions](https://support.wix.com/en/article/setting-permissions-for-a-member-badge) in the Site Members area of the dashboard.

Badge permissions can't be set in the API.

Site members receive permissions once a permission-granting badge is assigned to them.


## Limitations

Member permissions themselves cannot be managed via the badges API. They must be set by the site owner in the site's dashboard.
