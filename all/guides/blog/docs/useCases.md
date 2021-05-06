SortOrder: 2
# Use cases

This articles shares some possible uses of the Blog API endpoints and their respective responses.

## Post API
### Get a Post by ID or by Slug

To get a specific post, use [Get Post](/docs/LINK) to retrieve a post by its ID:

```
curl 'http://www.wixapis.com/blog/v3/posts/894a58a2-dc75-422d-9ca6-00a489750dfd' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```


Another option for retrieving a specific post is by using [Get Post by Slug](/docs/LINK):

```
curl 'http://www.wixapis.com/blog/v3/posts/slugs/my-vacation' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

An example response to both [Get Post](/docs/LINK) and [Get Post by Slug](/docs/LINK) will look something like this:

```
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

To get post metrics like the number of comments, likes, and views, use [Get Post Metrics](/docs/LINK) and pass the post ID

```
curl 'http://www.wixapis.com/blog/v3/posts/894a58a2-dc75-422d-9ca6-00a489750dfd/metrics' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will look something like this:

```
{
  "metrics": {
    "comments": 5,
    "likes": 8,
    "views": 31
  }
}
```

### Retrieving Multiple Posts

To retrieve more than one post, use either the [List Posts](/docs/LINK) or [Query Posts](/docs/LINK) endpoints.

#### List Posts

Using the [List Posts](/docs/LINK) endpoint, list the posts that belong to the category with the provided ID:

```
curl 'http://www.wixapis.com/blog/v3/posts?categoryIds=5f2bcaa5940a02003488af3e' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

An example response to the call above will look something like this:

```
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
If a more detailed query is needed, use [Query Posts](/docs/LINK).
In the example below we're going to request only posts that have a title starting with "My vacation".
Note that we're also requesting to include the `"URL"`, `"COUNTERS"`, and `"CONTENT_TEXT"` fields in the response:

```
curl 'https://www.wixapis.com/blog/v3/posts/query' --data-binary '{"fieldsToInclude": ["URL", "COUNTERS", "CONTENT_TEXT"], "filter":{"title":{"$startsWith": "My vacation"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response we got looked like this:

```
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

## Publication Stats API

The Publication Stats API allows for the retrieval of publication counts for each month of a specified time range, or the total number of posts published by the blog in context.

### Query Publications Count

Using [Query Publications Count](/docs/LINK), we're fetching statistics for the 3 months starting from November 2018, and ordered by oldest first:

```
curl --request POST 'http://social-blog.wix.com/_api/communities-blog-node-api/v2/stats/publications/count' \
--header 'Authorization: <AUTH> --header 'Content-Type: application/json' \
--data-raw '{
	"rangeStart": "2018-11-01T00:00:00Z",
	"order": "OLDEST",
	"months": 3
}'
```

The response will look like this:

```
{
  "stats": [
    {
      "periodStart": "2018-11-01T00:00:00.000Z",
      "publicationsCount": 1
    },
    {
      "periodStart": "2018-12-01T00:00:00.000Z",
      "publicationsCount": 2
    },
    {
      "periodStart": "2019-01-01T00:00:00.000Z",
      "publicationsCount": 2
    }
  ]
}
```

## Category API

### Get a Category

To get a specific category, use [Get Category](/docs/LINK) to retrieve a category by its ID:

```
curl 'http://www.wixapis.com/blog/v3/categories/894a58a2-dc75-422d-9ca6-10a489750dfd' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will contain a category object:

```
{
  "category": {
    "id": "894a58a2-dc75-422d-9ca6-10a489750dfd",
    "label": "Summer",
    "postCount": 17,
    "description": "Posts about my summer",
    "title": Summer,
    "rank": 1,
    "language": "en",
    "translationId": "111a58a2-dc75-422d-9ca6-00a489750dfd"
  }
}
```

### Retrieving Multiple Categories

To retrieve more than one category, use either the [List Categories](/docs/LINK) or [Query Categories](/docs/LINK) endpoints.

#### List Categories

Using the [List Categories](/docs/LINK) endpoint, retrieve all existing categories:

```
curl 'http://www.wixapis.com/blog/v3/categories' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will be an array of the retrieved categories:

```
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

If a more detailed query is needed, use [Query Categories](/docs/LINK).
In the example below we're going to request only categories that have a title starting with "Summer":

```
curl 'https://www.wixapis.com/blog/v3/categories/query' --data-binary '{"fieldsToInclude": ["URL"], "filter":{"title":{"$startsWith": "Summer"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will be an array of the categories that passed the query:

```
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
    "title": Summer,
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