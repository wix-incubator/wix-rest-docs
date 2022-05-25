SortOrder: 0
# About Wix Restaurants Orders

With Wix Restaurants Orders, site owners can retrieve orders and update their statuses. They can also receive a notification when a new order has been placed.

The Orders API allows your app to:

* Retrieve orders
* Mark orders as **accepted**, **fulfilled**, and **canceled**
* Listen to domain events

## Terminology

* **Catalog:** All **menus**.
* **Line Item:** Any **dish** or **dish option** defined in the catalog.
* **Dish Option:** Any **extra** that you can add to a dish, any **size** of the dish, or any **deselection** that you can remove from the dish.
* **Discount:** A price reduction for an **item** or the **order**. The discount can be an amount, a percentage or free delivery. Discounts may depend on entering a coupon code.
* **Order Statuses**:
    * **Pending:** The order has been placed by the customer, but the payment or validation checks have not cleared yet.

        > **Note:** Site owners can't see **pending** orders in their dashboard.
    * **New:** The order has passed validation checks and the payment has cleared, but the site owners have not **accepted** or **canceled** the order yet.
    * **Accepted:** The site owners have agreed to fulfill the order.
        > **Note:** Site owners can set up an automation in the Business Manager to immediately accept every **new** order.
    * **Canceled:** The site owners have decided not to fulfill the order or to mark an already **fulfilled** order as problematic.
    * **Fulfilled:** The order has been successfully distributed.

## Limitations

* **Discounts:** Percentage discounts can only be applied to an item but not the entire order.
* Currently the Restaurants Orders API doesn’t include create functionality. You can update order statuses and listen to domain events.
