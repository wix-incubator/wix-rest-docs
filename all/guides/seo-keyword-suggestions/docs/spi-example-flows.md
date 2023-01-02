SortOrder: 1
# Example Flows
This article shares some use cases your app could support, as well as an example flow that could support each use case. You're certainly not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation

## Configuration Flow

When configuring your app in the JSON Editor of the Wix Dev Center, use the following as a guide:

- `base_uri` - url of your service provider site, as a string

- `upgrade_url` - url to select a paid plan, as a string

- `supported_country_codes` - array of countries supported by your service, as strings

- `quota_enabled` - boolean value signifying if there is a quota limitation for the service

- `landing_page_url` - url to an information page on your site, as a string


# SEO List Suggested Keywords Flow with Quota

A Wix user wishes to determine the strongest SEO keywords for their site. In this case, the quota_enabled parameter is true and a quota object is returned.   

1. The Wix user provides a keyword to Wix to check its SEO strength.

2. Wix builds a List Suggested Keywords request. 

```
{
    "keyword": "pizza",
    "country_code": "US"
}
```

3. The service provider integration triggers the flow and sends the request to the service provider.

Wix expects an object containing the List Suggested Keywords response, and either a 4xx HTTP status code (and some errors) or a 200 HTTP status code.

Example of a successful response:
```
{
    "data":   [
    "keyword": "pizza",
    "volume": "201,000",
    "difficulty": "HARD",
    "latest_trends": [
        0,
        0.06,
        0.16,
        0.07,
        0.66,
        1,
        0.16,
        0.11,
        0.09,
        0.07,
        0.09,
        0.04
      ],
    "searcher_intent": ["COMMERCIAL"]
},
{
    "keyword": "pizza hut",
    "volume": "823,000",
    "difficulty": "MEDIUM",
    "latest_trends": [
        1,
        1,
        1,
        0.81,
        0.81,
        0.66,
        0.81,
        0.81,
        0.66,
        0.66,
        0.66,
        0.66
      ],
    "searcher_intent": ["COMMERCIAL"]
},
{
    "keyword": "pizza express",
    "volume": "301,000",
    "difficulty": "HARD",
    "latest_trends": [
        0.44,
        0.3,
        0.13,
        0.16,
        0.2,
        0.3,
        0.36,
        0.44,
        1,
        0.66,
        0.66,
        0.44
      ],
    "searcher_intent": ["NAVIGATIONAL"]
}
],
  "quota":   {
    "remaining": 4,
    "limit": 10,
    "startDate": "2023-11-04T07:04:35Z",
    "endDate": "2023-11-05T07:04:35Z",
    "isPaidPlan": false,
    "paidPlan": false
  }
} 
```

# SEO List Suggested Keywords Flow without Quota

A Wix user wishes to determine the strongest SEO keywords for their site. In this case, the quota_enabled parameter is false and a quota object is not returned.   

1. The Wix user provides a keyword to Wix to check its SEO strength.

2. Wix builds a List Suggested Keywords request. 

```
{
    "keyword": "pizza",
    "country_code": "US"
}
```

3. The service provider integration triggers the flow and sends the request to the service provider.

Wix expects an object containing the List Suggested Keywords response, and either a 4xx HTTP status code (and some errors) or a 200 HTTP status code.

Example of a successful response:
```
{
    "data":   [
    "keyword": "pizza",
    "volume": "201,000",
    "difficulty": "HARD",
    "latest_trends": [
        0,
        0.06,
        0.16,
        0.07,
        0.66,
        1,
        0.16,
        0.11,
        0.09,
        0.07,
        0.09,
        0.04
      ],
    "searcher_intent": ["COMMERCIAL"]
},
{
    "keyword": "pizza hut",
    "volume": "823,000",
    "difficulty": "MEDIUM",
    "latest_trends": [
        1,
        1,
        1,
        0.81,
        0.81,
        0.66,
        0.81,
        0.81,
        0.66,
        0.66,
        0.66,
        0.66
      ],
    "searcher_intent": ["COMMERCIAL"]
},
{
    "keyword": "pizza express",
    "volume": "301,000",
    "difficulty": "HARD",
    "latest_trends": [
        0.44,
        0.3,
        0.13,
        0.16,
        0.2,
        0.3,
        0.36,
        0.44,
        1,
        0.66,
        0.66,
        0.44
      ],
    "searcher_intent": ["NAVIGATIONAL"]
}],
} 
```









<!-- ## Provider with query limits
1. Wix will understand your provider is using quota limits by setting `quota_enabled` as `true` in your SPI configuration data.

2. Then call `getQuota` endpoint to get the update amount of available quota.

3. User will enter the desired keyword, and select one of the countries (provided in SPI configuration).

4. While clicking analyze, Wix will call the `listSuggestedKeywords` endpoint.

5. As part of the response, Wix will get the updated quota, and update the UI accordingly.

## Provider without query limits
1. Wix will understand your provider is not using quota limits by setting `quota_enabled` as `false` in your SPI configuration data.

2. User will enter the desired keyword, and select one of the countries (provided in SPI configuration).

3. While clicking analyze, Wix will call the `listSuggestedKeywords` endpoint. -->
