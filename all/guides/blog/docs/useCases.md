SortOrder: 2
# Use cases

This article shares some possible uses of the Blog API endpoints and their responses.

## Post API

### Get a Post by ID or by Slug

To get a specific post, use [Get Post](https://dev.wix.com/api/rest/community/blog/post/get-post) to retrieve a post by its ID:

```
curl 'http://www.wixapis.com/blog/v3/posts/894a58a2-dc75-422d-9ca6-00a489750dfd' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

Another option for retrieving a specific post is [Get Post by Slug](https://dev.wix.com/api/rest/community/blog/post/get-post-by-slug):

```
curl 'http://www.wixapis.com/blog/v3/posts/slugs/my-vacation' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

An example response to both [Get Post](https://dev.wix.com/api/rest/community/blog/post/get-post) and [Get Post by Slug](https://dev.wix.com/api/rest/community/blog/post/get-post-by-slug) will look this:

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

To get post metrics (the number of comments, likes, and views) use [Get Post Metrics](https://dev.wix.com/api/rest/community/blog/post/get-post-metrics) and pass the post ID:

```
curl 'http://www.wixapis.com/blog/v3/posts/894a58a2-dc75-422d-9ca6-00a489750dfd/metrics' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will look like this:

```json
{
  "metrics": {
    "comments": 5,
    "likes": 8,
    "views": 31
  }
}
```

### Bulk Get Post Metrics

To get post metrics for multiple posts, use [Bulk Get Post Metrics](https://dev.wix.com/api/rest/community/blog/post/bulk-get-post-metrics) and pass the post IDs:

```
curl 'http://www.wixapis.com/blog/v3/posts/metrics' --data-binary '{"post_ids": ["894a58a2-dc75-422d-9ca6-00a489750dfd"]}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>' -X PUT
```

The response will look like this:

```json
{
  "894a58a2-dc75-422d-9ca6-00a489750dfd": {
      "metrics": {
        "comments": 5,
        "likes": 8,
        "views": 31
      }
  }
}
```

### Retrieving Multiple Posts

To retrieve more than one post, use either the [List Posts](https://dev.wix.com/api/rest/community/blog/post/list-posts) or [Query Posts](https://dev.wix.com/api/rest/community/blog/post/query-posts) endpoints.

#### List Posts

Using the [List Posts](https://dev.wix.com/api/rest/community/blog/post/list-posts) endpoint, you can list all posts belonging to a category by providing the category ID:

```
curl 'http://www.wixapis.com/blog/v3/posts?categoryIds=5f2bcaa5940a02003488af3e' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

An example response to the call above will look like this:

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

If you need a more detailed query, use [Query Posts](https://dev.wix.com/api/rest/community/blog/post/query-posts).

In the example below we're going to request only posts that have a title starting with "My vacation".

Note that we're also requesting to include the `"URL"`, `"COUNTERS"`, and `"CONTENT_TEXT"` fields in the response:

```
curl 'https://www.wixapis.com/blog/v3/posts/query' --data-binary '{"fieldsToInclude": ["URL", "COUNTERS", "CONTENT_TEXT"], "filter":{"title":{"$startsWith": "My vacation"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will look like this:

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

To get a specific category, use [Get Category](https://dev.wix.com/api/rest/wix-blog/blog/category/get-category) to retrieve a category by its ID:

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

Using the [List Categories](https://dev.wix.com/api/rest/community/blog/category/list-categories) endpoint, you can retrieve all existing categories:

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

In the example below we request only categories that have a title starting with "Summer":

```
curl 'https://www.wixapis.com/blog/v3/categories/query' --data-binary '{"fieldsToInclude": ["URL"], "filter":{"title":{"$startsWith": "Summer"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will be an array of the categories that matched the query:

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



## Tag API

Tags, like categories, provide a way to group your posts. Tags are more lightweight and granular than categories.

### Query Blog Posts by Tag

Imagine a cooking blog where a site owner writes recipes as posts, and groups them by recipe type using categories.

Additional information about the main ingredients is also found in tags like `chicken`, `mushrooms`, `fresh pasta`, `etc`.

This allows the site owner to layer multiple classifications onto their posts, which you can then retrieve in more flexible ways.

1. **Retrieve List of Desired Tags**

To fetch all the tags representing ingredients from the blog, use the [Query Tags](https://dev.wix.com/api/rest/community/blog/tag/query-tags) endpoint.

In the specific example below, we request all tags with a label starting with word "coriander":

```
curl 'https://www.wixapis.com/blog/v2/tags/query' --data-binary '{"filter":{"label":{"$startsWith": "coriander"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will be an array of the tags that matched the query:

```json
{
  "tags": [
    {
      "id": "f0ad2e22-2cfd-49ff-aa3a-eae68a9d5008",
      "label": "coriander leaves",
      "slug": "coriander-leaves",
      "createdDate": "2021-11-17T11:26:53.987Z",
      "updatedDate": "2021-11-17T11:26:53.987Z",
      "publicationCount": 1,
      "postCount": 1,
      "url": {
        "base": "https://fantastic-cooking.com",
        "path": "/recipes/tags/coriander-leaves"
      },
      "language": "en"
    },
    {
      "id": "fec0b26b-fdcd-4662-badb-fd23a123f0ec",
      "label": "coriander seeds",
      "slug": "coriander-seeds",
      "createdDate": "2021-11-17T11:31:45.892Z",
      "updatedDate": "2021-11-17T11:31:45.892Z",
      "publicationCount": 1,
      "postCount": 1,
      "url": {
        "base": "https://fantastic-cooking.com",
        "path": "/recipes/tags/coriander-seeds"
      },
      "language": "en"
    }
  ],
  "metaData": {
    "count": 2,
    "offset": 0,
    "total": 2
  }
}
```
1. **Retrieve Posts Matching the Tags**
  
The returned tag IDs can be used in the [Query Posts](https://dev.wix.com/api/rest/community/blog/post/query-posts) endpoints, to get all the posts with the specified tag:

```
curl 'https://www.wixapis.com/blog/v3/posts/query' --data-binary '{"fieldsToInclude": ["URL"], "filter":{"tagIds":{"$hasSome": ["f0ad2e22-2cfd-49ff-aa3a-eae68a9d5008", "fec0b26b-fdcd-4662-badb-fd23a123f0ec"]}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

The response will look like this:

```json
{
  "posts": [
    {
      "id": "ccedcbe1-5588-4833-b2d7-7d33b9c24d15",
      "title": "Pepper and Coriander Crusted Tuna",
      "excerpt": "Pepper and Coriander Crusted Tuna",
      "firstPublishedDate": "2021-11-17T11:30:59.861Z",
      "lastPublishedDate": "2021-11-17T11:30:59.861Z",
      "slug": "pepper-and-coriander-crusted-tuna",
      "featured": false,
      "pinned": false,
      "categoryIds": [],
      "memberId": "2d24cb8a-adcc-466a-ab59-fa74e0889a37",
      "hashtags": [],
      "commentingEnabled": true,
      "minutesToRead": 1,
      "tagIds": [
        "f7a2fa4d-c3b3-48a6-91bf-9b6a422971fe",
        "d45f3110-00e0-4339-8619-7b6863002e37",
        "fec0b26b-fdcd-4662-badb-fd23a123f0ec",
        "215f3038-2a7a-460f-b876-fe1e17dea1cd"
      ],
      "relatedPostIds": [],
      "pricingPlanIds": [],
      "language": "en"
    },
    {
      "id": "20b6a0a9-8492-406a-898b-a793b09048a9",
      "title": "Pico de gallo salsa",
      "excerpt": "Pico de gallo salsa",
      "firstPublishedDate": "2021-11-17T11:27:34.603Z",
      "lastPublishedDate": "2021-11-17T11:27:34.603Z",
      "slug": "pico-de-gallo-salsa",
      "featured": false,
      "pinned": false,
      "categoryIds": [],
      "memberId": "2d24cb8a-adcc-466a-ab59-fa74e0889a37",
      "hashtags": [],
      "commentingEnabled": true,
      "minutesToRead": 1,
      "tagIds": [
        "0a57ac1a-1733-4fd3-8a17-123b1578399b",
        "f0ad2e22-2cfd-49ff-aa3a-eae68a9d5008",
        "c0dac587-0963-43dd-ae48-9afa432bab22",
        "4f801cd8-47d3-4434-81ff-5ff9178ae40e"
      ],
      "relatedPostIds": [],
      "pricingPlanIds": [],
      "language": "en"
    }
  ],
  "metaData": {
    "count": 2,
    "offset": 0,
    "total": 2
  }
}
```

#### Retrieve single tag

You can also retrieve a single tag either by ID, slug or label.

To fetch a tag by ID, use the [Get Tag](https://dev.wix.com/api/rest/community/blog/tag/get-tag) endpoint:

```
curl \
'http://www.wixapis.com/blog/v3/tags/6d72a3bb-053c-4de5-a897-5ef6be30b1b0' \
-H 'Content-Type: application/json' \
-H 'Authorization: <AUTH>'
```

The [Get Tag By Label](https://dev.wix.com/api/rest/community/blog/tag/get-tag-by-label) endpoint can be used to fetch tag when the label is known:

```
curl \
  'http://www.wixapis.com/blog/v3/tags/labels/eggplant' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>'
```

To fetch a tag using its URL slug, use [Get Tag By Slug](https://dev.wix.com/api/rest/community/blog/tag/get-tag-by-slug):

```
curl \
  'http://www.wixapis.com/blog/v3/tags/slugs/eggplant' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>'
```

The response structure is the same for all three requests; a single tag object.

```json
{
  "tag": {
    "id": "6d72a3bb-053c-4de5-a897-5ef6be30b1b0",
    "label": "eggplant",
    "slug": "eggplant",
    "createdDate": "2021-08-13T08:58:20.145Z",
    "updatedDate": "2021-08-13T08:58:20.145Z",
    "publicationCount": 2,
    "postCount": 1,
    "language": "en"
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
