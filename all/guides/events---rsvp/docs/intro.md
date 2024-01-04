SortOrder: 0
# Introduction

#### Registration (RSVP)

When a guest responds to a RSVP **Registration Form** then a new RSVP 
is created *and a confirmation email is sent*.

Rsvp registration settings can be configured in Business Manager.
Rsvp options can be Yes only or Yes and No. 

Limiting the number of guests is optional. Once the guest list is
full the registration is closed, unless Waitlist is enabled.

*If user RSVP to Waitlist, he will get a email once 
additional space in event is available*

### API

#### RSVP management

* [RsvpManagement.Create][rsvp-management-create] - creates RSVP and associates a contact of the site.
The *Form response* has to be sent according to *Registration Form* input fields when creating RSVP or at checkout.
If site member is creating a RSVP the site member id is associated.  
To change existing RSVP - use dashboard.
* [RsvpManagement.List][rsvp-management-list] - a lightweight RSVPs listing service with basic filter support.
* [RsvpManagement.Query][rsvp-management-query] - a service for listing RSVPs supporting structurized queries.
* [RsvpManagement.Get][rsvp-management-get] - a service to get a single rsvp.
* [RsvpManagement.Update][rsvp-management-update] - a service to update rsvp.
* [RsvpManagement.Delete][rsvp-management-delete] - a service to delete rsvp.
* [RsvpManagement.CheckIn][rsvp-management-check-in] - a service to check-in rsvp.
* [RsvpManagement.DeleteCheckIn][rsvp-management-delete-check-in] - a service to delete rsvp check-in.

[rsvp-management-create]: ../reference/rsvp/.wix.events.rsvp.-rsvp-management.-create
[rsvp-management-list]: ../reference/rsvp/.wix.events.rsvp.-rsvp-management.-list
[rsvp-management-query]: ../reference/rsvp/.wix.events.rsvp.-rsvp-management.-query
[rsvp-management-get]: ../reference/rsvp/.wix.events.rsvp.-rsvp-management.-get
[rsvp-management-update]: ../reference/rsvp/.wix.events.rsvp.-rsvp-management.-update
[rsvp-management-delete]: ../reference/rsvp/.wix.events.rsvp.-rsvp-management.-delete
[rsvp-management-check-in]: ../reference/rsvp/.wix.events.rsvp.-rsvp-management.-check-in
[rsvp-management-delete-check-in]: ../reference/rsvp/.wix.events.rsvp.-rsvp-management.-delete-check-in
