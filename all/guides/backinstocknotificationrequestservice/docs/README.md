SortOrder: 0
# Back In Stock Notification Request Service

## About This API
With this service you can manage back in stock notification requests.

Use this API to:
1. Create BackInStockNotificationRequest
2. Get a specific BackInStockNotificationRequest
3. Query BackInStockNotificationRequests using [api query language](https://dev.wix.com/api/rest/getting-started/api-query-language).
4. Delete a specific BackInStockNotificationRequest
5. Move BackInStockNotificationRequest to status NOTIFICATION_SENT (relevant for manual flow)
6. Report that specific item is back in stock (in case when `catalog_reference` parameter is present) or BackInStockNotificationRequests with given
   statuses can be resolved (in case when `request_ids` parameter is present)

# Back In Stock Settings Service

## About This API
With these service you can manage back in stock notification settings.

Use this API to:
1. Enable BackInStockNotificationRequest collection
2. Disable BackInStockNotificationRequest collection
3. Get current notification settings

## Usage Example Automation Flow

1. UoU creates BackInStockNotificationRequest, which references specific catalog item.  
    1.1. Site owner receives notification about new BackInStockNotificationRequest to chat message with UoU and his email.
2. Requested catalog item becomes available (by inventory update or any other way)
3. BackInStockNotificationRequestService triggers preconfigured automation event which initiates notification to UoU via email.  
    3.1. UoU receives email notification about item being back in stock.  
    3.2. Site owner receives notification about sent notification (via chat with UoU)
4. BackInStockNotificationRequest is moved to status `NOTIFICATION_SENT` and won't trigger other notifications for any item availability changes

## Usage Example: Manual Flow

1. UoU creates BackInStockNotificationRequest, which references specific catalog item.  
    1.1. Site owner receives notification about new BackInStockNotificationRequest to chat message with UoU and his email.  
2. Site owner manually notifies UoU about item being back in stock.
   Notification channel and notification time is site owner's decision and is not driven by inventory events.
3. Site owner marks BackInStockNotificationRequest as done. BackInStockNotificationRequest is moved to status `NOTIFICATION_SENT`