# About Inventory
The Wix Stores Inventory service allows you to:
* Enable and disable inventory tracking (per product/item).
* Query and modify the inventory for product variants.

<blockquote class='note'>
<p>
  <strong>Note:</strong><br/>
See the <a href="https://dev.wix.com/api/wix-stores#about-wix-stores">Wix Stores Terminology</a> defined above.
</p>
</blockquote>

A product's inventory item ID is included in the response returned by the [Query Products](https://dev.wix.com/api/wix-stores#catalog.product.query-products) endpoint.

<blockquote class='note'>
<p>
  <strong>Note:</strong><br/>
When inventory tracking is disabled, Wix store owners may still update the variant quantity manually.
</p>
</blockquote>

## Use Case 
1. Get the inventory item ID for the product you want to read/update.  
a. Call the [Query Products](https://dev.wix.com/api/wix-stores#catalog.product.query-products) endpoint.  
b. Collect the inventory item ID from the response.  
<blockquote class='note'>
<p>
  <strong>Note:</strong><br/>
You can change or check the inventory status for this product using the <a href="https://dev.wix.com/api/wix-stores#inventory.get-item-inventory-status"> Get Item Inventory Status</a> or the <a href="https://dev.wix.com/api/wix-stores#inventory.update-item-inventory-status"> Update Item Inventory Status</a> endpoints.
</p>
</blockquote>

2. Call the [Get Variant Inventory Status](https://dev.wix.com/api/wix-stores#inventory.get-variant-inventory-status) endpoint, filtering for the relevant choices/variants.
