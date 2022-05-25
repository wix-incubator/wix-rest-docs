SortOrder: 1
# Field Support for Filtering and Sorting

Endpoints that allow for querying follow the [API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language).

Note that the "hasSome" operator works the same as the operator "IN" in SQL.

## Post API
### Fields That Allow Filtering

| Field | Operators | Sorting Allowed|
| --- | --- | --- |
| id |$eq, $ne, $hasSome|Allowed|
| categoryId |$eq, $ne||
| title |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome||
| ownerId |$eq, $ne ||
| contentText |$eq, $ne, $contains, $hasSome, $startsWith, $endsWith, $hasSome||
| bestAnswerCommentId |$eq, $ne||
| pinned |$eq, $ne |Allowed|
| commentingEnabled |$eq, $ne ||
| commentCount |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| likeCount |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| viewCount |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| createdDate |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| updatedDate |$eq, $ne, $lt, $lte, $gt, $gte||
| lastActivityDate |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| slug |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|


### Examples

**Query pinned posts**

```
curl 'https://www.wixapis.com/forum/v1/posts/query' --data-binary '{"filter": {"pinned": {"$eq": true}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get all posts, sorted by created date (latest first)**

```
curl 'https://www.wixapis.com/forum/v1/posts/query' --data-binary '{"sort":[{"fieldName": "createdDate", "order": "DESC"}]}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get posts by IDs**

```
curl 'https://www.wixapis.com/forum/v1/posts/query' --data-binary '{"filter": {"id": {"$hasSome": ["POST_ID_1","POST_ID_2"]}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

## Category API
### Fields That Allow Filtering

| Field | Operators | Sorting Allowed|
| --- | --- | --- |
| id |$eq, $ne, $hasSome|Allowed|
| parentId |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome||
| name |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome||
| rank |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| headerTitle |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome||
| headerType |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome||
| description |$eq, $ne, $contains, $hasSome, $startsWith, $endsWith, $hasSome||
| postCount |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| postViewCount |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| slug |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome||


### Examples

**Query categories by description**

```
curl 'https://www.wixapis.com/forum/v1/categories/query' --data-binary '{"filter": {"description": {"$contains": "cat"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get all categories, sorted by rank**

```
curl 'https://www.wixapis.com/forum/v1/categories/query' --data-binary '{"sort":[{"fieldName": "rank"}]}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get categories by IDs**

```
curl 'https://www.wixapis.com/forum/v1/categories/query' --data-binary '{"filter": {"id": {"$hasSome": ["CATEGORY_ID_1","CATEGORY_ID_2"]}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```
