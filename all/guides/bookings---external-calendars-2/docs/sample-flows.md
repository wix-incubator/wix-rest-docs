SortOrder: 1
# Sample Flows

This article shares a possible use case your implementation could support, as well as a sample flow. You're not limited to this use case, but it can be a helpful jumping off point for your planing.

## Check which connection method to use for a provider

External calendar providers use different methods for authenticating a connection. Some use an OAuth flow, while others require a user’s credentials (email address and password). To check the appropriate connection method for a provider:

1. Call the [List Providers](#list-providers) endpoint to retrieve details about all supported external calendar providers.
2. The response contains an array with details about each external calendar provider. Find the provider you want to connect with.
3. Save the `id` for the provider you want to connect with.
4. Check the `features.connectMethods` array for the chosen provider. If the array contains `OAUTH`, you can [connect by OAuth](#connect-an-external-calendar-by-oauth). If the array contains `CREDENTIALS`, you can [connect by credentials](/docs/connect-an-external-calendar-by-credentials).

## Connect an external calendar by credentials

Before you can sync events with a Wix site user’s external calendar, you need to establish a connection with the external calendar. If the external provider supports [connecting by credentials](#check-which-connection-method-to-use-for-a-provider), create the connection as follows:

1. Get the email address and password associated with the external calendar account from the user.
2. If you don’t already have the ID of the external calendar provider you want to connect to, use [List Providers](#list-providers) to get it.
3. Use [List Schedules](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/list-schedules) to get the ID for the schedule to connect the external calendar with.
4. Call the [Connect By Credentials](#connect-by-credentials) endpoint with the details and credentials you’ve collected. 
5. The response includes a `connection` object with details of the new external calendar connection. If the connection was established successfully, the connection’s `status` is `CONNECTED`.
6. Use [Update Sync Config](/docs/update-sync-config) to configure the connection and enable importing and/or exporting events.

## Connect an external calendar by OAuth

Before you can sync events with a Wix site user’s external calendar, you need to establish a connection with the external calendar. If the external provider supports [connecting by OAuth](#check-which-connection-method-to-use-for-a-provider), create the connection as follows:

1. If you don’t already have the ID of the external calendar provider you want to connect to, use [List Providers](#list-providers) to get it.
2. Use [List Schedules](https://dev.wix.com/api/rest/wix-bookings/schedules-and-sessions/schedule/list-schedules) to get the ID for the schedule to connect the external calendar with.
3. Call the [Connect By OAuth](#connect-by-o-auth) endpoint using the details you’ve collected. The `redirectUrl` parameter should include the URL the user is redirected to after authorizing access to their external calendar.
4. The response includes a URL for the external calendar authorization page. Redirect the user to this page.
5. The user authorizes access to their external calendar. 
6. The connection is now established. The user is redirected to the URL provided in `redirectUrl`, with the connection ID as a query parameter.
7. Retrieve details about the newly established external calendar connection, including its ID, using the [Get Connection](#get-connection) endpoint.
8. Use [Update Sync Config](/docs/update-sync-config) to configure the connection and enable importing and/or exporting events.

## Retrieve a list of events in connected external calendars

To retrieve an aggregated list of events in connected external calendars during a particular time range:

1. [Create a connection](#check-which-connection-method-to-use-for-a-provider) with each of the user’s external calendars, following the steps above.
2. Use the [List Events](#list-events) endpoint with the relevant start and end times to retrieve an aggregated list of events in all the user’s connected external calendars.
