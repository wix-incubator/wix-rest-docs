SortOrder: 0
# Integration

The service is currently meant to serve only the corresponding Cairo client [Export to](https://bo.wix.com/pages/cairo/?path=/story/infinite-scroll-table-features--exportto).

Before starting the Cairo integration, make sure to complete this server-side integration.

## Prepare A Query Endpoint
`ExportService` fetches data from [platformized query endpoints](https://bo.wix.com/wix-docs/rnd/platformization-guidelines/api-query-language#platformization-guidelines_api-query-language_api-query-language), and is aligned with the [Nile](https://github.com/wix-private/server-infra/tree/master/nile) standards. For example:

```protobuf
service MyService {
  rpc QueryMyEntity (QueryRequest) returns (QueryResponse) {}
}
```

### Implement Request/Response Protocol
You query endpoint should support the following request/response structure, with some possible variations. 

If your endpoint does not comply, you should create a new "proxy" endpoint that implements the protocol, and transforms the request and response accordingly. 

### Transform / format data
Ask your product manager for exact requirements of how the data should look like inside the CSV.

If your existing endpoint doesn't answer theses requirements because the CSV should contain formatted data (i.e, data not in its raw form) - create a new "proxy" endpoint that transforms the data according to your product requirements.

#### Request
```protobuf
syntax = "proto3";

import "wix/fedinfra/exportservicespi/v1/export_query_v2.proto";

message QueryRequest {
  .wix.fedinfra.exportservicespi.v1.ExportQueryV2 query = 1;
}
```

- Message may contain other fields 
- Message must contain a `QueryV2 query` field. Field number may be different from 1, configure it by passing [`method_spec.request_query_field_number=FIELD_N`](#method-spec)

#### Response
```protobuf
syntax = "proto3";

import "wix/common/paging.proto";

message QueryResponse {
  message MyEntity {}
  
  repeated MyEntity my_items = 3;
  .wix.common.PagingMetadataV2 paging_metadata = 5;
}
```

- Message must contain at least one `repeated` field (any field number is allowed), pass the name of the field to [`method_spec.response_repeated_field_name`](#method-spec)
- Message must contain a `PagingMetadataV2` field (any field number is allowed). If your `PagingMetadataV2` is not named `paging_metadata`, pass the name of the field to [`method_spec.response_paging_metadata_field_name`](#method-spec)


### Method Spec
Method spec is part of the [`ExportService.CreateExportAsyncJob`](#test) API. It allows slight variations in the request/response structure of your endpoint.

```protobuf
syntax = "proto3";

message MethodSpec {
  QueryFieldNumber request_query_field_number = 1; // the field number of the request query field (default=QueryFieldNumber.DEFAULT)
  string response_repeated_field_name = 2; // the name of the response repeated field (required)
  string response_paging_metadata_field_name = 3; // the name of the response PagingMetadata field (default=paging_metadata)

  enum QueryFieldNumber {
    DEFAULT = 0;
    FIELD_8 = 8;
  }
}
```

### Fields
`Fields` is part of the [`ExportService.CreateExportAsyncJob`](#test) API. It tells ExportService how to map your query endpoint response repeated field proto message into CSV columns.

To get a list of available fields from your proto message, you can run the following script (replace `ProductOrVaraint` with your proto message):

> Pass this list to your FED team, they will need to pass them to Cairo in the client-side integration.

```scala
import com.wixpress.fedinfra.exportservice.v1.ProductOrVariant // replace with your proto message
import scalapb.descriptors.FieldDescriptor
import scalapb.descriptors.ScalaType.Message

import scala.collection.mutable

object SearchAllFieldsTestApp extends App {
  def extractFieldDescriptor(field: FieldDescriptor): Unit = {
    val q = mutable.Queue((field, Seq[String]()))

    while (q.nonEmpty) {
      val node = q.dequeue()

      node._1.scalaType match {
        case Message(descriptor) =>
          node._1.asProto.label.map(_.name).getOrElse("") match {
            case "LABEL_REPEATED" =>
              descriptor.fields.foreach(f => {
                (0 to 0).foreach(index => {
                  q.enqueue((f, node._2 ++ Seq(node._1.name, index.toString)))
                })
              })
            case _ =>
              descriptor.name match {
                case "Value" | "ListValue" =>
                  println(
                    (node._2 ++ Seq(node._1.name)).mkString(".")
                  )
                case "Struct" =>
                case _ =>
                  descriptor.fields.foreach(f => {
                    q.enqueue((f, node._2 ++ Seq(node._1.name)))
                  })
              }
          }

        case _ =>
          println(
            (node._2 ++ Seq(node._1.name)).mkString(".")
          )

      }
    }
  }

  ProductOrVariant.scalaDescriptor.fields.foreach(field => {
    extractFieldDescriptor(field)
  })
}

```

### Create A PR to ExportService that includes the new endpoint
Once your endpoint complies, create a PR that adds it to [this list](https://github.com/wix-private/fed-infra/blob/master/export-service/src/com/wixpress/fedinfra/exportservice/v1/components/ValidateUnknownEndpointMethod.scala#L21) 

## Test
Use fire-console to call [CreateExportAsyncJob](https://pbo.wix.com/fire-console/?artifact=com.wixpress.fedinfra.exportservice.export-service&service=wix.fedinfra.exportservice.v1.ExportService&method=CreateExportAsyncJob&body=eyJmaWVsZHMiOltdLCJxdWVyeSI6eyJzb3J0IjpbXSwiZmllbGRzZXRzIjpbXSwiZmllbGRzIjpbXSwiY3Vyc29yUGFnaW5nIjp7ImxpbWl0Ijo1MH19LCJtZXRob2RfbWV0YWRhdGEiOnsiYXJ0aWZhY3QiOiIiLCJtZXRob2QiOiIiLCJzZXJ2aWNlIjoiIn0sIm1ldGhvZF9zcGVjIjp7InJlc3BvbnNlX3JlcGVhdGVkX2ZpZWxkX25hbWUiOiIifX0%3D) and fill in the missing requried fields:

- `method_metadata`
- `method_spec.response_repeated_field_name`
- `query.pagingMethod`
- `fields`

> Don't forget to add relevant `MetaSiteId` aspect

Take the `id` from the response and call [GetExportAsyncJob](https://pbo.wix.com/fire-console/?artifact=com.wixpress.fedinfra.exportservice.export-service&service=wix.fedinfra.exportservice.v1.ExportService&method=GetExportAsyncJob&body=eyJqb2JfaWQiOiIifQ%3D%3D). 
Eventually the job status should become `COMPLETED` and `data.signedUrl` with a media platform URL to download the file.

#### Investigating Errors
If you're getting errors from `CreateExportAsyncJob` or job status is `FAILED` when accessing `GetExportAsyncJob` - check out `ExportService` [NewRelic dashboard](https://one.newrelic.com/nr1-core/apm-features/overview/MjM0Mjh8QVBNfEFQUExJQ0FUSU9OfDEwNDM2NzE1MzY).


## Done!
🙌🥳🎉👏  Your endpoint is now ready for the Cairo client side integration 🙌🥳🎉👏  

## Support 
[`#cairo`](https://wix.slack.com/archives/C02K83200PL)
