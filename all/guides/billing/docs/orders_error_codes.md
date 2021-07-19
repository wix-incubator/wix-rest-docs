SortOrder: 2
# Pay Invoice Application Error Codes

## What is it?
In order to start payment  process call [createOrder](https://bo.wix.com/wix-docs/rest/business-apis#billing.orders.create-order)
or [previewOrder](https://bo.wix.com/wix-docs/rest/business-apis#billing.orders.preview-order)
This API can throw an Exception that contains the ApplicationError.
For example:
**{"message":"Payment failed", 
   "details":
     {"applicationError":
        {"code":"ERR400",
        "description":"Create Order Error"
        }
     }
  }**

## Error Codes
This is a list of all possible error codes:


code: ERR17,  description: CouponNotApplicable<br/> 
code: ERR25,  description: CouponNotValidForDate<br/> 
code: ERR26,  description: CouponNotValidForProduct<br/> 
code: ERR27,  description: CouponNotValidForCycle<br/> 
code: ERR44,  description: CouponMaxUsageReached<br/>
    
**Declined Error Messages**<br/>

code: ERR400, description: Default Create Order Error<br/>
code: ERR401, description: Default Preview Order Error<br/>
code: ERR402, description: Failed to retrieve payment plan<br/>
code: ERR403, description: Failed to validate order tax<br/>
