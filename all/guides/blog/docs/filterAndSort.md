SortOrder: 1
# Field Support for Filtering and Sorting

The table below shows field support for filters and sorting.

## Query Language

Endpoints that allow for querying follow the [API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language).

## Post API
### Fields That Allow Filtering

| Field | Operators | Sorting Allowed|
| --- | --- | --- |
| id |$eq, $ne, $hasSome|Allowed|
| title |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| excerpt |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| contentText |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| firstPublishedDate |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| lastPublishedDate |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| url |$eq, $ne, $lt, $lte, $gt, $gte||
| memberId |$eq, $ne, $hasSome||
| slug |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| featured |$eq, $ne|Allowed|
| pinned |$eq, $ne|Allowed|
| categoryIds |$hasSome, $hasAll||
| hashtags |$hasSome, $hasAll||
| commentingEnabled |$eq, $ne|Allowed|
| tagIds |$hasSome, $hasAll||
| paidPlans |$hasSome, $hasAll||
| pricingPlanIds |$hasSome, $hasAll||
| language |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| translationId |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|

** Note that "hasSome" is same as the operator "IN" in SQL

### Examples

**Query pinned posts**

```
curl 'https://www.wixapis.com/blog/v3/posts/query' --data-binary '{"filter": {"pinned": {"$eq": true}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get all posts, sorted by publication date (latest first)**

```
curl 'https://www.wixapis.com/blog/v3/posts/query' --data-binary '{"sort":[{"fieldName": "firstPublishedDate", "order": "DESC"}]}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get posts by IDs**

```
curl 'https://www.wixapis.com/blog/v3/posts/query' --data-binary '{"filter": {"id": {"$hasSome": ["POST_ID_1","POST_ID_2"]}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

## Category API
### Fields That Allow Filtering

| Field | Operators | Sorting Allowed|
| --- | --- | --- |
| id |$eq, $ne, $hasSome|Allowed|
| label |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| postCount |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| url |$eq, $ne, $lt, $lte, $gt, $gte||
| description |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| title |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| rank |$eq, $ne, $lt, $lte, $gt, $gte|Allowed|
| language |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|
| translationId |$eq, $ne, $contains, $hasSome, $urlized, $startsWith, $endsWith, $hasSome|Allowed|

** Note that "hasSome" is same as the operator "IN" in SQL

### Examples

**Query categories by description**

```
curl 'https://www.wixapis.com/blog/v3/categories/query' --data-binary '{"filter": {"description": {"$contains": "cat"}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get all categories, sorted by rank**

```
curl 'https://www.wixapis.com/blog/v3/categories/query' --data-binary '{"sort":[{"fieldName": "rank"}]}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```

**Get categories by IDs**

```
curl 'https://www.wixapis.com/blog/v3/categories/query' --data-binary '{"filter": {"id": {"$hasSome": ["CATEGORY_ID_1","CATEGORY_ID_2"]}}}' -H 'Content-Type: application/json' -H 'Authorization: <AUTH>'
```
