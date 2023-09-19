SortOrder: 0
# About Discount Rules API

The Wix eCommerce Discount Rules API allows you to create and manage discount rules.
Discount rules are sets of triggers and scopes that together define the necessary conditions for a discount to apply to items in the cart/checkout.

With the Discount Rules API, you can:

+ [Create](https://dev.wix.com/api/rest/wix-ecommerce/discount-rules/create-discount-rule), [update](https://dev.wix.com/api/rest/wix-ecommerce/discount-rules/update-discount-rule), and [delete](https://dev.wix.com/api/rest/wix-ecommerce/discount-rules/delete-discount-rule) discount rules.
+ [Get](https://dev.wix.com/api/rest/wix-ecommerce/discount-rules/get-discount-rule) and [query](https://dev.wix.com/api/rest/wix-ecommerce/discount-rules/query-discount-rules) discount rules.

## Before you begin

+ Currently only item-level discounts are supported. Discounts for an entire cart/checkout are not yet supported.
+ Up to 5 triggers can be chained together.

## Terminology

- **Discount rule:** A set of conditions (scope and trigger) that dictate whether an item qualifies for a specified discount.

- **Discount:** The change applied to an item's price when conditions are met. Discounts can reduce an item's price by percentage or a specified amount, and also by setting an item to a fixed price.
  - Discounts must have a defined scope/s


- **Scope:** A group of catalog items that qualify for a discount.
  - Every catalog has 2 scopes "out of the box". For example, Wix Stores has `Specific Products` and `All Products` scopes.
  - Scopes are required in default triggers and discount objects.
  - Triggers and discounts can have multiple scopes.


- **Trigger**: A set of conditions that must be met for a discount to become applicable. Triggers can be chained so that more than 1 condition must be met.
  - **Default triggers:** These built-in triggers fire when a specified minimum/maximum item quantity (for example, "at least 5 items") or cart subtotal ("no more than $100") is reached. For this trigger to fire, the items must also be part of a defined scope.
