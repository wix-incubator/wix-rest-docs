SortOrder: 2
# Validate Endpoint Requests

The requests Wix sends to a Payment Service Provider's (PSP's) endpoints include a header called `"Digest"` whose value is `"JWT="` followed by a [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token) (JWT). This token is included so that the PSP can ensure that the request comes from Wix and hasn't been tampered with.

The token is encrypted using SHA256. The token can be decrypted using the PSP's public webhook key. This key can be [found](https://devforum.wix.com/kb/en/article/find-your-apps-public-key) in the Wix Developers Center. Decrypting the token results in a JSON object with the following format:

```javascript
{
  "data": {
    "SHA256": "5f4b44d3...dae0412016a89b03844e9a7361" // SHA-256 digest of the request body.
  },
  "iat": 1625836375, // Token issue time in seconds since 1970-01-01 00:00:00Z.
  "exp": 1625836475 // Token expiration time in seconds since 1970-01-01 00:00:00Z.
}
```
To validate requests from Wix, the PSP must:
1. Obtain the JWT by extracting the value of the `Digest` header and removing the `JWT=` prefix.  
   Note that header names are case-insensitive, so the `Digest` header can also be called `DIGEST` or `digest`.
1. Validate the signature of the JWT by decrypting it using the PSP's public key.
1. Check that the JWT's `exp` claim hasn't passed. This means the request is still valid.
1. Encode the body of the request received from Wix using SHA256 and compare the result to the value of the JWT's `"data"` claim.
   > **Note:** When calculating the message digest, use the raw bytes of the request body. Do not parse the request body before calculating the message digest. Parsing the request body or converting bytes into text may result in a different message digest, leading to validation failure.

Wix recommends using [jwt.io](https://jwt.io) for debugging purposes.

We created a [code example](https://github.com/wix-incubator/payment-spi-sample/blob/master/jwt-validation.mjs) using Node.js that demonstrates how to validate requests from Wix. You can use this code as a reference when you implement your own validation logic.

