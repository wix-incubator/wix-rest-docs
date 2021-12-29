SortOrder: 0
# Billing Tokenizer

## What is it?
The Billing Tokenizer service is a PCI service that is part of the Billing API. 
It is used to tokenize sensitive billing details so it does not travel in non PCI environment.
Billing details can be credit card (number and cvv) or iban.

The billing-token, which is a result of the tokenization process, is used for creating/updating a payment source in the Billing API.

## How does the Billing Tokenizer work?
The Billing Tokenizer uses a PCI Compliant component for tokenization of the sensitive data. 
The generated token is linked to a specific user, and can not be used by other customers.


![](https://s3.amazonaws.com/wixplorer-readme-images/billing-tokenizer%2FBillingTokenizerDiagram.png)


## Onboarding
                  
Billing Tokenizer service supports only WIX user or external apps users(OAuth) identity.
If the caller is not making the request from wix.com domain we need to add them to allow CORS.