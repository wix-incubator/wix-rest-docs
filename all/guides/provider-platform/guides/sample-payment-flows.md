SortOrder: 8
# Sample Payment Flows
This article shows how to handle payment flows when implementing a [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) endpoint. For general information about this endpoint, see [Processing Payments](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/processing-payments).

The Payment Provider Platform supports the following payment flows:
* [Card payments](#card-payments)
* [Digital wallet payments](#digital-wallet-payments)
* [Redirection-Based payments](#redirection-based-payments)
* [Recurring payments](#recurring-payments)
* [Mail order/telephone order (MOTO) payments](#mail-ordertelephone-order-payments)

The following sections include examples of each payment flow. These examples are based on the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) request body and the [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) request body. The values in these examples are fake. Examples are applicable for both `live` and `sandbox` modes.

## Card payments

Card payments are payments made using a credit or debit card. In the simplest case, card payments are processed without additional buyer input. These payments are either instantly approved or declined, or are in a pending state for a short time while fraud verification is completed. In some cases, card payments require additional buyer input in the form of [3D Secure](https://en.wikipedia.org/wiki/3-D_Secure) verification. In these cases, the PSP must treat the card payment as a redirection-based payment. See [3D Secure Payments](#3d-secure-payments) for more information.

Here are some examples of instant card payments flows:

### Instant approval

1. Wix calls [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction). The total amount for the payment and the credit card details are included in the request body as follows:
    ```javascript
    {
      //...
      "order": {
      //...
        "description": {
          "totalAmount": 1000,
          "currency": "USD"
          //...
        }
      },
      //...
      "paymentMethodData": {
        "card": {
          "number": "4111111111111111",
          "year": 2030,
          "month": 12,
          "cvv": "777",
          "holderName": "John Smith"
        }
      }    
    }
    ```

1. The PSP approves the payment and responds with an HTTP status code of `200`, and this JSON object:
    ```json
    {
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
    ```

1. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):
    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
      "event": {
        "transaction": {
          "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
          "pluginTransactionId": "e89b-12d3-a456-42665"
        }
      }
    }'
    ```

1. Wix marks the payment as approved and responds with an HTTP status code of `200` and an empty JSON object.

### Instant decline

>**Note:** In some cases of instant decline, a PSP may not create a transaction ID. In these cases, the PSP doesn't need to include a `pluginTransactionId` field in the response in step 1 of this flow, and doesn't need to send the webhook in step 2.

1. Wix calls [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction). The remaining card limit isn't enough to cover the payment. The PSP responds with an HTTP status code of `200`, and the following JSON object:
    ```json
    {
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 3019,
      "errorCode": "CARD_LIMIT_EXCEEDED",
      "errorMessage": "Not enough credit left on the card limit for this payment."
    }
    ```

1. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):

    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
      "event": {
        "transaction": {
          "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
          "pluginTransactionId": "e89b-12d3-a456-42665",
          "reasonCode": 3019,
          "errorCode": "CARD_LIMIT_EXCEEDED",
          "errorMessage": "Not enough credit left on the card limit for this payment."
        }
      }
    }'
    ```
1. Wix marks the payment as declined and responds with an HTTP status code of `200` and an empty JSON object.

### Payment is pending and moves to the final state

1. Wix calls [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction). The payment requires fraud verification. The PSP responds with an HTTP status code of `200` and this JSON object:

    ```json
    {
      "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "reasonCode": 5005
    }
    ```

1. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):

    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
      "event": {
        "transaction": {
          "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
          "pluginTransactionId": "e89b-12d3-a456-42665",
          "reasonCode": 5005
        }
      }
    }'
    ```

1. Wix marks the payment as pending and responds with an HTTP status code of `200`, and an empty JSON object.

1. If the fraud verification passes, the PSP sends the following webhook to indicate a successful payment:

    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
      "event": {
        "transaction": {
          "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
          "pluginTransactionId": "e89b-12d3-a456-42665"
        }
      }
    }'
    ```

1. Wix marks the payment as approved and responds with an HTTP status code of `200`, and an empty JSON object.

1. If fraud verification fails, the PSP sends the following webhook:  
    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
      "event": {
        "transaction": {
          "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
          "pluginTransactionId": "e89b-12d3-a456-42665",
          "reasonCode": 5001,
          "errorCode": "RISK_MANAGEMENT_DECLINED",
          "errorMessage": "Risk management declined"
        }
      }
    }'
    ```

1. Wix marks the payment as declined and responds with an HTTP status code of `200` and an empty JSON object.

## Digital wallet payments
The Payment Provider Platform supports payments from digital wallet services such as Google Pay. Digital wallet transaction requests are similar to credit card requests but include additional decrypted payment data. The platform will never send an encrypted digital wallet token such as a Google Pay token as part of a transaction request. Because of this, PSPs never need to contact merchants about these transactions. They should process these requests the same way they process credit card payments. 

In some cases, digital wallet transactions require additional buyer input in the form of [3D Secure](https://en.wikipedia.org/wiki/3-D_Secure) verification. In these cases, the PSP must treat the digital wallet payment as a redirection-based payment. See the examples below for more details.

> **Note:** Currently, the platform only supports instant payment transactions for digital wallets. Recurring payments are not supported.

Here are some examples of sample flows for the digital wallet services currently supported by the platform:

### Google Pay

Google Pay transaction requests include the [decrypted payment details](https://developers.google.com/pay/api/web/guides/resources/sample-tokens#decrypted-payload) from a Google Pay transaction as well other relevant data. These requests never include Card Verification Values (CVV) since these are not supported by Google Pay.

#### Google Pay instant approval

1. Wix calls [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction). The total amount for the payment and the Google Pay payment details are included in the request body as follows:

    ```json
    {
      "wixMerchantId": "fcd2655f-e261-4c5b-8129-72a241461a27",
      "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
      "paymentMethod": "googlePay",
      "merchantCredentials": {
        "client_id": "e89b-12d3-a456-42665",
        "client_secret": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1"
      },
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
      "offSession": true
    }
    ```

1. The PSP approves the payment and responds with an HTTP status code of `200`, and this JSON object:

    ```json
    {
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "cardDetails": {
        "bin": "444444",
        "lastFour": "4444"
      }
    }
    ```

1. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):

    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
      "event": {
        "transaction": {
          "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
          "pluginTransactionId": "e89b-12d3-a456-42665",
          "cardDetails": {
            "bin": "444444",
            "lastFour": "4444"
          }
        }
      }
    }'
    ```

