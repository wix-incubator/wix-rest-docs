SortOrder: 13
### Google Pay payment

1. Wix initiates a `$10 US` payment with Google Pay and sends a request.

```bash
curl -X POST https://psp.example.com/sale \
 -H 'Content-Type: application/json' \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "wixMerchantId": "333333-3333-3333-3333-333333333333",
  "wixTransactionId": "000000-0000-0000-0000-000000000000",
  "paymentMethod": "googlePay",
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
  "paymentMethodData": {
    "googlePay": {
      "pan": "11111111-1111-1111-1111-111111111111",
      "expirationYear": 2025,
      "expirationMonth": 12,
      "authenticationMethod": "CRYPTOGRAM_3DS",
      "cryptogram": "uug1soribziny223gmxmh39gdegwve",
      "accountVerified": true,
      "cardholderAuthenticated": false,
      "eci": "02"
    }
  },
  "offSession": true
}'
```

2. Provider responds with `200` HTTP status code, and a *JSON object*:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "cardDetails": {
    "bin": "444444",
    "lastFour": "4444"
  }
}
```

3. [Submit Event](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) with confirmation:

```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "cardDetails": {
        "bin": "444444",
        "lastFour": "4444"
      }
    }
  }
}'
```

### Google Pay payment with 3DS

1. Wix initiates a `$10 US` payment with Google Pay and sends a request.

```bash
curl -X POST https://psp.example.com/sale \
 -H 'Content-Type: application/json' \
 -H 'JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup' \
 -d '{
  "wixMerchantId": "333333-3333-3333-3333-333333333333",
  "wixTransactionId": "000000-0000-0000-0000-000000000000",
  "paymentMethod": "googlePay",
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
  "paymentMethodData": {
    "googlePay": {
      "pan": "11111111-1111-1111-1111-111111111111",
      "expirationYear": 2025,
      "expirationMonth": 12,
      "authenticationMethod": "PAN_ONLY",
      "accountVerified": true,
      "cardholderAuthenticated": false,
      "eci": "02"
    }
  },
  "offSession": true
}'
```

2. Provider responds with `200` HTTP status code, and a *JSON object*:

```json
{
  "pluginTransactionId": "e89b-12d3-a456-42665",
  "redirectUrl": "https://example.com/redirect-sale-form"
}
```

3. Wix opens a page with `redirectUrl` link.

4. After a buyer confirms the payment, [Submit Event](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) with confirmation:

```bash
curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: <AUTH>' \
 -d '{
  "event": {
    "transaction": {
      "wixTransactionId": "000000-0000-0000-0000-000000000000",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "cardDetails": {
        "bin": "444444",
        "lastFour": "4444"
      }
    }
  }
}'
```
