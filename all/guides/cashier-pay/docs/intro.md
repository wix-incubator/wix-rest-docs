SortOrder: 0
# Cashier Pay

## Payment Terminology and concept

In order to better understand the Cashier Pay API and Payment in general, let’s start with some terms needed here:

1. Payment Service Provider (PSP)

    This is a payment company that provides merchants with the set of online tools and APIs to accept, monitor and control payments. Acting as the gateway for the many payment method types, they usually works as SaaS with revenue share business model.

2. Payment method or alternative payment method

    Payment method refers usually to credit card and eWallet with global coverage where Alternative payment methods refer to local payments.  
    Types of payment methods are:

    - Credit / Debit / Prepaid Cards
    - eWallets (PayPal, PagSeguro, MercadoPago etc.)
    - Local Payments (iDeal, Sofort, Przelewy24, Klarna, Giropay, Kombini etc.)
    - Mobile Carrier Billing
    - Online Banking (ACH, SEPA)
    - Kiosks & Voucher (Boleto, Kiwi, etc.)
    - Offline
   
3. PCI / PCI Compliance

    The Payment Card Industry Data Security Standard (PCI DSS) is a set of security standards designed to ensure that ALL companies that accept, process, store or transmit credit card information maintain a secure environment. Wix Cashier is a certified PCI compliance level 1.

4. IPN, Webhooks or Callback URLs

    - IPN or Instant Payment Notifications are notifications used by PSPs to notify merchants about the status of initiated payment instantly. IPN messages can represent payment success or failures, order transaction status changes, accounting ledger information and many others depending on the payment gateway.
    - Webhook or Callback URL is an URL used by merchant to receive notifications from PSP about payment status. 

5. Transaction statuses

    While processing a transaction through the payment provider, it can ends up with one of the following status, depending on the provider platform or on the payment method used (if synchronous or asynchronous):

    - Success - transaction process successfully. The flow should finish with a thank you page.
    - Cancel - transaction was cancel by user (happens when the user is redirected to PayPal by example and is coming back to the site checkout).
    - Pending - transaction pending approval. It could be "Pending Merchant" while the merchant (our user) need to do something like manually approve the transaction OR "Pending user" while the provider might be reviewing the transaction because of fraud. As soon as the transaction is approved, we will send an IPN to the Cashier Pay API consumer for sync.
    - Error - transaction failed to be processed. It can happen due to several causes.  The flow should redirect the user back to checkout with a clear error message (we will be providing) for him to retry with a different card or by selecting a different payment method.

    You can find more information in [Order Overview document](/docs/./Order%20overview).

## What is it?

The "Cashier Pay" service is a service for business applications in Wix to initiate a payment for their users and be able to charge a visitor of the user’s website.

"Cashier Pay" includes one-time and recurring payment (limited to Stripe and PayPal for now) and support over 25 payment providers covering Credit Cards acceptance is almost all countries worldwide, with in addition some local payment methods (iDeal, Sofort and Alipay) and the most popular e-Wallets (PayPal, PagSeguro and MercadoPago)

