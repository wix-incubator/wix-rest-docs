# API Keys

## Introduction

API keys allow users to make API calls to an account or individual site without needing OUath authentication. In addition to the key itself, a set of permissions assigned when the key is created limit the types of API’s that can be accessed with the particular key.

Learn about creating and managing API keys at this [article](https://support.wix.com/en/article/about-wix-api-keys).

> **Note:**
> API keys and this documentation are currently in beta.

## API Requests with API Keys

The API request is constructed in the same way as with regular API requests, but with these changes:
- The API key is used for authentication instead of the OAuth token
- An account ID and/or site ID is added to the header as described below

## Finding Account and Site ID's

### Finding an Account ID

tbd

### Finding a Site ID

Site ID’s can be retrieved using Site List’s **Query Sites** API, described [here](https://bo.wix.com/wix-docs/rest/site-list/site-list/query-sites). This API requires authorization with the API key and an account ID.

## Constructing the Header of the API Request

Construct the header for the API by using the API key for authorization instead of the OAuth token. Note that the API key does not need to be refreshed like the OAuth token.

In addition to authorization, API calls made with an API key require the header to contain the account ID and/or the site ID. 

A complete header for an API request looks like this:

```
curl <GET/POST>\
‘<endpoint>’ \
-H 'Authorization: <APIKEY>’ \
-H wix-account-id:<ACCOUNTID>’ \
-H ‘wix-site-id:<SITEID>’ \
```

The body of the request is the same as for the standard API requests as per the documentation for each.

## Account-Level and Site-Level API Requests

When making API requests with an API key, differentiate between the headers required by account-level and site-level requests.

With requests made at the account level, you must include the account ID in the header along with the API key for authentication. Some API’s will also require the site ID as well. This is indicated in the documentation for each account-level API.

With site-level API requests, the account ID may be ommitted.

### Example: Account-Level “Create Account” API

This API creates a new Wix account as a sub-account of the targetAccountId and a new Wix user in this account who is defined as the account owner.

**Request:**

```
curl POST \
‘https://www.wixapis.com/accounts/v1/accounts/create’ \
-H 'Authorization: <APIKEY>’ \
-H ‘wix-account-id: <ACCOUNTID>’\

--data-binary '{
“User”: {
     “Email”: [{“emailAddress”: “test@example.com”, “isVerified”: “true”}],
     “ssoIdentities”: [{“ssoid”: “test123”, “userid”: “test1234”}]
     “targetAccountId”: “0g44jm7b-4059-4e86-8k3e-d185b1d5s1g7”
}}' \
```

**Response (JSON):**

```json
{
  Account: [
    “accountId”: “0c87cd5d-4059-4e86-8f6e-d185b1e4a1bd”
}
```

### Example: Site Level “Query Products” API in Wix Stores

**Request**:

```
curl POST \
‘https://www.wixapis.com/stores/v1/products/query’ \
-H 'Content-Type: application/json' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Authorization: <APIKEY>’ \
-H ‘wix-site-id: <SITEID>’\

--data-raw '{
“query”: {
     “filter”:
     “sort”: 
     “cursorPaging”:
}}' \
```

**Response (JSON)**:

```json
{
  products: [
   {
   “Id”:
    “Name”:
    etc….
}
```
