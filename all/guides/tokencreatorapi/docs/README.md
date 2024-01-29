SortOrder: 0
# Introduction

TokenCreatorApi is a signed instance creator service.
It takes your one time password and creates a signed instance for you.
The response will also contain an expiration timestamp for the token in the returned in the response ("expires" field)

## How to create a signed instance?

### gRPC

See proto file [here](/docs/../com/wixpress/tokencreator/v1/token_creator_api.proto)

### Rest

#### Endpoint

HTTP POST request

    POST /v1/token

#### Request body

    {
		"otp": "<YOUR_OTP>"
    }