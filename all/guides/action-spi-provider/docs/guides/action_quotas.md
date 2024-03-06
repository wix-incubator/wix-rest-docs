SortOrder: 3
# Displaying Action Quotas

As an action provider, you can enforce limits on the number of times a site owner uses an action. For example, an action provider can limit the number of messages a user can send per billing cycle. You can enforce different quotas on specific features of the app, depending on the user. For example, your app might have a basic plan that allows the user to send 500 emails a month, and a premium plan that lets the user send unlimited emails.

## Terminology

+ **quota**: A limit on the number of times a site owner can perform an action. For example, you can set a quota of 500 reminder emails that the user may send.

+ **plan**: Allows you to set different quotas for different users.

## Creating and enforcing quotas

You are responsible for enforcing quotas for features used by their actions. If the features provided by your service have quotas you can implement the [Get Action Quota Info](https://dev.wix.com/docs/rest/api-reference/wix-automations/action-provider-v1/get-quota-info) endpoint so that Wix can display your quotas in the user's site dashboard. Wix displays the quotas in the **Manage your automations quotas** modal. This modal opens when site contributors click the **Manage Your Quotas** button on the Automations page in the dashboard.

![Find the Manage your quotas modal](https://s3.amazonaws.com/wixplorer-readme-images/action-spi-provider%2Fmanage-quotas0.png)

The modal lists the quotas for all the features used by the site's automations. The list is organized by the apps providing the features.

<div style="text-align:center">

<img src="images/manage-quotas-modal0.png">

</div>

You can define the different elements of each quota display in the responses from your Get Action Quota Info endpoint. In general, each quota display includes a plan, and the plan features associated with it. The current usage and limit for each feature is displayed.

<div style="text-align:center">

<img src="images/plan-example0.png">

</div>

### One plan with one feature

To display one plan with a single feature quota, include the plan and quota data in the same `quotaInfo` object in your endpoint’s response.

Sample response body:

```json
{
  "enforced": true,
  "quotaInfo":[
    {
      "plans": [
        {
          "id": "fdc7fe4b-523f-4d8c-b6e1-5faf3850d01e",
          "name": "Reminder emails"
        }
      ],
      "quotas":
      [
        {
          "featureName": "Reminders sent",
          "currentUsage": "10",
          "limit": "40"
        },
        {
          "featureName": "Tasks created",
          "renewalDate": "2022-01-12T01:20:00.000Z",
          "currentUsage": "346",
          "limit": "500"
        }
      ],
      "upgradeCta": {
        "url": "https://www.example.com/upgrade",
        "label": "Upgrade For More"
      }
    }
  ]
}
```

The resulting quota display looks like this:

<div style="text-align:center">

<img src="images/quota-display0.png">

</div>

### One plan with two features

To display one plan with a single feature quota, include the plan and quota data in the same `quotaInfo` object in your endpoint’s response.

Sample response body:

```json
{
 "enforced": true,
 "quotaInfo":[
  {
   "plans": [
    {
     "id": "f32c650f-ecc4-4818-a81c-8fa681e325a6",
     "name": "Email Marketing"
    }
   ],
   "quotas":[
    {
     "featureName":"Emails sent",
     "currentUsage":"346",
     "limit":"500",
     "renewalDate":"2023-01-12T01:20:00.000Z"
    }
   ],
   "upgradeCta": {
          "url": "https://www.example.com/upgrade",
    "label": "Upgrade Email Plan"
   }
  }
 ]
}
```

The resulting quota display should look something like this:

<div style="text-align:center">

<img src="images/quota-display-2-features0.png">

</div>

### Two plans with different features

To display two different plans with different features that are both being used by your action service, include two `quotaInfo` objects in your response body.

Sample response body:

```json
{
  "enforced": true,
  "quotaInfo": [
    {
      "plans": [
        {
          "id": "94e55e1f-b845-47a5-afad-4b8fc977d545",
          "name": "Forms on your site"
        }
      ],
      "quotas": [
        {
            "featureName": "Forms on your site",
            "currentUsage": "6",
            "limit": "40"
        }
      ],
      "upgradeCta": {
          "url": "https://www.example.com/upgrade",
          "label": "Upgrade For More",
          "planId": "fd9830b5-ce89-495f-87e8-30893168afd9"
      }
    },
    {
      "plans": [
        {
          "id": "c7f255a5-0aa2-47ad-9607-8f87ea56df5b",
          "name": "Code Forms on your site"
        }
      ],
      "quotas": [
        {
          "featureName": "Code Forms on your site",
          "currentUsage": "1",
          "limit": "20"
        }
      ],
      "upgradeCta": {
          "url": "https://www.example.com/upgrade",
          "label": "Upgrade For More",
          "planId": "b19345c1-380c-4fc6-8e45-9f7f72b3de5f"
      }
    }
  ]
}
```

The resulting quota display looks like this:

<div style="text-align:center">

<img src="images/quota-display-2-plans-2-features0.png">

</div>

### Unlimited plans

If your service supports a plan where features are unlimited, you can still display the site contributor’s current usage. To do this, provide a `quotaInfo` object with the relevant plan details. Include the feature’s name and current usage, but not a usage limit.

Sample response body:

```json
{
 "enforced": true,
 "quotaInfo": [
    {
      "plans": [
        {
          "id": "1ccaa3a5-4994-4e17-b1d4-2fa3f76418e7",
          "name": "Marketing Emails"
        }
      ],
      "quotas": [
        {
          "featureName": "Emails",
          "currentUsage": "150"
        }
      ]
    }
  ]
}
```

The resulting quota display should look like this:

![Unlimited quota UI](https://s3.amazonaws.com/wixplorer-readme-images/action-spi-provider%2Fquota-display-unlimited0.png)

### User hasn't purchased a plan

If your service enforces a quota on a feature that a site contributor hasn’t paid for, you can display this in the dashboard. This lets the site contributor know that your action isn’t running when their automation is triggered. To display this, set both the current usage and limit for the feature to `0` in the relevant `quotaInfo` object in your response body.

Sample response body:

```json
{
  "enforced": true,
  "quotaInfo": [
    {
    "plans": [
        {
          "id": "d0a9fa93-f2a7-426a-89d6-a15d2e7c0d78",
          "name": "Marketing Emails"
        }
      ],
    "quotas":[
        {
          "featureName": "Monthly Emails",
          "renewalDate": "",
          "currentUsage": "0",
          "limit": "0"
        }
      ],
      "upgradeCta": {
          "url": "https://www.example.com/upgrade",
          "label": "Upgrade",
          "planId": "28d52c9c-7c59-4a14-bbc1-a7d9103e1038"
      }
    }
  ]
}
```

## Quota descriptions

You can define a tooltip that provides more details about a feature quota. To display the tooltip, add an `additionalInfo` object together with the feature details.

Sample response body:

```json
{
  "enforced": true,
  "quotaInfo": [
    {
      "plans": [
        {
          "id": "fa9bbb78-286f-46b4-83fe-4aa81d94c715",
          "name": "Marketing Messages"
        }
      ],
      "quotas": [
        {
          "featureName": "SMS sent",
          "renewalDate": "",
          "currentUsage": "400",
          "limit": "1200",
          "additionalInfo": {
            "description": "Your SMS quota will renew each month. Any remaining messages won't roll over to the next month.",
            "cta": {
                "url": "/home",
                "label": "Go to SMS Settings"
            }
          }
        }
      ],
      "upgradeCta": {
          "planId": "e15d2206-4226-4815-8684-41b101c7dcad",
          "url": "https://www.example.com/upgrade",
          "label": "Upgrade"
      }
    }
  ]
}
```

You should now see a message when you hover over the tooltip icon:

<div style="text-align:center">

<img src="images/quota-info0.png">

</div>




