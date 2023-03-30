SortOrder: 5
# Blog: Sample Use Cases & Flows

This article shares some possible use cases your app could support, as well as
a sample flow that could support each use case. This can be a helpful jumping
off point as you plan your app's implementation.

## Periodically send an email with latest posts to blog subscribers

You could help blog owners inform their subscribers of new posts. This flow relies on an external email delivery service and a database with emails of a blog's subscribers. 

1. Call [Query Posts](https://dev.wix.com/api/rest/wix-blog/blog/posts/query-posts) and filter for new posts since the last load. 

```javascript
{
  "filter": {
    "firstPublishedDate": {
      "$gt": "<PREVIOUS_LOAD_DATETIME>"
    }
  }
}
```

1. Extract the following data from the post payload: 
    - `title`
    - `excerpt`
    - `url`

1. Create a templatized email with the extracted information and send to subscribers. 

## Send out a social media post when a new blog post is marked as featured

You can help a blog owner to market their blog by creating a post on their social media with featured blog content. 
This flow relies on a user having provided permission for the app to access their social media accounts. 

1. When the [Post Created Webhook](https://dev.wix.com/api/rest/wix-blog/blog/posts/post-created-webhook) is triggered, you'll receive the entity in the payload.

1. Extract the `entityId` and use it to call [Get Post](https://dev.wix.com/api/rest/wix-blog/blog/posts/get-post). Check to see whether the post has been marked as featured. 

1. If `featured` is set to true, extract desired fields from the Get Post payload for the social media post. For example, a blog owner might want their social media post to include the following information: 
    - `title`
    - `url`
    - `excerpt` 
    - `minutesToRead`
    - `media`

1. Create a social media post to include the desired data, then post it to social media.  
 
<!-- ## Mirror a blog on another site

You could help blog owners mirror their blogs to another site. 
For example, a blog owner might want to take all of their content, translate and mirror it to a blog site in a different language.  -->

