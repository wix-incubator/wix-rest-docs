SortOrder: 1
# Supported Filters


[Query Sessions](https://dev.wix.com/api/rest/wix-bookings/calendar-v2/sessions/query-sessions) runs with these defaults:

- sorted by `start.timestamp` in `ASC` order
- `cursorPaging.limit` is `50`

> __Note:__ You can't override the default sorting.

The following table shows field support for filters
for the session object:

| Field           | Supported Filters                             |
| --------------- | --------------------------------------------- |
| `scheduleId` | `eq`, `ne`, `in` |
| `scheduleOwnerId` | `eq`, `ne`, `in`, `exists` |
| `affectedSchedules` | `exists` | 
| `affectedSchedules.scheduleId` | `hasSome`, `hasAll` | 
| `affectedSchedules.transparency` | `hasSome`, `hasAll` | 
| `affectedSchedules.scheduleOwnerId` | `hasSome`, `hasAll` | 
| `affectedSchedules.scheduleOwnerName` | `hasSome`, `hasAll` | 
| `title` | `eq`, `ne`, `in`, `exists`, `startsWith` | 
| `tags` | `hasSome`, `hasAll` | 
| `location` | `exists` | 
| `location.locationType` | `eq`, `ne`, `in`, `exists`, `startsWith` | 
| `location.customAddress` | `exists` | 
| `location.customAddress.formattedAddress` | `eq`, `ne`, `in`, `exists`, `startsWith` | 
| `location.businessLocation` | `exists` | 
| `location.businessLocation.id` | `eq`, `ne`, `in`, `exists` | 
| `location.businessLocation.name` | `eq`, `ne`, `in`, `exists`, `startsWith` | 
| `location.businessLocation.address.formattedAddress` | `eq`, `ne`, `in`, `exists`, `startsWith` | 
| `capacity` | `eq`, `ne`, `gt`, `lt`, `gte`, `lte`, `exists` | 
| `remainingCapacity` | `eq`, `ne`, `gt`, `lt`, `gte`, `lte`, `exists` |
| `rate` | `exists` |  
| `rate.priceText` | `eq`, `ne`, `in`, `exists`, `startsWith` | 
| `notes` | `eq`, `ne`, `in`, `exists`, `startsWith` | 
| `numberOfParticipants` | `eq`, `ne`, `gt`, `lt`, `gte`, `lte` | 
| `participants` | `exists` | 
| `participants.id` | `hasSome`, `hasAll` | 
| `participants.contactId` | `hasSome`, `hasAll` | 
| `participants.approvalStatus` | `hasSome`, `hasAll` | 
| `inheritedFields` | `hasSome`, `hasAll` | 
| `recurringSessionId` | `eq`, `ne`, `in`, `exists` | 
| `calendarConference.id` | `eq`, `ne`, `in`, `exists` | 
| `calendarConference.externalId` | `eq`, `ne`, `in`, `exists` | 
| `calendarConference.providerId` | `eq`, `ne`, `in`, `exists` | 
| `instanceOfRecurrence` | `eq`, `ne`, `in`, `exists` | 
| `scheduleOwnerName` | `eq`, `ne`, `in`, `exists` | 


To learn about working with _Query_ endpoints in general, see
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language)
and [Sorting and Paging](https://dev.wix.com/api/rest/getting-started/pagination).