SortOrder: 2
# Example Flows
This article shares some possible use cases your app could support, as well as an example flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation

## Provider with query limits
1. Wix will understand your provider is using quota limits by setting `quota_enabled` as `true` in your SPI configuraition data.

2. Then call `getQuota` endpoint to get the update amount of available quota.

3. User will enter the desired keyword, and select one of the countries (provided in SPI configuration).

4. While clicking analyze, Wix will call the `listSuggestedKeywords` endpoint.

5. As part of the response, Wix will get the updated quota, and update the UI accordingly.

## Provider without query limits
1. Wix will understand your provider is not using quota limits by setting `quota_enabled` as `false` in your SPI configuraition data.

2. User will enter the desired keyword, and select one of the countries (provided in SPI configuration).

3. While clicking analyze, Wix will call the `listSuggestedKeywords` endpoint.
