SortOrder: 0
# About the Ratings API

With the Ratings API you can manage ratings as part of a site's reviews or a site's comments. The rating object holds the rating score of an entity or an entity's attributes, the ID of the entity being rated, and information about the rating owner.  

The Wix Ratings API allows your app to:

- Import ratings from external systems and export ratings to external systems.
- Summarize attribute ratings by entity or group.
- Provide information about average rating scores.

## Comparison to Reviews API ratings
- The Ratings API enables multiple aspects of an entity to be rated, for example, value for money and quality. The [Reviews API](https://dev.wix.com/docs/rest/communication/community/reviews/reviews/introduction) provides only an overall rating score. 
- The Ratings API provides a rating range between 0 and 100. The Reviews API rating range is 1 to 5. 

## Use Cases
- [Real-time 2-way sync with an external system](https://dev.wix.com/api/rest/ratings/sample-flows#ratings_sample-flows_real-time-2-way-sync-with-an-external-system).

## Before you begin

- A rating owner is limited to one rating per attribute. Duplicate ratings receive an error response.
- It is possible to categorize attributes only by `entityId` or `group`.

## Terminology

| Term | Definition |
|---------------|-------------------------|
| Entity | The entity to rate. For example, a Wix Stores product. |
| Namespace | The Wix module or app that the Ratings API is integrated with. Currently only Wix Reviews as `reviews` and Wix Comments as `comments`. |
| Group | A category that includes one or more entities. For example, for the `reviews` namespace, `stores` and `bookings` groups. |
| Attribute | Characteristic of an entity that can be rated individually. For example, `quality`, `usability`, `value`. |
| Attribute Summary | Rating summary of the attributes in a group or entity. The summary includes the average rating value for each attribute and the number of ratings with each value. |
| Value | Rating score from 0 to 100. |