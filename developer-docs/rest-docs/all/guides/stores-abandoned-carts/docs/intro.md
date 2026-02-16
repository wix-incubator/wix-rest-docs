SortOrder: 0
# Abandon Cart Service

## About This API
With these services you can manage the abandoned cart lifecycle, including:
    * Schedule a time for that cart to be abandoned upon cart creation
    * Fire a cart abandoned event
    * Fire a cart recovered event

Use this API to:
1. Query abandoned carts
2. Get a specific abandoned cart
3. Delete a specific abandoned cart
4. Get notifications (via webhook events) about abandoned & recovered cart

*Note: Write operations are not supported at this time*

## Usage Example - Abandoned Cart Lifecycle
The service listens to each created cart by carts service.   
If the customer completes their purchase *before* 1 hour has passed, the status will change to *Completed*.  
If a customer does not complete their purchase within 1 hour, the cart becomes *Abandoned*.  
When status changes to *Abandoned*, the service will trigger `CartAbandonedEvent`.  
If the customer completes their purchase after the cart is *Abandoned*, the status will be changed to *Recovered*.

#### Learn more about the [service use case](use_case.md)
  
## Permissions

This API requires the following permissions:
1. Query & Get - `WIX_STORES.READ_ABANDONED_CARTS`
2. Delete - `WIX_STORES.DELETE_ABANDONED_CARTS`