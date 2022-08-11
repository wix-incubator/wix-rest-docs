SortOrder: 0
# About Dispute Case API
Dispute responses allow you to challenge disputes. The purpose of a dispute response is to prove the validity of the original transaction.
A dispute, also known as chargeback, occurs when a cardholder questions your payment with their card issuer. There are multiple types of chargebacks, each requiring a different kind of evidence.

With the help of a dispute case, a walk-through tool, you can build compelling evidence to increase your chances of winning a dispute.
A typical dispute process starts with answering a chargeback by gathering evidence of legit payment, such as screenshots of communication, shipping proof, and rebuttal letter. 

Structuring compelling evidence depends on knowing which evidence to include and how to gather all the evidence into a single file. 

Use dispute case to:
- create a pre-made template with all the information to back up the case - rebuttal letter and evidence files
- choose between the suggested types of evidence for a specific chargeback
- edit, re-upload, delete, and make changes to the evidence file uploads
- compile evidence to a single PDF file as the final output that can be submitted as evidence to any payment provider.

## Terminology
 - **Merchant**: Party selling goods or services to customers via an eCommerce website, a mobile app, on the point of sale, or across all three channels. Wix Payments enable merchants to accept payments from customers made with cards or local payment methods and manage payouts.
 - **Dispute**: Dispute occurs when a cardholder question the charge with their card issuer and initiate a chargeback. When this happens, the merchant is given the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.
 - **Chargeback**: Chargeback is a primary step in a dispute. It includes a reversal of a credit or debit card payment that comes directly from the bank. Chargeback occurs when a cardholder questions a transaction and asks their card-issuing bank to reverse it.
 - **Dispute Case**: Main entity. It represents a virtual case with evidence documents and enables to compile all evidence into one final PDF.
 - **Product type**: Type of goods or services provided by merchant to customer in regards to the opened dispute. Can be `merchandise`(selling tangible goods), `digital goods`(selling digital goods) or `event or service` (bookings, subscription, event, or other services).
 - **Dispute reason**: Main reason for the chargeback provided by the bank. You can get it using [Transactions API](https://dev.wix.com/api/rest/wix-payments/transactions) in [Transaction object](https://dev.wix.com/api/rest/wix-payments/transactions/transaction-object) nested disputes. If you don't have a dispute opened in Wix Payments, you can also use the chargeback reason code provided by bank, look up [chargeback reason codes](https://chargeback.com/chargeback-reason-codes/), and match it with our enum.
 - **Chargeback reason code**: Alphanumeric strings of text provided by the bank in a chargeback notification as a means of explaining the cause for the dispute.
 - **Evidence type**: Kind of evidence. To dispute a chargeback, merchant must provide suggested evidence document or describe it by text if the document is absent. If your evidence does not match any proposed evidence type, use `other` instead.
 
## Evidence types
 - **PROOF_OF_ORDER** - Proof that your customer ordered the product or service (invoice and/or order confirmation)
 - **PROOF_OF_RECEIPT** - Proof that your customer accessed or downloaded the digital product or service (shipping and/or delivery confirmation)
 - **PROOF_OF_USAGE** - Proof that your customer accessed or downloaded the digital product or service (login details: date, IP address, etc)
 - **TERMS_AND_CONDITIONS** - Proof that your customer violated the Terms & Conditions or refund policy (Terms & Conditions)
 - **ORDER_CONFIRMATION** - Proof that your customer acknowledged placing or receiving the order (emails or messages with your customer)
 - **RECEIPT_CONFIRMED_OR_DELAY_AGREED** - Proof that your customer acknowledged receiving the order, or communication about the delay (emails or messages with your customer)
 - **PROOF_OF_NO_COMPLAINTS** - Proof that your customer didn’t complain to you about the product or service (emails or messages with your customer)
 - **MULTIPLE_ORDER_ACKNOWLEDGED** - Proof that your customer made multiple orders knowingly (emails or messages with your customer)
 - **PROOF_OF_SEPARATE_ORDERS** - Proof that each payment was for a different product or service (separate order and/or shipping confirmations)
 - **CERTIFICATE_OF_AUTHENTICITY** - Proof that the product or services is authentic and legitimate (certificate of authenticity)
 - **OTHER** - Any other proof you have that might help your case

## Use Cases
### Compile images and text files into a single PDF file that can be submitted as evidence to dispute a chargeback
**Note:** Wix currently supports disputing chargebacks through Wix Payments only.
You can use generated evidence PDF file to [dispute a chargeback through Wix Payments](https://dev.wix.com/api/rest/wix-payments/transactions/disputes-overview) via Dispute API.

1. Get the fields `product_type`, `dispute_reason`, `dispute_info.account_id`, `dispute_info.transaction_id`, `dispute_info.dispute_id` from the [Transaction object](https://dev.wix.com/api/rest/wix-payments/transactions/transaction-object), using the [Get Transaction](https://dev.wix.com/api/rest/wix-payments/transactions/get-transaction) API call.
2. Create `Dispute Case` using [Create Dispute Case](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/create-dispute-case?localViewerId=oleksandrdo) API call. The request must contain the fields: `product_type`,  `dispute_reason`, `dispute_info.account_id`, `dispute_info.transaction_id`, `dispute_info.dispute_id`. These fields are necessary to help suggest appropriate evidence types (`suggested_evidences`) and create a strong evidence document (see [Get Compiled Evidence](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/get-compiled-evidence-document?localViewerId=oleksandrdo)). The `dispute_info.account_id`, `dispute_info.transaction_id`, `dispute_info.dispute_id` fields help the engine to pre-generate the documents by collecting data from WIX ecosystem. 

```
POST https://www.wixapis.com/payments/v1/dispute-cases
{
    "disputeCase" : {
        "productType" : "SERVICE_OR_EVENTS", // required immutable field
        "disputeReason" : "CANCELED_RECURRING", // required immutable field
        "disputeInfo" : { // optional but immutable field, updating it will be ignored after creation
            "accountId" : "2839af5e-f6fc-41f5-9787-6f519e2fe735",
            "trancationId" : "4e980086-cccd-4216-8545-5281f881466f",
            "disputeId" : "3578b98f-bf9c-40e0-9edd-1ff2f594ae3d"
        },
        // optional and can be updated later
        "businessDescription" : "Wix.com Ltd. operates and develops a web platform. The Company's platform offers solutions that enable businesses, organizations, and individuals to develop customized websites and application platforms. Wix.com serves customers worldwide.", 
        // optional and can be updated later
        "coverLetter" : ""
    }
}
```
3. You can update the created `dispute case` with `business_description` and `cover_letter`, using [Update Dispute Case](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/update-dispute-case?localViewerId=oleksandrdo) API call. This information is included in the final evidence PDF. An attempt to update `product_type`, `dispute_reason` or `dispute_info` at this stage will be ignored.

```
    PATCH https://www.wixapis.com/payments/v1/dispute-cases/{disputeCase.id}
    {
        "disputeCase" : {
            "businessDescription" : "Wix.com Ltd. operates and develops a web platform. The Company's platform offers solutions that enable businesses, organizations, and individuals to develop customized websites and application platforms. Wix.com serves customers worldwide.",
            "coverLetter" : "" 
        }
    }
```

### Add evidence document using image (jpeg/jpg/png) or PDF format
1. Create evidence using [Add Evidence](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/add-evidence?localViewerId=oleksandrdo) API call.
2. Provide evidence type (`DisputeEvidence.EvidenceType`) and fields `name` and `description`. They are included in the final evidence document with the provided document. 
3. Response returns `DisputeEvidence` object with fixed ID.
```
       POST https://www.wixapis.com/payments/v1/dispute-cases/{disputeCaseId}/evidences
       {
            // required immutable field
            "type" : "WEBSITE_OR_SERVICE_ACCESSED",
            // optional field
            "name" : "Proof of service accessed",
            // optional field
            "description" : "Customer have accesed service in next pay period"
       }
```
4. Call [Generate Evidence Upload Url](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/generate-evidence-upload-url?localViewerId=oleksandrdo) with associated evidence `evidence_id` and `file_name`, which appear in the evidence after a successful upload. Get the `upload_url` and `upload_token` for uploading file 
```
        POST https://www.wixapis.com/payments/v1/dispute-cases/{disputeCaseId}/evidences/{evidenceId}/generate-upload-url
        {}
```
The response includes:
```
        {
            "uploadUrl" : "https://url.to.upload.file",
            "uploadToken" : "ToKeNTouPLoaDFiLe"
        }
```
5. Upload document using `upload_url` and `upload_token` from the previous API call.
```
        curl --location --request POST 'https://url.to.upload.file' \
        --form 'upload_token="ToKeNTouPLoaDFiLe"' \
        --form '=@"/example.pdf"
```
6. Wait for [Update Event](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/dispute-case-updated-domain-event?localViewerId=oleksandrdo) or attach uploaded file synchronously using [Attach Uploaded Evidence Document](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/attach-uploaded-evidence-document?localViewerId=oleksandrdo) to make sure the server bind document to the corresponding evidence. This call returns an updated `DisputeCase` object
```
        POST https://www.wixapis.com/payments/v1/dispute-cases/{disputeCaseId}/evidence/{evidenceId}/attach-uploaded-document
        {}
```
7. To update evidence name and/or description, use [Update Evidence](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/update-evidence?localViewerId=oleksandrdo) API call. 
**Note:** changes in `type` will be ignored.
```
    PATCH https://www.wixapis.com/payments/v1/dispute-cases/{disputeCaseId}/evidence/{evidence.id}
    {
        "name" : "Proof of service accessed",
        "description" : "Customer have accesed service in next pay period"
    }
``` 
8. To update evidence document, use [Generate Evidence Upload Url](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/generate-evidence-upload-url?localViewerId=oleksandrdo) with [Attach Uploaded Evidence Document](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/attach-uploaded-evidence-document?localViewerId=oleksandrdo).
```
    POST https://www.wixapis.com/payments/v1/dispute-cases/{disputeCaseId}/evidences/{evidenceId}/generate-upload-url
    {}
``` 
```
    curl --location --request POST 'https://url.to.upload.file' \
    --form 'upload_token="ToKeNTouPLoaDFiLe"' \
    --form '=@"/example.pdf"
```
```
    POST https://www.wixapis.com/payments/v1/dispute-cases/{disputeCaseId}/evidence/{evidenceId}/attach-uploaded-document
    {}
```
9. To delete a document from evidence, use [Clear Evidence Document](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/clear-evidence-document?localViewerId=oleksandrdo). 
10. To delete the whole evidence, use [Remove Evidence](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/remove-evidence?localViewerId=oleksandrdo)
```
    POST https://www.wixapis.com/payments/v1/dispute-cases/{disputeCaseId}/evidence/{evidenceId}/clear-document
    {}
```
10. Use [Get Compiled Evidence](https://bo.wix.com/wix-docs/rest/all-apis/dispute-case/get-compiled-evidence-document?localViewerId=oleksandrdo) API call to get a compiled evidence document at any point of the process after you created `Dispute Case`.
```
    GET https://www.wixapis.com/payments/v1/dispute-cases/{disputeCaseId}/compiled-evidence-document
```
on response client will get with download link, token and expiration time
```
    {
        "document" : {
            "id" : "some id", // just ignore this field
            "url" : "https://www.url.to.download.compile.evidence.document",
            "urlExpirationDate" : "2020-09-04T13:54:12Z" // optional field and can be missed
        }
    }
```
11. The compiled dispute evidence file can be sent to a provider either using wix-payments (if a dispute is opened via wix-payments side) or any other payment provider that opened the dispute.
