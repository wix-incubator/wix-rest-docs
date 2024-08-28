# Bookings Schema for Wix Search

This article describes the Wix Bookings fields you can [search and aggregate](https://dev.wix.com/docs/rest/business-management/search/wix-site-search/search) on a site.

To search or aggregate Wix Bookings services on a site, set the search API `documentType` parameter to `BOOKING_SERVICES`. 


### Fields

#### documentType

**Description**: Document type that was searched. In this case, `BOOKING_SERVICES`.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### \_id

**Description**: Service ID.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### title

**Description**: Service name.

**Type**: String

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: No

**Can filter**: in, eq, ne, gt, ge, lt, le

#### description

**Description**: Service description.

**Type**: String

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### url

**Description**: Service page's link.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### image

**Description**: File source of the image for this service.

**Type**: String

**Can search the content of this field**: No

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### category

**Description**: Category associated with the service.

**Type**: String

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: No

**Can filter**: No 

#### tagLine

**Description**: Service's tagline (subtitle).

**Type**: String

**Can search the content of this field**: Yes

**Can facet**: No

**Can sort**: No

**Can filter**: No

#### staffMembers

**Description**: Staff members associated with the service.

**Type**: Array of Strings

**Can search the content of this field**: Yes

**Can facet**: Yes

**Can sort**: No

**Can filter**: hasSome, hasAll

#### benefits

**Description**: Member benefits.

**Type**: Array of Strings

**Can search the content of this field**: Yes

**Can facet**: Yes

**Can sort**: No

**Can filter**: hasSome, hasAll