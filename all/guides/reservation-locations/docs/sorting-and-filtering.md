SortOrder: 1
# Reservation Locations: Supported Filters and Sorting

The following table shows field support for filters and sorting
for the Reservation Location object:

| Field                                         | Supported Filters                                   | Sortable  |
| --------------------------------------------- | --------------------------------------------------- | --------- |
| `id`                                          | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `location.id`                                | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.onlineReservations.seatPacing.number` | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `configuration.onlineReservations.seatPacing.enabled` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.onlineReservations.partyPacing.number` | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `configuration.onlineReservations.partyPacing.enabled` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.onlineReservations.partySize.min` | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `configuration.onlineReservations.partySize.max` | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `configuration.onlineReservations.minimumReservationNotice.number` | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `configuration.onlineReservations.minimumReservationNotice.unit` | `$eq`, `$ne`, `$in`, `$nin`                        |           |
| `configuration.onlineReservations.defaultTurnoverTime` | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `configuration.onlineReservations.turnoverTimeRules` |                     `$isEmpty`, `$exists`                             |  |
| `configuration.onlineReservations.businessSchedule.periods` |                    `$isEmpty`, `$exists`                          |  |
| `configuration.onlineReservations.businessSchedule.specialHourPeriod` |                `$isEmpty`, `$exists`                       |  |
| `configuration.onlineReservations.showPhone`  | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.onlineReservations.onlineReservationsEnabled` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.onlineReservations.manualApproval.enabled` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.reservationForm.submitMessage`  | `$eq`, `$ne`, `$in`, `$nin`, `$startsWith`         |           |
| `configuration.reservationForm.policiesEnabled` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.reservationForm.termsAndConditions.enabled` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.reservationForm.privacyPolicy.enabled` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.reservationForm.customFieldDefinitions` |                       `$isEmpty`, `$exists`                     |  |
| `configuration.reservationForm.lastNameRequired` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.reservationForm.emailRequired` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.reservationForm.emailMarketingCheckbox.enabled` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `configuration.reservationForm.emailMarketingCheckbox.checkedByDefault` | `$eq`, `$ne`, `$in`, `$nin`, `$exists`     |           |
| `configuration.myReservationsFields`          |                               `$isEmpty`, `$exists`              | |
| `configuration.tableManagement.tableDefinitions` |                                  `$isEmpty`, `$exists`       |  |
| `configuration.tableManagement.deletedTableDefinitions` |                            `$isEmpty`, `$exists`        | |
| `configuration.tableManagement.tableCombinations` |                           `$isEmpty`, `$exists`             |  |
| `createdDate`                                | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `updatedDate`                                | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `revision`                                   | `$eq`, `$ne`, `$lt`, `$le`, `$gt`, `$ge`, `$in`, `$nin` | Sortable  |
| `default`                                    | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |
| `archived`                                   | `$eq`, `$ne`, `$in`, `$nin`, `$exists`             |           |


__Related content:__
[API Query Language](https://dev.wix.com/api/rest/getting-started/api-query-language),
[Query Reservation Locations](https://dev.wix.com/docs/rest/api-reference/wix-restaurants/reservations/reservation-locations/query-reservation-locations)
