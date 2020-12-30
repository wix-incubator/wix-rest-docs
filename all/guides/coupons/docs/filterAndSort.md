SortOrder: 1
# Filter and sort

## Query Language

Endpoints that allow querying follow these format [guidelines](https://dev.wix.com/api/rest/getting-started/api-query-language).

## Fields That Allow Filtering

| Field | Operators | Sorting Allowed|
| --- | --- | --- |
| id |$eq,$ne,$hasSome,$contains,$startsWith|Allowed|
| dateCreated |$eq,$ne,$hasSome,$lt,$lte,$gt,$gte|Allowed|
| expired |$eq,$ne||
| specification.active |$eq,$ne||
| specification.name |$eq,$ne,$hasSome,$contains,$startsWith|Allowed|
| specification.code |$eq,$ne,$hasSome,$contains,$startsWith|Allowed|
| specification.usageLimit |$eq,$ne,$hasSome,$contains,$startsWith|Allowed|
| specification.limitedToOneItem |$eq,$ne||
| scope.namespace |$eq,$ne,$hasSome,$contains,$startsWith|Allowed|
| scope.group.name |$eq,$ne,$hasSome,$contains,$startsWith|Allowed|
| scope.group.entityId |$eq,$ne,$hasSome,$contains,$startsWith|Allowed|

** Note that "HasSome" is same as the operator "IN" in SQL

## Examples

**Query valid (i.e., non-expired) coupons**

```
curl 'https://www.wixapis.com/stores/v2/coupons/query' --data-binary '{"query":{"filter":"{\"expired\": false}"}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
``` 

**Get all coupons, sorted by creation date**

```
curl 'https://www.wixapis.com/stores/v2/coupons/query' --data-binary '{"query":{"sort":"[{\"dateCreated\": \"asc\"}]"}}' -H 'Content-Type: application/json' -H 'Authorization: XXX'
``` 

**Get coupons by IDs**

```
curl 'https://www.wixapis.com/stores/v2/coupons/query' --data-binary '{"query":{"filter":"{\"id\": {\"$hasSome\": [\"COUPON_ID_1\",\"COUPON_ID_2\"]}}"}}' -H 'Content-Type: application/json' -H 'Authorization: xxx'
``` 
