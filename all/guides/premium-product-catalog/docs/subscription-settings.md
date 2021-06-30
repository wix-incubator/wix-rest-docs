SortOrder: 2
## Subscription Settings

Collection of attributes configuring subscription-related settings: allowed actions (can a subscription be assigned to a different site than the one originally purchased?), policies (does this subscription have an official money-back guarantee policy?), user notifications (which e-mail to send to the user? On what events?), validation callbacks (when a purchase is initiated, call this web-hook that will validate if the operation is allowed), context exclusion criterion (only one subscription can exist in an account for the key "$metaSiteId.$appDefId") and basically, most behavioural variations between products will be modeled here (behaviours that are common to all will probably remain hard-coded).

All items in the product hierarchy (product > product family > product type) can be assigned to a subscription settings object.
Each attribute in a subscriptions settings object is optional.
The *effective subscription settings* of a product is built in an OO inheritance-like fashion: for each attribute, look for its definition in the product’s subscription settings.
If the property does not exist, look for its value in the product family subscription settings, and finally check the product type’s subscription settings if still empty.
Typically, most settings are defined at product type level.

##### Example:
Most products in the "Premium Plans" product type have an official 14 day trial. "Enterprise" product family (a sub-family of "Premium Plans" type) does not have an official trial. Now let's say Sergei, the PMM, wants to test a new Enterprise product variation that has a 1 day official trial.
The desired effective subscription settings is achieved by assigning policies with 14 days, 0 days, 1 day to "Premium Plans" (type), "Enterprise" (family), "Sergei’s test" (product) respectively.
When acting upon a subscription, one must always inspect the *effective* settings (using a dedicated API), and not the settings object referenced by the product.
