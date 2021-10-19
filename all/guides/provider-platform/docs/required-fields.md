SortOrder: 11
# Required Fields

Fields that can be marked as required by a *Payment Service Provider*. Buyers will be required to fill in all required fields during the payment flow.

| Name | Alias in [Dev Centre](https://dev.wix.com) configuration |
|---|---|
| Zip code of the billing address | ORDER:description.billingAddress.zipCode |
| City name of the billing address | ORDER:description.billingAddress.city |
| State of the billing address | ORDER:description.billingAddress.state |
| Billing address | ORDER:description.billingAddress.address |
| Country code of the billing address | ORDER:description.billingAddress.countryCode |
| Email of the billing address | ORDER:description.billingAddress.email |
| Phone of the billing address | ORDER:description.billingAddress.phone |
| First name of the billing address | ORDER:description.billingAddress.firstName |
| Last name of the billing address | ORDER:description.billingAddress.lastName |
| Street of the billing address | ORDER:description.billingAddress.addressDetails.street |
| House number of the billing address | ORDER:description.billingAddress.addressDetails.houseNumber |
| Tax id of the billing address | ORDER:description.billingAddress.taxIdentifier.id |
| CVV for credit/debit card even if it was already used in previous payment | SAVED_CREDIT_CARD:additional_information.cvv |