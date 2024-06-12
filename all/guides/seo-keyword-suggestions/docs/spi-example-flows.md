SortOrder: 1
# Sample Flows
This article shares some use cases your app could support, as well as a sample flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.



## SEO List Suggested Keywords Flow

A Wix user wishes to determine the strongest SEO keywords for their site. When the `quotaEnabled` parameter is set to `true` in the configuration, you return a quota object in addition to the data object.

1. The Wix user provides a keyword to Wix to check its SEO strength.

2. Wix sends a [List Suggested Keywords](https://dev.wix.com/api/rest/marketing/seo-keyword-suggestions-spi/list-suggested-keywords) request to your app using the configured `baseUri`. 

    ```json
    {
        "keyword": "pizza",
        "countryCode": "US"
    }
    ```

3. Your app sends a response. 

   Wix expects an object containing either a 4xx HTTP status code (and some errors) or a 200 HTTP status code and the List Suggested Keywords response.

You can see an example of the response in the [List Suggested Keywords](https://dev.wix.com/api/rest/marketing/seo-keyword-suggestions-spi/list-suggested-keywords) code example. 

## Get Quota Flow

When a Wix user initially opens the SEO page in the Dashboard, Wix requests information about the current quota plan.

1. The Wix user opens the SEO page in the Dashboard.

2. Wix sends a [Get Quota](https://dev.wix.com/api/rest/marketing/seo-keyword-suggestions-spi/get-quota) request to your app using the configured `baseUri`. No parameters are sent.

3. Your app sends a response. 

   Wix expects an object containing either a 4xx HTTP status code (and some errors) or a 200 HTTP status code and the Get Quota response.

You can see an example of the response in the [Get Quota](https://dev.wix.com/api/rest/marketing/seo-keyword-suggestions-spi/get-quota) code example. 
