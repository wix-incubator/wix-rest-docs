SortOrder: 0
**Introduction**    
About Payment Records

Payment Records provides the context and contains an overview of payment.  
Payment Records are not complete without a solid foundation. Solid foundation consists of processing, refunds and dispute.  

*Terminology*
  - **Payment Record** - consolidated information about the payment that consists attributes, such as payment method; payment service provider;
  - **Payment History Record** - a change in Payment Record Status;
dates (created and updated); payment status; application info; various types of amount; order ID etc.
  - **Application** - the entity that provides an entrypoint for funds collection;
  - **Customer** - the entity that purchase good or service using application;
  - **Authorization** - the process through which the amount to be paid on a payment method is verified. In case of credit cards, authorization specifically involves contacting the payment system and blocking the required amount of funds against the credit card;
  - **Capture** - the process to complete a credit or debit card purchase by capturing or settling the funds for the transaction;
  - **Cancellation** - also known as void transaction is a transaction that is canceled by a merchant before it settles;
  - **Refund** - A refund is funds which is returned to buyer, for example because buyer have paid too much or because they returned goods to a shop ;
  - **Dispute** - A dispute occurs when a cardholder disputes a payment and contacts their issuer to initiate a chargeback.

Payment Records API allows a business owner to retrieve the payment history, as well as filter, search and retrieve payment history by specific parameters:
- Payment method;
- Payment service provider;
- Date (Created and updated);
- Payment status;
- Application;
- Various types of amount;
- Order ID.

The Payment Records exposes functionality to work with payment historic data.  
These are examples of possible use cases for the API:  
- Retrieve the list of payments;
- Filter the list of payment records by certain parameters such as:  
  - Buyer;
  - Dates;
  - Amounts;
  - Payment service provider;
  - Payment method;
- Retrieve data for the customer, if available, such as:  
  - Billing information;
  - Shipping information;
  - Personal details;
  - Purchase history;
  - Payment method;
  - Order Information;
  - Status Information.
  - See list of historical events for each payment;

*This article shares some possible use cases your app could support, as well as an example flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.*

*These are example flows that can be achieved with Payment Records API, but certainly not a limit.*

*List payment records for some period*
1. Call `Search Payment Records` passing start and end time within `search.filter` and page size in `cursorPaging.limit`:
    ```json
    {
      "search": {
        "filter": {
          "$and": [
            {
              "createdDate": {
                "$ge": "2022-01-01T00:00:00.000Z"
              }
            },
            {
              "createdDate": {
                "$lt": "2023-01-01T00:00:00.000Z"
              }
            }
          ]
        },
        "cursorPaging": {
          "limit": 100
        }
      }
    }
    ```
2. In addition to `paymentRecords` you’ll get `pagingMetadata.hasNext`, if it’s `true` then proceed with next step.
3. Call `Search Payment Records` passing `pagingMetadata.cursors.next` from the previous call and page size:
    ```json
    {
      "search": {
        "cursorPaging": {
          "limit": 100,
          "cursor": "84e67a9b-45aa-4a57-b686-f86199558226"
        }
      }
    }
    ```
4. Repeat from the step 2.

*List payment records for some contact*
1. Call `Search Payment Records` passing contact ID within `search.filter` and page size in `cursorPaging.limit`:
    ```json
    {
      "search": {
        "filter": {
          "contactId": "73d6cc8a-3957-4af6-a3dd-10c73c4ffe01"
        },
        "cursorPaging": {
          "limit": 100
        }
      }
    }
    ```
2. In addition to `paymentRecords` you’ll get `pagingMetadata.hasNext`, if it’s `true` then proceed with next step.
3. Call `Search Payment Records` passing `pagingMetadata.cursors.next` from the previous call and page size:
    ```json
    {
      "search": {
        "cursorPaging": {
          "limit": 100,
          "cursor": "84e67a9b-45aa-4a57-b686-f86199558226"
        }
      }
    }
    ```
4. Repeat from the step 2.

*List last records for payments made with credit/debit cards*
1. Call `Search Payment Records` passing `creditCard` as `paymentMethodInfo.paymentMethodTypeId` within `search.filter` and limit in `cursorPaging.limit`, ordering results by `createdDate` descending:
    ```json
    {
      "search": {
        "filter": {
          "paymentMethodInfo.paymentMethodTypeId": "creditCard"
        },
        "sort": [
          {
            "fieldName": "createdDate",
            "order": "DESC"
          }
        ],
        "cursorPaging": {
          "limit": 100
        }
      }
    }
    ```
2. You’ll get last payment records in `paymentRecords`.

*List last records for payment initiated by certain applications*
1. Call `Search Payment Records` passing application IDs within `search.filter` and limit in `cursorPaging.limit`, ordering results by `createdDate` descending:
    ```json
    {
      "search": {
        "filter": {
          "orderInfo.orderAppId": {
            "$in": [
              "5e9fbeb1-59ba-457d-a72c-d761bf8c26ba",
              "7ef5b71e-2a6b-42bf-8ace-760a166ba09b"
            ]
          }
        },
        "sort": [
          {
            "fieldName": "createdDate",
            "order": "DESC"
          }
        ],
        "cursorPaging": {
          "limit": 100
        }
      }
    }
    ```
2. You’ll get last payment records in `paymentRecords`.

*Show history for a certain payment*
1. Call `Query Payment History Records` passing payment record ID within `query.filter` and page size in `cursorPaging.limit`:
    ```json
    {
      "query": {
        "filter": {
          "paymentRecordId": "ed93db32-230b-45d4-92c3-e8022aba4579"
        },
        "cursorPaging": {
          "limit": 100
        }
      }
    }
    ```
2. In addition to `paymentHistoryRecords` you’ll get `pagingMetadata.hasNext`, if it’s `true` then proceed with next step.
3. Call `Query Payment History Records` passing `pagingMetadata.cursors.next` from the previous call and page size:
    ```json
    {
      "query": {
        "cursorPaging": {
          "limit": 100,
          "cursor": "53c32b88-6b1e-41ce-ab14-e51e45d1a8c1"
        }
      }
    }
    ```
4. Repeat from the step 2.
