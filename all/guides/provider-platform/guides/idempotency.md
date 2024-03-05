SortOrder: 3
# Idempotency

Idempotency, when applied to HTTP endpoints, means that a call can be made multiple times with a particular set of data, but only the first call has the intended effect. Subsequent calls with the same data don't cause any change. This property allows for safe retries when calls are interrupted due to network issues. Wix expects calls to some endpoints implemented by PSPs to be idempotent. For each endpoint's idempotency details, see the following:

+ [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/processing-payments#idempotency)
+ [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/processing-refunds#idempotency)
