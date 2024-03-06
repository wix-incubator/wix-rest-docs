SortOrder: 1
# About the Wix Automations Action SPI

The Action Provider SPI allows you to implement an action that site contributors can add to automations on their sites. This means you can take actions in your service in response to events that happen on Wix sites or in the business manager. For example, in response to a trigger, your service can send an email, generate an invoice, or update another Wix service using its APIs.

The Action SPI lets you do the following:

+ [Validate](https://dev.wix.com/docs/rest/api-reference/wix-automations/action-provider-v1/validate-configuration) the input values to the action and return an error to the user if they are invalid.
+ [Display the limits](https://dev.wix.com/docs/rest/api-reference/wix-automations/action-provider-v1/get-quota-info) you enforce on the number of actions a user can perform.

## Before you begin

+ Keep in mind that once you publish an app with a custom action, there are limitations to the changes you can make to the input schema you define when configuring your action. Learn more about [editing a published input schema](https://dev.wix.com/docs/rest/api-reference/wix-automations/action-spi/about-the-action-spi-input-schema#editing-a-saved-input-schema).
+ Wix does not validate breaking changes to an input schema that uses composition. To ensure the user does not make errors when configuring an action that uses composition in its schema, we recommend performing the validation on your end.

## Terminology

+ **Input schema**: A [JSON Schema](https://json-schema.org/) object that defines the fields that Wix needs to pass to your Action SPI endpoints. Learn more about the input schema [here](https://dev.wix.com/docs/rest/api-reference/wix-automations/action-spi/about-the-action-spi-input-schema).
+ **UI schema**: The JSON schema that defines the UI for your action configuration in the user's site dashboard.

## How to set up an action

To configure your action in the Wix Developers Center:

1. Select **Automations** from the left menu, then select **Create New** > **Action**.
  ![Create a new action](https://s3.amazonaws.com/wixplorer-readme-images/action-spi-provider%2Fcreate-new-action0.png)
2. Give your action a name. This is displayed to users when they add the action in the Automations UI.

    > **Notes:**
    > + Your action key is generated automatically from the action name. Once you save your action you cannot change the action key.
    > + The action key is not displayed to users.

3. Add a short description explaining what your action does. The description is displayed to users when they select your action. This is an optional field.
4. Choose whether to hide the action, so it doesn't appear as an individual action on a user site. You should do this if the action is part of a pre-installed automation.
5. Under **Action's SPI endpoints**, enter your base provider URI and select the SPI endpoints you intend to implement.
6. Configure your [input schema](https://dev.wix.com/docs/rest/api-reference/wix-automations/action-spi/about-the-action-spi-input-schema).
7. Optionally, configure your action's [UI](https://www.wix-pages.com/automations-ui-lib/?path=/story/getting-started--about).
8. Click **Save** at the top of the page in order to save your action.
9. Next, you need to test your action to make sure everything's working. You can install your app on a [free Premium development site](https://dev.wix.com/docs/build-apps/build-your-app/testing/how-to-test-your-app-on-a-free-premium-development-site) to test it.

    Once you create the test site, return to your app in the Wix Developers Center and click **Test Your App** > **Dashboard**. Select the test site you installed your app on earlier. Use this site to make sure your action is working.
10. When you have tested your app and are ready to publish your new action, [submit your app for review](https://devforum.wix.com/kb/en/article/submit-your-app-for-review). A member of our team will check the changes and approve the latest version.

Once our team has approved your app, it will be published and available for users to install on their sites. When a user installs your app, your actions become available for their automations, as shown here:

![Choose an action](https://s3.amazonaws.com/wixplorer-readme-images/action-spi-provider%2Fchoose-action0.png)
