# Webhooks
When you [register for webhooks](https://devforum.wix.com/en/article/about-webhooks#register-for-webhooks) in the Wix Developers Center, and you’ve configured your OAuth and Permissions settings correctly, Wix will send an HTTPS POST request to your server URL with the relevant data when an event occurs.

The event’s data is included in the body of the request as a [JSON Web Token (JWT)](https://jwt.io/introduction/).  
The data received will vary by the type of event, but the following will always be included:
* **instanceId**: The App Instance ID. This is the unique identifier of the app within the website.
* **eventType**: A description of the event type, e.g., OrderEvent.