The list of supported payment provider can be found on [support page](https://support.wix.com/en/article/changing-your-payment-provider-3305157). 

The "Cashier Pay" service can also be used with the "Save Credit Cards" service during checkout and will allow to create a 1-click checkout for registered customers who would like to buy again from the same site.

## What is the main workflow and advantage for the users?

The main workflow for the users and especially for their buyers is the following

1. Wix User connect payment method(s) to his website through the business manager.
2. During checkout on the website, the UoU will be presented with the Cashier payment component, allowing him to pay for a service or a product by selecting a payment method he would like to pay with and actually pay.

## What is provided by the Cashier Pay service?

### Server APIs

- Order

    The Order entity includes all the details of the product(s) or service(s) and details on the buyers needed for the transaction. The order also include setting up an event hook, allowing to get asynchronous update on the order for later time.

- Payment

    The Payment will process the payment for a specific order created ahead or it also support create an order and charge for it, in 1 call. For supported providers, it will allow to set installments for the payment (supported for Leumi Card (IL) and PayU Turkey (TR)).

- Payment Method

    The Payment Method allows TPA to retrieve the list and details of the connected payment methods related to a specific website. It allows to display the payment method selection without using the standard payment component or just to run a validation that the website does have something connected. 

- Mandatory Fields

    The Mandatory fields are the fields, per provider, who are mandatory to provide in order to have a successful transaction. This functionality is fully integrated in the Payment component but it can be used to display the mandatory fields in the TPA’s logic (such as done in Stores logic).

- Account

    The Account will allow the TPA to get the information about specific account (like buyer country, merchant county and site url).
    
### UI components

- Cashier Payments Widget

    This is the Payment component including the full Cashier functionality. It is loaded with the OrderId and will automatically display the possible payment method for the specific website and will also display below the payment methods selection the possible mandatory fields for the provider connected to the site. It also include the “Buy Now button just below the section, to submit the payment.

    The component have 2 versions:

    1. Accordeon Version - where the details of the payment method are display below the selection.

        ![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-pay%2FCashierPaymentsWidget.png)

    2. Separated Version - where the details of the payment method are display below the payment method selection area.
    
        ![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-pay%2FCashierPaymentsComponent.png)
    
### Client side wrapper SDK

Documentation on the Cashier SDK can be found [here](https://bo.wix.com/cashier-docs#/buyer-payment-sdk).

## How to integrate with Cashier Pay Service

The Cashier Pay service can be integrated in several way

- Standard - By integrating the Cashier Payments Widget and setting up webhook. The easiest integration that makes everything for you. Though it’s not as configurable as other integration methods.

- SDK - By using the Cashier Payments SDK with Cashier Payments Method Component  and setting up webhook. This is more powerful integration than the previous one, but requires much more work.

- Advanced - Deeper integration might be needed if you decide to manage the full front-end experience (such as done in Stores). For this case, please get in touch with us to find the best way to integrate.

Integration documentation can be found in more details [Cashier Payments Widget™](https://bo.wix.com/cashier-docs#/?id=cashier-docs) documentation.

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-pay%2FTPACashierIntegrationSimplified.png)

### Standard Integration

In order to integrate with the Cashier Pay as a “black box", those are the workflow you should apply:

- Use [Create Order Request][1] to create the order with the data you are gathering at first, associated with the Success / Cancel / Pending / Error URL of the pages we should use for each scenario. You might also want to set up [event hook][2] for order notifications. This function will return the OrderId.
- Optionally, you can edit the buyer information by using [Update Buyer Info Request][3].
- Then with this OrderId initialize Cashier Payments Widget™ and let the magic happen. For more information, please refer [Cashier Payments Widget™ documentation](https://bo.wix.com/cashier-docs#/?id=cashier-docs).

### SDK Integration

- Use [Create Order Request][1] to create the order with the data you are gathering at first, associated with the Success / Cancel / Pending / Error URL of the pages we should use for each scenario. You might also want to set up [event hook][2] for order notifications. This function will return the OrderId.
- Optionally, you can edit the buyer information by using [Update Buyer Info Request][3].
- Then you need to initialize Cashier Payments SDK and use OrderId to retrieve available payment methods.
- Using Cashier Payments Method Component render payment methods and the pay button. Subscribe to UI events (switching payment method, clicking pay button).
- Once buyer clicks pay button, use Cashier Payments SDK to initialize charge.
- For more information, please refer to [Cashier Payments SDK documentation](https://bo.wix.com/cashier-docs#/buyer-payment-sdk).


  [1]: http://wixplorer.wixpress.com/cashier-pay/reference/order/.wix.payment.api.pay.v2.-order-service.-create
  [2]: https://bo.wix.com/cashier-docs#/buyer-payment-component
  [3]: http://wixplorer.wixpress.com/cashier-pay/reference/order/.wix.payment.api.pay.v2.-order-service.-update-buyer-info