SortOrder: 2
## Authentication and Authorization

The support requests POST endpoints are closed under API keys identity with the right permissions. It supports a flow where the caller is a parent account, performing requests on behlaf of it's users (sub accounts).

In terms of the caller, it resolves the identity of an `externalAppIdentity` and will throw `UNAUTHENTICATED` if not found.
In order to authenticate, an account owner must include a JWT `Authentication` header - a token which is obtained while creating an API key with the relevant scope. Furthermore, it must include the `wix-account-id` header of the account owner.

The scope to include while creating an API key: `SCOPE.ACCOUNT.CUSTOMER-CARE`.

In terms of the users who originally requested support, `isPermittd` is called with their Wix account details - only if they are sub accounts of the caller they are granted the permission which was originally created with the API key.

Some parent accounts are allowed to make these requests for users who are anonymous to Wix, i.e., users who don't have a Wix account yet and thus just the caller is verified as an allowed account to perfrom anonymous actions via the API.
