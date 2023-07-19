SortOrder: 0
# Introduction

As a provider of SEO keyword research tools, you can integrate with Wix to enable Wix users to optimize their SEO strategy. 

Using the SEO Keyword Suggestions SPI, you can design your app to:
- Enable Wix users to check the SEO strength of a potential keyword.
- Suggest similar keywords to compare SEO strength.
- Provide analysis about the suggested keywords based on search volume and ranking difficulty.
- Update Wix users about remaining credit in their plan.

## Prerequisites for integration

Create an [app](https://dev.wix.com/dc3/my-apps/) and retrieve its app ID either from the URL or as displayed in the My Apps dashboard in the [Wix Developers Center](https://dev.wix.com/).  

![appId](https://s3.amazonaws.com/wixplorer-readme-images/seo-keyword-suggestions%2FappId-small.jpg "App ID")  

## How to become an SEO keyword suggestion provider

Send an email to this email address `seo-integration@wix.com` to request sign-up. Enter "SEO Keyword Suggestion Integration" as the subject, and provide the following details:  
- Type of business (marketing, web services).  
- A few words about your business and the market you serve.  
- `baseUri`: URL of the site hosting your app.  
- `upgradeUrl`: URL to select a paid plan (optional).  
- `supportedCountryCodes`: Countries supported by your service as a 2-letter country code in [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format.  
- `quotaEnabled`: Whether there is a quota limit for the service.
- `landingPageUrl`: Home page URL for more information.
- ID of the app you created.

Your sign-up request will be reviewed and you will be notified by return email.

## Terminology

 - **Suggested keywords**: Keywords suggested by your app to compare SEO strength of potential keywords and enable optimization of SEO strategy.

- **Quota**: Details of the plan such as credit remaining in terms of number of searches left, total available searches, and start and end dates of the quota cycle.
 