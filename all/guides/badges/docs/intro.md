SortOrder: 0
#Badges

## What is it?

Badges API enables users to create badges on their website or Wix App and assign them to site members.
Badges assigned to specific site members help them stand out from all the other members. 

## Badge Permissions
Badges can have special permissions to access specific members-only pages.  
User can [set badge permissions](https://support.wix.com/en/article/setting-permissions-for-a-member-badge) in the Site Members area of the dashboard.
Site members will receive relevant permissions once assigned such badge.

## Use cases
1. Auto assigning badge for active members 
    * A developer wants to create a loyalty program app that auto assign members with badges, based on their activities
    * The required info
        * Member's details (Site members API)
        * Member's activities (Activities counters API)
        * Member's orders list / bookings etc (based on stores / booking APIs)
        * Create badge
        * Assign badge 
2. Members assign badges to members
    * A developer wants to create a community in which members can assign badges to one another and see all badges
    * The required info
        * Member's details (Site members API)
        * List of all badges on site
        * Assign a badge for members
        * List member's badges IDs

