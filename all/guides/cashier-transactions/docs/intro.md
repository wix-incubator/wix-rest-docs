SortOrder: 0
# Cashier Transactions

## What is it?

The "Cashier Transactions" service is a way for verticals in Wix to retrieve in different way the  transactions processed through Wix Cashier and also to be able to refund a transaction.

For the Transactions, you will be able to get a list of transactions or to get a specific transaction but you also will be able to filter the list by:

1. Verticals
2. Payment methods.

For the refund, you will be able to create a full refund for a specific transaction (by transactionID). As of June 2018, only Wix Payment in Brazil support this functionality. Please note the refund is implemented per provider and the roll-out of it will probably happen in phases with PayPal and major CC providers in the first place, followed by the rest.

## What are the main workflows and advantages for the users?

The main workflow for the users is to be able to see the payment transactions made on his site or per vertical order and allow him to filter the view or to refund the transaction.

The main goal is to allow each vertical to incorporate payment data into their own business model and deliver to the user the best transparent experience on his income.

The flow used today in Cashier Payment Dashboard could be used in any verticals showing orders:

1. As a user, I am logging in my dashboard in Wix and my Payment dashboard.
2. I will be able to see there my total income, my transactions, to filter them and also be able to refund if needed.

Clear advantages for the users is to have full control on his transactions and take action if needed.

## What is provided by the Cashier Transactions service?

### Server APIs

- Transaction entity describes a transaction made through Cashier (order and payment details, with buyer addresses if exist). 
- Refund entity describes a simple refund transaction, based on the original transactionID.

### UI components

No UI component available - Server Side only.

