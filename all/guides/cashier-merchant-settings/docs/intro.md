SortOrder: 0
# Payment Settings API

Managing and viewing payment settings. It's intended to be used by merchants
only.

## Nomenclature

### Merchant

At Wix we have two types of 'users' - direct users and users of our users (UoU).
In many places and during casual conversations we (at Payments) refer to them
as to merchants and buyers respectively.

### Payment provider

Payment provider (aka payment gateway) is a service that authorises credit card
or direct payments processing. The gateway may be provided by a bank or by a
specialised financial service provider as a separate service.

In a nutshell, payment provider is the services that moves money from a buyer to
the merchant.

Here are few examples of payment providers:

- Wix Payments
- PayPal
- Stripe
- Square
- MercadoPago
- Interkassa
- BitPay

We also have a special payment provider called 'offline' (formally represented
by string `NA` because of historical reasons) which is used for 'cash'
transactions.

In order to get the list of all available payment providers, please use the
Metadata API _(TODO: Add link)_. Keep in mind that the set of available payment
providers depends on the country.

When merchant has connected payment provider it means, that he/she/it has an
account in the provider system and provided us with access to this account.

Account itself can be in different states. For example, `CLAIMED` means that
there are no restrictions on it and we can freely initiate transactions. Any
other status means that account is restricted in some way. For example,
`BLOCKED` means that account was blocked by provider and can't be used by
buyers. Please refer to the documentation of `AccountStatus` for more
information _(TODO: Add link)_.

### Payment method

On the contrary, payment method is the way that a buyer chooses to compensate
merchant. It can either be cash, credit card, PayPal account or some other
Wallet.

During the checkout flow, buyer deals only with payment methods and not with
payment providers

So every payment provider supports at least one payment method. For example, Wix
Payments supports credit cards, iDeal, Sofort and Apple Pay. Square supports
credit cards and point of sale (PoS). TwoCheckout supports only credit cards.

We also have several special payment methods for offline payments (supported
only by offline payment provider): `cash`, `inPerson` and `offline`. Please
checkout the relevant section for more information on the differences between
these payment methods.

In order to get the list of all available payment methods, please use the
Metadata API.

Payment method has three fundamental statuses:

- Not connected - there is no special status for this, but if the payment method
  is missing in the list of available payment methods, then it's not connected.
- Selected - means that the merchant has payment method in question, but has not
  connected any payment provider to it, meaning that it can't be used during
  checkout.
- Connected - means that the payment method has associated payment provider,
  meaning that it can be used during checkout (with respect to the account
  status).
  
![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-selected-vs-connected.png)
  
There is also a special property of every payment method - `showToBuyer`, which
is available only to connected payment methods and just indicates if this
payment method should be available during checkout.

### Payment method and payment provider instances

TODO: please fill me.

## Getting merchant information

In some of the scenarios you might need merchant info. For example, country and
email. This information can be fetched by using
`MerchantInfoService.GetMerchantInfo`. Please refer to its documentation for
more information _(TODO: Add link)_.

### Country

Country (or business location) is a very important piece of data for the
onboarding process. Firstly, it defines the list of available payment methods
and the list of available payment providers. Secondly, merchant must have legal
permissions to process transactions in the country in question.

We **DO NOT** store merchant country in our database. Instead we are using
`SiteProperties` to get the actual value of the country. Users can edit their
business location under general settings in the site dashboard.

In some cases, site properties doesn't contain country. In such cases we have
several fallback scenarios for the country resolving. So country resolving tries
following options step by step and selects the first available option.

1. Business location from site properties (also known as postal address). Fails
   if data is missing.
2. Geo location - based on the IP of the caller. Fails if for some reasons IP is
   not present in the request (aspects). This may happen in some rare scenarios
   when request history involves Kafka and multiple servers. Also this may fail
   if for some reason IP resolves to non-country values like `EU`.
3. Premium billing address. If the user already have a premium (maybe on other
   sites), we get the country from billing address. In most cases this is good
   fallback value. If you buy premium in some country, then most probably your
   business is located there. Fails when there is no premium.
4. Locale - our last resort, taken from site properties. Locale consists of
   country and language. So we use the country part. In should be present in
   100% of situations, but may fail if for some reason we can't reach
   `SiteProperties`
   
Since country resolving may lead to 'invalid' country, we allows users to change
it in **Smart onboarding** flows.

## Onboarding

Onboarding is a process of connecting payment methods and payment providers.

There are several types of onboarding: smart and manual. Read further to get
more information on every type.

Keep in mind, that currently our onboarding process is payment-method-centric.
Which means that in most cases merchant deals with payment methods and not with
payment providers. Which means that merchant connects payment methods and not
payment providers. Which also means that from the merchant point of view,
payment method is something one can configure and not payment provider.

