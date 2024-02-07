SortOrder: 3
# Cashier Pay API: Supported values

## Supported Payment Methods

`CreditCard`, `Alipay`, `AstropayCash`, `AstropayDBT`, `AstropayMBT`, `Bitcoin`,
`BitPay`, `Cash`, `ConvenienceStore`, `EPay`, `Fake`, `Giropay`, `IDeal`,
`InPerson`, `Klarna`, `MercadoPago`, `Netpay`, `NordeaSolo`, `Offline`,
`PagSeguro`, `PayEasy`, `PayPal`, `Paysafecard`, `Paysafecash`, `PointOfSale`,
`Poli`, `Privat24`, `Przelewy24`, `RapidTransfer`, `Sepa`, `Skrill`,
`Sofort`, `Trustly`,`Neteller`, `Unionpay`, `UniPay`

## Supported Payment Providers

`WixPay`, `AuthorizeNet`, `BitPay`, `Braintree`, `Epsilon`,
`Eway`, `Fake`, `FatZebra`, `Interkassa`, `Isracard`, `MercadoPago`,
`Offline`, `PagSeguro`, `PagueloFacil`, `PaymentExpress`, `PayPal`,
`PayUCitrus`, `PayUTurkey`, `Skrill`, `Square`, `Stripe`, `SumUp`,
`TwoCheckout`, `UniPay`, `WixPayUS`, `WorldPay`

## Supported Currencies

`USD`, `EUR`, `AED`, `AFN`, `ALL`, `AMD`, `ANG`, `AOA`, `ARS`, `AUD`,
`AWG`, `AZN`, `BAM`, `BBD`, `BDT`, `BGN`, `BHD`, `BIF`, `BMD`, `BND`,
`BOB`, `BRL`, `BSD`, `BTN`, `BWP`, `BYN`, `BZD`, `CAD`, `CDF`, `CHF`,
`CLP`, `CNY`, `COP`, `CRC`, `CVE`, `CZK`, `DJF`, `DKK`, `DOP`, `DZD`,
`EGP`, `ERN`, `ETB`, `FJD`, `FKP`, `GBP`, `GEL`, `GHS`, `GHS`, `GIP`,
`GMD`, `GNF`, `GTQ`, `GYD`, `HKD`, `HNL`, `HRK`, `HTG`, `HUF`, `IDR`,
`ILS`, `INR`, `IQD`, `ISK`, `JMD`, `JOD`, `JPY`, `KES`, `KGS`, `KHR`,
`KMF`, `KRW`, `KWD`, `KYD`, `KZT`, `LAK`, `LBP`, `LKR`, `LRD`, `LSL`,
`LYD`, `MAD`, `MDL`, `MGA`, `MKD`, `MMK`, `MNT`, `MOP`, `MRO`, `MUR`,
`MVR`, `MWK`, `MXN`, `MYR`, `MZN`, `MZN`, `NAD`, `NGN`, `NIO`, `NOK`,
`NPR`, `NZD`, `OMR`, `PAB`, `PEN`, `PGK`, `PHP`, `PKR`, `PLN`, `PYG`,
`QAR`, `RON`, `RON`, `RSD`, `RUB`, `RWF`, `SAR`, `SBD`, `SCR`, `SEK`,
`SGD`, `SHP`, `SLL`, `SOS`, `SRD`, `STD`, `SZL`, `THB`, `TJS`, `TMT`,
`TMT`, `TND`, `TOP`, `TRY`, `TTD`, `TWD`, `TZS`, `UAH`, `UGX`, `UYU`,
`UZS`, `VEF`, `VND`, `VUV`, `WST`, `XAF`, `XCD`, `XOF`, `XPF`, `YER`,
`ZAR`, `ZMW`, `ZMW`

## Supported Reason Codes


