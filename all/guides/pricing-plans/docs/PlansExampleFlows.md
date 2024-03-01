SortOrder: 7
# Plans: Sample Use Case & Flow

This article shares a possible use case your app could support, as well as
a sample flow that could support the use case. This can be a helpful jumping
off point as you plan your app's implementation.

## Sync available pricing plans to an external system

Site owners can use your app to keep their external platform up to date with the pricing plans they offer. For example, 
when a site owner adds a new pricing plan to their Wix site, the external platform will have the new plan available for purchase. 

Use this flow to implement a sync from a Wix site to an external system:
1. Create a mapping from Wix pricing plans to the plans stored on an external app using a common field, like name. Store this mapping on your app's server.
1. Listen for any changes to which pricing plans are available with the [Plan Created Webhook](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/plans/plan-created-webhook) and the [Plan Archived Webhook](https://dev.wix.com/api/rest/wix-pricing-plans/pricing-plans/plans/plan-archived-webhook).
1. When one of the webhooks is triggered you receive the details of the pricing plan, in `createdEvent.entity` if a plan was created, or `actionEvent.body.plan` if a plan was archived.
1. Use these pricing plan details to add the new plan to, or remove the archived plan from, your external app.
