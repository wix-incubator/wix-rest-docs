SortOrder: 1
# Order

## Order Status

Order can have one of the following statues:

- `UNDEFINED`
- `INITIALIZED` - meaning the order was created
- `IN_PROCESS` - meaning payment process for this order has started OR has been successfully completed
- `EXPIRED` - meaning payment process for this order didn't finish in time
- `NOT_APPROVED` - meaning payment process has failed (due to any of the reasons)
- `SUBSCRIPTION_PENDING` - meaning recurring payment is not active yet, waiting for the first payment
- `SUBSCRIPTION_ACTIVE` - meaning recurring payment is active
- `SUBSCRIPTION_CANCELLED` - meaning recurring payment was cancelled by user
- `SUBSCRIPTION_FINISHED` - meaning the total billing cycles for the optional trial and the regular payment periods was completed (not yet supported)

### Order Status Flow (one-time)

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-pay/OrdersnapshotStatusFlowchartOneTime.png)

### Order Status Flow (recurring)

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-pay/OrdersnapshotStatusFlowchartRecurring.png)

## Order event hooks

In most cases TPA want to get notifications when something changes with the order. For such cases one must setup an
event hook when [creating an order](/cashier-pay/reference/order/.wix.payment.api.pay.v2.-order-service.-create).

Event hook is either a Web URL (starting with `https://`) or an RPC endpoint (`rpc:${groupId.artifactId}`). In order to
use RPC hook, your TPA must be registered on cashier side as rpc service.

There three types of notifications.

- Order has expired notification.
- Transaction status update notification.
- Subscription status update notification.

### HTTP Notifications

#### Order expired

```json
{
  "type": "ORDER_EXPIRED",
  "expiredOrderEvent": {
    "orderId": "string"
  }
}
```

#### Transaction event

```json
{
  "type": "TRANSACTION",
  "transactionEvent": {
    "transactionId": "string",
    "orderId": "string",
    "verticalOrderId": "string",
    "paymentMethod": "string",
    "provider": "string",
    "transactionStatus": "string",
    "merchantId": "string"
  }
}
```

#### Subscription event

```json
{
  "type": "SUBSCRIPTION_STATUS_CHANGE",
  "subscriptionStatusChangeEvent": {
    "orderId": "string",
    "status": "string"
  }
}
```