The idea behind is that users are easily overwhelmed by plethora of payment
providers we support. Online payments is already a complex topic by itself and
we want to remove that cognitive overhead as much as possible.

Add to this the fact that we do not support multiple settings for one payment
method, which means that user can't connect Stripe and Square as payment
providers for credit card. By being payment-method-centric we avoid confusion.
Not fully, but this is a topic for another article.

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-1.png)

### Authentication models

Before we dive into onboarding itself, let's cover the authentication models we
are using to access payment provider account data and authorize payments. In
general, we need to have some sort of API keys, which can be provided to us in
three ways.

1. Manual. User types required keys manually in our UI.
2. Redirect. User is redirected to the payment provider site where user can
   confirm connection. This flow is OAuth-like.
3. Automatic connection. When we create an account in the payment provider
   system on behalf of the merchant.

Please note that every provider requires different set of keys. Not only they
have different names, but also they can vary in quantity (e.g. 1, 2 or more).

#### Manual connection

This method is really straight-forward, user just enters required keys in our UI
on the 'Accept Payments' tab and then client sends them to our server, which in
turn validates them against payment provider and persists them in the database.

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-manual-creds.png)
![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-manual-creds.png)

#### Redirect (or oAuth) connection

This flow is much more complex as user doesn't manually provide us with any sort
of keys.

First, user is redirected from our UI to the login page of the payment provider.
There user is prompted to login into the system and then is asked to allow Wix
to access account information.

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-redirect-1.png)
![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-redirect-2.png)

Then the user is redirected back to our server, so we can store API keys and
then user is returned to our UI.

Here is the sequence diagram describing the flow. It fully describes how Stripe
connection works.

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-redirect-creds.png)

This diagram might look overwhelming, but it's really simple. The most important
bit her is that we retrieve API keys from payment provider server. In case of
Stripe when user is redirected to our server we do an additional call to Stripe
server to exchange the code for API keys.

#### Automatic connection

Some of the payment providers (like Wix Payments, PayPal, Stripe and others)
support automatic account creation. This means that we can create an account in
the payment provider system on behalf of the merchant.

We refer to automatically created accounts as to deferred accounts as they have
some restrictions (based on specific payment provider). Usually merchant can get
one transaction and then must complete setup of the deferred account on the
payment provider side. Usually that involves document work.

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-complete-setup.jpg)

Merchant can then switch to other account later if he already has one and don't 
want to use the one created automatically.

### Smart onboarding

Smart onboarding is the onboarding process which requires the merchant to select
few payment methods and let the server to decide what payment providers to
connect.

This is how it looks from the merchant perspective.

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsmart-onboarding-1.png)
![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsmart-onboarding-2.png)
![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsmart-onboarding-3.png)

The procedure is the following:

1. Client calls `PaymentMethodsService.List` to get the information about
   selected and connected payment methods.
2. If the result doesn't have any merchant facing payment methods
   (`isMerchantFacing` field), then it means that merchant didn't connect
   anything yet or disconnected all payment methods. Which means that we should
   begin **Smart onboarding** flow.
3. The merchant is now prompted to select at least one payment method (first
   screenshot).
4. After the merchant clicks *Connect* button, client sends
   `PaymentMethodsService.Connect` with the list of payment methods to connect.
5. The magic begins on the server side. 
   1. Server updates country if necessary.
   2. For every payment method we get the recommended payment provider (based on
      ranking from the Metadata API and the merchants country).
   3. If the payment provider supports *automatic connection*, we create a
      deferred account for the merchant.
   4. All settings are written to the database.
6. After that UI is refreshed and if any deferred account was created, merchant
   is ready to receive payments. Otherwise merchant needs to setup payment
   provider accounts manually.
   
![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsmart-onboarding.png)
   
So after **Smart onboarding** process, the merchant ends up with several payment
methods, some of them may be just in `selected` state, others are connected.

Also it's important to note that **Smart onboarding** screen is the place where
user can select and change business location. Please read further to get some
understanding on how we store and how we resolve the country.

For more information refer to the documentation of the following API:

- `PaymentMethodsService.List`
- `PaymentMethodsService.Connect`

### Manual onboarding

Manual onboarding is a process where merchant manually connects payment method.
It can occur in multiple flavors:

- After smart onboarding some of the payment methods can be in the `selected`
  state, which means that they need to be connected to specific payment
  provider.
- After smart onboarding merchant can manually select any payment methods by
  clicking 'Add Payment Methods' button. After that merchant needs to connected
  specific payment provider.
