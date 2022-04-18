SortOrder: 1
## Use Cases

Begin using third-party payment services with your Wix integration in three steps:

1. Spot the best payment methods and providers in the desired country.
2. Set up payment provider accounts to sell with Wix via chosen payment methods.
3. Periodically check statuses of your provider accounts to ensure the continuity of your sales.

### Spot the best payment methods and providers in the desired country

#### Check the merchant information

Check the accuracy of country and eligibility to sell with Wix.

```
curl 'www.wixapis.com/cashier/v2/settings/merchant' -H 'Content-Type: application/json' -H 'Authorization: XXX'
```

```json
{
  "merchant": {
    "country": "USA",
    "paymentsAllowed": true,
    "email": "merchant@example.com"
  }
}
```

####  Get a list of payment methods available in the country of merchant

Check `recommendations` attribute, where you can find:

- The list of available payment methods
- Available payment providers for each payment method accordingly (sorted by recommendation)

```
curl 'www.wixapis.com/cashier//v2/settings/payment-method-types' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```

```json
{
  "methodTypes": [
    {
      "id": "creditCard",
      "title": "Credit/Debit Cards",
      "description": "Accept payments with credit and debit cards. Fees vary between payment providers.",
      "icon": {
        "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-methods/onboarding/svg/creditCard.svg"
      },
      "paymentProviderInfos": [
        {
          "paymentProviderId": "com.wix.wixpay.us"
        },
        {
          "paymentProviderId": "com.stripe"
        },
        {
          "paymentProviderId": "com.square"
        },
        {
          "paymentProviderId": "com.braintreegateway"
        },
        {
          "paymentProviderId": "239e7846-6f6c-4801-86bc-d14b9151c534"
        }
      ],
      "promoted": true
    },
    {
      "id": "pinWheel",
      "title": "Pinwheel",
      "description": "Accept credit/debit cards from customers around the world, including for high-risk businesses.",
      "icon": {
        "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-methods/onboarding/svg/pinWheel.svg"
      },
      "paymentProviderInfos": [
        {
          "paymentProviderId": "239e7846-6f6c-4801-86bc-d14b9151c534"
        }
      ],
      "promoted": false
    },
    {
      "id": "offline",
      "title": "Manual",
      "description": "Accept cash, check or other custom forms of payment.",
      "icon": {
        "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-methods/onboarding/svg/offline.svg"
      },
      "paymentProviderInfos": [
        {
          "paymentProviderId": "NA"
        }
      ],
      "promoted": true
    },
    ...
  ]
}
```

#### Get a list of payment providers available in the country of merchant

```
curl 'www.wixapis.com/cashier/v2/settings/payment-providers' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```

