SortOrder: 0
# About the Reviews API

With the Reviews API you can manage reviews for a site's services, content, or products. The review object holds the content of the review, a rating score, images or video media, and information about the author. Learn more about [Wix Reviews](https://support.wix.com/en/article/wix-stores-adding-and-setting-up-wix-reviews).

The Wix Reviews API allows your app to:

- Import reviews from other sites and export reviews to other sites.
- Retrieve and display positive review data. Use the [Media API](https://dev.wix.com/api/rest/media) to retrieve associated review media.
- Retrieve negative review data enabling site owners to respond effectively.

The Reviews API can be used in conjunction with the [Ratings API](https://dev.wix.com/api/rest/ratings) to provide broader rating functionality. For example, the Ratings API enables rating of multiple attributes of a product such as comfort and value for money.

## Moderation

If moderation is turned on, reviews are checked for content that requires moderation. If moderation is required, the review remains pending until the site owner rejects or approves it in the site's [Dashboard](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Freviews/pending). 
The site owner can configure moderation settings in the site's [Dashboard](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Freviews/settings/moderation).  Learn more about [managing reviews](https://support.wix.com/en/article/wix-stores-managing-wix-reviews).

## Before you begin
It’s important to note the following points before starting to code:

- Every review needs a contact. To check whether a contact exists, your app can call the [Contacts API](https://dev.wix.com/api/rest/contacts) with the author's email. If the author is already listed as a contact, use either [Create Review](https://dev.wix.com/api/rest/reviews/create-review) or [Create Review and Contact](https://dev.wix.com/api/rest/reviews/create-review-and-contact). If the author is not yet a site contact, use [Create Review and Contact](https://dev.wix.com/api/rest/reviews/create-review-and-contact).  
- A review author is limited to one review per entity. Duplicate reviews receive an error response.
- Replying to a review is available only in the site owner's [Dashboard](https://www.wix.com/my-account/site-selector/?buttonText=Select%20Site&title=Select%20a%20Site&autoSelectOnSingleSite=true&actionUrl=https:%2F%2Fwww.wix.com%2Fdashboard%2F%7B%7BmetaSiteId%7D%7D%2Freviews/pending).

## Use Cases
- [Real-time 2-way sync with an eCommerce solution](https://dev.wix.com/api/rest/reviews/sample-flows#reviews_sample-flows_real-time-2-way-sync-with-an-ecommerce-solution).
- [Display review media in a widget](https://dev.wix.com/api/rest/reviews/sample-flows#reviews_sample-flows_display-review-media-in-a-widget).
- [Get immediate updates of negative customer feedback](https://dev.wix.com/api/rest/reviews/sample-flows#reviews_sample-flows_get-immediate-updates-of-negative-customer-feedback).
- [Display the most helpful product reviews in a widget](https://dev.wix.com/api/rest/reviews/sample-flows#reviews_sample-flows_display-the-most-helpful-product-reviews-in-a-widget).

## Terminology

- **Entity**: The entity to review. For example, a Wix Stores product.  
- **Namespace**: The Wix module that the Reviews API is integrated with. Currently only Wix Stores.
- **Rating**: The rating score for the review item. An author can give a rating score between 1 and 5. The rating is displayed with the site review.  
- **Helpfulness**: Helpfulness is the overall helpfulness score calculated by subtracting Found Unhelpful from Found Helpful. Site visitors can indicate whether a review was helpful or not.  
- **Reply**: A direct reply to a review that was left on the site. The reply is displayed with the review.  