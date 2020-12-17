SortOrder: 0
## About This API
The main scope of the service is customer cart management. With these services you can
 * Produce a cart created event
 * Produce a cart completed event
 * Get cart by Id
 * Get my cart - the current visitor in the site
 * Get cart checkout URL
 
 
*Note: Write operations are not supported at this time*

## Permissions

Get cart by Id - The API requires `WIX_STORES.READ_CARTS`
Get cart checkout URL - The API requires `WIX_STORES.READ_CARTS`


## Usage Example - Monitoring abandoned carts
1. Listen to `CartCreatedEvent`.
2. Register the cart to a scheduling service.  
   If the buyer did not checkout with the above cart after 1 hour, the cart will become *Abandoned*.
3. Listen to `CartComlpletedEvent`.  
   If the customer completes his purchase when cart is *Abandoned*, the status will change to *Recovered*.  
   If the customer completes his purchase *before* 1 hour has passed, the status will change to *Completed*.
