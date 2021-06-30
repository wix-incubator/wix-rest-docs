SortOrder: 0
The Product Catalog stores and manages the templates of all products sold by Wix.
It is a key component in the Dynamic Offering subscriptions management platform.
It does not deal with display related concerns and/or translations (to be handled by "Display Layer", WIP).

![Dynamic Offering diagram](https://s3.amazonaws.com/wixplorer-readme-images/premium-product-catalog%2Fdynamic-offering.png)

The catalog has a 2-level hierarchy of products: each product belongs to a "product family", which in turn belongs to a "product type":

![Product catalog diagram](https://s3.amazonaws.com/wixplorer-readme-images/premium-product-catalog%2Fproduct-catalog-color.png)

### Main entities:

#### Product

A salable unit. buying a product results in the creation of a subscription or a one-time paid asset.
A product defines the "contract" between the vendor and the subscription buyer: the set of features that will be delivered when purchased, the name of the resulting subscription, the pricing for different currencies and additional subscription management settings.
    
#### Feature
* Feature Spec
    
    e.g.: "Site storage".
    The spec defines the base characteristics of the feature: is the usage countable (boolean/quantitive) and how is it measured (measurement units and period), the context in which it applies (site/account), the default (freemium) quota, the product types that permitted to include it, etc.
    The actual amount is inlined inside the product (so multiple similar features that only differ by their quantity require only 1 Feature Spec).

* Product Feature
    
    e.g.: "20 GB site storage".
    Defined when including a feature in a product (many-to-many).
    Contains a reference to a Feature Spec and a quantity (if applicable), thus includes all the required information to deliver the feature.   

* Feature instance
    
    e.g.: site 'x' has 20 GB site storage.
    Instance of a Product Feature.
    Feature instances are allocated for the account/context on every subscription purchase.
    These entities are not part of the product catalog, but are portrayed here to explain the bigger picture. Features instance context cannot be manipulated independently, and is always derived from that of the subscription containing it. 
        
#### Product Type

 Top level hierarchy for products - e.g.: Premium plans, Domains, Apps, Ascend.
 Product type is very significant for funnel-related concerns: An offering (a.k.a package picker) will always contain products from a single product type. Switch contracts (a.k.a. 2nd upgrades/downgrades) are only possible between products of the same product type.
 Subscriptions (instances of a product) of the same product type under the same account typically have context-based limitations (e.g.: each site can only have 1 active premium plan connected; each <siteId, appDefId> can only have 1 active External App subscription, etc.).
 Different product types may share feature specs (see below).

#### Product Family
     
2nd level hierarchy of products. Designed to group different variations of the same product (e.g.: “Combo Price Testing 2019” and “Combo With New AdWords Voucher” will most likely share the same family).
This allows maintaining external pointers to products, that remain stable even when creating new product variations within the same family (e.g.: if we want a coupon to be eligible for all “Combo” products, we can achieve this by “pointing” to the “Combo” family instead of pointing directly to a specific list of products. This way, when a new product is added to the Combo family, it will automatically be eligible for the coupon).
Unlike product type, product family currently has no implication on subscription management settings (unless explicitly overridden, see below).

 
#### Subscription settings

Defines different subscription management rules: cancellation policy, e-mails sent, allowed subscription actions and more.
Settings are defined on product-type level, and are therefore shared between products of the same type. However, it is also possible to override the subscription settings per each product separately.

### Design

Product Catalog uses [Greyhound's key-value store](https://github.com/wix-private/server-infra/blob/master/iptf/greyhound/greyhound-state).
As such, the "Product" aggregate is published to a _compact topic_, allowing others to easily create different local materialized views of the catalog.
of course, you may use the platformized APIs provided as well at any time. 
