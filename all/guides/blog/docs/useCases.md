SortOrder: 2
# Use cases

This articles shares some possible uses of the Blog API endpoints and their respective responses.

## Post API
### Get a Post by ID or by Slug

To get a specific post, use [Get Post](https://dev.wix.com/api/rest/community/blog/post/get-post) to retrieve a post by its ID:

```
curl 'http://www.wixapis.com/blog/v3/posts/894a58a2-dc75-422d-9ca6-00a489750dfd' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```


Another option for retrieving a specific post is by using [Get Post by Slug](https://dev.wix.com/api/rest/community/blog/post/get-post-by-slug):

```
curl 'http://www.wixapis.com/blog/v3/posts/slugs/my-vacation' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

An example response to both [Get Post](https://dev.wix.com/api/rest/community/blog/post/get-post) and [Get Post by Slug](https://dev.wix.com/api/rest/community/blog/post/get-post-by-slug) will look something like this:

```json
{
  "post": {
    "id": "894a58a2-dc75-422d-9ca6-00a489750dfd",
    "title": "My vacation",
    "firstPublishedDate": "2020-08-06T09:18:07.839Z",
    "lastPublishedDate": "2020-08-06T09:18:07.839Z",
    "featured": true,
    "pinned": false,
    "categoryIds": [
      "5f2bcaa0879ad500173577f3",
      "5f2bcaa5940a02003488af3e"
    ],
    "memberId": "5ee77ebfffeab500188f496b",
    "hashtags": [
      "sea",
      "sun"
    ],
    "commentingEnabled": true,
    "minutesToRead": 1,
    "tagIds": [
      "5f2bcaa0879a4400173577f1",
      "5f2bc445940a02003488af3a"
    ],
    "pricingPlanIds": [
      "5f2bc445940a02003498af3e"
    ],
    "relatedPostIds": [
      "111a58a2-dc75-422d-0015-00a489750dfd", 
      "211a58a2-dc75-422d-1512-00a489750dfd"
    ],
    "language": "en",
    "translationId": "111a58a2-dc75-422d-9ca6-00a489750dfd"
  }
}
```

### Get a Post's Metrics

To get post metrics like the number of comments, likes, and views, use [Get Post Metrics](https://dev.wix.com/api/rest/community/blog/post/get-post-metrics) and pass the post ID

```
curl 'http://www.wixapis.com/blog/v3/posts/894a58a2-dc75-422d-9ca6-00a489750dfd/metrics' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will look something like this:

```json
{
  "metrics": {
    "comments": 5,
    "likes": 8,
    "views": 31
  }
}
```

### Retrieving Multiple Posts

To retrieve more than one post, use either the [List Posts](https://dev.wix.com/api/rest/community/blog/post/list-posts) or [Query Posts](https://dev.wix.com/api/rest/community/blog/post/query-posts) endpoints.

#### List Posts

Using the [List Posts](https://dev.wix.com/api/rest/community/blog/post/list-posts) endpoint, list the posts that belong to the category with the provided ID:

```
curl 'http://www.wixapis.com/blog/v3/posts?categoryIds=5f2bcaa5940a02003488af3e' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

An example response to the call above will look something like this:

```json
{
  "posts": [
    {
      "id": "894a58a2-dc75-422d-9ca6-00a489750dfd",
      "title": "My vacation",
      "firstPublishedDate": "2020-08-06T09:18:07.839Z",
      "lastPublishedDate": "2020-08-06T09:18:07.839Z",
      "featured": true,
      "pinned": false,
      "categoryIds": [
        "5f2bcaa0879ad500173577f3",
        "5f2bcaa5940a02003488af3e"
      ],
      "memberId": "5ee77ebfffeab500188f496b",
      "hashtags": [
        "sea",
        "sun"
      ],
      "commentingEnabled": true,
      "minutesToRead": 1,
      "tagIds": [
        "5f2bcaa0879a4400173577f1",
        "5f2bc445940a02003488af3a"
      ],
      "pricingPlanIds": [
        "5f2bc445940a02003498af3e"
      ],
      "relatedPostIds": [
        "111a58a2-dc75-422d-0015-00a489750dfd",
        "111a58a2-dc75-422d-1512-00a489750dfd"
      ],
      "language": "en",
      "translationId": "111a58a2-dc75-422d-9ca6-00a489750dfd"
    }
  ],
  "metaData": {
    "count": 1,
    "offset": 0,
    "total": 1
  }
}
```

### Query Posts
If a more detailed query is needed, use [Query Posts](https://dev.wix.com/api/rest/community/blog/post/query-posts).
In the example below we're going to request only posts that have a title starting with "My vacation".
Note that we're also requesting to include the `"URL"`, `"COUNTERS"`, and `"CONTENT_TEXT"` fields in the response:

```
curl 'https://www.wixapis.com/blog/v3/posts/query' --data-binary '{"fieldsToInclude": ["URL", "COUNTERS", "CONTENT_TEXT"], "filter":{"title":{"$startsWith": "My vacation"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response we got looked like this:

```json
{
  "posts": [
    {
      "id": "894a58a2-dc75-422d-9ca6-10a489750dfd",
      "title": "My vacation",
      "contentText": "This is my post of my holidays #sea #sun",
      "firstPublishedDate": "2020-08-01T09:18:07.839Z",
      "lastPublishedDate": "2020-08-06T09:18:07.839Z",
      "url": {
        "base": "https://some.wixsite.com/something-to-prod/blog",
        "path": "/blog/post/my-vacation"
      },
      "featured": true,
      "pinned": false,
      "categoryIds": [
        "5f2bcaa0879ad500173577f3",
        "5f2bcaa5940a02003488af3e"
      ],
      "memberId": "5ee77ebfffeab500188f4961",
      "hashtags": [
        "sea",
        "sun"
      ],
      "commentingEnabled": true,
      "metrics": {
        "comments": 5,
        "likes": 2,
        "views": 25
      },
      "minutesToRead": 1,
      "tagIds": [
        "5f2bcaa0879a4400173577f1",
        "5f2bc445940a02003488af3a"
      ],
      "pricingPlanIds": [
        "5f2bc445940a02003498af3e"
      ],
      "relatedPostIds": [
        "111a58a2-dc75-422d-0015-00a489750dfd", 
        "211a58a2-dc75-422d-1512-00a489750dfd"
      ],
      "language": "en",
      "translationId": "111a58a2-dc75-422d-9ca6-00a489750dfd"
    }
  ],
  "metaData": {
    "count": 1,
    "offset": 0,
    "total": 1
  }
}
```

## Category API

### Get a Category

To get a specific category, use [Get Category](https://dev.wix.com/api/rest/community/blog/category/get-category) to retrieve a category by its ID:

```
curl 'http://www.wixapis.com/blog/v3/categories/894a58a2-dc75-422d-9ca6-10a489750dfd' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will contain a category object:

```json
{
  "category": {
    "id": "894a58a2-dc75-422d-9ca6-10a489750dfd",
    "label": "Summer",
    "postCount": 17,
    "description": "Posts about my summer",
    "title": "Summer",
    "rank": 1,
    "language": "en",
    "translationId": "111a58a2-dc75-422d-9ca6-00a489750dfd"
  }
}
```

### Retrieving Multiple Categories

To retrieve more than one category, use either the [List Categories](https://dev.wix.com/api/rest/community/blog/category/list-categories) or [Query Categories](https://dev.wix.com/api/rest/community/blog/category/query-categories) endpoints.

#### List Categories

Using the [List Categories](https://dev.wix.com/api/rest/community/blog/category/list-categories) endpoint, retrieve all existing categories:

```
curl 'http://www.wixapis.com/blog/v3/categories' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will be an array of the retrieved categories:

```json
{
  "categories": [
    {
      "id": "93f76102-d776-414f-b19f-854b0028035b",
      "label": "Vegetarian",
      "postCount": 0,
      "description": "Vegetarian recipes",
      "title": "Vegetarian",
      "coverMedia": {
        "enabled": true,
        "displayed": true
      },
      "rank": 0,
      "language": "en"
    },
    {
      "id": "05211adc-ae26-43fa-9f09-6cdbb53174ce",
      "label": "Fish",
      "postCount": 2,
      "description": "Fish recipes",
      "title": "Fish",
      "coverMedia": {
        "enabled": true,
        "displayed": true
      },
      "rank": 1,
      "language": "en"
    },
    {
      "id": "a68da372-6bfa-412c-ad29-a3f1000ea3f2",
      "label": "Spices",
      "postCount": 0,
      "description": "Ideas how to create your own spices",
      "title": "Spices",
      "coverMedia": {
        "enabled": true,
        "displayed": true
      },
      "rank": 2,
      "language": "en"
    }
  ],
  "metaData": {
    "count": 3,
    "offset": 0,
    "total": 3
  }
}
```

#### Query Categories

If a more detailed query is needed, use [Query Categories](https://dev.wix.com/api/rest/community/blog/category/query-categories).
In the example below we're going to request only categories that have a title starting with "Summer":

```
curl 'https://www.wixapis.com/blog/v3/categories/query' --data-binary '{"fieldsToInclude": ["URL"], "filter":{"title":{"$startsWith": "Summer"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will be an array of the categories that passed the query:

```json
{
  "categories": [
  {
    "id": "894a58a2-dc75-422d-9ca6-10a489750dfd",
    "label": "Summer",
    "postCount": 17,
    "url": {
      "base": "https://some.wixsite.com/something-to-prod/blog",
      "path": "/blog/categories/summer"
    },
    "description": "Posts about my summer",
    "title": "Summer",
    "rank": 1,
    "language": "en",
    "translationId": "111a58a2-dc75-422d-9ca6-00a489750dfd"
  }],
  "metaData": {
    "count": 1,
    "offset": 0,
    "total": 1
  }
}
```

## Post Stats API
#### Get Total Posts
Retrieves total post count by given language. For example to get total count for publications written in english language use request: 
```
curl 'www.wixapis.com/blog/v2/stats/posts/total?language=en' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>'
```
The response will be a json object with `total` field which represents total publication count for given language:
```json
{ "total": 9 }
```
`language` parameter is optional and when is not present post count for all languages will be present

#### Query Post Count
Retrieves the number of posts per month published from first day of a month, ignoring days value in period start field.  
For example, to retrieve statistics for posts in English language for last 3 months starting from `2018-11-01` ordered by oldest month first:

```
curl --request POST 'http://social-blog.wix.com/_api/communities-blog-node-api/v2/stats/posts/count' \
    --header 'Authorization: <AUTH>' \
    --header 'Content-Type: application/json' \
    --data-raw '{
                  "rangeStart": "2018-11-01",
                  "order": "OLDEST",
                  "months": 3,
                  "language": "en"
                }'
```
The response will be a json object with `stats` array field where each entry represents statistic of posts in english language count for a single month 
```json
{ "stats": [
    {
    "periodStart": "2018-11-01T00:00:00.000Z",
    "postCount": 1
  },
    {
    "periodStart": "2018-12-01T00:00:00.000Z",
    "postCount": 2
  },
    {
    "periodStart": "2019-01-01T00:00:00.000Z",
    "postCount": 2
  }
]} 
```
