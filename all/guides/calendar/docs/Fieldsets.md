SortOrder: 2
# Supported Fieldsets

Fieldsets let you return a predefined partial `session` object.
The following table shows the fields that are returned by [Get Session](#get-session), [Query Sessions](#query-sessions), and [List Sessions](#list-sessions) for each fieldset.

| <div style="width:150px">Fieldset</div>          | <div style="width:200px">Returned Fields</div>          |
| --------------- | --------------------------------------------- |
| `NO_PI` | Returns partial session objects without personal information. This means the following fields are excluded: `participants`, `location`, `calendarConference`, and `externalCalendarOverrides`.| 
| `ALL_PI` | Returns complete session objects including personal information. This requires the Read Bookings Calendar - Including Participants or the Manage Bookings Services and Settings or the Manage Business Calendar [permission scope](https://devforum.wix.com/kb/en/article/available-permissions).|

> __Notes__:
> + `NO_PI` is the default if you don't pass a value for `fieldsets`.
> + If you pass both `NO_PI` and `ALL_PI` in the same call, complete session objects are returned.