SortOrder: 4
# Reason Codes
These codes must be used in provider responses as well as during event requests to Wix.
They provide the user (merchant) with more detailed information about the status of different entities like Transactions, Refunds, etc., as well as notifications about error cases.

Reason codes can be divided into three groups:
- Account Connection issues
- Transaction Submission issues
- General technical issues

## General
| Reason Code | Name |
|------------|------|
| 1000 | Provider connection error |
| 1001 | Timeout error |
| 1002 | Provider access error |
| 1003 | Provider technical error |
| 1004 | Required fields are missing |
| 1005 | Malformed bank response |
| 1006 | Request is not allowed |
| 1007 | Invalid format parameter |
| 1008 | Duplicated request |
| 1009 | Invalid value |
| 1010 | Test mode |
| 1011 | Outdated API |
| 1012 | Payment method not available |
| 1013 | Refund technical error |

## Onboarding
| Reason Code | Name |
|------------|------|
| 2000 | Merchant account is not active |
| 2001 | Merchant account blocked or restricted |
| 2002 | Merchant account invalid |
| 2003 | Merchant account expired |
| 2004 | Merchant authorization failed |
| 2005 | Merchant contact provider |
| 2006 | Merchant limit exceeded |
| 2007 | Payment method is not activated |
| 2008 | Merchant account is in test mode |
| 2009 | Merchant account does not match currency |

## Sale and Refund
| Reason Code | Name |
|------------|------|
| 3000| General bank decline |
| 3001| Invalid amount |
| 3002| Transaction type is not supported |
| 3003| Currency is not supported |
| 3004| 3D secure failed |
| 3005| 3D secure not enabled |
| 3006| Country is not supported |
| 3007| Conversion error |
| 3008| Address verification failed |
| 3009| Buyer to repeat purchase |
| 3010| Return buyer to provider |
| 3011| AVS CVC check failed |
| 3012| Insufficient funds |
| 3013| Card expired |
| 3014| Invalid expiration date |
| 3015| Invalid card number |
| 3016| Invalid CVV CVC |
| 3017| Card type not supported |
| 3018| Too many requests |
| 3019| Card limit exceeded |
| 3020| Test card declined |
| 3021| Tokenization issue |
| 3022| Refund not allowed |
| 3023| Payment already refunded |
| 3024| Partial refund not allowed |
| 3025| Insufficient funds for refund |
| 3026| Receiving limit |
| 3027| Transaction already processed |
| 3028| Insufficient funds wallet |
| 3029| Expired payment source |
| 3030| Buyer cancelled |
| 3031| Transaction action already committed |
| 3032| Refund attempts exceeded |
| 3033| Refund time limit exceeded |
| 3034| Installments failed |
| 3035| Transaction expired |
| 3036| Invalid PIN |
| 3037| Terminal not available |
| 3038| Revocation of payment |
| 3039| Payment account invalid |
| 3040| Security violation |
| 3041| Invalid account |
| 3042| Do not try again |
|4000 | Cart amount does not match order |
|4001 | Billing address missing |
|4002 | Shipping address missing |
|4003 | ZIP code missing |
|4004 | Phone number missing or invalid |
|5000 | Lost or stolen card |
|5001 | Risk management declined |
|5002 | Restricted or blocked card |
|5003 | Restricted or blocked buyer |
|5004 | Buyer declined and contact provider |
|5005 | Pending fraudulent transaction |
|5006 | Risk bank decline |
|5007 | Pick up card |
|6000 | General error |