|  Code  | Reason name                              |
| ------ |------------------------------------------|
| `1000` | `Provider_connection_error`              |
| `1000` | `Provider_connection_error`              |
| `1001` | `Timeout_error`                          |
| `1002` | `Provider_access_error`                  |
| `1003` | `Provider_technical_error`               |
| `1004` | `Required_fields_are_missing`            |
| `1005` | `Malformed_bank_response`                |
| `1006` | `Request_is_not_allowed`                 |
| `1007` | `Invalid_format_parameter`               |
| `1008` | `Duplicated_request`                     |
| `1009` | `Invalid_value`                          |
| `1010` | `Test_mode`                              |
| `1011` | `Outdated_API`                           |
| `1012` | `payment_method_not_available`           |
| `2000` | `Merchant_account_is_not_active`         |
| `2001` | `Merchant_account_blocked_or_restricted` |
| `2002` | `Merchant_account_is_invalid`            |
| `2003` | `Merchant_account_expired`               |
| `2004` | `Merchant_auth_failed`                   |
| `2005` | `Merchant_contact_provider`              |
| `2006` | `Merchant_limit_exceeded`                |
| `2007` | `Payment_method_is_not_activated`        |
| `3000` | `General_bank_decline`                   |
| `3001` | `Invalid_amount`                         |
| `3002` | `Transaction_type_is_not_supported`      |
| `3003` | `Currency_is_not_supported`              |
| `3004` | `3D_secure_failed`                       |
| `3005` | `3D_secure_not_enabled`                  |
| `3006` | `Country_is_not_supported`               |
| `3007` | `Conversion_error`                       |
| `3008` | `Address_verification_failed`            |
| `3009` | `Buyer_to_repeat_purchase`               |
| `3010` | `Return_buyer_to_provider`               |
| `3011` | `AVS_CVC_check_failed`                   |
| `3012` | `Insufficient_funds`                     |
| `3013` | `Card_expired`                           |
| `3014` | `Invalid_expiration_date`                |
| `3015` | `Invalid_card_number`                    |
| `3016` | `Invalid_CVV_CVC`                        |
| `3017` | `Card_type_is_not_supported`             |
| `3018` | `Too_many_requests`                      |
| `3019` | `Card_limit_exceeded`                    |
| `3020` | `Test_card_decline`                      |
| `3021` | `Tokenization_issue`                     |
| `3022` | `Refund_is_not_allowed`                  |
| `3023` | `Payment_already_refunded`               |
| `3024` | `Partial_refund_is_not_allowed`          |
| `3025` | `Insufficient_funds_for_refund`          |
| `3026` | `Receiving_limit`                        |
| `3027` | `Transaction_already_processed`          |
| `3028` | `Insufficient_funds_wallet`              |
| `3029` | `Expired_payment_source`                 |
| `3030` | `Buyer_cancelled`                        |
| `3031` | `Transaction_action_already_commited`    |
| `3032` | `Refund_attempts_exceeded`               |
| `3033` | `Refund_time_limit_exceeded`             |
| `3034` | `Installments_failed`                    |
| `3035` | `Transaction expired`                    |
| `3036` | `Invalid_PIN`                            |
| `3037` | `Terminal_not_available`                 |
| `3038` | `Revocation_of_payment`                  |
| `3039` | `Payment_account_invalid`                |
| `3040` | `Security_violation`                     |
| `3041` | `Invalid_account`                        |
| `3042` | `Do_not_try_again`                       |
| `3043` | `Buyer_revoked_authorization`            |
| `3044` | `Bank_notification_failed`               |
| `3045` | `Mandate_canceled`                       |
| `3046` | `Mandate_not_active`                     |
| `4000` | `Cart_amount_do_not_match_order`         |
| `4001` | `Billing_address_missing`                |
| `4002` | `Shipping_address_missing`               |
| `4003` | `Zip_code_missing`                       |
| `4004` | `Phone_number_missing_or_invalid`        |
| `5000` | `Lost_or_stolen_card`                    |
| `5001` | `Risk_management_decline`                |
| `5002` | `Restricted_or_blocked_card`             |
| `5003` | `Restricted_or_blocked_buyer`            |
| `5004` | `Buyer_declined_and_contact_provider`    |
| `5005` | `Pending_fraudulent_transaction`         |
| `5006` | `Risk_bank_decline`                      |
| `5007` | `Pick_up_card`                           |
| `5009` | `Pending_general`                        |
| `6000` | `General_error`                          |
| `6404` | `No_matching_rules`                      |
| `6500` | `Error_mapping_unavailable`              |
