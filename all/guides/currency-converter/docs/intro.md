SortOrder: 0
# Currency Converter Service

## About This API
Currency Converter api allows third party apps to get the conversion rate  and convert amounts between currencies
Use this API to:
1. get supported currency list
2. convert an amount to a different currency

#### Learn more about the [service use case](use_case.md)
  
## Permissions

This API requires the following permission:
`CURRENCY_CONVERTER.READ_CURRENCIES`

## Decimal Value explanation
Decimal_Value is made of 2 fields value and decimal places.
value is limited to the number of digits in a "Long" type, 
meaning the value return has a max number of digits of 17.

for example: the number 1.2345678910111213 will be represented in Decimal_Value as
 { 
    value:  12345678910111213
    decimal_places : 16
 }
 
a number that the unscale version is larger then a Long will be cut to fit 17 digits



