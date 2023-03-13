SortOrder: 0
# Coupons Core Service

## What is it?
Coupons core service exposes coupon management capabilities. It is a standalone coupons management service and provides coupons management per tenant.

## Onboarding
Coupon service supports only known applications.
Each application mapped to specific tenant. 
Based on the customer we will either allocate new tenant or map to existing one, 
Whether it's an external application or service, you need to define your app at https://dev.wix.com. 
And then provide an appDefId as a tenantId.  

## What is Coupon?

Coupon is basically some code that represents a discount that can be applicable during purchase of something. 
Coupon Code is unique identifier of the coupon stored in the system. It can be either something meaningful like "saleAug2020" or cryptic like "3C0W4PHFCKBGG0WC5DFC".
Using code you can view and manage coupon details. During purchase Billing system can validate and redeem coupon by applying coupon's discount.       

Coupon is applicable on products (or other entities) and can be assigned to users (or other entities).
See Coupons Overview for details.

## What is Coupon Template?

In order to generate that same coupons to different users and different effective dates it is possible 
to store coupon definition in coupon template.   
In later tempalte can be used to generate coupon for given user.