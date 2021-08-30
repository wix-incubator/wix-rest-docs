SortOrder: 0
# About the Resources API

A resource is a business asset like a staff member, a room, or equipment that is needed to provide a service.

Each resource owns a schedule. The schedule defines the resource's availability. You can set up a custom schedule for a resource, use the business's default working hours, or combine the two.

Resources have tags that you can use for grouping. For example, add a `"room"` tag for classroom resources and an `"equipment"` tag for resources like computers and projectors.

There are 2 tags used by the Wix Bookings app:
  + `"staff"`: Resources with the `"staff"` tag appear in the Bookings app's **Staff** page. Resources created using the Wix Bookings UI will be created with the `"staff"` tag.
  + `"business"`: The Bookings app creates a resource with a name and tag value of `"business"`. This resource owns a schedule that contains the operating hours of the business and cannot be deleted. This schedule is used when creating resources that use the business’s operating hours for the resource's working hours.
 
>**Note:** 
>You can have up to 135 active resources and an additional 135 deleted resources.
