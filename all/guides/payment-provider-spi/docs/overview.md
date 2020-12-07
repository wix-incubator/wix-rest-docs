SortOrder: 1
# Integration
To integrate your payment provider with the Wix Payment Platform, please contact the team at [cashier-provider-integration@wix.com](mailto:cashier-provider-integration@wix.com).

## High-level schema
One major difference between this SPI and a regular API is that you will have to implement a server on your side, rather than use an existing API.
To accomplish this integration fully, use the Wix Event API described further below.

The following diagrams describe a high-level visualization of the integration process. 

![Onboarding-sale-refund](https://s3.amazonaws.com/wixplorer-readme-images/payment-provider-spi%2Fonboarding_sale_refund_flow.png)
At first glance it might seem synchronous, but we also support an asynchronous flow.
In the case of an asynchronous sale process in step *4*, having received a successful response, you are able to return a `PENDING` status for payment or refund, and later send us an event with the final state. 

![pci-redirect-flow](https://s3.amazonaws.com/wixplorer-readme-images/payment-provider-spi%2Fpci_redirect_flow.png)
