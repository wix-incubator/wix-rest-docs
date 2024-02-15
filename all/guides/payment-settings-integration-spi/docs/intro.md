SortOrder: 0
# About the Wix eCommerce Payment Settings SPI

As a payment settings service provider, you can integrate your service with Wix's payment process to allow merchants to request and use your services on their Wix sites. By integrating your service with Wix, the payment settings that are checked will then apply during the payment process.

The integration is done via an app in the Wix App Market (created in the [Wix Developers Center](https://dev.wix.com/)) and the Wix Payment Settings SPI.  

Learn more about [implementing an SPI with Wix](https://dev.wix.com/api/rest/getting-started/service-provider-interface).

## Before you begin

To collect payments, a Wix site must [connect a payment provider](https://support.wix.com/en/article/connecting-a-payment-provider). Once a payment provider is connected you may use the Payment Settings SPI to enforce 
additional payment settings to a site's transactions. For example, a site may require additional [3d secure payments](https://support.wix.com/en/article/about-3d-secure-3ds-payments-with-third-party-payment-providers) 
(3DS) for certain payment methods.
Note that each payment provider may have specific payment settings they accept with their Wix integration. For example, [Tranzila](https://support.wix.com/en/article/connecting-tranzila-as-a-payment-provider) 
is a payment provider that supports 3DS payments, but not all payment providers offer this feature. We recommend [contacting payment providers directly](https://support.wix.com/en/article/receiving-payouts-from-third-party-payment-providers) 
to confirm which payment settings they have implemented as part of their Wix integration. 

## Use cases

Using the SPI, you can design your app to apply specific settings and send additional information to the payment provider. For example, your app can determine whether to apply 3DS during the payment process. 

## Configuration

To enable Wix to communicate with your app:

1. Go to the [Extensions](https://dev.wix.com/docs/build-apps/developer-tools/extensions/about-extensions) tab in the Wix Developers Center.
2. Click **Create Extension** in the top right.
3. Filter by **eCommerce** in the left menu, then find **Ecom Payment Settings** and click **Create**.
4. Provide the following configuration:

| Name                               | Type    | Description                                                                                                                                               |
|------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `deploymentUri`                    | string  | **Required.** Base URI where the endpoints are called. Wix eCommerce appends the endpoint path to the base URI. For example, to call the Get Payment Settings endpoint at `https://my-payment-settings.com/v1/payment-settings`, the base URI you provide here is `https://my-payment-settings.com`. |
| `componentName`                    | string  | A unique name for this component. This is an internal name that will only appear in the Dev Center.                                                       |
| `fallbackValueForRequires3dSecure` | boolean | The value to set for `paymentSettings.requires3dSecure` if the SPI call fails. Default: `false` |

## Terminology

+ **3 Domain Secure (3DS):** An additional layer of security for online credit and debit card transactions. The name refers to the "three domains" which interact using the protocol: the card issuer, the acquiring bank, and the payment gateway that facilitates the transaction. Learn more [about 3DS payments with third-party payment providers](https://support.wix.com/en/article/about-3d-secure-3ds-payments-with-third-party-payment-providers).
+ **Merchant:** A business that offers products to customers on their Wix site.
+ **Wix site owner:** The person managing the merchant's Wix site.
+ **Payment Settings Service Provider:** A 3rd-party app that implements custom logic to return payment settings.
