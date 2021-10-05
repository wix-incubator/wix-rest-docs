SortOrder: 1
# Example Flow: Wix Marketing Tags

This article shares a possible use case your app could support, as well as an example flow. You're certainly not limited to this use case, but it can be a helpful jumping off point as you plan your app's implementation.


## Manage Marketing Tags

Your app could help site owners manage their marketing tags after they have updated their site structure. First, you’ll list the existing tags. Then your app will update the associated domains.


### Step 1: List the Embedded Marketing Tags

First, your app will call the [List Marketing Tags endpoint](https://dev.wix.com/api/rest/marketing/marketing-tags/list-marketing-tags) to retrieve the marketing tags that the owners have previously embedded. 

```sh
curl -X GET \
    https://www.wixapis.com/marketing/v1/tags \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>'
```

In the response of the call, you can see that the associated domains are out-dated, and thus the marketing tags won’t load anymore. 


```json
{"tags": [
    {
        "id": "994ba324-682c-4d81-abd6-84e4be44ba3c",
        "type": "GOOGLE_ADS",
        "enabled": true,
        "google_ads":   {
            "domain": "old-domain.com",
            "tracking_id": "AW-672490861"
        }
    },
    {
        "id": "123ba321-678c-4d81-abd6-84e4be44ba3c",
        "type": "FACEBOOK_PIXEL",
        "enabled": true,
        "facebook_pixel":   {
            "domain": "old-domain.com",
            "tracking_id": "123456789"
        }
    }
]}
```



### Step 2: Update an Embedded Marketing Tag

Then, you’ll do a separate call of the [Upsert Marketing Tags endpoint](https://dev.wix.com/api/rest/marketing/marketing-tags/upsert-marketing-tags) for each tag to change the associated domain. You’ll need to pass the new domain in the body of each call, as shown in the example below for the Google Ads Conversion tag.

```sh
curl -X POST \
    https://www.wixapis.com/marketing/v1/tags  \
    -H 'Content-Type: application/json' \
    -H 'Authorization: <AUTH>'
    -d '{
             "tag": {
                 "enabled": true,
                 "google_ads": {
                  "domain": "new-domain.com",
                  "tracking_id": "AW-672490861",
                 }
               }
             }'
```
