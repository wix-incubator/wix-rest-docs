SortOrder: 1
# Supported Filters


[Query Extended Bookings](https://dev.wix.com/api/rest/wix-bookings/bookings-reader-v2/query-extended-bookings) runs with these defaults:

+ sorted by `id` in `ASC` order
+ cursorPaging.limit is `50`

`query.fields` and `query.fieldsets` aren't supported for this endpoint.

The following table shows field support for filters for the booking object:


| Field                                                                       | Supported Filters                             |
|-----------------------------------------------------------------------------| --------------------------------------------- |
| id                                                                          | `eq`, `ne`, `in` |
| bookedEntity.item.slot.sessionId                                            | `eq`, `ne`, `in` |
| bookedEntity.item.slot.serviceId                                            | `eq`, `ne`, `in` |
| bookedEntity.item.slot.scheduleId                                           | `eq`, `ne`, `in` |
| bookedEntity.item.slot.resource.id                                          | `eq`, `ne`, `in` |
| bookedEntity.item.slot.location.id                                          | `eq`, `ne`, `in` |
| bookedEntity.item.slot.location.locationType                                | `eq`, `ne`, `in` |
| bookedEntity.item.schedule.scheduleId                                       | `eq`, `ne`, `in` |
| bookedEntity.item.schedule.serviceId                                        | `eq`, `ne`, `in` |
| bookedEntity.item.schedule.location.id                                      | `eq`, `ne`, `in` |
| bookedEntity.item.schedule.location.locationType                            | `eq`, `ne`, `in` |
| bookedEntity.tags                                                           | `hasSome`, `hasAll` |
| contactDetails.contactId                                                    | `eq`, `ne`, `in` |
| status                                                                      | `eq`, `ne`, `in` |
| paymentStatus                                                               | `eq`, `ne`, `in` |
| selectedPaymentOption                                                       | `eq`, `ne`, `in` |
| createdDate                                                                 | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin` |
| externalUserId                                                              | `eq`, `ne`, `in` |
| createdBy.contactId                                                         | `eq`, `ne`, `in` |
| createdBy.id.appId                                                          | `eq`, `ne`, `in` |
| createdBy.id.wixUserId                                                      | `eq`, `ne`, `in` |
| createdBy.id.memberId                                                       | `eq`, `ne`, `in` |
| createdBy.id.anonymousVisitorId                                             | `eq`, `ne`, `in` |
| startDate                                                                   | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin` |
| endDate                                                                     | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin` |
| updatedDate                                                                 | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin` |
| doubleBooked                                                                | `eq`, `ne` |
| participantsInfo.type.totalParticipants.value                               | `hasSome`, `hasAll` |
| participantsInfo.type.participantsChoices.serviceChoices.choices.optionId       |  `hasSome`, `hasAll` |
| participantsInfo.type.participantsChoices.serviceChoices.choices.choice.custom.value |  `hasSome`, `hasAll` |


You can only specify a filter only once per query. If a filter is provided 
more than once, only the first occurrence affects the returned bookings.

When using filters for dates, you must use [UTC time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).

Bookings belonging to a schedule don't have a `sessionId`. Therefore you 
must use the `sessionId` filter that isn't part of the `query` object to 
filter bookings for courses.

To learn about working with _Query_ endpoints, see
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Sorting and Paging](https://dev.wix.com/api/rest/getting-started/sorting-and-paging),
and [Field Projection](https://dev.wix.com/api/rest/getting-started/field-projection).