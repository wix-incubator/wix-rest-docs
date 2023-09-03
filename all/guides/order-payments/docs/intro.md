SortOrder: 0
# About the eCommerce Order Payments API

The eCommerce Order Payments API concentrates the following order payment-related actions:

* Creating and managing payment records - payment information associated with an order
* Calculating and triggering refunds, as well as managing refund records and assessing an order's refundability status
* Generating invoices and managing their records on the order

## Terminology

* **Transaction**
Global term for transfer of funds - either a **payment** to the merchant or a **refund** to the buyer.
* **Add Payment**
This endpoint does **NOT** make a monetary transaction or charge the payment method. This endpoint adds one or more payment **records** to the order.

