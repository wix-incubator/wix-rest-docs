SortOrder: 1
#Coupons Overview 

## Coupon Definition

Coupon definition contains elements like:
1) Usage limits
2) Discount definition. For example, percent.
3) Dates when coupon is applicable
4) Applies-to definition. On what coupon can be applied. For example, product or service.
5) Assigned-to definition. Who coupon assigned to and can use it during purchase.  

**Discount** is mandatory. While all the rest is optional. Discount has discounting rules and support both one-time and recurring purchases.  

**Applies-to** and **Assigned-to** are lists of entities with pair of "id" and "category" to identify id source.
For easy understanding, lets use simple example that assignedTo is user and appliesTo is a product.  

## Example: Wix Premium Coupons

Wix Premium is first tenant using coupons.

There are several Corvid bases applications and Wix services assigned to "Premium" tenant. 
Premium Checkout enables insertion or injection of coupons to get discount and SBS backend billing system validates applies coupon.

Applies-to supported categories: "product", "product-group"
Assigned-to supported categories: "user"  

## What is valid coupon? 
In order coupon will be redeemable it must be valid and applicable in specific purchase.
A valid coupon is an enabled coupon that already effective and not yet expired based on defined valid from and to dates.
Also is should not reach its usage limit. Meaning that amount of usages is less then the limit.
A valid coupon can be applied on some purchase if it matches product, purchase cycle type and user that making the purchase.

## Operations on Coupons

#### Read & Manage
It is possible to retrieve information on coupon and perform operations on it.

#### Querying
Simple Listing and Querying for coupons supported based on filtering parameters. While List and Query returns all coupons answering filtering params, 
coupons are not filtered whether coupons are valid or not.
EligibleFor api returns only **valid** coupons.     
 
#### Validate & Redeem
Using purchase context "redeem-params" we can validate if coupon can be applied. 
Redeem operation called by Billing system validates this as well and increase usage amount coupon while applying the discount during purchase.
