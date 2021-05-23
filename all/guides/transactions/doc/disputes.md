SortOrder: 1
## Disputes Overview  

**The dispute process involves the following parties**:
1. **Cardholder**: The owner of the card involved in a transaction.
2. **Merchant**: The party who sold the goods or services that are under dispute.
3. **Card Issuer**: The bank that issued the card to the cardholder.
4. **Acquirer**: The bank tasked with acquiring payment on the merchant's behalf.
5. **Card Association**: The card brands (Visa, Mastercard, and others) oversee the process.

![Dispute lifecycle](https://s3.amazonaws.com/wixplorer-readme-images/transactions%2Fdispute_lifecycle.png "Dispute lifecycle")

### RFI
A dispute can be created upon receiving an RFI (Request For Information), which is a preliminary step before a chargeback (no movement of funds).

It starts with *Open* status - *RFI_OPEN*. In response, the merchant can either refund the payment or upload evidence with clarifications about the purchase. 

If the merchant refunds the payment, the status will be updated to *Refunded*, and the dispute will not be escalated into a chargeback.

If the merchant provided evidence, the status will be updated to *RFI_UNDER_REVIEW*. 

If the evidence provided proves sufficient, depending on the Card Scheme rules, the status will be updated to *RFI_CLOSED*, which means the RFI has timed out and did not escalate into a chargeback.

### Chargeback
In some cases, a chargeback will follow an RFI if it wasn’t resolved at the RFI stage. However, in most cases the dispute is created as a Chargeback right away with the status CHARGEBACK_OPEN, and skips the optional RFI stage. At this point, the funds are deducted from the merchant’s account, and the merchant can’t refund the money on their own.

Merchants have a timeframe of 14-40 days (the time frame is being detected by the card scheme) to submit evidence against the chargeback. If no actions are taken within this timeframe, the chargeback status is updated to *LOST*.

Uploading evidence changes the dispute status to *CHARGEBACK_UNDER_REVIEW*. The evidence will be reviewed by the card schemes. The timeframe varies depending on the card scheme, up to 80 days in some cases.

Once the review is complete, the chargeback status will be updated to **WON** or **LOST**, as decided by the card issuer.

**Dispute statuses**:
- RFI_OPEN - expecting evidence from the client
- RFI_UNDER_REVIEW
- RFI_CLOSED - final status
- CHARGEBACK_OPEN - expecting evidence from the client
- CHARGEBACK_UNDER_REVIEW
- WON - final status
- LOST - final status

### Responding to disputes using the API
**Step 1: Find out when a dispute is opened**

There are 7 transaction events related to the dispute. Each event includes a `disputeId`. 

Types of dispute related events:

- DisputeRfiOpen
- DisputeRfiUnderReview
- DisputeRfiClosed
- DisputeChargebackOpen
- DisputeChargebackUnderReview
- DisputeChargebackLost
- DisputeChargebackWon

1. Register to receive the [Transaction Webhook](https://dev.wix.com/api/rest/transactions/transaction-webhook).
2. Upon receipt of the webhook with a dispute-related event, retrieve the `disputeId`, `transactionId`, and `accountId`.

**Step 2: Call the transaction**
Call [GetTransaction](https://dev.wix.com/api/rest/drafts/transactions/get-transaction) and pass the `transactionId` and `accountId` retrieved from the webhook. All the transaction's disputes and their current status will be returned under `transaction.disputes`.

**Step 3: Decide how to deal with the dispute (accept or submit evidence).**

To accept the dispute, skip to step 5. To submit evidence, go to step 4.

**Step 4: Respond to the dispute with evidence**

To respond to the RFI/chargeback, you should upload evidence, associate it with the correct dispute and submit the evidence to the issuing bank.

To upload evidence:

1. Call [Generate Evidence Upload Url](https://dev.wix.com/api/rest/drafts/transactions/generate-evidence-upload-url). 
2. Retrieve the `upload_url` and `upload_token`.
3. Call the retrieved `upload_url` as an HTTP POST, and pass the `upload_token` as a path parameter.

For example:
```
curl --location --request POST 'https://wixmp-90ef227251107558e3a6a71f.appspot.com/_ah/upload/test_upload_token_url/' \
--form 'upload_token="test_upload_token"' \
--form '=@"/example.pdf"'
```

![Evidence Upload](https://s3.amazonaws.com/wixplorer-readme-images/transactions%2Fevidence_upload.png "Evidence Upload")


3. Retrieve the `payload.id` from the JSON response.  
For example:

```
{
   "message": "OK",
   "code": 0,
   "payload": {
       "mimeType": "image/jpeg",
       "hash": "5d61d4349e8380b3eaa97e767391dfd9",
       "dateCreated": "2020-09-04T13:54:12Z",
       "id": "2411686768ca469dabd7cc64e52c502e",
       "path": "/tenants/a001a0c3-0ffa-4b76-8a13-aa0df0d7913c/accounts/0f226e8a-3b1f-44de-8f3f-9a4abdab5db3/transactions/a036c
       "lifecycle": null,
       "size": 3733,
       "urn": "urn:file:2411686768ca469dabd7cc64e52c502e",
       "bucket": null,
       "acl": "private",
       "dateUpdated": "2020-09-04T13:54:12Z",
       "type": "-"
   }
}
```

`payload.id` should be passed as `evidence.fileId` below. (in this example, payload.id = "2411686768ca469dabd7cc64e52c502e")

> **Important:** The evidence still needs to be associated with the relevant dispute after upload.

4. Call [Add Evidence](https://dev.wix.com/api/rest/drafts/transactions/add-evidence) to associate the evidence you uploaded with the relevant dispute. Pass the `disputeId`, `transactionId`, and `accountId` retrieved in step 1, and map the `payload.id` retrieved above to `evidence.fileId`.
5. When all the evidence has been uploaded and associated with the dispute, call [Submit Evidence](https://dev.wix.com/api/rest/drafts/transactions/submit-evidence) to trigger the submission of the evidence to the issuing bank.

**Step 5: Responding to a chargeback by accepting the dispute.**

Accept the dispute by calling [Accept Dispute](https://dev.wix.com/api/rest/drafts/transactions/accept-dispute) - relevant only when the dispute status is *CHARGEBACK_OPEN*. This action moves the dispute status to *LOST*.

