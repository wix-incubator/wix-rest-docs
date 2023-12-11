SortOrder: 0
Wix Atlas
------------------------------

> *Wix-Atlas* provides a gRPC platformized API for global search

For the POC phase, *Wix-Atlas* uses *Google Maps API*. We are currently looking for in-memory solutions ([Pelias](https://github.com/pelias/pelias))

#### Bazel Dependency

Add the following dependancy to your `BUILD.bazel` file:

```
@velocity_infra//rnd-tools/wix-atlas/wix-atlas-service/wix-atlas-service-api/src/main/proto:proto_scala
```

## Atlas V2 API Authorization
Atlas V2 API's contains:
* AutocompleteServiceV2 - ListPredictions, Predict
* LocationServiceV2 - Search, ReverseGeocoding
* PlacesServiceV2 - GetPlace

Those APIs are protected with permissions and available only for:
* Site visitors (requests that contains `svSession` cookie).
* Site members (requests that contains `smSession` cookie).
* Wix's users (with metasite in the request context).
* Server 2 server calls (requests that contain server2server signature from server that contain the relevant permission).

### Slack Channels

For support and questions, use [wix-atlas](https://wix.slack.com/archives/CQQGK1ALD)

For urgent matters, use [wix-atlas-urgent](https://wix.slack.com/archives/CTU8H0J12)

In case of severe urgent, you can restart Atlas service using [Nasa](https://www.wixnasa.com/?modal=restartService&artifact=com.wixpress.vi.wix-atlas-service-web)
