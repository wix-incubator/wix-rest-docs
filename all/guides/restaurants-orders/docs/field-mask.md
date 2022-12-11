SortOrder: 2
# Field Masks

The [List Orders](https://dev.wix.com/api/rest/wix-restaurants/orders/list-orders) 
and [Get Order](https://dev.wix.com/api/rest/wix-restaurants/orders/get-order) endpoints 
allow you to return a partial `order` object
including only the fields you request.
To do this, you can use projected fields in the `fieldMask.paths` array in your request.

## Supported Projected Fields

The following fields can be returned in a partial object
by specifying them in `fieldMask.paths`:

> **Note:**
> `id` and `revision` are always returned,
> even if you don’t include them in the `fieldMask.paths` array in your request.

- `id` 
- `revision`
- `created_date`
- `updated_date`
- `comment`
- `currency`
- `status`
- `line_items`
- `discounts`  
- `payments`
- `activities` 
- `channel_info`
- `channel_info.type`  
- `coupon.code`
- `coupon.id`
- `fulfillment`  
- `fulfillment.type`
- `fulfillment.promised_time`
- `fulfillment.asap`
- `fulfillment.delivery_details`
- `fulfillment.delivery_details.charge`
- `fulfillment.delivery_details.address`
- `fulfillment.delivery_details.address.formatted`
- `fulfillment.delivery_details.address.country`
- `fulfillment.delivery_details.address.city`
- `fulfillment.delivery_details.address.street`
- `fulfillment.delivery_details.address.street_number`
- `fulfillment.delivery_details.address.apt`
- `fulfillment.delivery_details.address.floor`
- `fulfillment.delivery_details.address.entrance`
- `fulfillment.delivery_details.address.zip_code`
- `fulfillment.delivery_details.address.country_code`
- `fulfillment.delivery_details.address.approximate`
- `fulfillment.delivery_details.address.comment`
- `fulfillment.delivery_details.address.address_line2`
- `fulfillment.delivery_details.address.on_arrival`
- `fulfillment.delivery_details.address.location`
- `fulfillment.delivery_details.address.location.latitude`
- `fulfillment.delivery_details.address.location.longitude` 
- `fulfillment.pickup_details`
- `fulfillment.pickup_details.fee`
- `fulfillment.pickup_details.curbside`
- `fulfillment.pickup_details.curbside.info`
- `fulfillment.dine_in_details`
- `fulfillment.dine_in_details.label`
- `fulfillment.dine_in_details.value`
- `customer`
- `customer.first_name`
- `customer.last_name`
- `customer.phone`
- `customer.email`
- `customer.contact_id`
- `customer.member_id`
- `customer.visitor_id`
- `totals` 
- `totals.subtotal`
- `totals.total`
- `totals.delivery`
- `totals.tax`
- `totals.quantity`
- `totals.loyalty_savings`
- `totals.tip`
- `loyalty_info`
- `loyalty_info.reward_id`
- `loyalty_info.applied_amount`
- `loyalty_info.redeemed_points`
- `loyalty_info.transaction_id`
- `loyalty_info.estimated_account_balance`
- `loyalty_info.estimated_points_earned`
- `loyalty_info.reward_revision`
