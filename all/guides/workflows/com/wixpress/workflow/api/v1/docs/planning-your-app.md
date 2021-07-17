SortOrder: 1
# Planning Your App

When working with the Workflows API,
your app could encounter some limits placed on Wix sites,
such as the maximum number of workflows per site,
cards or phases per workflow,
or the 1:1 relationship between contacts and cards.

This article covers the limits you should keep in mind as you plan your app.

## Active vs. Inactive Cards

**Active cards:** Cards that are in progress in a workflow are considered active,
and they count toward the workflow's [active card limits][active-cards-limit].
In the [workflow object][workflow-obj],
active cards are contained in any phase in the `phaseList.phases` array.

**Inactive cards:** Conversely, cards that are no longer in progress are considered inactive,
and they don't count toward the workflow's active card limits.
Cards are inactive when they are completed (i.e., moved to the win phase)
or archived.

## Limits

The following table describes the limits placed on Wix sites
that your app might need to handle:

| Limit                               | Maximum | HTTP Response if Exceeded |
| ----------------------------------- | ------- | ------------------------- |
| Number of active cards per contact  | 1       | `409 CONFLICT`            |
| Number of active cards per workflow | 5,000   | `403 FORBIDDEN`           |
| Number of phases per workflow       | 60      | `403 FORBIDDEN`           |
| Number of workflows per site        | 30      | `403 FORBIDDEN`           |

[workflow-obj]: https://dev.wix.com/api/rest/drafts/workflows/workflows/workflow-object
[active-cards-limit]: #5000-active-cards-per-workflow-max