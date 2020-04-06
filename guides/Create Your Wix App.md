# Tutorial: Create Your First Wix App
In this tutorial we review how to create a Wix application that interacts with the Wix platform and you can submit to the Wix App Market, where Wix site owners can deploy it on their sites.   

## Step 1: Set Up Your App in a Wix Developers Account 
1. Log in (or sign up) to [Wix Developers](https://dev.wix.com/).
2. Click **Create New App**.
3. Go to **Workspace** > **OAuth** and copy your App ID and App Secret Key - you'll need them later.
![oaurg](../media/oauth-settings.png)

## Step 2: Set Up Your App to Receive Inbound HTTPS Connections
Since most developers machines are not open for inbound connection and don't have HTTPS certificates, we will describe the process using **ngrok**.  
(If you are hosting your application on a server without these restrictions, you can skip this step.)

1. Install and run [ngrok](https://dashboard.ngrok.com/get-started).
2. Start an HTTP tunnel on the port your app is listening on  (default is 3000).
  You should get something like this:  
![ngrok screen](../media/ngrok.png)
3. Make note of the forwarding URL - you'll need it later.

<blockquote class='important'>
<p>
  <strong>Important:</strong><br/>
Don't close the ngrok process - You will need it running for the entire process.
</p>
</blockquote>

## Step 3: Enter Your App URLs in the Wix Developers Center
1. Go to **Workspace** > **OAuth**:     
   a. In **Redirect URL** enter: `https://<NGROK_STRING>.ngrok.io/login`     
   b. In **App URL** enter: `https://<NGROK_STRING>.ngrok.io/signup`     
![update application urls](../media/urls.png)
<blockquote class='important'>
<p>
  <strong>Important:</strong><br/>
Remember to replace <NGROK_STRING> with the string from the forwarding URL in step 2 ('18ab6468' in the example above).  
</p>
</blockquote>

2. Click **Save**.


## Step 4: Register For a Webhook
1. Go to **Workspace** > **Webhooks** and click **+ Add Webhook**.
2. Select the **App Management** webhook category and the **APP INSTALLED** event.  
![New webhook](../media/add-webhook.png)

3. Set up the webhook callback URL to https://<12345678>.ngrok.io/webhook-callback.  
![webhook url](../media/webhook-callback.png)  

<blockquote class='important'>
<p>
  <strong>Important:</strong><br/>
Remember to replace '12345678' with your ngrok string from step 2.  
</p>
</blockquote>

4. Click **Save**.
  Now you should see your Public key on the bottom of the screen. 
5. Copy your Public key - you'll need it later.
![public key](../media/get-public-key.png)


## Step 5: Create and Run Your App

1. Download and install [npm](https://www.npmjs.com/get-npm).
2. Clone the [Wix Sample Application](https://github.com/shaykewix/sample-wix-rest-app) to your machine.
3. Go to **src** > **config.js**:  
  a. Find and replace the APP_ID with the value you copied from Wix Developers:  
![Change app id](../media/change-config.png)
  b. Find and replace the PUBLIC_KEY with the value you copied from Wix Developers:
![Change public key](../media/change-public-key.png)
  
4. Go to **src** > **credentials.js**:
  a. Find and replace the APP_SECRET  with the value you copied from Wix Developers:
![Change app secret](../media/change-credentials.png)

5. Run your app:  
  a. Browse to the cloned sample application.  
  b. Run `npm install`.  
  c. Run `npm build`.  
  d. Run `npm start`.  
  You should get something like this:  
![Listening](../media/listening.png)

Well done! Now it's time to make sure your app works as expected.

## Step 6: Test Your App

1. In the Wix Developers Center Workspace, click **Test Your App**.  
![test your app](../media/test-button.png)  

2. Select a site and click **Test Your App**.  
![site selector](../media/site-selector.png)

3. When prompted, click **Add To Site**.  
![site selector](../media/add-to-site.png)

4. Provide consent for the app to collect data by clicking **Allow and Install**.  
![site selector](../media/consent.png)

5. You should get a print into the browser with your application ID and your site instance ID.  
![site selector](../media/end.png)

## Congrats, you're done!
**Now you can add your app logic and other WIX APIs to your app.**
