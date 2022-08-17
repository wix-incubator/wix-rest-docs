SortOrder: 2
# Internal Fieldsets


[List Sessions](https://bo.wix.com/wix-docs/rest/bookings/calendar-v2---wip/list-sessions) 
and 
[Query Sessions](https://bo.wix.com/wix-docs/rest/bookings/calendar-v2---wip/query-sessions) 
accept the following values as `fieldsets`:

| <div style="width:150px">Fieldsets value</div>          | <div style="width:200px">Returned data</div>          |
| --------------- | --------------------------------------------- |
| `NO_PI` | Returns session objects without personal information. This means without `participants`, `location`, `calendarConference`, and `externalCalendarOverrides`. `NO_PI` is the default in case you don't pass a value for `fieldsets`. | 
| `ALL_PI` | Returns complete session objects.|
| `CURRENT_MEMBER_PI` | Returns some, but not all, session objects with personal information. This means `participants` and `calendarConference`are only included in sessions belonging to the currently logged-in member. | 
| `CURRENT_USER_PI` | Returns some, but not all, session objects with personal information. This means `participants` and `calendarConference`are only included in sessions belonging to the currently logged-in user. |  

> __Notes__:
> + `NO_PI` is the default in case you don't pass a value for `fieldsets`.
> + If you pass both `NO_PI` and `ALL_PI` in the same call complete session objects are returned.
> + In the public endpoints for 
>   [List Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar-v2/sessions/list-sessions)
>   and [Query Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar-v2/sessions/query-sessions) 
>   only `ALL_PI` and `NO_PI` are supported.