SortOrder: 5
# Reason Codes

Wix uses reason codes to provide detailed information about the statuses of payment, refund, and account connection requests to merchants. Payment Service Providers (PSPs) should use these codes when responding to requests from Wix and when [sending webhooks](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/webhooks) to Wix.

The reason codes break down into these types:
* [General errors](#general-errors)
* [Account connection failure](#account-connection-failure)
* [Transaction pending](#transaction-pending)
* [Transaction declined](#transaction-declined)
* [Refund declined](#refund-declined)

The following tables list the reason codes that Wix supports for each type and the error messages that Wix displays to merchants for each code.

We suggest that PSPs map their internal errors to Wix's reason codes. This way, both merchants handling payments in the Wix dashboard and buyers who are completing their payments on the PSP's site get consistent error messages.

If you can't find a reason code for your error, use code `6000`. Provide the error details in the `errorCode` and `errorMessage` fields of your response so the merchant can handle it properly.

## General errors

These are general codes that can be returned in any response.

| Reason Code | Message |
|---|---|
| 1002 | Provider access error. |
| 1003 | Provider technical error. |
| 1004 | Required fields are missing. |
| 1005 | Malformed bank response. |
| 1006 | Request is not allowed. |
| 1007 | Invalid format parameter. |
| 1009 | Invalid value. |
| 1010 | Test mode. |
| 1012 | Payment method not available. |
| 1013 | Refund technical error. |

## Account connection failure

Use these codes when responding to [`Connect Account`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/accounts/connect-account) requests.

| Reason Code | Message |
|------------|------|
| 2000 | Merchant account is not active. |
| 2001 | Merchant account blocked or restricted. |
| 2002 | Merchant account invalid. |
| 2007 | Payment method is not activated. |
| 2008 | Merchant account is in test mode. |
| 2009 | Merchant account does not match currency. |

## Transaction pending

Use these codes when responding to [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) requests.

> **Note**
> Responding with a `Pending` reason code means the transaction is likely to be approved in the future.

| Reason Code | Message |
|---|---|
| 5005 | Pending fraudulent transaction. |
| 5009 | Pending general. |

## Transaction declined

Use these codes when responding to [`Create Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/transactions/create-transaction) requests.

| Reason Code | Message                              |
|-------------|--------------------------------------|
| 3000        | General bank decline.                 |
| 3001        | Invalid amount.                       |
| 3002        | Transaction type is not supported.    |
| 3003        | Currency is not supported.            |
| 3004        | 3D secure failed.                     |
| 3006        | Country is not supported.             |
| 3008        | Address verification failed.          |
| 3011        | AVS CVC check failed.                 |
| 3012        | Insufficient funds.                   |
| 3013        | Card expired.                         |
| 3014        | Invalid expiration date.              |
| 3015        | Invalid card number.                  |
| 3016        | Invalid CVV CVC.                      |
| 3017        | Card type not supported.              |
| 3018        | Too many requests.                    |
| 3019        | Card limit exceeded.                  |
| 3020        | Test card declined.                   |
| 3026        | Receiving limit.                      |
| 3028        | Insufficient funds wallet.            |
| 3029        | Expired payment source.               |
| 3030        | Buyer canceled.                       |
| 3031        | Transaction action already committed. |
| 3034        | Installments failed.                  |
| 3035        | Transaction expired.                  |
| 3036        | Invalid PIN.                          |
| 3037        | Terminal not available.               |
| 3040        | Security violation.                   |
| 3041        | Invalid account.                      |
| 3042        | Do not try again.                     |
| 3043        | Buyer revoked authorization.          |
| 3044        | Bank notification failed.             |
| 3045        | Mandate canceled.                     |
| 3046        | Mandate not active.                   |
| 4000        | Cart amount does not match order.     |
| 4001        | Billing address missing.              |
| 4002        | Shipping address missing.             |
| 4003        | ZIP code missing.                     |
| 4004        | Phone number missing or invalid.      |
| 5000        | Lost or stolen card.                  |
| 5001        | Risk management declined.             |
| 5002        | Restricted or blocked card.           |
| 5003        | Restricted or blocked buyer.          |
| 5006        | Risk bank decline.                    |
| 5007        | Pick up card.                         |
| 6000        | General error.                        |

## Refund declined

Use these codes when responding to [`Refund Transaction`](https://dev.wix.com/docs/rest/api-reference/payment-provider-spi/refunds/refund-transaction) requests.

| Reason Code | Message |
|---|---|
| 3022        | Refund not allowed.                   |
| 3023        | Payment already refunded.             |
| 3024        | Partial refund not allowed.           |
| 3025        | Insufficient funds for refund.        |
| 3032        | Refund attempts exceeded.             |
| 3033        | Refund time limit exceeded.           |