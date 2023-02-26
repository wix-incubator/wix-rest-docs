SortOrder: 1
# Sessions: Supported Filters

Field support for filters depends on the type of sessions you are querying: session instances of type `EVENT`, session instances of all types, or recurring session definitions.
They also depend on whether `includeExternal` is `true`.

## Wix Calendar session instances of type `EVENT` (Default)

The following table shows field support for filters for session instances of type `EVENT` when `includeExternal` is `false`:

| Logical Operators |
| ----------------- |
| `$and`, `$or`, `$not` |

| Field           | Supported Filters                             |
| --------------- | --------------------------------------------- |
| `scheduleId` | `eq`, `ne`, `in` |
| `scheduleOwnerId` | `eq`, `ne`, `in` |
| `scheduleOwnerName` | `eq`, `ne`, `in` | 
| `affectedSchedules` | `exists` | 
| `affectedSchedules.scheduleId` | `hasSome`, `hasAll` | 
| `affectedSchedules.transparency` | `hasSome`, `hasAll` | 
| `affectedSchedules.scheduleOwnerId` | `hasSome`, `hasAll` | 
| `affectedSchedules.scheduleOwnerName` | `hasSome`, `hasAll` | 
| `title` | `eq`, `ne`, `in`, `startsWith` | 
| `tags` | `hasSome`, `hasAll` | 
| `location` | `exists` | 
| `location.locationType` | `eq`, `ne`, `in` | 
| `location.customAddress` | `exists` | 
| `location.customAddress.formattedAddress` | `eq`, `ne`, `in`, `startsWith` | 
| `location.businessLocation` | `exists` | 
| `location.businessLocation.id` | `eq`, `ne`, `in` | 
| `location.businessLocation.name` | `eq`, `ne`, `in`, `startsWith` | 
| `location.businessLocation.address.formattedAddress` | `eq`, `ne`, `in`, `startsWith` | 
| `capacity` | `eq`, `ne`, `gt`, `lt`, `gte`, `lte`, `exists` | 
| `remainingCapacity` | `eq`, `ne`, `gt`, `lt`, `gte`, `lte` |
| `numberOfParticipants` | `eq`, `ne`, `gt`, `lt`, `gte`, `lte` | 
| `participants.id` | `hasSome`, `hasAll` | 
| `participants.contactId` | `hasSome`, `hasAll` | 
| `participants.approvalStatus` | `hasSome`, `hasAll` | 
| `inheritedFields` | `hasSome`, `hasAll` | 
| `recurringSessionId` | `eq`, `ne`, `in`, `exists` |
| `calendarConference` | `exists` |
| `calendarConference.id` | `eq`, `ne`, `in` | 
| `calendarConference.externalId` | `eq`, `ne`, `in` | 
| `calendarConference.providerId` | `eq`, `ne`, `in` | 
| `instanceOfRecurrence` | `eq`, `ne`, `in`, `exists` | 

## Session instances of all types

The following table shows field support for filters for session instances of all types. When `includeExternal` is `true` this table always applies, even if you only query session instances of type `EVENT`:

| Logical Operators |
| ----------------- |
| `$and` |

| Field | Supported Filters  |
| ----- | ------------------ |
| `scheduleId` | `eq`, `in` | 
| `affectedSchedules.scheduleId` | `hasSome`, `hasAll` | 
| `tags` | `hasSome` |
| `location.locationType` | `eq`, `in` |
| `location.businessLocation.id` | `eq`, `in` |
| `participants.contactId` | `hasSome` |
| `recurringSessionId` | `eq`, `in` |
| `calendarConference` | `exists` |

## Recurring sessions

The following table shows field support for filters for recurring session definitions:

| Field           | Supported Filters                             |
| --------------- | --------------------------------------------- |
| `scheduleId` | `eq`, `in` |

To learn about working with _Query_ endpoints in general, see
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language).