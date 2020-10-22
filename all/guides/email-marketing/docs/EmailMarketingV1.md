SortOrder: 1
## Email Marketing

The Email Marketing API allows caller to manage their marketing campaigns, setup sender details and retrieve account information. 
It is also used to setup email automation actions.

All email campaigns and automations are created from templates. 
Templates are created by Design Studio designers using our special tools. 
You can show to a user a selection of templates but most often you just hard-code the template ID received from Design Studio.
Templates can have placeholders and you need to provide their values while creating message from template or during the publishing. 
Placeholders are inserted into template content. 
All HTML is escaped. New lines are replaced to \<br> tags.
You can also add dynamic image to template. There is no fallback for it. You must always send image value.
Image link can be full url or Wix image id. It is decided during creation of template by Design Studio.

Email Marketing has its own customer account status - malicious users can be banned or suspended till they are proven not guilty. 
Depending on their premium package users have different quotas, you can check how many campaigns left in given quota period.
All this info is available in AccountDetails service.

We let users send emails from their own domain address. This setup is performed in SenderDetails service. 
It only works on domains managed by Wix. Email marketing service adds all required records on customer domain.
User needs to confirm that email address belongs to him by entering verification code sent to his email address.
There is only one sender details setup per metasite. 
Different automations and email marketing campaigns all share the same sender details.

 