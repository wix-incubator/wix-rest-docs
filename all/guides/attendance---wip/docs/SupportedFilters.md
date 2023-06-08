SortOrder: 1
# Supported Filters and Sorting


[Query Attendance](https://dev.wix.com/api/rest/wix-bookings/attendance/query-attendance) runs with these defaults:

+ sorted by `id` in `ASC` order
+ cursorPaging.limit is `50`

The following table shows field support for filters for the `Attendance` object:


| Field             | Supported Filters                                                     | Sortable  |
|-------------------|-----------------------------------------------------------------------| --------- |
| `id`                | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`                               | Sortable |
| `bookingId`         | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`                               | Sortable |
| `sessionId`         | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`                               | Sortable |
| `status`            | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`                               | Sortable |
| `numberOfAttendees` | `$eq`, `$ne`, `$in`, `$nin`, `$hasSome`, `$lt`, `$lte`, `$gt`, `$gte` | Sortable |


> **Notes:**
> + Only 1 filter is supported per query. If you define multiple filters in the same query, only the first is processed.



To learn about working with query endpoints, see
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Sorting and Paging](https://dev.wix.com/api/rest/getting-started/sorting-and-paging),
and [Field Projection](https://dev.wix.com/api/rest/getting-started/field-projection).