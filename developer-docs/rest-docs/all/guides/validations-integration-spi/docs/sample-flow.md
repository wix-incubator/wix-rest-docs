SortOrder: 1
# Validation Violations: Sample Use Cases & Flows

This article presents sample flows your app can support. You aren't limited to this exact flow, but it can be a helpful jumping off point as you plan your Validations integration.

## Validate a coupon code for a Wix checkout

1. A site visitor adds a coupon code to their Wix checkout. 

2. Wix sends a [Get Validation Violations](https://dev.wix.com/api/rest/wix-ecommerce/validations-integration-spi/get-validation-violations) SPI request to your app. 

3. Your server validates the request. If the coupon code is valid, the validation is sucessful and the SPI returns an object containing an empty list. If the coupon isn't valid, the validation isn't successful. In this case, Wix eCommerce expects an object containing the validation violations, and the severity and target of the violations.
    
    Example of a violations response from your app:
    
    ```json
    {
      "violations": [{
        "severity": "ERROR",
        "target": {
          "other": {
            "name": "OTHER_DEFAULT"
          }
        },
        "description": "Can't apply coupon because minimum cart value has not been reached.",
      }]
    } 
    ```

4. With this validation violation, the site visitor can't proceed with the checkout.


## Validate a line item's quantity

In this flow, due to limited quantity of white wine, a site visitor can't add more than 5 cases of white wine to their cart.

### App configuration prerequisites

When configuring your app in the Wix Developers Center,
use these sample settings:

When configuring your app in the Wix Developers Center, set the `validateInCart` property to `true` in the integration component’s configuration file. This validates a site visitor's cart in addition to a site visitor's checkout. 

### The flow

1. A site visitor adds 6 cases of white wine to their cart, which is over the amount that is permitted.

2. Wix sends a [Get Validation Violations](https://dev.wix.com/api/rest/wix-ecommerce/validations-integration-spi/get-validation-violations) SPI request to your app. 

3. Your server validates the request and finds it unsuccessful. Wix eCommerce expects an object containing the validation violations, and the severity and target of the violations.
    
    Example of a violations response from your app:
    
    ```json
    {
      "violations": {
        "severity": "ERROR",
        "target": {
          "other": {
            "name": "LINE_ITEM_DEFAULT"
          }
        },
        "description": "Can't proceed with checkout. Remove 1 case of white wine from your cart.",
      }
    }
    ```

4. After this validation violation, the site visitor removes 1 case of white wine to proceed to Wix Checkout.

5. Again Wix sends a [Get Validation Violations](https://dev.wix.com/api/rest/wix-ecommerce/validations-integration-spi/get-validation-violations) SPI request to your app. 

6. Your server validates the request and finds it successful. In this case, Wix eCommerce expects an object containing an empty list.