SortOrder: 0
# Introduction

Rating definitions allow you to configure ratings: the entity that users rateß, the attributes of the rated entity, and
the range of rating values allowed.

## Terminology

* **Rating** A set of user-provided values and rated attributes for a single rated entity.
* **Attribute** An aspect of the rated entity that users can evaluate, defined by the site owner or 3rd-party developer.
* **Definition** A configuration describing how user can apply the rating.
* **Namespace** The type of entities that can users can rate with this definition. For example: store (products), blog (
  posts), media gallery (images, videos, etc.)
* **Entity** The entity users can rate, e.g. a product for sale, a user-contributed image, a blog post, etc.

## Use cases

This article shares some possible use cases your app can support. You are not limited to these use cases, but they can
be a helpful jumping off point as you plan your integration.

### Allow users to define their own rating attributes

1. Create user input for a new rating, providing at least one attribute's ID (name).
2. Pass user input to the [Create Definition](https://dev.wix.com/api/rest/drafts/rating-definitions/create-definition)
   endpoint to set up the new type of rating.
3. Update user interface with the new rating type automatically by subscribing to
   the [Definition Created Webhook](https://dev.wix.com/api/rest/drafts/rating-definitions/definition-created-webhook).
