SortOrder: 0
# Introduction

As a provider of SEO keyword research tools, you can integrate with Wix to enable Wix users to optimize their SEO strategy. 

Using the SEO Keyword Suggestions SPI, you can design your app to:
- Enable Wix users to check the SEO strength of a potential keyword.
- Suggest similar keywords to compare SEO strength.
- Provide analysis about the suggested keywords based on search volume and ranking difficulty.
- Update Wix users about remaining credit in their plan.

## How to become an SEO keyword suggestion provider

To become an SEO keyword suggestion provider,
[add the **Seo Keywords Suggestions** extension](https://dev.wix.com/docs/rest/articles/getting-started/service-provider-interface#configure-an-extension-in-the-development-center)
in your app's configuration in Wix Developers Center.

Provide the necessary configuration for your app:

| Name                    | Type          | Description                                                                                                                                                                                           |
| ----------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `baseUri`               | string        | **Required.** Base URL of your SEO implementation. Wix sends API requests to endpoints implemented using this URL.                                                                                                  |
| `upgradeUrl`            | string        | URL of the page where users can purchase a paid plan. Wix offers a link to this page when you respond with a value of `false` in quota's `paidPlan` property.                                         |
| `supportedCountryCodes` | array<string> | **Required.** List of countries you support for SEO analysis. 2-letter country code in [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format. |
| `quotaEnabled`          | boolean       | Whether there is a quota limit in the service. When set to true, include the quota object in responses.                                                                                               |
| `landingPageUrl`        | string        | **Required.** Your website's landing page.                                                                                                                                                            |

## Terminology

 - **Suggested keywords**: Keywords suggested by your app to compare SEO strength of potential keywords and enable optimization of SEO strategy.

- **Quota**: Details of the plan such as credit remaining in terms of number of searches left, total available searches, and start and end dates of the quota cycle.
 
