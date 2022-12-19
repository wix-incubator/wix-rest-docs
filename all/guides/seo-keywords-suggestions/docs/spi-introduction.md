SortOrder: 1
# Introduction

SEO keywords are using in services in Wix.

This SPI allowing implement a service provider for keywords suggestion, 
Allowing Wix users to find the strongest keyword options using search volume, ranking difficulty and more. Compare keyword performance and find options that can help you get more traffic.
Service also check for user quota, in case the provider has any limits related to query quota.

The integration is done via an app in the Wix App Market (created in the [Wix Developer Center](https://dev.wix.com/))

Complete the following steps to adapt Wix system's integration to make your delivery methods available to merchants and their customers.

## Prerequisites
1. Create an [app](https://dev.wix.com/apps/) with a Dashboard component.

## Signing up to the Integration
Send an email to this email address: seo-keywords-suggestions-integration@wix.com to request sign-up. Enter "SEO Keywords Suggestions Integration" as the subject, and provide the following details:

1. App ID - from dev.wix.com
2. Configuration data:

|Value|Description|
|---|---|
|Base URL|The URL of the SPI implementation|
|Landing page URL|Provider service landing page to redirect user for more information|
|Upgrade URL (optional)|URL to redirect the user in case they want to purchase a plan, will be used in case `Quota.paid_plan` will be `false`|
|Quota enabled|Signifies if there is a quota limit in the service|
|Supported country codes|List of supported countries to be used once getting the keywords suggestions|

Your sign-up request will be reviewed, and you will be notified by return email.


