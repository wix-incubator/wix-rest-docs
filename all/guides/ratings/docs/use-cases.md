SortOrder: 1
# Ratings: Sample Use Cases and Flows

This article shares some possible use cases your app can support. You are not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.

## Real-time 2-way sync with an external system

Site owners can use your app to keep ratings from an external system up to date with their ratings on Wix with a two-way sync. To synchronize Wix and an external system, think about how your app will handle these flows:

- Initial setup
- Synchronize to external site
- Synchronize from external site

### Initial setup

Create mappings for the following from the Wix site to the external system using common fields so the ratings can be synced:
- Wix site groups and entities to groups and entities on the external system.
- Wix site contact IDs to IDs on the external system, for example using email addresses.  
- Wix rating field to the rating field on the external system.  

Store the mappings on your app's server. Then follow these flows to create the two-way sync.

### Synchronize to the external system

Listen for a change in Wix ratings with the following webhooks:

- [Rating Created Webhook](https://dev.wix.com/api/rest/ratings/rating-created-webhook).
- [Rating Updated Webhook](https://dev.wix.com/api/rest/ratings/rating-updated-webhook).
- [Rating Deleted Webhook](https://dev.wix.com/api/rest/ratings/rating-deleted-webhook).

When one of the webhooks is triggered,
you'll receive the rating in the payload.
You can send those changes to the external system with a flow like this one:

1. Get the `slug` (which tells you what the event was),
    `entityId` (ID of item rated),
    and other relevant information from the payload data.

2. Use the mappings (from the [initial setup](#initial-setup))
    to send the relevant information to the external system.

3. Ignore the resulting event from the external system
    so you don’t create an endless loop of updates.

### Synchronize to Wix

Listen for rating events from the external system.
When your app receives a change it needs to synchronize,
follow this basic flow:

1. Use the [Contacts API](https://dev.wix.com/api/rest/contacts) to check if the creator of the rating has a contact ID on the Wix site. 

2. Use the mappings from the [initial setup](#initial-setup)
    to check if the site already has a rating from the contact for the attributes in each rating from the external system. The Ratings API allows only one rating for each attribute per rating owner. Duplicate ratings receive an error response.  
    
3. Use the mappings from the [initial setup](#initial-setup) to send the rating to the 
    [Create Rating](https://dev.wix.com/api/rest/ratings/create-rating) endpoint.

4. Ignore the resulting event from Wix
   so you don’t create an endless loop of updates.

<!-- ## Export Product Ratings

1. Invoke QueryRating API:

```
{
    "query":{
        "filter":{
            "namespace": "reviews",
            "group": "stores",
            "entityId": "<product-id>"
        },
        "cursorPaging":{
            "limit":10
        }
    }
}
```

Replace `<product-id>` with actual product id you wish to export Ratings

2. To get next page use nextCursor which is in response of previous page. Next page request might look similar to example below

```
{
    "query":{
        "cursorPaging":{
            "limit": 10,
            "cursor": "5iKtPmVjdbk9BVMBXgz15i6BXPpoT0QM/TBOTBY7AMw="
        }
    }
}
```


## Importing Stores Product Ratings from external system

1. Export ratings from external service
2. For each exported Rating invoke CreateRating API with such parameters:

```
{
    "namespace": "reviews",
    "group": "stores",
    "entityId": "<product-id>",
    "attributeName": "overall",
    "value": <rating-value>,
    "ratingOwner": 
    {
      "contactId": "<contact-id>"
    }
}
```

This will create Ratings and they will be visible in your product page ( only if you're using Wix Reviews ) -->

