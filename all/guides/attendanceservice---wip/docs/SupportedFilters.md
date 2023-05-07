SortOrder: 1
# Supported Filters


[Query Attendance](https://dev.wix.com/api/rest/wix-bookings/bookings-attendance-v2/query-attendance) runs with these defaults:

+ sorted by `id` in `ASC` order
+ cursorPaging.limit is `50`

`query.fields` and `query.fieldsets` aren't supported for this endpoint.

The following table shows field support for filters for the attendance object:


| Field             | Supported Filters                             |
|-------------------| --------------------------------------------- |
| id                | `eq`, `ne`, `in` |
| bookingId         | `eq`, `ne`, `in` |
| sessionId         | `eq`, `ne`, `in` |
| status            | `eq`, `ne`, `in` |
| numberOtAttendees | `eq`, `ne`, `in` |


You can only specify a filter only once per query. If a filter is provided
more than once, only the first occurrence affects the returned attendances.


To learn about working with _Query_ endpoints, see
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Sorting and Paging](https://dev.wix.com/api/rest/getting-started/sorting-and-paging),
and [Field Projection](https://dev.wix.com/api/rest/getting-started/field-projection).