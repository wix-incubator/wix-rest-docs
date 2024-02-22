SortOrder: 0

# Billing (aka Billing As A Service)

## What is it?
Billing service exposes basic billing features, such as product 
catalog with pricing, invoices management, orders, payments and services.
Billing notifications integration is done via SBS (Wix Billing System).
Please contact the team at #billing-discussions


![](https://s3.amazonaws.com/wixplorer-readme-images/billing%2FBillingGatewayDiagram.png)


## Onboarding
Billing service supports only known appDefIds, the reason for it is because Billing service is a multi-tenant 
service and it treats each **appDefId** as a different tenant. <br/>
First of all you have to define your app at https://dev.wix.com and come to us with the appDefId.
We will add the appDefId to the white list and define a **productClass**, a **productAction** and a **vendor** internally in the 
Wix Billing System (aka **SBS**) for you. <br/>
Note also that the Billing service supports only WIX users.

## What is the correct flow to work with Billing service?
Following chapters will give you a basic idea about Billing service features and the way to operate with it.

### Products and price plans
After you finished the Onboarding process you have to define your [products](/docs//billing/reference/products/.com.wixpress.billing.api.v1.-product-service.-create-product) 
and their [price plans](/docs//billing/reference/product-price-plans/.com.wixpress.billing.api.v1.-product-price-plan-service.-create-product-price-plan). <br/>
The basic idea behind product price plans is that same product can have different price for
a different combination of currency and recurring cycle. 

### Orders
Once the products are defined you can create [orders](/docs//billing/reference/orders/.com.wixpress.billing.api.v1.-order-service.-create-order).
An order is actually a container of order items. It also dictates the behavior of the payment but not the payment itself.

The order's boolean **capture** field specified whether the payment will be captured automatically or manually. Setting it for `true` will make it an auto capture order. Otherwise, it will require a manual capture. We will elaborate it in the `Invoices` section.
The result of order creation is actually an invoice entity. </br>

A newly created order that you receive in the [response](/docs//billing/resources/createorderresponse) contains the **invoice id**.

#### Order Properties

##### ContractSwitchType
Can allow us to override the SBS-internally calculated contract switch type for order creation through `OrderLineItem.ContractSwitchType` or order preview with `OrderPreviewItem.ContractSwitchType`.
Possible values:
1. REGULAR - relying on SBS internal ContractSwitchType calculation
2. FULL_AMOUNT_PERIOD - overriding SBS internal ContractSwitchType calculation - switch to a new package prices without credit/refund calculated, and dates will be from now
3. DOWNGRADE - switch to a lower plan or cycle.
3. UPGRADE - switch to a higher plan or cycle.

#### Taxes

For recurring services, internal tax calculation is the one always used without the ability to override it. To change your vendor taxation, please contact the `#billing-rd` team in Slack.
For one time charges, there are two possible tax calculations use cases - using the order item level `Tax` **OR** order level `OrderTaxContext` (if both of them are set, an error will be returned). 

##### One time charge, Order Item level Tax

Order items could have a multiple `Tax` parameters with `tax_included` value that indicate if order amount already include that tax amount or not.

There are a few rules associated with taxes:

1. You can't pass **Taxes** without **Tax Included** value.

2. For **one time orders** you must to pass some **Tax Included** parameter. In this case your tax zone rules would be overridden.

##### One time charge, Order level OrderTaxContext

In this case the internal tax calculation that will be based on your vendor tax configuration will be used. 
It's possible to pass your country and vat specific `TaxDetails` **OR** `payment_source_id`.

### Invoices 
The invoice is an entity that generated as part of order creation. The customer should pay for the invoice.

<p>

* Pay <br/> 

In order to start payment process call [invoice pay](/docs//billing/reference/invoices/.com.wixpress.billing.api.v1.-invoice-service.-pay-invoice). <br/>
Split Invoice, Is a side effect that will happen if the invoice passed in has multiple line items which are assinged to 
services assigned to different payment sources than the one being passed to Pay.  

* Payment Source <br/> 

As part of the payment request you should provide a payment source.
If the customer already has a registered payment source from previous purchases then its payment source id can be specified. 
If this is the first purchase or if the customer want to create a new payment source within the payment process then the 
_payment source details_ should be provided within the payment request. 

* Billing Token <br/>

The _payment source details_ has the _billing token_ field. The _billing token_ should be acquired by calling the PCI _billing-tokenizer_ service.    

* Capture <br/>

If the order was created with _capture=false_ then the [invoice pay](/docs//billing/reference/invoices/.com.wixpress.billing.api.v1.-invoice-service.-pay-invoice) should be called to capture the authorized invoice. 
However if the capture in the order was specified with _capture=true_ then the invoice will be captured automatically (usually a couple of days after the payment).

#### 3DS
In order to pay for for an invoice, you need to provide a 3DS data.
3DS (3D Secure) also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. 
The basic concept of the protocol is to tie the financial authorization process with an online authentication to provide an additional layer of verification.

##### Adyen

##### WorldPay

Data we will return / expect to receive in `data` map:

Expecting to receive:

`Billing3DsDeviceFingerprintData.data.sessionId`

`Billing3DsChallengeData.data.orderCode`
`Billing3DsChallengeData.data.sessionId`
`Billing3DsChallengeData.data.machineCookie`

`Billing3DsV1FallbackData.data.orderCode`
`Billing3DsV1FallbackData.data.sessionId`
`Billing3DsV1FallbackData.data.machineCookie`

Returning:

`Billing3DsDeviceFingerprintAction.data.jwt`

`Billing3DsAction.data.jwt`
`Billing3DsAction.data.orderCode`
`Billing3DsAction.data.transactionId3DS`
`Billing3DsAction.data.threeDSVersion`
`Billing3DsAction.data.machineCookie`
`Billing3DsAction.data.sessionId`

## Services

Once order provisioned, a _Service_ is created. It describes the provisioned product on SBS side.
As part of the Service, you will have the _serviceId_, the _lastInvoiceId_, _serviceStatus_ and more.

#### Updatable fields

Fields you will be able to update with the `update` endpoint. Trying to update other fields will result in an error.

* endOfPeriod


## Metadata
A few entities (i.e. order, order line item, product, etc.) include the _map<string, string> metadata_ field. This is a useful way to associate external system data with these entities.
It can be used for instance to store id of the mirrored entity in your system. This way the external system has the ability to map between its entity and the Billing one.
<br/>
Note that when a new order with order line items created the Billing service automatically creates an invoice with invoice line items and also a service for each order line item.
The metadata of the order is copied to the invoice and the metadata of the order line items is copied to the service. The metadata of the invoice line item will be referenced to the 
service's metadata. If the service is recurring then each new invoice line item that is created from the service in the future will reference to the same metadata belongs to the service.       

## Amounts<br/>
All the amounts in the Billing system are in minor unit. For example to override amount of order line item with $10 USD provide _override_amount_ value of 1000 (i.e. 1000 cents).
Not all currencies are multiply of 100 minor units, such as JPY has no minor units and so amount with 1000 JPY will have value 1000. 
<br/> Please see the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) table with a list of all currencies with their minor units.   

