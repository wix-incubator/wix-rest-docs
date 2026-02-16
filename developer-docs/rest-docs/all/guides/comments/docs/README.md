SortOrder: 0
# Introduction

Comment Service provides commenting functionality in which visitors can interact with other visitors (members, guests)
and site owners. Comments can be created, updated and deleted as well as have other features such as leaving reactions,
upvotes/downvotes, ratings or mark comments.

## Terminology

* appId - identifier of vertical.
* Comment - message posted by visitor in response to a blog post, forum post, or other resource. These messages can be
  written or in a media format, they are often used to start a conversation or share information with other users.
* Reply - response made by visitor to previously posted comments. Unlike comments, replies cannot be posted directly
  under a resource; they are posted under other comments or replies. Replies are typically used to respond to a comment,
  provide feedback or support, or offer additional information.
* Context (contextId) - logical containers are defined by verticals, for example in Blog and Forum it is posts, and in
  Groups it is group.
* Resource (resourceId) - item that comments are attached to, for example in Blog and Forum it is posts, and in Groups
  it is item.
* Content - it is comment content.
* Draft Content - comments content that have been updated after being published. If comment moderation rules are enabled
  such comment content goes to moderation.
* Comment Status:
    * Published - public comment. Comments with the status Published can be unpublished, deleted or hidden.
    * Unpublished - invoke moderation rules. Comments with the status Unpublished can be published, hidden or deleted.
    * Deleted - it is a permanently deleted comment which does not return author and content information. Comments with
      the status deleted cannot be published. Comment can be deleted either when:
      Comment owner deletes comment
      Site owner deletes comment with status Hidden
    * Hidden - temporary hidden comment which returns author and content. If requested, the author and content could be
      not returned, for example to livesite. Comments with the status Hidden can be published, unpublished or deleted.
      Comments can be hidden only by the site owner.
* Mark - it is a sign for comment, example pinned, best or other.

## Permissions

* Permissions are managed by the vertical. Creating permissions is done per Context.
* Permissions management (internal information):
    * Visitor/members flow: comment service calls vertical service, which returns permissions describing what actions
      are allowed in Context.
    * Other flows: Comments Service calls and checks is permitted API. A user with permission can take action anywhere
      without regard to vertical permissions. Used for site owners, and third parties (external apps).

## Limitations

Permissions limitations. Third parties cannot add their permission logic to the visitor/member flow. It only can be
managed by internal verticals, like Blog, Forum, Groups, and others. Third parties can make anything that is predefined
by verticals. It depends on what scope third party apps have. 




