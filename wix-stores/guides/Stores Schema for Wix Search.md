# Stores Schema for Wix Search

This article describes the Wix Stores fields you can [search and aggregate](https://dev.wix.com/docs/rest/business-management/search/wix-site-search/search) on a site.

To search or aggregate Wix Stores products on a site, set the search API `documentType` parameter to `STORES_PRODUCTS`. 


### Fields

#### documentType

**Description**: Document type that was searched. In this case, `STORES_PRODUCTS`.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### \_id

**Description**: Product ID.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### title

**Description**: Product name.

**Type**: String

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: No

**Can filter**: in, eq, ne, gt, ge, lt, le

#### description

**Description**: Product description.

**Type**: String

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### url

**Description**: Relative URL of the product's page on your site.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### image

**Description**: File source of the main media image for this product.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### sku

**Description**: Product's stock keeping unit number.

**Type**: String

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: Yes

**Can filter**: in, eq, ne, gt, ge, lt, le 

#### inStock

**Description**: Indicates whether the product is in stock.

**Type**: Boolean

**Can search the content of this field**: No

**Can facet**: Yes

**Can sort**: Yes

**Can filter**: eq, ne 

#### collections

**Description**: Collections the product belongs to.

**Type**: Array of Strings

**Can search the content of this field**: Yes

**Can facet**: Yes

**Can sort**: No

**Can filter**: hasSome, hasAll 

#### onSale

**Description**: Indicates whether the product is on sale.

**Type**: Boolean

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: Yes

**Can filter**: eq, ne

#### discountedPrice

**Description**: Price after a discount has been applied.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: Yes

**Can filter**: in, nin, eq, ne, gt, gte, lt, lte, exists, startsWith 

#### discountedPriceNumeric

**Description**: Numeric representation of the price after a discount has been applied.

**Type**: Double

**Can search the content of this field**: No

**Can facet**: Yes

**Can sort**: Yes

**Can filter**: eq, ne, gt, gte, lt, lte, exists

#### currency

**Description**: Currency of the store product's price.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: Yes

**Can filter**: in, nin, eq, ne, gt, gte, lt, lte, exists, startsWith

#### infoSections

**Description**: Additional information sections for a product.

**Type**: Array of Strings

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: No

**Can filter**: in, nin, eq, ne, gt, gte, lt, lte, exists, startsWith