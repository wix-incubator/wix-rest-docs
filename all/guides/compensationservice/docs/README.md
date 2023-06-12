SortOrder: 0
# Introduction
 
About Compensation Service

Compensation service provide ability to cover fraudulent chargebacks for WP credit/debit cards 
with permissions checking.

Compensation service operates on Compensation object with following fields:
* String **id**
* String **profile_id**
* String **account_id**
* String **transaction_id**
* String **provider_transfer_id**
* Money **amount**
* CompensationType **compensation_type**
* CompensationStatus **status**

The fields *transaction_id*, *account_id*, *profile_id*, *compensation_type (BRAZIL_CHARGEBACK_COVERAGE)* are mandatory 
for create compensation.

The service provide following methods:
* **createCompensation** - to create compensation and call pagarMe API (see below)
* **queryCompensations** - to find out if the compensation is already done for some transaction

The BO user must have these permissions to do compensations:
* PAYMENTS.BO_COMPENSATION_CREATE
* PAYMENTS.BO_COMPENSATION_READ

**Details of the Pagar.me's API call required to move money between Wix Payments BR accounts:**

* amount (integer): amount (in cents) to be transferred from the Wix Liable account (source) to the merchant account (target). Mandatory
* source_id (string): ID of the account from where we will get the amount to be transferred (Wix Liable Account). Mandatory
* target_id (string): ID of the account that will receive the amount (Merchant Account). Mandatory
* metadata (json): any additional information that can be used for data analysis in the future. Not
mandatory, but in our case maybe we could inform that it's related to CHB coverage
```
curl -X POST https://api.pagar.me/1/transfers -H 'content-type: application/json' -d '{
      "api_key": "WIX_API_KEY",
      "amount": 10000,
      "source_id": "re_cj82qx11u04rdj65zq4q3z16p",
      "target_id": "re_cj5b2mazp00329o6e1xy0hjgs",
      "metadata": {
            "obs": "transferbetweenrecipients"       
      }
}'
```
