SortOrder: 1
## Use Cases

### Sending notifications when new comment is created

3rd party developer might want to send notification to external system when new comment is written. Notifications
usually includes details about resource where comment was written. To retrieve this data developer can
use `GetCommentContextResources` API method, that will return `title`, `url` and `imageUrl` for current resource.

So to achieve this goal, developer could listen
to [Comment Created Domain event](https://dev.wix.com/docs/rest/api-reference/community/comments-service#comment-created).

He might get domain event similar to:

```json
    {
  "data": {
    "eventType": "wix.comments.v2.comment_created",
    "instanceId": "<app-instance-id>",
    "data": {
      "id": "4d97c478-4854-4957-9911-8ff29aba35c7",
      "revision": "1",
      "createdDate": "2023-05-09T08: 25: 05.014Z",
      "updatedDate": "2023-05-09T08: 25: 05.014Z",
      "appId": "14bcded7-0066-7c35-14d7-466cb3f09103",
      "contextId": "6f46dbf6-1a48-4870-86b2-f807d8f31b3e",
      "resourceId": "6f46dbf6-1a48-4870-86b2-f807d8f31b3e",
      "content": {
        "richContent": {
          "nodes": [
            {
              "type": "PARAGRAPH",
              "id": "foo",
              "nodes": [
                {
                  "type": "TEXT",
                  "textData": {
                    "text": "Interesting 🤯"
                  }
                }
              ]
            }
          ],
          "metadata": {
            "version": 1,
            "createdTimestamp": "2023-05-09T08: 25: 01.014Z",
            "updatedTimestamp": "2023-05-09T08: 25: 01.014Z",
            "id": "726cb137-a9c3-408b-9cc2-2b64c6be8a95"
          }
        },
        "mentions": [],
        "attachments": []
      },
      "author": {
        "memberId": "81b3e2a2-60f4-4016-ab20-c2fda4c4c4f2"
      },
      "parentIdsInThread": [
        "4d97c478-4854-4957-9911-8ff29aba35c7"
      ],
      "replyCount": 0,
      "voteSummary": {
        "netVoteCount": 0,
        "upvoteCount": 0,
        "downvoteCount": 0
      },
      "status": "PUBLISHED",
      "reactionSummary": {
        "total": 0,
        "reactionCodeCount": {}
      },
      "marked": false
    }
  }
}
```

From given example we can take `appId`, `contextId` and `resourceId` values:

* `appId` - `14bcded7-0066-7c35-14d7-466cb3f09103`
* `contextId` - `6f46dbf6-1a48-4870-86b2-f807d8f31b3e`
* `resourceId` - `6f46dbf6-1a48-4870-86b2-f807d8f31b3e`

Using this data developer can invoke `GetCommentContextResources` API, request might look similar to:

```json
{
  "appId": "14bcded7-0066-7c35-14d7-466cb3f09103",
  "resourceIds": [
    {
      "contextId": "6f46dbf6-1a48-4870-86b2-f807d8f31b3e",
      "resourceId": "6f46dbf6-1a48-4870-86b2-f807d8f31b3e"
    }
  ]
}
```

Server response will contain metadata about requested resource:

```json
{
  "resources": [
    {
      "contextId": "6f46dbf6-1a48-4870-86b2-f807d8f31b3e",
      "resourceId": "6f46dbf6-1a48-4870-86b2-f807d8f31b3e",
      "title": "An Introduction to Computer",
      "pageUrl": {
        "relativePath": "/blog/intro-to-computer",
        "url": "https://mysite.com/blog/intro-to-computer"
      },
      "imageUrl": "https://static.wixstatic.com/media/4acbb8_5646ee01a5524905af4f2e7c567cbbcef002.jpg",
      "resourceOwner": {
        "contactId": "90decb5f-d0f2-4ac7-a6c2-78efc156e3d9",
        "identityType": "MEMBER",
        "memberId": "90decb5f-d0f2-4ac7-a6c2-78efc156e3d9"
      }
    }
  ]
}
```

Provided data can be used to enrich notification message.
Check [Wix Notifications](https://dev.wix.com/api/rest/wix-notifications/notifications/introduction) documentation for
more details how to send notifications.