SortOrder: 1
# Event Guests: Supported Filters and Sorting

The following table shows field support for filters and sorting for the Event Guest object:

| Field                            | Query Filter Operators                                                    | Sortable |
|----------------------------------|---------------------------------------------------------------------------|----------|
| `createdDate`                    | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      | Sortable |
| `updatedDate`                    | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      | Sortable |
| `attendanceStatusUpdatedDate`    | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      | Sortable |
| `id`                             | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          |
| `eventId`                        | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          |
| `rsvpId`                         | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          |
| `memberId`                       | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          |
| `contactId`                      | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          |
| `attendanceStatus`               | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          | 
| `ticketNumber`                   | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          | 
| `orderNumber`                    | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          | 
| `attendanceStatus`               | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          | 
| `guestType`                      | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          | 
| `guestDetails.checkedIn`         | `$eq`, `$ne`, `$exists`                                                   |          |  
| `secondaryLanguageCode`          | `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$nin`, `$exists`      |          |
| `tickets`                        | `$exists`                                                                 |          |   

__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Event Guest Query endpoint](https://dev.wix.com/api/rest/all-apis/event-guests/query-event-guests)