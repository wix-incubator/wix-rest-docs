SortOrder: 1
# Filter and Sort

## Guidelines

Read [these guidelines](https://dev.wix.com/api/rest/getting-started/api-query-language) to get more information on how to construct a correct query request with filtering and sorting.

## Query Event Guests

The following table displays what operators can be used with various fields and if sorting is possible.

| Field                          | Query Filter Operators                          | Sorting |
|--------------------------------|-------------------------------------------------|---------|
| createdDate                    | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      | Allowed |
| updatedDate                    | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      | Allowed |
| attendanceStatusUpdatedDate    | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      | Allowed |
| id                             | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   |
| eventId                        | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   |
| rsvpId                         | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   |
| memberId                       | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   |
| contactId                      | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   |
| attendanceStatus               | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   | 
| ticketNumber                   | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   | 
| orderNumber                    | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   | 
| attendanceStatus               | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   | 
| guestType                      | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   | 
| guestDetails.checkedIn         | $eq,$ne,$exists                                 |   N/A   |  
| secondaryLanguageCode          | $eq,$ne,$lt,$lte,$gt,$gte,$in,$nin,$exists      |   N/A   |
| tickets                        | $exists                                         |   N/A   |   

