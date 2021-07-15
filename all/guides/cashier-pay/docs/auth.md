SortOrder: 2
# Authentication

Most of the methods of `pay-api` require identity to be present in the request
header or aspects. We are using `ApiGatewayClientV2` in order to extract
identities from request headers or aspects. So you must be compatible with it.

When performing client to server calls, one can provide an identity by sending a
`WixInstance` (aka. `SignedInstance`) in the `Authorization` header. More info
about `WixInstance` can be found on the [developer portal][1].

When performing server to server calls that originated from the client, you
should send `WixInstance` in `Authorization` header in the initial client to
server call. It will be automatically propagated further in the aspects.

When performing server to server calls that were not originated from the client,
one can provide an identity by sending signed server token. More info about
signed server token can be found in this [article][2].

  [1]: https://dev.wix.com/docs/infrastructure/app-instance/#overview
  [2]: https://github.com/wix-private/users/blob/master/identification/identification-api/src/main/proto/docs/Server2Server.md

# Authorization

Please refer to each method's documentation for information on authorization
rules.

In general, there are three rules:

1. A method is available for any person or a server.
2. A method is available only for a site owner, or buyer related to specific
   data (e.g. order).
3. A method is available only for a site owner, or buyer related to specific
   data (e.g. order), or a server.
