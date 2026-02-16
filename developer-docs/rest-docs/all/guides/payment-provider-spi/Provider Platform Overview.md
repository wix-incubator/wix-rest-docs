SortOrder: 0
# Provider Platform Overview

This SPI is designed for deeper integration between Wix and external payment providers and should be considered as a B2B solution.
To integrate your payment provider with the `Wix Payment Platform`, you'll need to implement the following SPI. All request and response models are designed to be extensible, as we might add fields/objects in later versions, but we'll keep backward compatibility (so make sure that new fields/objects won't break your existing code).
Here you can find all needed information and steps on how to integrate new payment methods and payment providers inside Wix.

## Payment Providers and Payment Methods
`Provider` or `Payment Provider` - a payment service provider or a payment gateway that is integrated into `Payment by Wix` via API. Providers allow Wix to represent a huge variety of payment methods in different locations all over the globe.

`Payment method` - a financial instrument used by our customers (merchants) to perform transactions using Wix. For example: `iDeal`, `SEPA`, `Bank Card`, etc. One provider can allow for more than one payment method.

There are two main flows that you can integrate with:
- Redirect payment
- PCI payment

## Redirect payment flow
In this flow, Wix does not host any of your data. Either the user is redirected to your site, or
your information is displayed within a modal window. Both cases are configurable.

## PCI payment flow
This flow requires PCI DSS compliance as all communications between Wix and provider must be within PCI environments.
This payment flow provides more flexibility and usability for the Wix user, as we handle a lot on our side:
- Securely saving credit card data
- Pre-filling data
- Display using Wix UI
- No redirects for the buyer
- Handling 3DS and 3DS 2.0 flows

> **Note**: Both flows can be integrated simultaneously. For example, supporting native PCI payment, as well as alternative payment methods via redirect flow.
