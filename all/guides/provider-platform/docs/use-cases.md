SortOrder: 2
# Use cases
This article shares some possible use cases your app can support. You are not limited to these use cases, but they can be a helpful jumping off point as you plan your *Payment Plugin* integration.

The following examples describe flows:
- Redirection-based payment with a hosted page
- Successful full refund initiated by Wix

### Redirection-based payment with a hosted page
Payment service provider can support a *Hosted Page*, where *buyer* selects an actual payment method.
1. Buyer initiates a `$10 US` purchase (transaction) on a merchant's website.
2. Wix sends [Create Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/create-transaction) request to the payment service provider with transaction details. For example:
```bash
curl -X POST https://psp.example.com/sale \
 -H 'Content-Type: application/json' \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "wixMerchantId": "333333-3333-3333-3333-333333333333",
  "wixTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "order": {
    "id": "11111111-1111-1111-1111-111111111111",
    "description": {
      "totalAmount": 1000,
      "currency": "USD",
      "items": [
        {
          "id": "it_1",
          "name": "Digital camera",
          "quantity": 1,
          "price": 1000,
          "description": "Portable digital camera",
          "category": "physical"
        }
      ],
      "buyerInfo": {
        "buyerId": "ffc0a971-60cb-4c63-8016-39b1bce41e8d",
        "buyerLanguage": "en"
      }
    },
    "returnUrls": {
      "successUrl": "https://merchant.com/success",
      "errorUrl": "https://merchant.com/error",
      "cancelUrl": "https://merchant.com/cancel",
      "pendingUrl": "https://merchant.com/pending"
    }
  },
  "installments": 1,
  "mode": "live",
}'
```
4. *Payment Plugin* triggers the required flow on its platform, and responds to Wix with a `200` HTTP status code and a *JSON object* with a `redirectUrl` to a "hosted" payment page:
```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```
5. Wix displays the `redirectUrl` to the *buyer*, who proceeds with the payment on the hosted page.
6. *Payment Plugin* redirects the browser to `successUrl`, received in the [Create Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/create-transaction) request, and calls the [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) webhook. For example:
```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
  }
}'
```
7. Wix responds with a `200` HTTP status code, and an empty *JSON object*:
```json
{}
```
8. Transaction is approved on Wix side after the [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) is received by Wix.

### Successful full refund initiated by Wix
1. Buyer requests a refund of a $10 US payment from a site owner.
2. Site owner initiates the refund.
3. Wix calls [Refund Transaction](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/refund-transaction) for a $10 US refund. For example:
```bash
curl -X POST https://psp.example.com/refund \
 -H 'Content-Type: application/json' \
 -H 'Digest: JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "wixTransactionId": "11111111-1111-1111-1111-111111111111",
  "wixRefundId": "33333333-3333-3333-3333-333333333333"
  "pluginTransactionId": "000000-0000-0000-0000-000000000000",
  "merchantCredentials": {
    "client_id": "MerchantClientId",
    "client_secret": "MerchantClientSecret"
  },
  "refundAmount": 1000,
  "mode": "live",
  "reason": "REQUESTED_BY_CUSTOMER"
}'
```
3. Payment Plugin initiates the refund, and responds with a `200` HTTP status code and a *JSON object*:
```json
{
  "pluginRefundId": "22222222-2222-2222-2222-222222222222"
}
```
4. Payment Plugin calls [Submit Event](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/event/submit-event) to notify Wix about the refund status:
```bash
curl -X POST https://www.wixapis.com/payments/v1/provider-platform-events \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "refund": {
      "wixTransactionId": "11111111-1111-1111-1111-111111111111",
      "pluginRefundId": "22222222-2222-2222-2222-222222222222",
      "amount": "1000",
      "wixRefundId": "33333333-3333-3333-3333-333333333333"
    }
  }
}'
```
5. Wix responds with a `200` HTTP status code and an empty *JSON object*:
```json
{}
```
6. Payment (transaction) is fully refunded to buyer.
