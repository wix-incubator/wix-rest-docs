SortOrder: 3
# About the Comments API

The Comments API allows you to manage a customized commenting program that lets site visitors share feedback or engage in discussions around different types of resources, including blog posts, forum threads, or other site content.

With the Wix Comments API, you can:
+ Allow commenting on any page of your site.
+ Mark specific comments to highlight and feature to your readers.
+ Engage with visitors who are not site members through guest commenting.

## Integrations
The Comments API is fully integrated with several Wix solutions. Each integration uses a slightly different configuration to work with Comments.  

The following table details the currently supported integrations:
| Wix App | `appId` | `contextId` | `resourceId` |
| --- | --- | --- | --- |
| Wix Blog | 14bcded7-0066-7c35-14d7-466cb3f09103 | `internalId` | `internalId` |
| Wix Comments | 91c9d6a7-6667-41fb-b0b4-7d3b3ff0b02e | `categoryId` | `componentId` |
| Wix Forum | 14724f35-6794-cd1a-0244-25fd138f9242 | `forumPostId` | `forumPostId` |
| Wix Groups | 148c2287-c669-d849-d153-463c7486a694 | `groupId` | `feedItemId` |

## Use cases
+ [Highlight popular comments in a widget](https://dev.wix.com/api/rest/comments/comments/sample-flows#comments_comments_sample-flows_highlight-popular-comments-in-a-widget)
+ [Provide comment analytics](https://dev.wix.com/api/rest/comments/comments/sample-flows#comments_comments_sample-flows_provide-comment-analytics)

## Terminology
+ **Marked comments:** When a comment's `marked` field is set to `TRUE`, it indicates that the comment has been flagged or marked for special attention. No additional automated behavior or action is taken with the comment. However, you can manually filter for comments marked as such with [Query Comments](https://dev.wix.com/api/rest/comments/comments/query-comments) and highlight them to your visitors as needed.
+ **Parent comments:** Parent comments refer to comments that have subsequent comments directly responding to them. They serve as the original or initial comments in a conversation thread. The parent comment's unique identifier is stored in the `parentComment.id` field of the corresponding reply comment.
+ **Replies:** Replies are comments that are made in direct response to earlier comments within a discussion. They are specifically intended as responses to a particular parent comment and contribute to the ongoing conversation. Replies help maintain the hierarchical structure of comment threads and enhance the engagement and interactivity among users.
