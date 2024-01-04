SortOrder: 3
# Fieldset

Fieldset is a unified control for additional data that can be returned in the response. 

## RSVP fieldset

By default, the `rsvps` data returned in the response contains `id`, `eventId`, `contactId` and `memberId` fields. 
The response will also include the following parameters based on the fieldset provided in the request.

 | Fieldset         | Fields                                                                                             |
 |------------------|----------------------------------------------------------------------------------------------------|
 | DETAILS          | `created`, `modified`, `firstName`, `lastName`, `status`, `totalGuests`, `guests` and `anonymized` |
 | FORM             | `rsvpForm`                                                                                         |
 | CONTACT_DETAILS  | `email`                                                                                            |
