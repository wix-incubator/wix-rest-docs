SortOrder: 0
# Introduction

As a provider of SEO keyword research tools, you can integrate with Wix to enable Wix users to optimize their SEO strategy. 

Using the SEO Keyword Suggestions SPI, you can design your app to:
- Enable Wix users to check the SEO strength of a potential keyword.
- Suggest similar keywords to compare SEO strength.
- Provide analysis about the suggested keywords based on search volume and ranking difficulty.
- Update Wix users about remaining credit in their plan.


 ## How to become a keyword suggestions provider

- Create an [app](https://dev.wix.com/apps/) with an integration component. 

- Configure your app in the JSON Editor of the Wix Dev Center. For more information about SPI integration setup, see Service Provider Interface [Setup](https://dev.wix.com/api/rest/getting-started/service-provider-interface#getting-started_service-provider-interface_setup).
  - `baseUri`: String. URL of your site.
  - `upgradeUrl`: String. URL to select a paid plan.
  - `supportedCountryCodes`: Array of strings. Countries supported by your service. 2-letter country codes in [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format.
  - `quotaEnabled`: Boolean. Whether there is a quota limit for the service.
  - `landingPageUrl`: String. URL of your website.


## Terminology

 - **Suggested keywords**: Keywords suggested by your app to compare SEO strength of potential keywords and enable optimization of SEO strategy.

- **Quota**: Details of the plan such as credit remaining in terms of number of searches left, total available searches, and start and end dates of the quota cycle.
 

 
<!-- # Complete the following steps to adapt Wix system's integration to make your SEO tools available to Wix users.

# This SPI allowing implement a service provider for keywords suggestion, 
# Allowing Wix users to find the strongest keyword options using search volume, ranking difficulty and more. Compare keyword performance and find options that can help you get more traffic.
# Service also check for user quota, in case the provider has any limits related to query quota.

# The integration is done via an app in the Wix App Market (created in the [Wix Developer Center](https://dev.wix.com/))

# Complete the following steps to adapt Wix system's integration to make your delivery methods available to merchants and their customers. -->

<!-- ## Prerequisites -->
<!-- Create an [app](https://dev.wix.com/apps/) with a Dashboard component. This component represents the SEO dashboard page to add to the Wix user's site. -->

<!-- ## Signing up to the Integration




# Send an email to this email address: seo-keywords-suggestions-integration@wix.com to request sign-up. Enter "SEO Keywords Suggestions Integration" as the subject, and provide the following details:

1. App ID - from dev.wix.com
2. Configuration data:

|Value|Description|
|---|---|
|Base URL|The URL of the SPI implementation|
|Landing page URL|Provider service landing page to redirect user for more information|
|Upgrade URL (optional)|URL to redirect the user in case they want to purchase a plan, will be used in case `Quota.paid_plan` will be `false`|
|Quota enabled|Signifies if there is a quota limit in the service|
|Supported country codes|List of supported countries to be used once getting the keywords suggestions|

Your sign-up request will be reviewed, and you will be notified by return email. -->


