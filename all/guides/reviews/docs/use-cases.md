SortOrder: 1
# Reviews: Sample Use Cases and Flows

This article shares some possible use cases your app can support. You are not limited to these use cases, but they can be a helpful jumping off point as you plan your app's implementation.

## Real-time 2-way sync with an eCommerce solution

Site owners can use your app to keep reviews from an eCommerce solution up to date with their reviews on Wix with a two-way sync. To synchronize Wix and the eCommerce solution, think about how your app will handle these flows:

- Initial setup
- Synchronize to the eCommerce solution
- Synchronize to Wix

### Initial setup

Create mappings for the following from the Wix site to the eCommerce solution using common fields so the reviews can be synced:
- Wix site entities to entities in the eCommerce solution.
- Wix site Contact IDs to author IDs in the eCommerce solution, for example using email addresses.  
- Wix review fields to the review fields in the eCommerce solution for example, title, body, author.  

Store the mappings on your app's server. Then follow these flows to create the two-way sync.

### Synchronize to the eCommerce solution

Listen for a change in Wix reviews with the following webhooks:

- [Review Created Webhook](https://dev.wix.com/api/rest/reviews/review-created-webhook).
- [Review Updated Webhook](https://dev.wix.com/api/rest/reviews/review-updated-webhook).
- [Review Deleted Webhook](https://dev.wix.com/api/rest/reviews/review-deleted-webhook).

When one of the webhooks is triggered,
you'll receive the review in the payload.
You can send those changes to the eCommerce solution with a flow like this one:

1. Get the `slug` (which tells you what the event was),
    `entityId` (ID of the review),
    and other relevant information from the payload data.

2. Use the mappings from the [initial setup](#initial-setup)
    to send the relevant information to the eCommerce solution.

3. Ignore the resulting event from the eCommerce solution
    so you don’t create an endless loop of updates.

### Synchronize to Wix

Listen for review events from the eCommerce solution.
When your app receives a change it needs to synchronize,
follow this basic flow:

1. Use the [Contacts API](https://dev.wix.com/api/rest/contacts) to check if the review author has a contact ID on the Wix site. 

2. The Reviews API allows only one review for each entity per contact. Use the mappings from the [initial setup](#initial-setup) to filter out imported reviews if there is already a Wix site review from the contact for the entity. 
    
3. Use the mappings from the [initial setup](#initial-setup) and call 
    [Create Review](https://dev.wix.com/api/rest/reviews/create-review) if the author is a contact. If the author is not a contact, call [Create Review And Contact](https://dev.wix.com/api/rest/reviews/create-review-and-contact).

4. Ignore the resulting event from Wix
   so you don’t create an endless loop of updates.

## Display review media in a widget 

> **Note:** This flow requires Wix Blocks which is currently in Beta. 

To enable a site owner to create a media gallery of photos from reviews, retrieve images from reviews and then display them in media layout.

1. Use [Query Reviews](https://dev.wix.com/api/rest/reviews/query-reviews) to retrieve reviews that have media.

2. Extract the `image.url` from the response and use the [Media API](https://dev.wix.com/docs/rest/api-reference/media/media-manager/files/import-file) to retrieve the media.

3. Display the retrieved media items in gallery layout in a widget using Wix Blocks. Learn more about [Wix Blocks apps](https://support.wix.com/en/article/wix-blocks-design-guidelines-for-applications).  

## Get immediate updates of negative customer feedback

To enable a site owner to receive timely customer feedback, gain insights into product satisfaction, and identify areas for improvement, follow this basic flow.

1. Listen for new reviews using the [Review Created Webhook](https://dev.wix.com/api/rest/reviews/review-created-webhook).

2. Get the `entityId` (ID of the review), `content`, and any other relevant information from the payload data.

3. Extract reviews from the payload that have `content.rating` less than 3. 

4. Provide the extracted review IDs to the site owner so they can reply in the Dashboard.

## Display the most helpful product reviews in a widget

> **Note:** This flow requires Wix Blocks which is currently in Beta. 

To enable a site owner to display the most helpful reviews in order to promote products, follow this basic flow.

1. Use [Query Reviews](https://dev.wix.com/api/rest/reviews/query-reviews) to get a list of the 10 most helpful reviews, sorted by most to least helpful.

2. Display the retrieved reviews in a widget using Wix Blocks. Learn more about [Wix Blocks apps](https://support.wix.com/en/article/wix-blocks-design-guidelines-for-applications). 

