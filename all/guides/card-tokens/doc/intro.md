SortOrder: 0
## About the Card Tokens API
With Card Tokens API, you can securely store one or more payment details per customer in PCI DSS environment. Tokenization allows recurring payments and gives customers a faster checkout experience by using their stored card data. A token refers to saved payment details - credit card number and security code. Tokenization is the process of protecting customer's payment details by replacing them with an algorithmically generated number called token. Tokenization is used to prevent credit card fraud. 

You can use tokens for:
- **One-time payment**: Customer can either store their payment details or pay in the website or app later using their saved details.
- **Recurring transaction**: Periodic automatic payments during a set amount of time for a product or a service.

> **Note:** Tokens cannot be stored or used more than once. Create a new `card_token` for each transaction request. Create and pass a card token to [CreateTransaction](/doc/needs link to endpoint) when a credit/debit card is the chosen payment method.
> If you are creating a recurring transaction (MIT/CIT) you only need to tokenize the `card_number` and pass it in the [CreateTransaction](/doc/needs link to endpoint) request together with [COF](/doc/link needed) flags.

### PCI Compliance
To collect credit or debit card data, you need to be fully PCI DSS compliant. If you are accepting card payments, you need to validate your PCI DSS compliance annually. According to the PCI DSS guidelines, services are not allowed to store credit card information outside of the secured PCI environment. 

The Payment Card Industry Data Security Standard (PCI DSS) is an information security standard for organizations that handle branded credit cards from major card schemes. The PCI Standard is mandated by the card brands but administered by the Payment Card Industry Security Standards Council.

Card Tokens API's functionality is provided to tokenize customers' sensitive data in compliance with the PCI DSS.
