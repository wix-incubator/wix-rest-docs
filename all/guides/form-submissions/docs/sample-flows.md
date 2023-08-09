SortOrder: 1
# Form Submissions: Sample Use Cases and Flows

This article shares some possible use cases your app could support, as well as
a sample flow that could support each use case. This can be a helpful jumping
off point as you plan your app's implementation.


## Submit a form with media

You can upload media files to a media manager folder by creating a new submission for a form that contains a field for uploading files.  

1. Call [Get Media Upload URL](https://dev.wix.com/docs/rest/api-reference/wix-forms/form-submissions/get-media-upload-url) to generate the upload URL for the specified file. 

1. Call [Create Submission](https://dev.wix.com/docs/rest/api-reference/wix-forms/form-submissions/create-submission) and use the generated URL as the value for the file upload field. 


## Periodically sync with an external analysis and reporting tool

You can retrieve submission data and upload it to an external data analysis tool. With the external tool, site owners can easily do a statistical analysis of their form submission data.

1. For the first load, use [Query Submissions By Namespace](https://dev.wix.com/docs/rest/api-reference/wix-forms/form-submissions/query-submissions-by-namespace) and filter for all submissions whose status has been confirmed.

1. Extract any desired data from the `submissions` payload, then upload the data to your app. 

1. For all subsequent loads, use the Query Submissions By Namespace endpoint and filter for submissions that are confirmed and have not yet been seen. 

1. Repeat step 2 to 3 for each subsequent load. 


## Sync with an external CRM for marketing purposes

Every time a form gets submitted, you can add the form submitter to an external CRM. A site owner can then use their CRM to send marketing emails to their form submitters. This flow relies on forms that requires a submitters email, and on an external CRM service. 

1. When the [Submission Created](https://dev.wix.com/docs/rest/api-reference/wix-forms/form-submissions/submission-created) Webhook is triggered, you'll receive the submission in the payload from `createdEvent.entity`.

1. Exract the email address from the `submissions` object. 

1. Check that the email adress is not already listed as a subscriber in the external CRM. 

1. Upload the new subscriber to the CRM. 