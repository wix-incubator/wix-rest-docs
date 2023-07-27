SortOrder: 4
# Sample Flows
This article shares possible use cases your app could support, as well as sample flows. You're certainly not limited to these use cases, but it can be a helpful jumping off point as you plan your app's implementation.

## Highlight popular comments in a widget
>**Note:** This flow requires Wix Blocks which is currently in Beta. 
Your app can help site owners find the most popular comments left on their site and feature those comments to other site visitors. 

To find and highlight the most popular comments:
1. Use [Query Comments](https://dev.wix.com/api/rest/comments/comments/query-comments) to filter and sort comments for the highest `replyCount`, `rating`, and `reactionSummary.total`.
2. Use [Mark Comment](https://dev.wix.com/api/rest/comments/comments/mark-comment) for each of the top comments to set `marked` as `TRUE`.
3. Display marked comments in a widget. Widgets can be built using Wix Blocks. Learn more about [Wix Blocks and adding widgets](https://support.wix.com/en/article/wix-blocks-a-blocks-app-workflow).

## Provide comment analytics
Your app can gather insights and generate reports about a site's comments.

To get the information follow these steps:
1. Use [Query Comments](https://dev.wix.com/api/rest/comments/comments/query-comments) to retrieve a list of comments based on specified filters.
2. Analyze the statistical data, such as [comment count](https://dev.wix.com/api/rest/comments/comments/count-comments) and engagement rates based on `replyCount`, `reactionSummary.total`, and `voteSummary.netVoteCount`.
3. Use the comment metrics to generate comprehensive reports on comment activity, user engagement, and popular discussions.
4. Customize the reporting with segmentation based on available filtering and sorting options.
5. Visualize parts of the data in an easily understandable format, such as charts and graphs.
6. Schedule and distribute the reports at regular intervals.
