SortOrder: 2
# Consumers

Currently, Comments Services are widely used by other Verticals:

* Wix Comments
* Wix Blog
* Wix Forum
* Wix Groups

Each vertical uses different configuration to read/write comments, to access each vertical's resource comments use such
appId/contextId/resourceId configurations:

| Application      | appId                                | contextId  | resourceId |
|------------------|--------------------------------------|------------|------------|
| Wix Comments     | 91c9d6a7-6667-41fb-b0b4-7d3b3ff0b02e | `categoryId` | `componentId` |
| Wix Blog         | 14bcded7-0066-7c35-14d7-466cb3f09103 | `contentId` | `contentId` |
| Wix Forum        | 14724f35-6794-cd1a-0244-25fd138f9242 | `forumPostId` | `forumPostId` |
| Wix Groups       | 148c2287-c669-d849-d153-463c7486a694 | `groupId`   | `feedItemId` |
