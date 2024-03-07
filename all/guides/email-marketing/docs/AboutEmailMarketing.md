SortOrder: 0
## About Email Marketing

The Email Marketing API allows for management of email marketing campaigns and sender details, as well as retrieving account information. 
Use this service to access existing marketing campaigns, send them to contact lists and check campaign statistics for a Wix site with an active Email Marketing account.

Managing and sending email marketing campaigns is only possible
if the site has an active email marketing account. An email marketing account can be suspended 
if Wix Email Marketing [Terms of Use](https://support.wix.com/en/article/wix-email-marketing-terms-of-use) are breached. 
Each site has its own email marketing campaigns and emails quota. This is the number of monthly campaigns and emails available to create and send.
The quota rolls over each month. Quota information is available in Account Details. 

Sites can send email marketing campaigns only if they have verified sender details. 
Verification of sender details is only possible if the user owns the email address they want to send emails from.

New campaigns can be created in the Wix UI using templates, created from scratch in the Wix Email Marketing Composer, or reusing old campaigns. Via API, the only way to create a new campaign is to reuse an existing one.

Campaigns can be published without sending any emails. 
When a campaign is published you will receive a landing page URL that can be shared on social media.

Email marketing campaigns are sent to site contacts. 
Campaign statistics become available a few minutes after distribution.
Emails are never sent to contacts that have unsubscribed from the site.  

Access to the Email Marketing APIs are dependant on the user's account status, as follows:
- Account Details API: Always accessible.
- Sender Details API: Accessible only when email account status = ACTIVE (and sender details are verified).
- Campaign API: Accessible only when email account status = ACTIVE (and quota has not been reached).  

If an account is in a state of suspension they must visit their email marketing account in the dashboard and follow the instructions.