```json
{
  "providers": [
    {
      "id": "com.stripe",
      "title": "Stripe",
      "paymentMethodTypeInfos": [
        {
          "paymentMethodTypeId": "creditCard",
          "fee": {
            "formattedMinimumFee": "2.9% + 30¢"
          },
          "supportRecurring": true,
          "brands": [
            {
              "title": "Visa",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-visa.svg"
              }
            },
            {
              "title": "MasterCard",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-mastercard.svg"
              }
            },
            {
              "title": "Amex",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-amex.svg"
              }
            },
            {
              "title": "ChinaUnionPay",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-chinaunionpay.svg"
              }
            },
            {
              "title": "Jcb",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-jcb.svg"
              }
            },
            {
              "title": "Diners",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-diners.svg"
              }
            },
            {
              "title": "CartesBancaires",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-cartesbancaires.svg"
              }
            },
            {
              "title": "Discover",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-discover.svg"
              }
            },
            {
              "title": "Electron",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-electron.svg"
              }
            },
            {
              "title": "Maestro",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-maestro.svg"
              }
            }
          ]
        },
        {
          "paymentMethodTypeId": "iDeal"
        },
        {
          "paymentMethodTypeId": "sofort"
        },
        {
          "paymentMethodTypeId": "alipay",
          "fee": {
            "formattedMinimumFee": "2.9% + 30¢"
          }
        },
        {
          "paymentMethodTypeId": "bancontact"
        }
      ],
      "accountConnection": {
        "oauthConnect": {},
        "oauthCreate": {},
        "oauthClaim": {}
      },
      "links": {
        "wixHelpUrl": "https://support.wix.com/en/article/setting-up-stripe-as-a-payment-gateway-2085625",
        "providerHelpUrl": "https://support.stripe.com/"
      },
      "icon": {
        "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-providers/svg/com.stripe.svg"
      }
    },
    {
      "id": "NA",
      "title": "Offline Payments",
      "paymentMethodTypeInfos": [
        {
          "paymentMethodTypeId": "offline"
        },
        {
          "paymentMethodTypeId": "cash"
        },
        {
          "paymentMethodTypeId": "inPerson"
        },
        {
          "paymentMethodTypeId": "posCash"
        }
      ],
      "accountConnection": {
        "directConnect": {}
      },
      "links": {
        "wixHelpUrl": "",
        "providerHelpUrl": ""
      }
    },
    {
      "id": "239e7846-6f6c-4801-86bc-d14b9151c534",
      "title": "Pinwheel",
      "paymentMethodTypeInfos": [
        {
          "paymentMethodTypeId": "pinWheel",
          "fee": {
            "formattedMinimumFee": "2.9% + 20¢"
          }
        },
        {
          "paymentMethodTypeId": "creditCard",
          "fee": {
            "formattedMinimumFee": "2.9% + 20¢"
          },
          "brands": [
            {
              "title": "Visa",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-visa.svg"
              }
            },
            {
              "title": "MasterCard",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-mastercard.svg"
              }
            },
            {
              "title": "Amex",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-amex.svg"
              }
            },
            {
              "title": "ChinaUnionPay",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-chinaunionpay.svg"
              }
            },
            {
              "title": "Jcb",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-jcb.svg"
              }
            },
            {
              "title": "Diners",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-diners.svg"
              }
            },
            {
              "title": "Discover",
              "icon": {
                "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-brands/svg/brand-discover.svg"
              }
            }
          ]
        }
      ],
      "accountConnection": {
        "directConnect": {
          "credentialsFields": [
            {
              "name": "creditCard",
              "description": "Username"
            },
            {
              "name": "password",
              "description": "Password"
            }
          ]
        },
        "directCreate": {
          "directUrl": "https://pinwheelpay.com/"
        }
      },
      "links": {
        "wixHelpUrl": "https://support.wix.com/en/article/connecting-pinwheel-as-a-payment-provider",
        "providerHelpUrl": "https://pinwheelpay.com/contact-us.php"
      },
      "icon": {
        "url": "https://images-wixmp-6613fa290e8c1ac70a0297b6.wixmp.com/payment-providers/svg/239e7846-6f6c-4801-86bc-d14b9151c534.svg"
      }
    }
    ...
  ]
}
```

### Set up payment provider accounts to sell with Wix via chosen payment methods

Workflow:

1. Choose the desired combination of payment method and provider as described above.
2. Call `Get Payment Providers` with the payment provider of choice and check the `onboarding` attribute that defines the establishment of a connection.
    - For a direct type connection, call `Connect Provider Account Directly` with credentials that the payment provider issues.
    - For an OAuth type connection, call `Connect Provider Account OAuth` and follow the link returned in response to finalize the connection.

When the payment provider account is connected, you will be returned to the `returnUrl`, passed in the initial call.

3. Check the Provider Account Created Domain Event. Payment Provider Account object will indicate the payment provider's connection status, ability to receive payments and payouts, and required actions (if any).

#### Add payment provider account with Direct Connection

Send credentials as required in the onboarding of payment provider metadata.

```
curl -X POST \
   'www.wixapis.com/cashier/v2/settings/provider-accounts/direct-connect' \
        --data-binary '{
                     "paymentProviderId": "239e7846-6f6c-4801-86bc-d14b9151c534",
                     "credentials": {
                       "username": "merchant@example.com ",
                       "password": "xxxxxxxxxxxxxxxx"
                     },
                     "installments": null,
                     "paymentMethodTypeIds": [
                       "pinWheel"
                     ]
                   }' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```

```json
{
  "providerAccounts": [
    {
      "id": "239e7846-6f6c-4801-86bc-d14b9151c534",
      "paymentProviderId": "239e7846-6f6c-4801-86bc-d14b9151c534",
      "payinsAllowed": true,
      "payoutsAllowed": true,
      "status": "OK",
      "providerAccountName": "Test******",
      "additional": {},
      "paymentMethodTypeSetups": [
        {
          "paymentMethodTypeId": "pinWheel",
          "enabled": true
        }
      ]
    }
  ]
}
```

#### Add payment provider with OAuth connection

```
curl -X POST \
   'www.wixapis.com/cashier/v2/settings/provider-accounts/oauth-connect' \
    --data-binary '{
                     "paymentMethodTypeIds": ["creditCard"],
                     "paymentProviderId": "com.stripe",
                     "returnUrl": "https://www.wix.com/dashboard/2xxxx-28f3-4154-b27c-xxxxxx/payments/methods"
                   }' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```

