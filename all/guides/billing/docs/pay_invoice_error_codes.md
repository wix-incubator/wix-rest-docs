SortOrder: 1
# Pay Invoice Application Error Codes

## What is it?
In order to start payment process call [invoice pay](/docs//billing/reference/invoices/.com.wixpress.billing.api.v1.-invoice-service.-pay-invoice).
This API can throw an Exception that contains the applicationError.
For example:
**{"message":"Payment failed", 
   "details":
     {"applicationError":
        {"code":"ERR312",
        "description":"This transaction was declined"
        }
     }
  }**



## Error Codes
This is a list of all possible error codes:

code: ERR1,   description: UnexpectedError<br/> 
code: ERR3,   description: ReferenceNotFound<br/> 
code: ERR4,   description: StaleObject<br/> 
code: ERR11,  description: AccessDenied<br/>
code: ERR14,  description: ProductNotAvailableForPurchase<br/> 
code: ERR15,  description: MissingPrice<br/> 
code: ERR16,  description: NegativePriceException<br/> 
code: ERR17,  description: CouponNotApplicable<br/> 
code: ERR18,  description: InvalidInvoiceStatus<br/> 
code: ERR19,  description: NoGatewaysForCurrency<br/> 
code: ERR22,  description: GatewayTransactionNotAuthorized<br/> 
code: ERR23,  description: InvalidCurrencyForSwitchContact<br/> 
code: ERR24,  description: InvalidServiceState<br/> 
code: ERR25,  description: CouponNotValidForDate<br/> 
code: ERR26,  description: CouponNotValidForProduct<br/> 
code: ERR27,  description: CouponNotValidForCycle<br/> 
code: ERR35,  description: CurrencyConversionUpdateFailure<br/> 
code: ERR36,  description: InvalidBillingAccount<br/> 
code: ERR43,  description: UnableToProcessPaymentForCountry<br/>
code: ERR44,  description: CouponMaxUsageReached<br/>
code: ERR47,  description: MissingParameterException<br/>
code: ERR48,  description: NoDefaultBillingAccountForCustomer<br/>
code: ERR49,  description: OrderFormDoublePurchaseAttemptException<br/>
code: ERR50,  description: PurchaseFailedException<br/>
code: ERR51,  description: MissingMandatoryGatewayConfigException<br/>
code: ERR52,  description: CountryCurrencyMappingAlreadyExistsException<br/>
code: ERR53,  description: InvalidEuVatNumberException<br/>
code: ERR54,  description: EuVatServiceError<br/>
code: ERR59,  description: InvoiceNotFoundException<br/>
code: ERR60,  description: InvoiceDoesNotBelongToCustomerException<br/>
code: ERR69,  description: PurchaseBlockedException<br/>
code: ERR70,  description: InvalidPropertyValue<br/>
code: ERR84,  description: CreditPlanNotValidForDate<br/>
code: ERR85,  description: NoAmountForCurrencyInCreditPlan<br/>
code: ERR87,  description: CreditAmountNotAvailable<br/>
code: ERR88,  description: VirtualAmountNotAvailable<br/>
code: ERR91,  description: TransactionDoesNotBelongToInvoiceException<br/>
code: ERR92,  description: PaymentAlreadyPendingException<br/>
code: ERR93,  description: PaymentTechnicalErrorException<br/>
code: ERR94,  description: TooManyPendingSepaPayments<br/>
code: ERR96,  description: ServicePaymentAlreadyPendingException<br/>
code: ERR97,  description: IbanCountryCodeNotSupportedException<br/>
code: ERR99,  description: PaymentMethodNotSupported<br/>
code: ERR100, description: RateDefinitionConflictDetected<br/>
code: ERR101, description: DuplicateConfigurationDetected<br/>
code: ERR103, description: MissingCurrencyRate<br/>
code: ERR104, description: InvalidObjectState<br/>
code: ERR108, description: CouldNotFindCapturedTransaction<br/>
code: ERR112, description: InvalidCpfCnpj<br/>
code: ERR118, description: SwitchContractEventNotFound<br/>
code: ERR119, description: LastTransactionNotFoundException<br/>
code: ERR120, description: ContractSwitchValidationException<br/>
code: ERR125, description: ValidationError<br/>
code: ERR127, description: CouponAssignedNotValid<br/> 
code: ERR128, description: AddressInvalid<br/> 
code: ERR129, description: ZipCodeNotExist<br/> 
code: ERR130, description: ZipAndStateNotMatch<br/> 
code: ERR133, description: InvalidTaxId<br/>

**Declined Error Messages**<br/>
code: ERR300, description: Default Payment Error<br/>
code: ERR301, description: The transaction resulted in an AVS mismatch<br/>
code: ERR303, description: A duplicate transaction has been submitted<br/>
code: ERR305, description: This card is still blocked for use<br/>
code: ERR306, description: This Credit card is blocked for online transactions<br/>
code: ERR307, description: This transaction was not authorized<br/>
code: ERR308, description: This Credit card is expired<br/>
code: ERR310, description: This type of card is not accepted by us<br/>
code: ERR312, description: This transaction was declined<br/>
code: ERR313, description: 3DS authentication failed<br/>
code: ERR314, description: 3DS challenge timeout exceeded<br/>
code: ERR315, description: 3DS challenge cancelled by user<br/>