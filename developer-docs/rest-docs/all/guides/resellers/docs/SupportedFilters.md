SortOrder: 2

# Resellers: Supported Filters, Sorting, and Search

This article covers field support for filtering and sorting
in the Resellers API.


## Query Packages: Supported filters and sorting

The table below shows field support for filters and sorting
in the [Query Packages](https://dev.wix.com/api/rest/account-level-apis/resellers/packages/query-packages)
endpoint.

| Field                        | Supported Filters                             | Sortable |
| ---------------------------- | --------------------------------------------- | -------- |
| `id`                         | `$eq`, `$ne`, `$in`, `$exists`                |          |
| `createdDate`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `updatedDate`                | `$eq`, `$ne`, `$gt`, `$lt`, `$gte`, `$lte`    | Sortable |
| `accountId`                  | `$eq`, `$ne`, `$in`, `$exists`                |          |
| `externalId`                 | `$eq`, `$ne`, `$in`, `$exists`                |          |
| `productInstances`           | `$hasSome`, `$hasAll`                         |          |
| `productInstances.instanceId`          | `$hasSome`, `$hasAll` |          |
| `productInstances.siteId`          | `$hasSome`, `$hasAll` |          |
| `productInstances.catalogProductId`          | `$hasSome`, `$hasAll` |          |
| `productInstances.status`          | `$hasSome`, `$hasAll` |          |
| `productInstances.instanceId`          | `$hasSome`, `$hasAll` |          |
| `productInstances.failure`          | `$hasSome`, `$hasAll` |          |
| `productInstances.failure.code`          | `$hasSome`, `$hasAll` |          |
| `productInstances.failure.message`          | `$hasSome`, `$hasAll` |          |
| `productInstances.billingInfo`          | `$hasSome`, `$hasAll` |          |
| `productInstances.billingInfo.type`          | `$hasSome`, `$hasAll` |          |
| `productInstances.billingInfo.cycleDuration`          | `$hasSome`, `$hasAll` |          |
| `productInstances.billingInfo.cycleDuration.unit`          | `$hasSome`, `$hasAll` |          |
| `productInstances.billingInfo.cycleDuration.count`          | `$hasSome`, `$hasAll` |          |
| `productInstances.createdDate`                | `$hasSome`, `$hasAll` |          |
| `productInstances.updatedDate`                | `$hasSome`, `$hasAll` |          |
| `productInstances.countryCode`                | `$hasSome`, `$hasAll` |          |


To learn about working with _Query_ endpoints in general, see
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language)
and [Sorting and Paging](https://dev.wix.com/api/rest/getting-started/sorting-and-paging).