SortOrder: 0
## About the Transactions API
Use Wix Payments server-to-server API integration to accept different payment methods and manage transactions. Wix Payments act as a standalone solution to independently process payments, deal with chargebacks and disputes via Wix infrastructure, and can be used by any third-party.

### **Wix Payments integration prerequisites**
Before testing the Transactions API, you need to get a Wix Payments account ID. Wix also applies a Know Your Customer (KYC) and evaluation procedure. Contact Wix via transactions-api-support@wix.com and provide the following details to start the evaluation process:
- Put "Wix Payments integration" in the subject of the email
- Provide your name and email
- Include the purpose of your integration with the Transactions API

**Transactions API supports the following flows:**
-   Authorization (reserving funds)
-   Capture (transferring of reserved funds)
-   One-time transaction (Authorization and Capture)
-   Recurring transactions (MIT and CIT)
-   Refund/Void (canceling an authorized or captured transaction)
-   Dispute

**Wix Payments supports the following payment methods:**
-   Card
-   ACH
-   Apple Pay
-   Boleto
-   Giropay
-   iDEAL
-   PayPal
-   Pix
-   SEPA
-   SOFORT

## Terminology
-   **Merchant**: A party selling goods or services to customers via an eCommerce website, a mobile app, on the point of sale, or across all three channels. Wix Payments enable a merchant to accept payments from customers made with cards or local payment methods and manage payouts.
-   **Customer**: Someone who buys goods or services from a merchant. In terms of Transactions API, a customer makes a cashless online payment by using either cards or local payment methods to pay.
-   **Cardholder**: Customer who uses a card issued by a bank to make cashless online payments to a merchant. 
-   **Transaction**: Agreement between a merchant and a customer to exchange goods, services, or financial instruments. The [transaction object](https://dev.wix.com/api/rest/wix-payments/transactions/transaction-object) contains the basic information required to securely process the payment, execute related actions (delivery, analytics, inventory management) and comply with financial regulations.
-   **Merchant Initiated Transaction** (MIT): Payment or a series of payments with fixed or variable amounts that the merchant performs without direct involvement of a customer, such as automatic account top-ups, and installments.
-   **Cardholder Initiated Transaction** (CIT): Payment initiated by the cardholder on their own after the initial successful transaction.
-   **Authorization**: Process of card issuer verifying payment details and reserving funds to capture them later. When the card is verified with the issuer, the funds are reserved for the transaction.
-   **Transaction reference**: Transaction ID of the first transaction for recurring transactions. It should be passed with each subsequent transaction.
-   **Capture**: Transfer of reserved funds from the customer to the merchant. A payment that was already authorized, must be captured to be completed.
-   **Refund** Transfer of funds from the merchant back to the customer - merchant-initated. When the merchant makes a refund, the funds are sent back to the card issuer. If an authorized payment hasn't been captured yet, a refund can't be made, but the merchant can void the payment instead.
-   **Void**: Voiding a transaction will tell the customer’s card issuing bank that the merchant does not intend to collect the transaction corresponding to the original six-digit approval code and, therefore, those held funds are made available to the customer again. Merchant can void a transaction until it is captured.
-   **Dispute**: Refers to the entire process from the moment the customer applies to their issuing bank. Dispute occurs when a cardholder questions the charge with their card issuer and initiates a chargeback. When this happens, the merchant is given the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.
-   **Request for Information (RFI)**: Optional first step in a dispute, initiated when the cardholder does not recognize or disagrees with a charge and requests more information from their bank.
-   **Chargeback**: Second and primary step in a dispute. It includes a reversal of a credit card payment that comes directly from the bank. Chargeback occurs when a cardholder questions a transaction and asks their card-issuing bank to reverse it. 
-   **Evidence**: Documentation in response to the dispute (RFI or chargeback steps), appropriate to the reason for the dispute. For example, evidence responding to a dispute with the reason “product not received” can include shipping information and any screenshots of package tracking. Weblogs, email communications, shipment tracking numbers, delivery confirmation, proof of prior refunds, or replacement shipments can all be helpful.

## Recurring transactions
Wix Payments API allows merchants to set up recurring payments. It adds flexibility and full control of the entire business flow. For subsequent transactions, only the `card_number` should be tokenized using the [Create Card Token](https://dev.wix.com/api/rest/wix-payments/card-tokens/create-card-token) endpoint, and the appropriate token passed to the [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction).

>**Note** to achieve the best approve ratio, the correct MIT/CIT flag must be passed as well.
> To achieve the best approve ratio, pass all possible values received from the card schemes:
>-   __Network_transaction_id__
>-   __ds_transaction_id__ (in case the initial transaction was performed by the 3DS2 regulations)

> [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction) endpoint is fully compatible with the new PSD2 regulations and supports 3DS 2 mechanism.

## Interaction types
| Interaction Type        | Additional Parameters           |Comments  |
| ------------- |-------------| -----|
| ONE_TIME     |  | Regular one-time transaction|
| SETUP_COF_ONSESSION      | | Initial transaction with the subsequent CIT (setup one-click)
| SETUP_COF_RECURRING | |   Initial transaction with the subsequent MIT transactions according to a defined schedule|
| SETUP_COF_UNSCHEDULED     |  | Initial transaction with the subsequent MIT transactions without the defined schedule |
| COF_ONSESSION      | transaction_reference      |  Subsequent transaction initiated by the customer (perform one-click) |
| COF_RECURRING |transaction_reference      |    Recurring transactions initiated by the merchant according to the defined schedule|
| COF_UNSCHEDULED | transaction_reference|    Recurring transactions initiated by the merchant without a schedule|

## Use cases
Create and manage transactions with the following flows:

1. Create a one-time payment and simultaneously authorize and capture funds.
2. Create a one-time payment. Authorize and Capture the funds separately.
3. Create a first/initial recurring payment and subsequent one when the cardholder is not present - authorization and capture in one step.
4. Create an initial “on session” (cardholder present) payment and notify Wix of credential storage to execute a subsequent one in the future when the cardholder is present.
5. Charge a customer and refund funds afterwards.

### 1. Create a one-time payment and simultaneously authorize and capture funds.

Transaction info: $10 USD, one-time credit card transaction, using a card token. A new `card_token` must be generated for each transaction request.   
(A card token must be passed to [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction) when a credit/debit card is the chosen payment method.) 

To create a transaction, call [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction). 

Parameters to include:
```
{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef",
  "amount": "1000",
  "currency": "USD",
  "paymentMethodTypeId": "creditCard",
  "card": {
    "numberToken": "41c29a2-9bd5-4552-1296-6a24c6g0f1ef",
    "expiryMonth": 11,
    "expiryYear": 2027,
    "holderName": "John Doe",
    "securityCodeToken": "71c7932-9bd5-48d2-9196-6df4c640f1ef"
  },
  "automaticCapture": {},
  "oneTimePayment": {}
}
```
> Note: Pass an empty object for the type of transaction `oneTimePayment`, but not null or missing.

### 2. Create a one-time payment. Authorize and Capture the funds separately.

Transaction info: $10 USD, one-time credit card transaction, using a card token. A new `card_token` must be generated for each transaction request.   
(A card token must be passed to [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction) when a credit/debit card is the chosen payment method.)

1. Call [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction).

Parameters to include:
```
POST https://www.wixapis.com/payments/v3/transactions

{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef",
  "amount": "1000",
  "currency": "USD",
  "paymentMethodTypeId": "creditCard",
  "card": {
    "numberToken": "41c29a2-9bd5-4552-1296-6a24c6g0f1ef",
    "expiryMonth": 11,
    "expiryYear": 2027,
    "holderName": "John Doe",
    "securityCodeToken": "71c7932-9bd5-48d2-9196-6df4c640f1ef"
  },
  "oneTimePayment": {}
}
```

2. Call [Capture Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/capture-transaction). Retrieve the transactionId from the step 1.

Parameters to include:
```
POST https://www.wixapis.com/payments/v3/transactions/2ac75a2-91d5-4752-6h96-6aj74640f1ef/capture

{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef"
}
```

### 3. Create a first/initial recurring payment and subsequent one when the cardholder is not present - authorization and capture in one step.

Transaction info: $10 USD, one-time credit card transaction, using a card token. A new card_token must be generated for each transaction request.   
(A card token must be passed to [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction) when a credit/debit card is the chosen payment method.)   
When creating a recurring transaction (MIT/CIT), you only need to tokenize the `card_number` and pass it in the Create Transaction request together with COF.

1. Call [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction).

Parameters to include:
```
{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef",
  "amount": "1000",
  "currency": "USD",
  "paymentMethodTypeId": "creditCard",
  "card": {
    "numberToken": "41c29a2-9bd5-4552-1296-6a24c6g0f1ef",
    "expiryMonth": 11,
    "expiryYear": 2027,
    "holderName": "John Doe",
    "securityCodeToken": "71c7932-9bd5-48d2-9196-6df4c640f1ef"
  },
  "automaticCapture": {}
  "setupCofRecurring": {}
}
```

2. Retrieve the `transactionId` of the created transaction from the response from step 1. (In this example, `transactionId` = 01csa932-9bd5-38d2-91d6-6jf5c640f1ef). You’ll need to pass it as the `transactionReference` in all subsequent transactions.

3. When a subsequent payment is due, call [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction) and pass the `transactionId` from step 1 as the `transactionReference`.

Parameters to include:
```
{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef",
  "amount": "1000",
  "currency": "USD",
  "paymentMethodTypeId": "creditCard",
  "card": {
    "numberToken": "41c29a2-9bd5-4552-1296-6a24c6g0f1ef",
    "expiryMonth": 11,
    "expiryYear": 2027,
    "holderName": "John Doe"
  },
  "automaticCapture": {},
  "cofRecurring": {
    "transactionReference": {
      "transactionId": "01csa932-9bd5-38d2-91d6-6jf5c640f1ef"
    } 
  }
}
```

### 4. Create an initial “on session” (cardholder present) payment and notify Wix of credential storage to execute a subsequent one in the future when the cardholder is present.

Transaction info: $10 USD, one-time credit card transaction, using a card token. A new card_token must be generated for each transaction request.  
(A card token must be passed to [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction) when a credit/debit card is the chosen payment method.)   
When creating a recurring transaction (MIT/CIT), you only need to tokenize the `card_number` and pass it in the Create Transaction request together with COF.

1. Call [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction).

Parameters to include:
```
{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef",
  "amount": "1000",
  "currency": "USD",
  "paymentMethodTypeId": "creditCard",
  "card": {
    "numberToken": "41c29a2-9bd5-4552-1296-6a24c6g0f1ef",
    "expiryMonth": 11,
    "expiryYear": 2027,
    "holderName": "John Doe",
    "securityCodeToken": "71c7932-9bd5-48d2-9196-6df4c640f1ef"
  },
  "automaticCapture": {},
  "setupCofOnSession": {}
}
```

2. Retrieve the transactionId (in this example, `transactionId` = 01csa932-9bd5-38d2-91d6-6jf5c640f1ef). You’ll need to pass it as the `transactionReference` in all subsequent transactions.

3. Call [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction). 
`transactionReference` is the ID of the transaction in the response from step 1.

Parameters to include:
```
{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef",
  "amount": "1000",
  "currency": "USD",
  "paymentMethodTypeId": "creditCard",
  "card": {
    "numberToken": "41c29a2-9bd5-4552-1296-6a24c6g0f1ef",
    "expiryMonth": 11,
    "expiryYear": 2027,
    "holderName": "John Doe",
    "securityCodeToken": "71c7932-9bd5-48d2-9196-6df4c640f1ef"
  },
  "automaticCapture": {},
  "cofOnSession": {
    "transactionReference": {
      "transactionId": "01csa932-9bd5-38d2-91d6-6jf5c640f1ef"
    } 
  }
}
```

### 5. Charge a customer and refund funds afterward.

Transaction info: $50 USD, one-time credit card transaction, using a card token.

1. Call [Create Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/create-transaction).

Parameters to include:
```
{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef",
  "amount": "5000",
  "currency": "USD",
  "paymentMethodTypeId": "creditCard",
  "card": {
    "numberToken": "41c29a2-9bd5-4552-1296-6a24c6g0f1ef",
    "expiryMonth": 11,
    "expiryYear": 2027,
    "holderName": "John Doe",
    "securityCodeToken": "71c7932-9bd5-48d2-9196-6df4c640f1ef"
  },
  "automaticCapture": {},
  "oneTimePayment": {}
}
```

2. Call [VoidOrRefund Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/void-or-refund-transaction).

a. For a full refund:
```
POST https://www.wixapis.com/payments/v3/transactions/71c7932-9bd5-48d2-9196-6df4c640f1ef/capture

{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef"
}
```

b. For a partial refund of $25:
```
POST https://www.wixapis.com/payments/v3/transactions/71c7932-9bd5-48d2-9196-6df4c640f1ef/capture

{
  "accountId": "81c79a2-9bd5-4852-9296-6a24c640f1ef",
  "amount": 2500
}
```
