SortOrder: 4
# Order 

## What is Order API of a Paid Plan?
The Order entity includes all the details of Paid Plans Orders and their status.

## Order Status
Order can have one of the following statuses:
* ORDER_STATUS_UNDEFINED - status undefined
* PENDING - order has been purchased offline but it's start date is in the future - it is not valid yet
* ACTIVE - order is active
* CANCELED - order has been canceled
* EXPIRED - order has expired and is no longer active
* PENDING_CANCELLATION - the site owner has selected to discontinue (cancel) the order, but the plan service remains 
active until it’s the end of the current payment period
