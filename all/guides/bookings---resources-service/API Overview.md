SortOrder: 0
# **Resources Service**

The Resources Service allows you to manage *schedule-able assets* in Wix Bookings. A resource is any business asset that can be booked or assigned to a session. Resources often include staff people, rooms and/or locations, and specialized equipment.
Each resource will have its own schedule.

A resource will typically be assigned to an *availability type schedule* (See Schedule documentation for more details). For example, a staff member resource with an *availability type schedule*, will be available for booking based on the free slots on their schedule. The same logic works to manage meeting rooms, based on the room's schedule. 

**Tags system:** You can apply a tag to a resource to group multiple resources together for management or display. 
For example:
A set of resources with the the tag `StaffMember` and another set of resources with the tag `room` can be filtered for by tag based on the data required for display.

We recommend applying tags to resources to categorize staff, rooms, equipment, etc. for easy filtering. 
You can create new tags when creating and updating resources via this API.

## **Usage in Wix Bookings**

In Wix Bookings, all default resources fall into 2 categories:

- A *Staff Member* resource is a service provider, and has its own schedule by which the service (and therefore the staff member) is available for booking. These resources automatically receive the tag `StaffMember` upon creation via the Wix Bookings UI, which cannot be removed.
- A *Business* resource represents the business entity's work schedule. For example, a Yoga Studio and its opening hours. This resource automatically receives the tag `Business` upon creation via the Wix Bookings UI, which cannot be removed.
