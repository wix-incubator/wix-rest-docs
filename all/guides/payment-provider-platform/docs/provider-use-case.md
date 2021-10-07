SortOrder: 2
# Use cases
This page explores some common use cases of how Wix interacts with provider's app/service during processing payments.

The following examples describe use cases:
1. Successful payment via a hosted page
2. Refund a payment

## Successful transaction via a hosted page
1. Wix sends a request with `createTransaction` endpoint information to the provider
2. Provider returns the URL to Wix: for hosted page/wallet -> redirect URL Plugin transaction ID
4. Wix redirects the buyer to the provider's hosted page
5. Buyer completes transaction
6. Provider redirects buyer to the succsessful or error page
6. Provider's system sends a notification to provider's web service about the result of the transaction
7. Provider submits event with the results back to Wix (webhook)

## Refund payment (directly via Wix)
1. Wix sends request for the refund data to provider
2. Provider processes payment and sends the final status of the refund back to Wix via submits event (webhook)