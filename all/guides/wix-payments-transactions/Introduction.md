SortOrder: 0
## Introduction:

Below you can find the information and guidelines that will teach you how to use the Wix Payments server to server API integration and accept different payment options. The Wix Payments acts as a standalone solution where payment can be initiated independently on the Wix infrastructure and used by any third-party developer.

## What I can do with it:

The set of API methods contains a variety of transaction types according to your company model and requirements to build a strong and efficient business.

-   Authorization
-   Capture
-   Sale
-   Refund/Void
-   Recurring (MIT and CIT)

The Wix Payments supports the following payment methods:

-   Credit Card
-   Sofort
-   Ideal
-   GiroPay
-   Boleto

## What is the transaction: 

A transaction is an agreement between a buyer and a seller to exchange goods, services, or financial instruments. The[ transaction object ](https://bo.wix.com/wix-docs/rest/drafts/wix-payments-transactions/transaction-object)contains the basic information needed to securely process the payment, execute related actions (delivery, analytics, inventory management) and satisfy local institutions' regulations.

## How to perform Recurring transactions:

The Wix Payments API allows the triggering of the Recurring payment from the merchant side. It adds flexibility and full control of the entire business flow. In the case, of the subsequent transactions, the only card_number should be tokenized by Card Token and the appropriate token passed to the [Create Transaction](https://bo.wix.com/wix-docs/rest/drafts/wix-payments-transactions/create-transaction).

Please note that in order to achieve the best approve ratio the correct MIT/CIT flag should be passed as well.

**MIT** (Merchant Initiated Transactions) - A payment or a series of payments with fixed or variable amounts that the merchant performs without the direct involvement of the shopper. Examples are subscriptions, automatic account top-ups, and installments.

**CIT** (Cardholder Initiated Transactions) - A payment initiated by the cardholder on his own after the initial successful transaction without entering the credit card data.

**Transaction reference** - a reference object to the initial (base) transaction which precedes all subsequent transactions. Please note that in order to achieve the best approve ratio please also pass all possible values received from the card schemes. :

-   __Network_transaction_id__
-   __ds_transaction_id__ (in the case if the initial transaction was performed by the 3DS2).


Notes:


>Note 1. Please contact cashier-provider-integration@wix.com  in order to get credentials to the test merchant account and start your integration. 

>Note 2.   In order to start a payment, you have to call Create Transaction.  The API is fully compatible with the new PSD2 regulations and support the 3DS 2  mechanism. 

>Note 3.  The parameter testMode should be passed according to your account setup for all API requests. 

| Wix Payments API Interaction Type        | Additional Parameters           |Comments  |
| ------------- |-------------| -----|
| ONE_TIME     |  | A regular one-time transaction|
| SETUP_COF_ONSESSION      | | An initial transaction with the subsequent CIT (setup one-click)
|SETUP_COF_RECURRING | |   An initial transaction with the subsequent MIT transactions by a certain schedule|
| SETUP_COF_UNSCHEDULED     |  |An initial transaction with the subsequent MIT transactions without a certain schedule |
| COF_ONSESSION      | transaction_reference      |  Subsequent transaction initiated by the customer (perform one-click) |
|COF_RECURRING |transaction_reference      |    Recurring transactions initiated by the merchant in the proper schedule|
|COF_UNSCHEDULED | transaction_reference|    Recurring transactions initiated by the merchant without the schedule|


## Use cases:

- Any no prohibited business inside or outside the Wix organization would like to process transactions and manage the full entire flow.
- The business model requires instant or delayed capturing of the funds.
- The business has a recurring business model and wants to build the logic on the own side.

Specifics of the API allow the client to manage all flavors of the business flow.
 
