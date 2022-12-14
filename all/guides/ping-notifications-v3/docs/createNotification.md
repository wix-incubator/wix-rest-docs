SortOrder: 2
# Create a Notification via Dev Center


## How to create a notification?
In dev center, choose your app. In the left side bar go to "Notifications" tab.
Press "Create notification" to create a new notification.
In the "create notification page" there are some sections:
1. Basic info - here you set the name & description, which are visible only to you and to users/uou. <br />
   You also should set the settings group of the notification. You can read more about settings group here.
   Here you can see the "Notification template ID" that will be used later on by the API who send the notification.
   <br/><br/>
2. Recipients - here you set what recipient type will receive the notification: All site contributors or Site owner only (and co-owner as well). <br />
   As well in this section you can set what are the channels where the recipients will see the notification. <br />
   Dashboard = BizMgr feed. <br />
   Mobile app = Mobile app feed + Mobile push.
   <br/><br/>   
3. Message - here you set the content of the notification. For Mobile app channel you can set also the title.
In order to define dynamic value that will be sent with the API, you can use its name under curley brackets.<br/>
<br/>
   Here is an example:<br/>
   Title: New {{roomType}} reservation <br />
   Message: {{customerName}} just made a new reservation for {{dayOfWeek}}
   <br/><br/>
4. API Consumption - here you can see an example how to use the API. <br/>
   Here is an example for payload
   ```js
   {
     notificationTemplateId: '04708bb4-b296-46e4-b836-d0fcb1e366c0',
     dynamicValues: {
       roomType: {
         text: 'Studio'
       },
       customerName: {
         text: 'Allen Watts'
       },
       dayOfWeek: {
         text: 'Friday'
       },
     }
   }
   ```
After setting the details of the notification you can press on "Save", the notification will be saved, a modal with
API usage example will open. From this moment you can send the notification.


