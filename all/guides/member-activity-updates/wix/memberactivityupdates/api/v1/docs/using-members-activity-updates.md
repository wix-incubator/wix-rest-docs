SortOrder: 2
## Using member activity updates

### Context

You can organize member activities by the context they happen in. The context can be:

- A site or an application.
- A context inside the application.

### Activity markers

A marker is a timestamp, set by the user, to mark a time reference for, e.g. the read or seen status of a forum post. The marker can refer to any specific container, resource, or individual activity. It only marks a point in time, even if no activities actually took place at that moment.

### Read token

A read token encodes the time when a change operation like marking as seen or read took place.

Read endpoints use the time from the read token to calculate how much time has elapsed since the change.
