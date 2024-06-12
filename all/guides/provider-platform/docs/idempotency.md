SortOrder: 8
# Idempotency

*Idempotency*, when applied to HTTP endpoints, means a call can be made multiple times with the same *idempotency key* but only the first invocation should have the intended effect. This property allows for safe retries when calls can be interrupted due to network issues.

For the [Create Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/create-transaction) call, it means only the first invocation with particular `wixTransactionId` should trigger a payment and create a corresponding *Transaction* entity with a unique `pluginTransactionId` on the side of a *Payment Plugin*. All subsequent invocations must return the latest state of that *Transaction* regardless of whether the first invocation has been successful or not. If the state changes between invocations, then the latest state should be returned. For example, if the first invocation returns `redirectUrl` but the transaction fails soon after, the second invocation should not return `redirectUrl` but `reasonCode`.

Regarding the [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) call, it means only the first invocation with a particular `wixRefundId` should trigger a refund and create a corresponding *Refund* entity with a unique `pluginRefundId` on the side of a *Payment Plugin*. All subsequent invocations should return the latest state of the *Refund* regardless of whether the first invocation has been successful or not. If the state changes between invocations, then the latest state should be returned.

If the [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) webhook was called to notify Wix about a refund not initiated by Wix, only the first invocation with a particular `pluginRefundId` creates a corresponding *Refund* entity on the Wix side. All subsequent invocations can only update the details of that refund.
