SortOrder: 6
# Fieldset

Fieldset is a unified control for additional data that can be returned in the response. 

## Event fieldset

By default, the `event` data in the response returns `id`, `title`, `slug`, `location`, `scheduling`, `tags`, `created`, `modified`, `status`, `guestListConfig`, `instanceId`, `userId` and `language` fields. 
The response will also include following parameters based on the fieldsets provided in the request.


 | Fieldset                    | Fields                                         |
 |-----------------------------|------------------------------------------------|
 | DETAILS                     | `description`, `mainImage` and `calendarLinks` |
 | TEXTS                       | `about`                                        |
 | REGISTRATION                | `registration`                                 |
 | URLS                        | `eventPageUrl`                                 |
 | FORM                        | `form`                                         |
 | DASHBOARD                   | `dashboard`                                    |
 | ONLINE_CONFERENCING_SESSION | `onlineConferencing`                           |
 | AGENDA                      | `agenda`                                       |
