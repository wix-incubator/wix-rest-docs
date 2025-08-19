# Webhooks
When you [register for webhooks](https://dev.wix.com/docs/build-apps/developer-tools/apis-and-webhooks/webhooks) in the Wix Developers Center, and you’ve configured your OAuth and Permissions settings correctly, Wix will send an HTTPS POST request to your server URL with the relevant data when an event occurs.

The event’s data is included in the body of the request as a [JSON Web Token (JWT)](https://jwt.io/introduction/). 
The data received will vary by the type of event, but the following will always be included:
* **instanceId**: The App Instance ID. This is the unique identifier of the app within the website.
* **eventType**: A description of the event type, e.g., OrderEvent.

> Important:
>   
> You must return a 200 response upon successful receipt of a webhook. The timeout for the response is 1250 ms. Additional attempts to send the request are made after a timeout as described in this <a href="https://devforum.wix.com/kb/en/article/about-webhooks#resend-policy">article</a>.
