# Supported session recurrence rules


A recurrence rule (RRULE) defines how a session recurs. The `recurrence` 
object is only present for recurring sessions, as defined in 
[iCalendar RFC 5545](https://icalendar.org/iCalendar-RFC-5545/3-3-10-recurrence-rule.html).

Supported keywords and values:

| <div style="width:80px">Keyword</div> | <div style="width:250px">Description</div> | <div style="width:230px">Supported values</div> | <div style="width:150px">Required/Optional</div> |
|---------|-------------|------------------|---------------------|
| `FREQ` | Frequency at which the session recurs. | `DAILY`, `WEEKLY`, `MONTHLY` | Required. |
| `INTERVAL` | Frequency interval. For example, `FREQ=WEEKLY` and `INTERVAL=2` mean that a session recurs once every 2 weeks. | Defaults to `1`. | Optional.|
| `UNTIL` | End date and time of the recurrence in UTC time. | | Optional.|
| `BYDAY` | Day of the week the event recurs. | `MO`, `TU`, `WE`, `TH`, `FR`, `SA`, `SU` | Required.|