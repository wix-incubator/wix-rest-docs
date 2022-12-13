# About API Keys

API keys allow you to make API calls at the account and site level while bypassing OAuth authentication. 

<blockquote class="important">

__Important:__
API Keys are currently available to selected beta users only.

</blockquote>

[API keys](https://support.wix.com/en/article/about-wix-api-keys) are created and managed in the [API Keys Manager](https://manage.wix.com/account/api-keys) where you can assign a set of permissions that determine the types of APIs the key can access.

![API Keys Manager](./../../media/APIKeysManager.jpg)



## Creating and Using API Keys

1. Create or request an API key:  
     a. If you have direct access to the site, create a key with the relevant permissions in the [API Keys Manager](https://manage.wix.com/account/api-keys). Collect the key and the account ID.  
     b. If you don't have direct access to the site, request the key and the account ID from the site owner.  
2. Call the Site API's **Query Sites** endpoint to collect all the account's associated site IDs.

    > **Note:**
    > The site ID for a current site can be obtained from the site URL in your browser.
    > For example, the site ID appears after the '/dashboard/' part of this URL: <br />
    > <br />
    > ![site Id in URL](./../../media/siteid.png)

     

     a. Enter the API key in the authorization header. Note that the API key does not need to be refreshed.  
     b. Enter the account ID in the account ID header, as shown below. (In other calls, the site ID header may be required. Refer to the documentation for each specific call.)

     A complete header for an API request looks like this:

     ```
     curl <GET/POST>\
     ‘<endpoint>’ \

     -H 'Authorization: <APIKEY>' \
     -H 'wix-account-id: <ACCOUNTID>' \
     -H 'wix-site-id: <SITEID>' \
     ```
3. Make all following calls using the account ID and/or site ID, as required.

## Account-Level and Site-Level API Requests
     
Depending on the call, an account ID and/or site ID must be included in the header of the API request.

For requests made exclusively at the account level, you must include the account ID in the header along with the API key for authentication. Some endpoints will require the site ID as well. This is indicated in the documentation for each account-level API.

With site-level API requests, the account ID can be ommitted.

### Sample Request: Site Folders API - Create Folder

This API creates a new folder that can hold Wix sites. 

**Request:**

```
curl POST \
'https://www.wixapis.com/site-folders/v2/folders \
-H 'Authorization: <APIKEY>' \
-H 'wix-account-id: <ACCOUNTID>\
{ "folder": {"name": "My Folder", "parentId": "root"}}' \
```

**Response:**

```
{"folder": {
  "id": "283f4660-8f6f-462b-94a1-160a57338032",
  "name": "My Folder",
  "createdDate": "2021-12-13T11:33:56.973Z",
  "updatedDate": "2021-12-13T11:33:56.973Z",
  "siteCount": 0,
  "parentId": ""
}} 
```

### Sample Request: “Query Products” API

This API retrieves a list of products from one of the account's sites. To make this call, you'll need an API key and the ID of the site you want to query.

**Request:**

```
curl POST \
'https://www.wixapis.com/stores/v1/products/query' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Authorization: <APIKEY>' \
-H 'wix-site-id: <SITEID>'\

-d '{
"query": {
     "filter":"{\paymentStatus\":\"PAID\"},
     "sort':"{\"number\": \"desc\"}",
     "paging": {
          "limit":"50"
     }
}}' \
```

**Response:**

```json:
{
  products: [
   {
   "Id": "5376f9ec-b92e-efa9-e4a1-f4f480aa0d3a",
    "Name": "Indian Blend Coffee",
    "Size:": "1 lb",
    "Price": "4.35",
    etc….
}
```
