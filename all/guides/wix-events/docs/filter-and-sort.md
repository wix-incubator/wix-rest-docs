SortOrder: 5
# Filter and Sort

Select endpoints allow sorting results by field. Use `field:asc` to sort results in **ascending** order, and `field:desc` to sort in **descending** order.

For example, to sort events by start date in ascending order, and then by modification date in descending order: 

```
?sort=start:asc,modified:desc
```

or 

```json
"sort": "start:asc,modified:desc"
```

Refer to the following tables to check which fields support sorting.

## List & Query Events
[//]: # (https://bo.wix.com/wix-docs/rest/events/wix-events/filter-and-sort#events_wix-events_filter-and-sort_list-query-event)

| Field            | Description       | Query Filter Operators                                  | Sorting | Facets  |
|------------------|-------------------|---------------------------------------------------------|---------|---------|
| created          | Creation date     | $eq,$ne,$lt,$lte,$gt,$gte,$hasSome                      | Allowed |         |
| modified         | Modification date | $eq,$ne,$lt,$lte,$gt,$gte,$hasSome                      | Allowed |         |
| start            | Start date        | $eq,$ne,$lt,$lte,$gt,$gte,$hasSome                      | Allowed |         |
| end              | End date          | $eq,$ne,$lt,$lte,$gt,$gte,$hasSome                      | Allowed |         |
| title            |                   | $eq,$ne,$lt,$lte,$gt,$gte,$hasSome,$contains,$urlized   | Allowed |         |
| slug             | URL slug          | $eq,$ne,$lt,$lte,$gt,$gte,$hasSome,$contains,$urlized   | Allowed |         |
| status           |                   | $eq,$ne,$hasSome                                        |         | Allowed |
| eventId          |                   | $eq,$ne,$hasSome                                        |         |         |
| userId           |                   | $eq,$ne,$hasSome                                        |         |         |
| categoryId       |                   | $eq,$ne,$hasSome                                        |         |         |
| categoryState    |                   | $eq,$ne,$hasSome                                        |         | Allowed |        
| recurrenceStatus |                   | $eq,$ne,$hasSome                                        |         | Allowed |
| recurringGroupId |                   | $eq,$ne,$hasSome                                        |         |         |

## List & Query RSVPs
[//]: # (https://bo.wix.com/wix-docs/rest/events/wix-events/filter-and-sort#events_wix-events_filter-and-sort_list-query-rsvp)

| Field        | Description             | Query Filter Operators                                           | Sorting | Facets  |
|--------------|-------------------------|------------------------------------------------------------------|---------|---------|
| created      | Creation date           |                                                                  | Allowed |         |
| modified     | Modification date       |                                                                  | Allowed |         |
| name         | Guest name              |                                                                  | Allowed |         |
| score        | Search phrase relevance |                                                                  | Allowed |         |
| email        | Guest email             |                                                                  | Allowed |         |
| totalGuests  | Guest count             |                                                                  | Allowed |         |
| status       | Guest response          | $eq,$ne,$hasSome                                                 | Allowed | Allowed |
| rsvpId       |                         | $eq,$ne,$hasSome                                                 | Allowed |         |
| eventId      |                         | $eq,$ne,$hasSome                                                 |         | Allowed |

## List & Query Available Tickets
[//]: # (https://bo.wix.com/wix-docs/rest/events/wix-events/filter-and-sort#events_wix-events_filter-and-sort_list-query-available-tickets)

| Field              | Description             | Query Filter Operators                                            | Sorting |
|--------------------|-------------------------|-------------------------------------------------------------------|---------|
| created            | Creation date           |                                                                   | Allowed |
| price              |                         |                                                                   | Allowed |
| orderIndex         |                         |                                                                   | Allowed |
| ticketDefinitionId |                         | $eq,$ne,$hasSome,$in                                              |         |
| eventId            |                         | $eq,$ne,$hasSome,$in                                              |         |
| name               |                         | $eq,$ne,$lt,$lte,$gt,$gte,$hasSome,$in,$contains,$urlized         | Allowed |

## List Tickets
[//]: # (https://bo.wix.com/wix-docs/rest/events/wix-events/filter-and-sort#events_wix-events_filter-and-sort_list-tickets)

| Field         | Description             | Sorting | Facets  |
|---------------|-------------------------|---------|---------|
| ticketNumber  |                         | Allowed |         |
| orderStatus   | Order status            | Allowed |         |
| price         | Ticket price            | Allowed |         |
| orderFullName | Buyer name              | Allowed |         |
| guestFullName | Guest name              | Allowed |         |
| score         | Search phrase relevance | Allowed |         |
| free          |                         |         | Allowed |
| archived      |                         |         | Allowed |
| checkedIn     |                         |         | Allowed |
| eventId       |                         |         | Allowed |


## List Ticket Definitions
[//]: # (https://bo.wix.com/wix-docs/rest/events/wix-events/filter-and-sort#events_wix-events_filter-and-sort_list-ticket-definitions)

| Field         | Description             | Sorting |  Facets |
|---------------|-------------------------|---------|---------|
| created       | Creation date           | Allowed |         |
| modified      | Modification date       | Allowed |         |
| orderIndex    |                         | Allowed |         |
| saleStatus    | Ticket sale status      |         | Allowed |
| saleStartDate | Ticket sale start date  | Allowed |         |
| saleEndDate   | Ticket sale end date    | Allowed |         |
| state         | Ticket state flags      |         |         |


## Query Ticket Definitions
[//]: # (https://bo.wix.com/wix-docs/rest/events/wix-events/filter-and-sort#events_wix-events_filter-and-sort_query-ticket-definitions)

| Field              | Description              | Query Filter Operators                                            | Sorting |  Facets |
|--------------------|--------------------------|-------------------------------------------------------------------|---------|---------|
| created            | Creation date            |                                                                   | Allowed |         |
| price              |                          |                                                                   | Allowed |         |
| orderIndex         |                          |                                                                   | Allowed |         |
| ticketDefinitionId |                          | $eq,$ne,$hasSome,$in                                              |         |         |
| eventId            |                          | $eq,$ne,$hasSome,$in                                              |         |         |
| name               |                          | $eq,$ne,$lt,$lte,$gt,$gte,$hasSome,$in,$contains,$urlized         | Allowed |         |
| saleStatus         | Ticket sale status       | $eq,$ne,$hasSome,$in                                              |         | Allowed |
| saleStartDate      | Ticket sale start date   | $lt,$gt                                                           | Allowed |         |
| saleEndDate        | Ticket sale end date     | $lt,$gt                                                           | Allowed |         |
| hidden             | Whether ticket is hidden | $eq,$ne,$hasSome,$in                                              |         | Allowed |

## List Orders
[//]: # (https://bo.wix.com/wix-docs/rest/events/wix-events/filter-and-sort#events_wix-events_filter-and-sort_list-orders)

| Field            | Description             | Sorting | Facets  |
|------------------|-------------------------|---------|---------|
| created          | Creation date           | Allowed |         |
| name             | Guest name              | Allowed |         |
| score            | Search phrase relevance | Allowed |         |
| orderNumber      |                         | Allowed |         |
| status           | Order status            |         | Allowed |
| archived         |                         |         | Allowed |
| fullyCheckedIn   |                         |         | Allowed |

 ## Query Policies
 [//]: # (https://bo.wix.com/wix-docs/rest/events/wix-events/filter-and-sort#events_wix-events_filter-and-sort_query-policies)

| Field            | Query Filter Operators      |
|------------------|-----------------------------|
| policyId         | $eq,$ne,$hasSome,$contains  |         
| eventId          | $eq,$hasSome                |         

## List Agenda Items
| Field            | Description             | Sorting | Facets  |
|------------------|-------------------------|---------|---------|
| stage_name       |                         |         | Allowed |
| track_name       |                         |         | Allowed |
| host_name        |                         |         | Allowed |


[//]: # (Full list of operators for reference: $eq,$ne,$lt,$lte,$gt,$gte,$hasSome,$in,$contains,$startsWith,$endsWith,$urlized,$exists)
