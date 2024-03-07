SortOrder: 0
# Introduction

Data Resource Usage Service reports current usage 
and limits on different data resources:
 - storage
 - data collections
 - data items

# Events

Service uses Duplexer 
`wix-data-resource-usage-notifications` channel
to notify about events:
 - `limits-changed` event with `ResourceUsage` limit fields in payload
