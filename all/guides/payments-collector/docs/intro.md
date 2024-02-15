SortOrder: 0
# About the eCommerce PaymentsCollector API

Normally UoU is the one who initiates payment by placing the order. This API allows merchants
to initiate payments (collect payments). Merchant is able to collect payments for any 
existing not fully paid order, or create order from scratch from behalf of the client
and make a payment using client's payment details. 

Merchant initiated payments are implemented as a 2step process: 
1) Prepare payment collection
2) Charge

This API implements the first step, where we perform the validation, and create payment gateway
order for the requested amount. 

Charge step can be done with Cashier's Pay API [ChargeForOrder](https://bo.wix.com/wix-docs/rest/wix-cashier/pay/charge/charge-for-order) 
or using Cashier [Payments Widget](https://github.com/wix-private/cashier-client/tree/master/packages/cashier-payments-widget)