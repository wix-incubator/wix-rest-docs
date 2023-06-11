SortOrder: 1
# Sample Flows

This article shares some possible use cases your app could support, as well as a sample flow that could support each use case. This can be a helpful jumping off point as you plan your app's implementation.

## Create staff member-based service variants


Your app can set up staff member-based service variants. This allows the site 
owner to offer customers different service prices depending on which 
staff member is providing the service.

1. Identify the relevant service ID. For example, call 
   [List services](https://dev.wix.com/api/rest/wix-bookings/services/service/list-services) 
   and choose the service you want to create options and variants for.

1. Pass the `serviceId` inside the `scheduleOwnerIds` array in the 
   [List schedules](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/list-schedules) 
   call. This retrieves all schedules related to the service.

1. Identify the active schedule from retrieved schedules. The active schedule 
   has a `status` of `CREATED` in contrast to all other retrieved schedules.

1. Save the `scheduleOwnerId` from the active schedule's 
   `availability.linkedSchedules` array. These are the IDs of the staff members 
   providing this service.

1. Call [Create Service Options and Variants](https://dev.wix.com/api/rest/wix-bookings/service-options-and-variants/create-service-options-and-variants) 
   and pass the relevant `serviceId`, `STAFF_MEMBER` (in the `options.type` field), 
   as well as the IDs of all staff members providing the service in the 
   `variants.choices` array. You can specify the price for each staff member 
   in `variants.price`.


## Create service variants based on the booked equipment 

Your app can set up service variants based on the booked equipment. This allows 
them to offer customers different service prices depending on what 
equipment the customer has booked.

1. Identify the relevant service ID. For example, call 
   [List services](https://dev.wix.com/api/rest/wix-bookings/services/service/list-services) 
   and choose the service you want to create options and variants for.

1. Call [Create Service Options and Variants](https://dev.wix.com/api/rest/wix-bookings/service-options-andvariants/create-service-options-and-variants) 
   and pass the relevant `serviceId`, `CUSTOM` (in the `options.type` field), 
   `Equipment` (in the `options.customData.name` field), as well as all 
   supported equipment in the `options.customData.choices` array. Make sure to 
   also pass all supported `variants`. You can specify the price for each 
   variant in `variants.price`.
