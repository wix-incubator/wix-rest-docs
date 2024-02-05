SortOrder: 0
# Account Server

## Accounts intro

### Definition

An account is a set of one or more Wix registered users, and possesses a set of assets: sites, domains, premium plans, etc.
A simple way of thinking about it is as an entity to which a Wix user logs in. Each Wix user can be registered to one account only.
When registering in the regular flow (not through an account invite) each new Wix user belongs to a single auto-generated account, where `accountId` equals to his `userId`, and is the account owner.
Each account has a single `accountOwner` - some Wix User.

### Motivation

The idea behind accounts comes from the need to manage teams of web designers and web design agencies,
the roles and permissions of each team member within an account, and managing Wix assets (sites, domains, logos, etc.) by the agencies for second-party customers.

### Entities: accounts, users and assets

Each Wix _asset_, such as a Wixsite, a domain or a premium plan, belongs to an account **and not to a User**.
For instance: a siteOwner is the `accountId`, and a free site's domain looks like: `account-slug.wixsite.com/some-site`.
The relation between Wix users and accounts is one-to-many: each account can contain multiple users (obviously),
but each user can belong to only one account.

As mentioned - an account can have one or more users in in (team members). An account can be marked as a 'team account' - regardless to the amount of members in it. The account has a _isTeam_ flag that marks the fact that this is a team account. An account that is marked with this flag has some extra capabilities (partners related).  

**Example:**
A Wix user, Alice, works for "Westeros Web-builders" agency as a web designer: she can log in to the Westeros account.
There are many more team members (Wix users) in this agency, they have different roles (admins, web-designers, content-writers, etc.) in the account.
All sites developed by Westeros agency have either Westeros account as a site-owner, or a customer account as a site-owner where Westeros have some contributor permissions on.

### Backward compatibility

A migration was made: for every existing Wix user an account was created, such that `accountId = userId`, `accountOwner = userId` and the user is the only one in the account.

This way no migration had to be made to wixsites' site owners: a site owner is now the account, and not the user, but the accountId is the same as the userId.

## Account Server overview

### General

A platformized Loom service, operating in production since October 2019, known as `com.wixpress:account-server` artifact.

It's the `account` CRUD service, which also manages the relations between users and accounts.

For questions please reach us on [#identity](https://wix.slack.com/archives/CKCMNK95F)

### Api

The service exposes and implements 4 logical sub-services (only three are relevant and will be described here):

1. `TeamService` - manage users in a team (account)
2. `AccountService` - CRUD operations on accounts, and query accounts per user
3. `AccountBackOfficeService` - backoffice operations on account level

For usage please import:
`//account/account-api/src/main/proto:proto_scala`

### Testkit

[AccountMatchers](https://github.com/wix-private/users/blob/master/account/account-testkit/src/main/scala/com/wixpress/account/testkit/AccountMatchers.scala) are available.

Import: `//account/account-testkit/src/main/scala/com/wixpress/account/testkit:testkit`