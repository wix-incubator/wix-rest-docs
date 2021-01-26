SortOrder: 2
# Scope Values

Wix site owners can define the coupon to apply to a specific product, a collection of products, or to all of their products within a specific Wix Business Solution. 

Coupons are available for the following Wix business solutions:

- Wix Stores
- Wix Bookings
- Wix Events

When creating a coupon via API, you will need to apply a coupon scope. The scope should include:
* Namespace (required)
* Group (optional - if not listed, the coupon will apply to all products/services/events in the namespace)
* Entity ID - (required only when Group is listed)

## Wix Stores

| Namespace | Group | Entity ID | Result|
| --- | --- | --- | --- |
| stores|N/A|N/A|Coupon applies to all products |
| stores|product|product ID|Coupon applies to the specific product with the provided ID |
| stores|collection|collection ID|Coupon applies to the specific collection with the provided ID |

## Wix Bookings

| Namespace | Group | Entity ID | Result|
| --- | --- | --- | --- |
| bookings|N/A|N/A|Coupon applies to all services |
| bookings|service|service ID|Coupon applies to the specific service with the provided ID |

## Wix Events

| Namespace | Group | Entity ID | Result|
| --- | --- | --- | --- |
| events|event|N/A|Coupon applies to all events |
| events|event|event ID|Coupon applies to the specific event with the provided ID |
| events|ticket|N/A|Coupon applies to all tickets |
| events|ticket|ticket ID|Coupon applies to the specific ticket with the provided ID |
