SortOrder: 1
# Site Members

## What is it?

Site members are users who registered to a Wix site. The site owner
can give his members special roles and permissions to
[see hidden pages](https://support.wix.com/en/article/creating-members-only-pages-596999).
Also, members are able to use social apps, such as
[Wix Forum](https://www.wix.com/app-market/wix-forum/overview), and access
their [member's area](https://support.wix.com/en/article/adding-a-members-area-to-your-site).

The **Site members API** can be used to manage site members programmatically. 

## Main entities

### Contact

Every Wix site has a list of contacts, accessible through the site's dashboard.
Contacts can be created either manually, by the site owner, or automatically
(for example, by a contact form submission).

### Site member

Site members are special kinds of contacts. When a new site member registers,
he's either connected to an existing contact, or to a new automatically created
contact. This contact will have a special `SITE MEMBER` label in the management
dashboard.

#### Lifecycle

Depending on the site settings, a site member can go through several lifecycle phases.

 * **Applicant** - if the site requires owner's approval, a newly registered site members
   will be considered an applicant until he's approved. During this time, the member
   will not be able to login. 
 * **Active** - upon approval, or if the site is open to all new registered members, the
   site member will become active.
 * **Blocked** - the site owner can block any member, effectively denying him the ability
   to login to the site.

## Services

### Members service

The members service is used to query and modify the attributes of a site member.

### Profile service

The profile service is used to query site member's profile, which include details
about the member as seen in the member's area (and potentially visible to other members).

### Auth service 

The auth service is used register new members. Depending on the site settings,
the result might include:

 * **Session token** - in case the site is open for all new members, meaning that the
   registered member is already active. The token should be passed to the client in order
   to obtain a valid session cookie, effectively logging-in the member.
 * **Approval token** - in case the site requires owner's approval, the registered member
   will be an _applicant_, until he's approved (either by the owner or using the API).
