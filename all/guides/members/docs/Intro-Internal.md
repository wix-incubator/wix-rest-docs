SortOrder: 0
# Introduction

Members is a service that allows Wix site members to create their own profiles on Wix sites.
Profiles can be private or public.
Private profiles are applicable for stores, bookings.
Public profiles are applicable for site communities with forum, blog.

## About Wix Members

Wix Members allows users to add a personal account area for their site members (UoU) - 
both for social communities or non social businesses. 
Members can choose if their account is private or public and set up their profile.

To learn more about Wix Members Area, [read this article](https://support.wix.com/en/article/about-members-area)

Wix members APIs:
* Members (all member's info)
* Following-Followers (member's following and followers list)
* Activity Counters (counter of posts, likes, comments)
* Badges (create Assign and get badges list per member)

## Members Scope

Members area is available for the following Wix business solutions:
- Wix Stores (my orders, my addresses, wishlist)
- Wix Bookings (my bookings - upcoming + history)
- Wix Forum (forum posts, forum, comments)
- Wix Blog (my drafts, blog posts, blog comments, blog likes)
- Wix Events (my events - upcoming + history)
- Wix File share (my files)

Members general pages:
- My Account (stores member's private info)
- Profile (stores member's public info)
- Following - Followers
- Settings
- Notifications
- Members list page (site level)

## Members Types

**Private member** - only the member and the site owner can see this member

**Public member** - anyone can see this member 

**Blocked member** - the member can not log-in to the site 

**Muted Member** - Member can not do social actions on this site (write posts / like / comment etc)

**Pending member** - a member that request to join the site and wasn't approved yet
  
## Use Cases 

**1. Adding an existing loyalty program app for members** (business use case - store).
A developer wants to add a loyalty program service to his store 

He is using a 3rd party app (like smile, swell etc.) in order to offer member's benefits

The required info for integration:
* Member details (id, first name, last name, address)
* Members events (signup, update)
* Activity counters events
* Store orders events
* Member’s status (approved / blocked - loyalty benefits are only for active members)
* Store orders history (from stores API)
* Badges events (getting a badge will give more points)

**2. Sending SMS to members who booked services** (business use case - bookings).
A developer wants to add an SMS service to update members on their bookings
* successful sign-up to class
* booking approved
* available spot on a class they signed to its wait-list

Integrate with 3rd party app that sends SMSs (like vonage)

The required info for integration:
* Member details (id, first name, last name, phone number)
* Bookings API + Events

**3. Syncing with an external CRM system** (mailchimp, hubspot).
A developer wants to sync all of his members data to his own dashboard in order to manage his members information 

The required info:
* Sign up event
* Member creation event
* Member details (id, first name, last name, phone number, email)
* Update event (for any information that the member changes)