#### Google Pay instant decline

Instant decline Google Pay payments are handled the same way as [instant decline credit card payments](#instant-decline).

#### Google Pay with successful 3DS verification

1. Wix calls [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction). The total amount for the payment and the Google Pay payment details are included in the request body as follows:
    ```json
    {
      "wixMerchantId": "fcd2655f-e261-4c5b-8129-72a241461a27",
      "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
      "paymentMethod": "googlePay",
      "merchantCredentials": {
        "client_id": "e89b-12d3-a456-42665",
        "client_secret": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1"
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
    }
    ```

1. The PSP responds with an HTTP status code of `200`, and this JSON object.  
   The object includes a `redirectUrl` field, whose value is the URL of the PSP's web page where the buyer can complete 3DS verification.

  ```json
  {
    "pluginTransactionId": "e89b-12d3-a456-42665",
    "redirectUrl": "https://example.com/redirect-sale-form"
  }
  ```

1. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window for the buyer to complete verification.

1. If the verification succeeds, the PSP's page redirects the browser to the `successUrl` sent in the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) request. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):
  ```bash
  curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: <AUTH>' \
  -d '{
    "event": {
      "transaction": {
        "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
        "pluginTransactionId": "e89b-12d3-a456-42665",
        "cardDetails": {
          "bin": "444444",
          "lastFour": "4444"
        }
      }
    }
  }'
  ```

  If the verification fails, is canceled, or is pending the PSP's page must redirect to other URLs and send different webhooks, depending on the case. See [Redirection-based payments](#redirection-based-payments) for more details.


## Redirection-based payments

The Payment Provider Platform allows PSPs to support redirection-based payments. In these cases, buyers select a payment method, such as Paypal, during checkout. Wix then redirects the buyer to the PSP's web page to complete the payment. The PSP then redirects the buyer back to Wix. Wix supports a large number of [payment methods](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/payment-methods). If the payment method you need isn't supported, you can implement a hosted-page payment flow. In this case, the buyer is redirected to a page hosted by the PSP where they can select a payment method.

Credit cards that require [3D Secure](https://en.wikipedia.org/wiki/3-D_Secure) verification are also treated as redirection-based payments. See [3D Secure payments](#3d-secure-payments) for more information.

Configure the redirection-based payment methods you support in your app's payment gateway extension in the [Wix Developers Center](https://dev.wix.com). 

>**Note:** Hosted-page payment methods don't support 3D Secure verification or recurring payments.

Here is an example of a redirection-based payment flow:

1. Wix calls [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction).  
   If the payment method selected is supported by Wix, it's included as the value for the `paymentMethod` field in the request body. For hosted-page payments, a string representing the PSP's Wix app ID is included. The request body also includes an `order.returnUrls` field with the URLs of the pages to redirect the buyer to after handling the payment request. Here is a sample request body with the relevant fields highlighted:
    ```javascript
    {
      //...
      "paymentMethod": "paypal",
      "order": {
        //...
        "returnUrls": {
          "successUrl": "https://merchant-site.com/success",
          "errorUrl": "https://merchant-site.com/error",
          "cancelUrl": "https://merchant-site.com/cancel",
          "pendingUrl": "https://merchant-site.com/pending"
        }
      }
    }
    ```
1. The PSP responds with an HTTP status code of `200`, and this JSON object.  
   The object includes a `redirectUrl` field, whose value is the URL of the PSP's web page where the buyer can complete the payment.

    ```json
    {
      "pluginTransactionId": "e89b-12d3-a456-42665",
      "redirectUrl": "https://example.com/redirect-sale-form"
    }
    ```
1. Wix opens the `redirectUrl` in an [iframe](https://en.wikipedia.org/wiki/HTML_element#Frames) or in a browser window for the buyer to complete. There are 4 possible outcomes, depending on the buyer's actions. The PSP must respond to each outcome differently:
     1. **Success:** If the verification succeeds, the PSP's page redirects the browser to the `successUrl` sent in the [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) request. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):
        ```bash
        curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
        -H 'Content-Type: application/json' \
        -H 'Authorization: <AUTH>' \
        -d '{
              "event": {
                "transaction": {
                  "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
                  "pluginTransactionId": "e89b-12d3-a456-42665"
                }
              }
            }'
        ```
      1. **Failure:** If the verification fails, the PSP's page redirects the browser to the `errorUrl` sent in the `Create Transaction` request. The PSP sends a webhook indicating why the payment failed. For example:
          ```bash
          curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
          -H 'Content-Type: application/json' \
          -H 'Authorization: <AUTH>' \
          -d '{
                "event": {
                  "transaction": {
                    "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
                    "pluginTransactionId": "e89b-12d3-a456-42665",
                    "reasonCode": 3012,
                    "errorCode": "INSUFFICIENT_FUNDS",
                    "errorMessage": "Insufficient funds"
                  }
                }
              }'
          ```
      1. **Cancelation:** If the buyer cancels the verification, the PSP's page redirects the browser to the `cancelUrl` sent in the `Create Transaction` request. The PSP sends this webhook:
          ```bash
          curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
          -H 'Content-Type: application/json' \
          -H 'Authorization: <AUTH>' \
          -d '{
                "event": {
                  "transaction": {
                    "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
                    "pluginTransactionId": "e89b-12d3-a456-42665",
                    "reasonCode": 3030,
                    "errorCode": "BUYER_CANCELED",
                    "errorMessage": "Buyer canceled"
                  }
                }
              }'
          ```
      1. **Pending:** If the verification is pending, the PSP's page redirects the browser to the `pendingUrl` sent in the `Create Transaction` request. The PSP sends this webhook with a `5005` reason code:
          ```bash
          curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
          -H 'Content-Type: application/json' \
          -H 'Authorization: <AUTH>' \
          -d '{
                "event": {
                  "transaction": {
                    "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
                    "pluginTransactionId": "e89b-12d3-a456-42665",
                    "reasonCode": 5005
                  }
                }
              }'
          ```

1. In each case, Wix marks the payment appropriately and responds with an HTTP status code of `200` and an empty JSON object.

1. If the payment was pending, the PSP sends a webhook to update the payment as either approved or declined when it's finalized.
   
   Payment approved request:
   ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
      "event": {
        "transaction": {
          "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
          "pluginTransactionId": "e89b-12d3-a456-42665"
        }
      }
    }'
    ```
    Payment declined request:
    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
      "event": {
        "transaction": {
          "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
          "pluginTransactionId": "e89b-12d3-a456-42665",
          "reasonCode": 5001,
          "errorCode": "RISK_MANAGEMENT_DECLINED",
          "errorMessage": "Risk management declined"
        }
      }
    }'
    ```
1. Wix marks the payment as approved or declined and responds with an HTTP status code of `200` and an empty JSON object.


### 3D secure payments
Cards that support [3D Secure](https://en.wikipedia.org/wiki/3-D_Secure) (3DS) verification require buyers to complete an additional verification step when making a payment. This verification step is completed on a web page hosted by the PSP. The flow for handling 3DS payments is similar to the flow for other redirection-based payments. The difference is that the value of `paymentMethod` in the [`Create Transaction`](https://dev.wix.com/api/rest/payment-provider-spi/provider-platform/transaction/create-transaction) request body is `creditCard`. It's up to the PSP to determine if the card supports 3DS verification and send the appropriate redirect response.

## Recurring payments

Recurring payments (also known as subscription payments, automatic payments, or recurring billing) occur when buyers authorize a merchant to charge them repeatedly for goods or services on a prearranged schedule such as monthly, weekly, or annually. In these cases, Wix sends a request to the PSP to set up the recurring payment. The PSP responds with a unique identifier for the recurring payment. Wix uses this identifier to charge the buyer based on an agreed schedule.

The Payment Provider Platform supports these unique identifiers for recurring payments:
* **Network ID:** An ID representing a payment created by credit card networks such as Visa and Mastercard. These IDs are used to represent the recurring payment in the card network. The PSP requests the ID from the credit card network and sends it to Wix.
* **Token:** A token representing a payment created by the PSP. Both the PSP and Wix store the token locally and use it to represent the recurring payment.

The payment processing flow for recurring payments includes these phases: 
+ Setting up an "off-session" payment. This is a payment where a buyer allows a merchant to charge them in certain cases even when the buyer isn't present to confirm the payment, such as a recurring payment.
+ Processing the recurring payments.
 

Here are examples of each phase:
### Off-session payment setup

1. Wix calls [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) with a request to set up a recurring payment.  
   This request looks the same as a credit card payment request, with one difference: it includes a `setupCredentialsOnFile` field whose value is an object with a field called `offSession` whose value is `true`. This flag indicates that Wix is requesting that the PSP set up a recurring payment, not process a one-time payment.
   Here is a sample request body with the relevant fields highlighted:
   ```javascript
   {
    //...
    "paymentMethod": "creditCard",
    //...
    "paymentMethodData" : {
      "card": {
        "number": "4111111111111111",
        "year": 2030,
        "month": 12,
        "cvv": "777",
        "holderName": "John Smith"
      }
    }, 
    "setupCredentialsOnFile": {
      "offSession": true
    }
   }
   ```
1. If the card supports 3D Secure verification, the PSP must redirect the buyer to a 3DS verification page before proceeding. See [3D Secure payments](#3d-secure-payments) for more information.
1. The PSP responds with an HTTP status code of `200`, and a JSON object that includes a `credentialsOnFile` field. The value of this field depends on the type of recurring payment identifier the PSP supports.  
   For network IDs, the response looks like this:
      ```json
      {
        "pluginTransactionId": "e89b-12d3-a456-42665",
        "credentialsOnFile": {
          "cardReference": {
            "networkTransactionId": "NTI-e89b-12d3-a456-42665"
          }
        }
      }
      ```  
    >**Note:** If 3DS verification occurs, the PSP must include the `dsTransactionId` field in the `cardReference` object. This field's value is the ID of the 3DS verification transaction.
    For tokens, the response looks like this:
      ```json
      {
        "pluginTransactionId": "e89b-12d3-a456-42665",
        "credentialsOnFile": {
          "paymentMethodReference": {
            "token": "PMR-e89b-12d3-a456-42665"
          }
        }
      }
      ```
1. The PSP sends a webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event) to confirm the recurring payment setup request.  
    For network IDs, the webhook looks like this: 
      ```bash
      curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: <AUTH>' \
      -d '{
            "event": {
              "transaction": {
                "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
                "pluginTransactionId": "e89b-12d3-a456-42665",
                "credentialsOnFile": {
                  "cardReference": {
                    "networkTransactionId": "NTI-e89b-12d3-a456-42665"
                  }
                }
              }
            }
          }'
      ```  
    For tokens, the webhook looks like this:  
    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
          "event": {
            "transaction": {
              "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
              "pluginTransactionId": "e89b-12d3-a456-42665",
              "credentialsOnFile": {
                "paymentMethodReference": {
                  "token": "PMR-e89b-12d3-a456-42665"
                }
              }
            }
          }
       }'
    ``` 
1. Wix responds with an HTTP status code of `200`, and an empty JSON object.

###  Processing recurring payments

1. Wix calls [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) with a request to charge a recurring payment.  
   This request's `paymentMethod` field has a value of `creditCard`. The request also includes a field called `offSession` whose value is `true`. This flag indicates that Wix is requesting that the PSP charge a recurring payment. The request's `paymentMethodData` field includes different data depending on the type of recurring payment identifier the PSP sent to Wix when the recurring payment was set up.  
   
   For network ID payments: 
      ```javascript
      "paymentMethodData": {
        "card": {
          "number": "4111111111111111",
          "year": 2030,
          "month": 12,
          "networkTransactionId": "NTI-e89b-12d3-a456-42665",
          "dsTransactionId": "DTI-e89b-12d3-a456-42665",
          "holderName": "John Smith"
        }
      }
      ```  
    For token payments:
      ```javascript
      "paymentMethodData": {
        "reference": {
          "token": "PMR-e89b-12d3-a456-42665"
        }
      }
      ```
1. The PSP processes the payment and responds with an HTTP status code of `200`, and this JSON object:
    ```json
    {
      "pluginTransactionId": "e89b-12d3-a456-42665"
    }
    ```

1. The PSP sends this webhook to [`Submit Event`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/events/submit-event):
    ```bash
    curl -X POST 'https://www.wixapis.com/payments/v1/provider-platform-events' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>' \
    -d '{
          "event": {
            "transaction": {
              "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
                "pluginTransactionId": "e89b-12d3-a456-42665"
            }
          }
        }'
    ```


## Mail Order/Telephone Order payments

A mail order/telephone order (MOTO) payment is a card-not-present transaction where a buyer provides a merchant with their order and payment details by regular mail, fax, or telephone. Once the order details are recorded in the Wix dashboard, Wix sends a request to the PSP to process the payment. This request is the same a standard credit card request, except it includes a field called `moto` whose value is `true`. The flow for processing this request is the same as for regular [card payments](#card-payments).