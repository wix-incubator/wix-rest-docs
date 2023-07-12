SortOrder: 2
# Services: Filtering and Sorting

Query endpoints allow you to filter and sort results based on service properties. This article covers field support for
filtering and sorting.

## Filtering

Specify the `filter` object in the following format:

```json
{
  "filter": {
    "fieldName": {
      "$eq": "value"
    }
  }
}
```

The following table shows field support for filters and sorting
for the `service` object:

| Field                         | Supported Filters                                         | Sortable |
|-------------------------------|-----------------------------------------------------------|----------|
| `name`                        | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` | Sortable |
| `type`                        | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`                | Sortable |
| `description`                 | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` | Sortable |
| `hidden`                      | `$eq`, `$ne`, `$exists`, `$in`                            |          |
| `tagLine`                     | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` | Sortable |
| `staffMemberIds`              | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` |          |
| `form.id`                     | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` |          |
| `category.id`                 | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` |          |
| `mainSlug.name`               | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` | Sortable |
| `supportedSlugs.name`         | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` | Sortable |
| `locations.business.id`       | `$eq`, `$ne`, `$exists`, `$in`, `$hasSome`, `$startsWith` |          |
| `onlineBooking.enabled`       | `$eq`, `$ne`, `$exists`, `$in`                            |          |
| `payment.options.online`      | `$eq`, `$ne`, `$exists`, `$in`                            |          |
| `payment.options.inPerson`    | `$eq`, `$ne`, `$exists`, `$in`                            |          |
| `payment.options.pricingPlan` | `$eq`, `$ne`, `$exists`, `$in`                            |          |

## Sorting


 The default sort is by `createdDate` in ascending (ASC) order.

Specify the `sort` object in the following format:

```json
{
  "sort" : [
    {
      "fieldName": "sortOrder",
      "order": "ASC"
    },
    {
      "fieldName": "createdDate",
      "order": "DESC"
    }
  ]
}
```

## Fields

Specify the `fields` object in the following format:

```json
{
  "fields": ["name", "type", "description"]
}
```

__Related content:__
- [API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language)
- [Query services](https://dev.wix.com/api/rest/wix-bookings/services-v2/query-services)
