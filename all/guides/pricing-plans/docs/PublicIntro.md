SortOrder: 1
# About Wix Pricing Plans

[Wix Pricing Plans](https://support.wix.com/en/article/about-pricing-plans) includes Plans and Orders, and allows a site owner to build a customized membership plan experience and sell it to their customers. With [Plans](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/plans), a site owner can create different types of plans, such as, free, one-time or recurring subscriptions. With [Orders](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/orders), a site owner can create and manage the purchases of these plans.

## Integrations

Wix site owners can use Wix Pricing Plans together with other Wix business solutions.

Pricing Plans can be used together with the following Wix business solutions:
- *Wix Bookings* - services from Wix Bookings (classes, treatments, workshops, etc.) can be included as a part of a plan (e.g. a plan for 10 private yoga classes).
- *Wix Blog* - blog (list of posts or a single complete post) can be limited to paying members who purchase a particular membership.
- *Wix Forum* - allow some forum categories to be accessible only for paying members.
- *Wix Events* - offer discounts on event tickets to paying members who purchase a particular membership.
- *Wix File Share* - access to files in your shared library can be limited to paying members.
- *Wix Online Programs* - access to an online program can be accessible only to paying members who purchase a particular membership.
- *Wix Video* - video channel access can be limited to paying members.
- *Wix Groups* - group membership can be accessible only to paying members who purchase a particular membership.

To learn more about Pricing Plans Integrations with other Wix business solutions, read [this article](https://support.wix.com/en/article/about-pricing-plans#connect-wix-bookings-services-to-a-pricing-plan).

## Plans and subscriptions

Every purchase of a pricing plan creates a new "subscription" to that plan for that buyer. Plans can be 1 of 3 different pricing models, `subscription`, `singlePaymentForDuration`, or `singlePaymentUnlimited`.
> **Note:** All orders are called subscriptions, not just the ones that use the `subscription` pricing model.

## Pricing models
Pricing models contain the [pricing and duration options](https://support.wix.com/en/article/pricing-plans-about-pricing-plans#pricing-duration-options) for a plan.

Plans are based on a pricing model, which is defined with the plan's `pricing` property. A pricing model can be one of the following:

+ **A subscription:** A plan with recurring payment cycles.

    *Example:* A 1-year subscription with monthly, recurring payments. Each payment is $25, so the total price for the plan is $300. In this example, the subscription is in its third month.

    `cycleDuration` is the length of one payment cycle. Multiply `cycleDuration`'s `count` by `cycleCount` to get the subscription duration. Currently, `cycleDuration` only supports a value of `1`.

    `index` of `currentCycle` is the current payment cycle for the subscription. `index` is `0` when the order is in a free trial period. In all other cases, the `index` starts with `1` for the first payment cycle in the subscription. For orders with a single payment, the `index` will remain `1` throughout the duration.

    ```javascript
        "pricing": {
            "subscription": {
                "cycleDuration": {
                    // Payment recurs every month
                    "count": 1,
                    "unit": "MONTH"
                },
                // for 12 times
                "cycleCount": 12
            },               
            "prices": [{              
                "duration": {
                    "cycleFrom": 1,
                    "numberOfCycles": 12
                },
                "price": {
                    "subtotal": "25",
                    "discount": "0",
                    "total": "25",
                    "currency": "USD"
                }
            }]
        }, 
        ...
        "currentCycle": {
            "index": 3,
            "startedDate": "2022-03-01T13:45:53.129Z",
            "endedDate": "2022-04-01T13:45:53.129Z"
        },
    ```

+ **A plan that does not renew:** A plan paid for with a single payment. The plan does not renew after the duration.

    *Example:* A plan with a single payment of $35 for 3 months. 

    The `duration` `cycleFrom` and `numberOfCycles` will both be `1`, as the single price applies to the entirety of the subscription.
    
    `index` of `currentCycle` will remain `1` throughout the duration.

    ```javascript
        "pricing": {
            "singlePaymentForDuration": {
                // Plan duration is 3 months
                "count": 3,
                "unit": "MONTH"
            },
            "prices": [{              
                "duration": {
                    "cycleFrom": 1,
                    "numberOfCycles": 1
                },
                "price": {
                    "subtotal": "35",
                    "discount": "0",
                    "total": "35",
                    "currency": "USD"
                }
            }]
        },
        ...
        "currentCycle": {
            "index": 1,
            "startedDate": "2022-01-01T13:45:53.129Z",
            "endedDate": "2022-04-01T13:45:53.129Z"
        },        
    ```

+ **An unlimited plan:** A plan paid for with a single payment. The plan does not expire and remains valid until canceled.

    *Example:* An unlimited plan that is paid for in advance with one payment of $200. 

    `singlePaymentUnlimited` is `true`.
    
    The `duration` `cycleFrom` and `numberOfCycles` will remain `1` throughout the duration of the plan.
    
    `index` of `currentCycle` will remain `1` throughout the duration. `singlePaymentUnlimitedPlans` don't return an `endedDate` in `currentCycle`.

    ```javascript
        "pricing": {
            "singlePaymentUnlimited": true,
            "prices": [{
                "duration": {
                    "cycleFrom": 1,
                    "numberOfCycles": 1
                },                
                "price": {
                    "subtotal": "200",
                    "discount": "0",
                    "total": "200",
                    "currency": "USD"
                }
            }]
        },
        ...
        "currentCycle": {
            "index": 1,
            "startedDate": "2021-06-015T13:45:53.129Z"
        },        
    ```

## Free plans and free trial periods
A free plan that is valid until canceled is a `singlePaymentUnlimited` pricing model. A free plan with a limited duration is treated as a `singlePaymentForDuration` pricing model.

A site owner can also add a free trial period, in days, to a `subscription` pricing model. When the free trial is over, the first payment cycle begins and the buyer is billed. During the free trial period, the `index` of `currentCycle` is `0`. A buyer only receives the free trial period for the first time they purchase a plan. For example, a buyer purchases a monthly plan for 3 months that includes a 7-day free trial period. The buyer may purchase the same plan again, for another 3 months, but will not receive the 7-day free trial period.

When a buyer cancels their order during the free trial period, their subscription will expire at the end of the free trial period and they will not be billed. A site owner can [cancel an ordered plan](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/orders/cancel-order) during the free trial period and choose to apply the cancellation `IMMEDIATELY` or at the `NEXT_PAYMENT_DATE`. Canceling at the `NEXT_PAYMENT_DATE` allows the buyer to continue using the benefits of the subscription until the end of the free trial period. Then, the subscription ends and the buyer is not billed.