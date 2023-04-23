# About the Resources Available in this Reference


## REST APIs 
A collection of API calls and events, based on Wix's databases, that can be used by any integration that is:
- installed on a site using standard HTTPS terminology   
AND EITHER
- [OAuth authentication](https://dev.wix.com/api/rest/getting-started/authentication),  
OR
- using [API Keys]().  

**Why this is available as an API**: Because the relevant information is stored in Wix's databases, which we're making available to you.

## REST SPIs 
A collection of SPI calls and events, based on the SPI hosts' databases, that can be implemented by any integration that is:
 - installed on a site using [OAuth authentication](https://dev.wix.com/api/rest/getting-started/authentication) 
 - set up SPI configuration (currently this requires reaching out to the relevant SPI owner specified in each SPI's documentation).  

**Why this is available as an SPI**: Because we want you to be able to push information from your databases into the Wix platform. There is no Wix database storing the relevant information. 

## Client-side JS APIs
A collection of APIs and events, based on Wix's databases, that can be used by any integration that is:
- installed on a site using standard HTTPS terminology and [OAuth authentication](https://dev.wix.com/api/rest/getting-started/authentication) 
- injects JavaScript into a Wix site using the [Embedded Script component](https://devforum.wix.com/en/article/about-embedded-script-components).  

**Why this is available as a client-side API**: Because the relevant information is triggered directly in the live Wix site.
