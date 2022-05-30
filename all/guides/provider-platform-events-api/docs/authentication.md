SortOrder: 1
# Authentication
In order to authenticate with Wix's server during an event request you'll need to use a OAuth bearer token with grant_type: client_credentials.
The request might look like this:
```bash
curl -v -X POST \
  'https://www.wixapis.com/oauth/access' \
  -H 'Content-Type: application/json' \
  -d '{
    "grant_type": "client_credentials",
    "scope": "CASHIER.GET_ACCESS",
    "client_id": "[YOUR_APP_ID]",
    "client_secret": "[YOUR_APP_SECRET_KEY]"
    }'
```
Response:
```bash
{
  "refresh_token": null,
  "access_token": "OAUTH2.eyJraWQiOiJLaUp3NXZpeSIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjoie1wiYXBwSWRcIjpcImIwYWJmMDZhLWJkNWMtNDZhNC05MWU0LTQxZjIwYWI0NTZjZVwiLFwic2NvcGVcIjpbXCJDQVNISUVSLkdFVF9BQ0NFU1NcIl19IiwiaWF0IjoxNTgzMjI4MzMyLCJleHAiOjE1ODMyMjg2MzJ9.FuJMVC3AhJ7gZ8Z6clGlFXZxO0pHz-GRI5kY0YhfzQT2SijAkcpfasQ4r1UBYBZzTW1bzOyKTcSHTBV1n4i5AaPY6CWIq5FRd9V2ukxeYi4eWvo2UVU5bjgr9kvj03QtB26aVjmNCsf3rCsU_wez9kItjjaDwyb7SKzWrmdfz_pZSgWH8G83ieSyaw1DUZjsYGoPMQ4PAttrFVd6_0iVoOoKhSTfET3eqCDN4xTpc5IJk41CKcF5WqIpzfsIlGwQr7exDZGK1Elu617WPmNB6bUvTx8eYNkySygwwf3XbTz05PGXH80C3pYAMKjp6iqwKrojZ-EGdhAv1TapZWEqxA"
}
```
This token is valid for only 1 minute. Therefore, we recommend you generate this token every time you try to make an event request to Wix. Due to security concerns, there is no `refresh_token` for this kind of token.
