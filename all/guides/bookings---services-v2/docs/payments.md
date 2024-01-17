SortOrder: 3
# Receiving payments

## Payment rates

The service price can be expressed in one of the following ways:

- **Fixed rate**: The service price is fixed and does not change.
- **Varied rate**: The service price may depend on different factors, such as the staff member providing the service or custom price options. [Read more about price options](https://support.wix.com/en/article/wix-bookings-understanding-price-options).
- **Custom rate**: The service price is expressed as a custom string. For example, "Free", "Donation", or "Contact us for pricing".

## Payment options

Payment options dictate in what manner the customer can pay for the service. The following payment options are available:

```javascript
{
        "onlinePayment": true, 
        "inPerson": true, 
        "deposit": true, 
        "pricingPlan": true,
}
```

> It's required to specify either `onlinePayment` or `inPerson` as `true`.

### Online payments
Enabling online payments allows customers to pay for the service at the time of booking.

To read more about the variety of ways you can receive online payments, please refer to the [dedicated article](https://support.wix.com/en/article/wix-bookings-about-getting-paid-online).

### Paying in person

Enabling a costumer to pay in person allows customers to pay for the service at the time of the service, and to book the service without going through the payment process.

> It's recommended to set up online payments as services that accept online payment significantly reduce no-shows.

### Requiring deposit

Setting a deposit requirement allows you to charge some amount of the service price as a deposit. The deposit is charged at the time of booking and the remaining balance is charged at the time of the service.

> Setting `deposit` to `true` requires `onlinePayment` to be `true` as well.

> The deposit amount should be specified in the rate object, and is supported both for fixed and varied rates.

### Pricing plans

Enabling payment with pricing plan enables customers to pay for the service using a pricing plan. [Read more about offering pricing plans](https://support.wix.com/en/article/wix-bookings-offering-packages).
