SortOrder: 0
# Introduction

Wixly is a Url shortening service. 
It takes your long urls and creates a short http://wix.to/?????? URL.
You can also update the long url the created short url redirects to.
This app is a Loom Prime platformized write head API for Wixly, useful
for creating and updating short URLs, but can't be used to redirect to the original
corresponding long URL.

## How to create a short URL?

### gRPC
See proto file [here](/docs/../com/wixpress/wixly/v1/wixly_api.proto)

### Rest

#### Endpoint - TODO: replace with real example

HTTP POST request

    POST /v1/wixly-writer/short-url

#### Request body

    {
		"url": "https://www.youtube.com/watch?v=SSbBvKaM6sk"
    }

#### Example
```
	POST /v1/wixly-writer/short-url HTTP/1.1
	Host: www.wix.com
	Content-Type: application/json
	Cache-Control: no-cache
	
	{"url": "https://www.youtube.com/watch?v=SSbBvKaM6sk"}
```

#### Response JSON
```
    {
		"id": "1SbFvKaM6sP",
		"url": "http://wix.to/1SbFvKaM6sP"
    }
```

## How to update a long URL the short URL redirects to?

### gRPC
See proto file [here](/docs/../com/wixpress/wixly/v1/wixly_api.proto)

### Rest

#### Endpoint - TODO: replace with real example

HTTP PATCH request

    PATCH /v1/wixly-writer/short-url

#### Request body

    {
        "id": "1SbFvKaM6sP",
		"url": "https://www.youtube.com/watch?v=SSbBvKaM6sk"
    }

#### Example
```
	PATCH /v1/wixly-writer/short-url HTTP/1.1
	Host: www.wix.com
	Content-Type: application/json
	Cache-Control: no-cache
	
	{"id": "1SbFvKaM6sP", "url": "https://www.youtube.com/watch?v=SSbBvKaM6sk"}
```

#### Response JSON
```
    {
		"id": "1SbFvKaM6sP",
		"url": "http://wix.to/1SbFvKaM6sP"
    }
```