- Merchant can switch payment provider of already connected payment method.
  While we also call this flow 'manual onboarding' we will cover it later.
  
![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-add-more-1.png)
![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fsettings-add-more-2.png)

This is how the process looks.

![](https://s3.amazonaws.com/wixplorer-readme-images/cashier-merchant-settings%2Fmanual-onboarding.png)

For more information refer to the documentation of the following API:

- `PaymentMethodsService.Connect`
- `PaymentMethodsService.ConnectProvider`

## Updating payment method settings

When payment method is in the `selected` state, nothing actually can be changed.
Well, except for connecting payment provider to it. But it was already covered
in **Manual onboarding** process overview.

Once payment method is in the `connected` state, merchant can toggle the Show to
buyer property.

This can be done using `PaymentMethodsService.Update`. Please refer
to its documentation for more information _(TODO: Add link)_.

## Updating payment provider settings

Once payment method is connected to specific payment provider, merchant can
update some of the settings of payment provider.

This can be done by using `PaymentProvidersService.Update`. Please refer to its
documentation for more information.

Please note that there is important implication of updating settings of payment
provider - if multiple payment methods are connected to one instance of payment
provider, all payment methods will be affected.

## Disconnecting payment method

Every connected payment method can also be disconnected. This can be done by
using `PaymentMethodsService.Delete`. Please refer to its documentation for more
information.

## Offline payment methods

There is a payment provider called `offline`, which is represented in the API as
`NA`. No one really knows why it's called `NA`, but most likely, because there
is no actual payment processing here. Every transactions is treated as
successful. Since we don't know it's status, there is a special transactions
status called `OFFLINE`, which represents this uncertainty. But now transactions
processed using offline payment provider can be approved or declined manually by
the merchant.

Offline payment provider supports three different payment methods.

- `offline` (aka manual) - payment method that is used by most verticals.
  Merchant can configure message that buyers will see on the checkout. Some
  merchants use it as 'cash' payment methods, others just leave instructions on
  how to pay (for example, it can be BTC wallet number, Privat24 instructions
  etc.)
- `cash` - historical payment method that is automatically connected during
  smart onboarding. It is used by Stores and merchant can't configure it. One of
  the non-merchant facing payment methods.
- `inPerson` - special payment method for Bookings that is connected by Bookings
  during checkout. Merchant can't configure it in "Accept Payments". It can be 
  configured in Bookings section of BM. This is fully controlled by Bookings and
  stored on their side.

## Merchant facing payment methods

At the moment all payment methods except for two (`cash` and `inPerson`) are
merchant facing. Which means that they are visible by merchants on the **Accept
payments** tab and can be configured by merchants.

If you are working with UI for merchants, make sure that you ignore non-merchant
facing payment methods. By design they should be hidden!

## Authentication

TL;DR: web clients must provide Meta Site ID in the `Authorization` header and
`wixSession2` cookie.

All of the methods require identity to be present in the request header or
aspects. We are using `ApiGatewayClientV2` in order to extract identities from
request headers or aspects. So you must be compatible with it.

When performing client to server calls, one can provide an identity by sending a
`WixInstance` (aka. `SignedInstance`) in the `Authorization` header. More info
about `WixInstance` can be found on the [developer portal][1].

For example,

```
GET https://www.wix.com/payment-settings-web/onboarding/v1/info
Authorization: MSID.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Cookie: wixSession2=JWT....
```

When performing server to server calls that originated from the client, you
should send `WixInstance` in `Authorization` header in the initial client to
server call. It will be automatically propagated further in the aspects.

When performing server to server calls that were not originated from the client,
one can provide an identity by sending signed server token. More info about
signed server token can be found in this [article][2]. But we don't permit such
flows.

  [1]: https://dev.wix.com/docs/infrastructure/app-instance/#overview
  [2]: https://github.com/wix-private/users/blob/master/identification/identification-api/src/main/proto/docs/Server2Server.md

## Authorization

All of the methods require the caller to have `Cashier.manage` permissions.
  
## HTTP errors

- 401 Unauthorized - means that user context is missing. Make sure that you are
  sending `Authorization` header with meta site identifier in it:
  `MSID.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.
- 403 Forbidden - means that you either didn't provide `wixSession2` cookie
  or you don't have `Cashier.manage` permissions.
- 400 Bad Request - make sure that you followed method's documentation and
  provided valid parameters. Also checkout details field in the response body.
- 500 Internal Server Error - something bad happened on our side. Don't hesitate
  to contact us.

Any request that resulted in an error has a body in the following format:

```json
{
  "message": String,
  "details": Map<String, String>
}
```

Please refer to specific method documentation for more details on the error body.

