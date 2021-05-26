SortOrder: 1
# Tokenization Application Error Codes

## What is it?
Calling the Billing Tokenizer V1/V2 API to [tokenize](https://bo.wix.com/wix-docs/rest/all-apis#billing-tokenizer.create-token)
 sensitive billing details can throw an Exception that contains an ApplicationError.
 
For example: <br/> 
**{"message":"Fail CC tokenization", 
   "details":
     {"applicationError":
        {"code":"ERR700",
        "description":"Fail CC tokenization"
        }
     }
  }**
  

## Error Codes
This is a list of all possible error codes:


code: ERR700,  description: Fail CC tokenization<br/> 
code: ERR701,  description: Fail IBAN tokenization<br/> 
code: ERR702,  description: Fail CVV_ONLY tokenization<br/> 

## GRPC Errors
In addition, standard GRPC exceptions will be thrown in the relevant flows such as `Status.INVALID_ARGUMENT`
 on failure in request validation fails and `Status.PERMISSION_DENIED` in no user identity persist on the request.
 
 INVALID_ARGUMENTS will response with error code 400
 PERMISSION_DENIED will response with error code 403
 
 