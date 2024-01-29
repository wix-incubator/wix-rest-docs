SortOrder: 0
# Introduction

Welcome to Wixly, our URL shortening service!

Wixly allows you to easily shorten long, complex URLs into shorter, 
more manageable links that can be easily shared and distributed.
Simply enter the URL that you want to shorten into our tool, and we'll create a unique 
code that is associated with the original URL.
This app is a Loom Prime read head API for Wixly. When someone accesses the shortened link,
they will be redirected to the original page by this app.

Wixly's write head API can be found here:
[proto](/docs/../../../wixly-writer/proto/com/wixpress/wixly/v1/wixly_api.proto) [docs](../../../wixly-writer/proto/docs/README.md)

## How to resolve a short URL?

### gRPC
See proto file [here](/docs/../com/wixpress/wixlyreader/v1/wixly_resolve_api.proto)

### Rest

#### Endpoint

HTTP GET request

    GET https://wix.to/abc123

will redirect to https://www.example.com