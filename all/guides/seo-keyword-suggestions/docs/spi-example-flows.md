SortOrder: 1
# Sample Flows
This article shares some use cases your app could support, as well as a sample flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.



## SEO List Suggested Keywords Flow

A Wix user wishes to determine the strongest SEO keywords for their site. When the `quotaEnabled` parameter is set to `true` in the configuration, you return a quota object in addition to the data object.

1. The Wix user provides a keyword to Wix to check its SEO strength.

2. Wix sends a [List Suggested Keywords](https://dev.wix.com/api/rest/all-apis/seo-keyword-suggestions/spi/list-suggested-keywords) request to your app using the configured `baseUri`. 

    ```json
    {
        "keyword": "pizza",
        "countryCode": "US"
    }
    ```

3. Your app sends a response. 

   Wix expects an object containing either a 4xx HTTP status code (and some errors) or a 200 HTTP status code and the List Suggested Keywords response.

You can see an example of the response in the [List Suggested Keywords](https://dev.wix.com/api/rest/all-apis/seo-keyword-suggestions/spi/list-suggested-keywords) code example. 

## Get Quota Flow

When a Wix user initially opens the SEO page in the Dashboard, Wix requests information about the current quota plan.

1. The Wix user opens the SEO page in the Dashboard.

2. Wix sends a [Get Quota](https://dev.wix.com/api/rest/all-apis/seo-keyword-suggestions/spi/get-quota) request to your app using the configured `baseUri`. No parameters are sent.

3. Your app sends a response. 

   Wix expects an object containing either a 4xx HTTP status code (and some errors) or a 200 HTTP status code and the Get Quota response.

You can see an example of the response in the [Get Quota](https://dev.wix.com/api/rest/all-apis/seo-keyword-suggestions/spi/get-quota) code example. 









<!-- ## Provider with query limits
1. Wix will understand your provider is using quota limits by setting `quotaEnabled` as `true` in your SPI configuration data.

2. Then call `getQuota` endpoint to get the update amount of available quota.

3. User will enter the desired keyword, and select one of the countries (provided in SPI configuration).

4. While clicking analyze, Wix will call the `listSuggestedKeywords` endpoint.

5. As part of the response, Wix will get the updated quota, and update the UI accordingly.

## Provider without query limits
1. Wix will understand your provider is not using quota limits by setting `quotaEnabled` as `false` in your SPI configuration data.

2. User will enter the desired keyword, and select one of the countries (provided in SPI configuration).

3. While clicking analyze, Wix will call the `listSuggestedKeywords` endpoint. -->
