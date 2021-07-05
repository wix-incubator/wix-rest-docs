SortOrder: 0
# Introduction

A Carrier Service can be registered by merchants to their shops, and then provide real time shipping rates to their buyers,
by implementing the following *SPI* (Service Provider Interface).

#### Reporting Failures

When a carrier service doesn't have enough information, or received invalid information, and is un-able
to calculate shipping rates due to that, we expect the following payload to be returned along with an HTTP `400` status:

```json
{
  "message": "We are missing important information",
  "details": {
    "validationError": {
      "fieldViolations": [
        {
          "field": "postalCode",
          "description": "MISSING"
        }
      ]
    }
  }
}
```
* message - can be any free text message or empty;

Currently, the following error codes are supported:
* field - `postalCode`; description - `MISSING`, `INVALID`;
    * Indicates that the given postal code is missing or invalid (when it's mandatory for shipping calculations).
* field - `shippingDestination`; description - `PARTIAL`
    * Indicates that the given destination address is partial (when a full address is mandatory for shipping calculations).

