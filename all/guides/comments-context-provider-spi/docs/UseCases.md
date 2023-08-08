SortOrder: 1
## Use cases

### Comments Platform as an E-commerce Reviews

3rd party developers might be using Comments Platform as a Reviews board to provide ability for site visitors to review
a product.

By implementing Comment Context Provider developer can set who can create a comment, reply, manage comments. When
visitor visits page where comments are being used Comments Platform will invoke `GetCommentContext` method, that must be
implemented by external developer, to gain details how comments should behave for current visitor.

> **Note**: Wix does not store/provide any data that may be required to maintain the constraints, the 3rd party will need to get any required data on their own.

For example, developer can set a constraint that only members that bought a product can review it. So if visitor has
bought the product external application might respond with payload similar to this:

```json
{
  "context": {
    "contextId": "<product-id>",
    "permissions": {
      "viewContext": true,
      "createComment": true,
      "createReply": false,
      "updateAnyComment": false,
      "deleteAnyComment": false,
      "markComment": false
    }
  }
}
```

This will allow visitor to read comments and create a new comment, although it will now allow to do any other actions.

If developer wants to open moderation capabilities for some of it's site members it might make response
similar to:

```json
{
  "context": {
    "contextId": "<product-id>",
    "permissions": {
      "viewContext": true,
      "createComment": true,
      "createReply": true,
      "updateAnyComment": true,
      "deleteAnyComment": true,
      "markComment": true
    }
  }
}
```

To check if member is moderator Site Owner could create special Badge to which all member moderators would be
assigned to and, developer might check if member has this special Badge using 
[List Badges per Member API](https://dev.wix.com/api/rest/members/badges/list-badges-per-member)

This will allow member to reply to other's comments, update, delete or mark them.

### Managing Comments in Wix Business Manager

To gain more insight and improve comments managing experience Site Owner might want to see metadata about resource which
are attached to comments. By implementing `GetCommentContextResources` method developer can open this functionality.
Wix will populate the data provided in the Business Manager page that enables site owners to manage the comments about a particular resource:

![single_comment.png](https://s3.amazonaws.com/wixplorer-readme-images/comments-context-provider-spi%2Fsingle_comment.png)

Comment Platform expects that this method would return necessary metadata about resource. Response might look similar
to:

```json
{
  "resources": [
    {
      "contextId": "38e593d8-96a1-4c61-b87f-3607ba80cd60",
      "resourceId": "38e593d8-96a1-4c61-b87f-3607ba80cd60",
      "title": "I'm a product",
      "pageUrl": {
        "relative_path": "/product-page/a-product",
        "url": "https://mysite.com/product-page/a-product"
      },
      "imageUrl": "https://static.wixstatic.com/media/22e53e_2fee033b2eca46cab4eec7fa74e99c31~mv2.jpg/v1/fill/w_96,h_96,al_c,q_85,usm_0.66_1.00_0.01/22e53e_2fee033b2eca46cab4eec7fa74e99c31~mv2.webp",
      "resourceOwner": {
        "identityType": "MEMBER",
        "memberId": "118799d6-67bf-46b1-9583-b8aed0932406"
      }
    }
  ]
}
```
