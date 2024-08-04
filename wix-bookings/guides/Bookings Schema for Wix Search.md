# Bookings Schema for Wix Search

This article describes the Wix Bookings fields you can [search and aggregate](https://dev.wix.com/docs/velo/api-reference/wix-search-v2/wix-site-search/search) on your site.

To search or aggregate Wix Bookings services on your site, set the search API `documentType` parameter to `BOOKING_SERVICES`. 

>**Note:** 
> The Bookings fields supported by Wix Search are not identical to the fields in your site's [Bookings/Services collection](../Wix%20Bookings%20with%20Velo/Wix%20Bookings%20%22Services%22%20Collection%20Fields.md).

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

**Description**: ?

**Type**: Array of Strings

**Can search the content of this field**: Yes

**Can facet**: Yes

**Can sort**: No

**Can filter**: hasSome, hasAll