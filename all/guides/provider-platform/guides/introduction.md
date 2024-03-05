SortOrder: 0
# About the Payment Provider SPI

The Payment Provider SPI is an [SPI](https://dev.wix.com/api/rest/getting-started/service-provider-interface) that allows Payment Service Providers (PSPs) to integrate their payment services with Wix. Once a service is integrated, it becomes available to all applicable Wix merchant sites. 

With the Payment Provider SPI a PSP can support:
* A variety of payment methods, including credit cards, e-wallets, and local payment methods.
* Different payment flows, including hosted 3rd-party pages that can support multiple payment methods.
* Refunds initiated by either Wix merchant sites or a PSP's platform.


## How to become a payment service provider

Before a PSP can integrate its services with Wix, it must onboard with Wix's business development team. During the onboarding process, the PSP and Wix agree on the terms of their partnership. Once the onboarding process is complete, the PSP can begin integrating its services with Wix. To start the onboarding process, fill out the [application form](https://www.wix-providerplatform.com/).

Learn more about the [onboarding process](https://providers-platform.wixanswers.com/kb/en/article/getting-started-what-to-expect).

## Terminology

| Term                           | Definition   |
| ------------------------------ | ---------------------|
| 3D Secure (3DS)                | A security protocol that adds a layer of authentication to online credit card payments by requiring customers to enter a one-time password or authenticate using biometrics.  |
| Buyer                          | A site visitor who makes a purchase on a Wix merchant site. |
| Currency minor units           | Representation of a currency in its smallest units. For example, the minor units equivalent of `1 USD` is `100` because `1 USD` is equal to `100` cents. However, `1 JPY` is equal to `1` because it has no minor units. |
| Hosted page                    | A payment page hosted by a Payment Service Provider. Wix redirects buyers to this page to complete their payments. |
| Idempotency                    | A property of computer operations. Idempotent operations can be applied multiple times to the same data without changing the result beyond the initial application.  |
| Installments                   | The number of payments in a multi-stage payment. An installment is a single payment within a multi-stage payment plan.  |
| JSON                           | An open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute-value pairs and arrays or other serializable values. Learn more about [JSON](https://www.json.org/json-en.html).  |
| JSON object                    | An object formatted as JSON.|
| JSON Web Token (JWT)                            | A [standard](https://en.wikipedia.org/wiki/JSON_Web_Token) for formatting data. JWTs include a signature whose payload holds a JSON object that asserts a number of [claims](https://en.wikipedia.org/wiki/Claims-based_identity). The tokens are signed with a private key that is used for verification. |
| Merchant                       | A Wix site that sells goods or services.|
| Off-session payment|  A payment where a merchant charges a buyer even when the buyer isn't present. For example, charging a credit card for a recurring payment. |
| Payment Service Provider (PSP) | An online service for accepting electronic payments. PSPs provides a single gateway for merchants, connecting them to multiple payment methods and handling the technical and financial aspects of payment processing. |
| Webhook                        | A real-time communication mechanism using HTTP requests that allows a PSP to notify Wix about payment and refund events and updates. |