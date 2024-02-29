SortOrder: 0
# About Forum

Wix Forum allows site owners and members to create and manage forum posts. The posts can be organized in categories.

Learn more [about Wix Forum](https://support.wix.com/en/article/wix-forum-about-wix-forum).

## Terminology

- **Post**
  A post written by a site member.

  Posts can be pinned (set to always appear at the top of a forum page), moved (to a new category), liked/unliked (to show approval, or not), and closed/opened (for replies). These actions happen in the site only, but third parties using the API can be notified of them via webhooks.

- **Category**
  A logical group that the site member assigns their post(s) to in the forum.

- **Draft Post**
  A pending post written by a site member used for post moderation.

  Draft posts can be approved (they are posted to the forum) or deleted.

## Use cases

The Forum API allows developers to reuse forum content in a modular fashion.

Example:
 - Set up an automated feed of new posts and sub-forums based on news, events, or other topics so that members and admins don't have to do it manually:
    1. Decide criteria for selecting forum posts to display, e.g. based on keywords or listing all categories, and retrieve these categories using the [Query Categories endpoint](https://dev.wix.com/api/rest/wix-forum/wix-forum/category/query-categories).
   2. Consume the [Post Created Webhook](https://dev.wix.com/api/rest/wix-forum/wix-forum/post/post-created-webhook) to get all new posts.
   3. Filter the new posts by their `categoryId`, or by keywords found in `contentText`, and link back to them using `url` and `title` to create links.
