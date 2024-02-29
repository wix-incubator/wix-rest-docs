SortOrder: 1
# Field Support for Filtering and Sorting

Endpoints that allow for querying follow the [API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language).

Note that the `$hasSome` operator works the same as the operator "IN" in SQL.

## Post API: Supported Filters and Sorting

The following table shows field support for filters and sorting for the post object:

| Field               | Supported Filters                            | Sortable  |
| ------------------- | -------------------------------------------- | --------- |
| `id`                | `$eq`, `$ne`, `$hasSome`                    | Sortable  |
| `categoryId`        | `$eq`, `$ne`                                |           |
| `title`             | `$eq`, `$ne`, `$contains`, `$hasSome`, `$urlized`, `$startsWith`, `$endsWith`, `$hasSome` |           |
| `ownerId`           | `$eq`, `$ne`                                |           |
| `contentText`       | `$eq`, `$ne`, `$contains`, `$hasSome`, `$startsWith`, `$endsWith`, `$hasSome` |           |
| `bestAnswerCommentId`| `$eq`, `$ne`                               |           |
| `pinned`            | `$eq`, `$ne`                                | Sortable   |
| `commentingEnabled` | `$eq`, `$ne`                                |           |
| `commentCount`      | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`  | Sortable  |
| `likeCount`         | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`  | Sortable  |
| `viewCount`         | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`  | Sortable  |
| `createdDate`       | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`  | Sortable  |
| `updatedDate`       | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`  |           |
| `lastActivityDate`  | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`  | Sortable  |
| `slug`              | `$eq`, `$ne`, `$contains`, `$hasSome`, `$urlized`, `$startsWith`, `$endsWith`, `$hasSome` | Sortable  |

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

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Posts](https://dev.wix.com/docs/rest/api-reference/wix-forum/wix-forum/post/query-posts)

## Category API: Supported Filters and Sorting

The following table shows field support for filters and sorting for the category object:

| Field            | Supported Filters                                      | Sortable |
| ---------------- | ------------------------------------------------------ | -------- |
| `id`             | `$in`, `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`    |          |
| `parentId`       | `$in`, `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`    |          |
| `name`           | `$in`, `$eq`, `$ne`                                   |          |
| `rank`           | `$in`, `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`    | Sortable |
| `headerTitle`    | `$in`, `$eq`, `$ne`                                   |          |
| `headerType`     | `$in`, `$eq`, `$ne`                                   |          |
| `headerDescription` | `$in`, `$eq`, `$ne`                                 |          |
| `postCount`      | `$in`, `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`    | Sortable|
| `postViewCount`  | `$in`, `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`    | Sortable |
| `slug`           | `$in`, `$eq`, `$ne`                                   |          |



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

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Categories](https://dev.wix.com/docs/rest/api-reference/wix-forum/wix-forum/category/query-categories)

## Draft Post API: Supported Filters and Sorting

The following table shows field support for filters and sorting for the draft post object:

| Field          | Supported Filters                           | Sortable  |
| -------------- | ------------------------------------------- | --------- |
| `id`           | `$eq`, `$ne`, `$hasSome`                   | Sortable  |
| `categoryId`   | `$eq`, `$ne`                               |           |
| `title`        | `$eq`, `$ne`, `$contains`, `$hasSome`, `$urlized`, `$startsWith`, `$endsWith`, `$hasSome` |           |
| `ownerId`      | `$eq`, `$ne`                               |           |
| `contentText`  | `$eq`, `$ne`, `$contains`, `$hasSome`, `$startsWith`, `$endsWith`, `$hasSome` |           |
| `commentingType` | `$eq`, `$ne`                             |           |
| `createdDate`  | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte` | Sortable  |


### Examples

**Query draft post by content text**

```
curl 'https://www.wixapis.com/forum/v1/draft-posts/query' --data-binary '{"filter": {"contentText": {"$contains": "cat"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get all draft posts, sorted by createdDate**

```
curl 'https://www.wixapis.com/forum/v1/draft-posts/query' --data-binary '{"sort":[{"fieldName": "createdDate"}]}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get draft posts by IDs**

```
curl 'https://www.wixapis.com/forum/v1/draft-posts/query' --data-binary '{"filter": {"id": {"$hasSome": ["DRAFT_POST_ID_1","DRAFT_POST_ID_2"]}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Draft Posts](https://dev.wix.com/docs/rest/api-reference/wix-forum/wix-forum/draft-post/query-draft-posts)