```json
{
  "redirectUrl": "/_api/payment-services-web/merchant/stripe/connect/start/login?appDefId=14bca956-e09f-f4d6-14d7-466cb3f09103&appInstanceId=66056ce8-c750-4e00-ae43-0313d26ebdb1&paymentMethod=creditCard&returnUrl=https://www.wix.com/dashboard/2xxxx-28f3-4154-b27c-xxxxxx/payments/methods"
}
```

In a case an error occurs during an OAuth flow, such error is reported as `errorCode` GET-parameter and added to `return_url`.

Possible values:

- `29` Generic connect complete error. Merchant declined to proceed with OAuth connect flow.
- `30` Authorization grant declined by the merchant.

#### Create payment method for added payment provider account

```
curl -X PATCH \
   'www.wixapis.com/cashier/v2/settings/provider-accounts/com.stripe/payment-method-type-setup/pinWheel' \
    --data-binary '{
                     "paymentMethodTypeSetup": {
                       "instructions": null,
                       "enabled": true,
                       "paymentMethodTypeId": "pinWheel"
                     },
                     "providerAccountId": "239e7846-6f6c-4801-86bc-d14b9151c534"
                   }' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```

```json
{
  "providerAccount": {
    "id": "239e7846-6f6c-4801-86bc-d14b9151c534",
    "paymentProviderId": "239e7846-6f6c-4801-86bc-d14b9151c534",
    "payinsAllowed": true,
    "payoutsAllowed": true,
    "status": "OK",
    "providerAccountName": "Test******",
    "additional": {},
    "paymentMethodTypeSetups": [
      {
        "paymentMethodTypeId": "pinWheel",
        "enabled": true
      }
    ]
  }
}
```

### Enable/disable payment methods at the checkout

Call Update Provider Account Payment Method and pass `enabled` property for the payment method of choice.

```
curl -X PATCH \
   'www.wixapis.com/cashier/v2/settings/provider-accounts/com.stripe/payment-method-type-setup/creditCard' \
    --data-binary '{
                     "paymentMethodTypeSetup": {
                       "instructions": null,
                       "enabled": false,
                       "paymentMethodTypeId": "creditCard"
                     },
                     "providerAccountId": "com.stripe"
                   }' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```

```json
{
  "providerAccount": {
    "id": "com.stripe",
    "paymentProviderId": "com.stripe",
    "payinsAllowed": true,
    "payoutsAllowed": true,
    "status": "OK",
    "providerAccountName": "Stri******",
    "additional": {},
    "paymentMethodTypeSetups": [
      {
        "paymentMethodTypeId": "creditCard",
        "enabled": false
      }
    ]
  }
}
```


### Periodically check the status of added provider accounts to ensure continuity of sales

Periodically call `List Provider Accounts` and monitor the status of Provider Accounts, as well as:

- Payments status
- Payouts status
- Required Actions

```
curl 'www.wixapis.com/cashier/v2/settings/provider-accounts' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```

```json
{
  "providerAccounts": [
    {
      "id": "239e7846-6f6c-4801-86bc-d14b9151c534",
      "paymentProviderId": "239e7846-6f6c-4801-86bc-d14b9151c534",
      "payinsAllowed": true,
      "payoutsAllowed": true,
      "status": "OK",
      "providerAccountName": "Test******",
      "additional": {},
      "paymentMethodTypeSetups": [
        {
          "paymentMethodTypeId": "pinWheel",
          "enabled": true
        }
      ]
    },
    {
      "id": "com.stripe",
      "paymentProviderId": "com.stripe",
      "payinsAllowed": true,
      "payoutsAllowed": true,
      "status": "OK",
      "providerAccountName": "Stri******",
      "additional": {},
      "paymentMethodTypeSetups": [
        {
          "paymentMethodTypeId": "creditCard",
          "enabled": false
        }
      ]
    }
  ]
}
```
### Enable/disable payment methods at checkout

Call `Update Provider Account Payment Method` and pass `enabled` property for the payment method of choice.

```
curl -X PATCH \
   'www.wixapis.com/cashier/v2/settings/provider-accounts/com.stripe/payment-method-type-setup/creditCard' \
    --data-binary '{
                     "paymentMethodTypeSetup": {
                       "instructions": null,
                       "enabled": true,
                       "paymentMethodTypeId": "creditCard"
                     },
                     "providerAccountId": "com.stripe"
                   }' \
   -H 'Content-Type: application/json' \
   -H 'Authorization: <AUTH>'
```

```json
{
  "providerAccount": {
    "id": "com.stripe",
    "paymentProviderId": "com.stripe",
    "payinsAllowed": true,
    "payoutsAllowed": true,
    "status": "OK",
    "providerAccountName": "Stri******",
    "additional": {},
    "paymentMethodTypeSetups": [
      {
        "paymentMethodTypeId": "creditCard",
        "enabled": true
      }
    ]
  }
}
```
