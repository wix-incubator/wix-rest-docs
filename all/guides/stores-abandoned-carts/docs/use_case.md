SortOrder: 1
# Abandon Cart Service

## Use Case
Listen to `CartAbandonedEvent`, call to carts service to get updated cart details & checkout url, then send a message to the buyer to complete his purchase. 
Listen to `CartRecoveredEvent` and cancel future messages (if planned) to the buyer. 

## Usage Example In WixStores - Using WixAutomations

* Listen to `CartAbandonedEvent`, call to carts service to get updated cart details & checkout url and trigger WixAutomations with this data.
* Listen to `CartRecoveredEvent` and cancel future WixAutomations tasks.

#### How To Create An Abandoned Cart Automation
*Example from Jan 2019*
![add automation selector](https://s3.amazonaws.com/wixplorer-readme-images/stores-abandoned-carts%2Fadd_new_automation.png)
    *Create new automation*

![set trigger selector](https://s3.amazonaws.com/wixplorer-readme-images/stores-abandoned-carts%2Fset_abandon_trigger.png)
    *Choose the "customer abandons a cart" trigger*

![set time selector](https://s3.amazonaws.com/wixplorer-readme-images/stores-abandoned-carts%2Fset_time.png)
    *Set time to "immediately" or choose "set a custom time" to send the mail after the trigger*
  
