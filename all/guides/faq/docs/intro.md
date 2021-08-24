SortOrder: 0
# About the FAQ API


With the FAQ app installed, site owners can create a "Frequently Asked Questions" section in their website for their members and visitors.

This FAQ API provides the ability to view and manage the questions and answers in the FAQ app.

It provides CRUD functionality for question entries and categories, as well as endpoints that allow you to change a question's order in a category, and its visibility status.

## Terminology
- **Categories** are themed groupings of FAQ entries that a site owner can create to organize their FAQ questions (e.g., Shipping, Returns, etc.).
- **Labels** are additional groupings of FAQ entries for organizing FAQ questions in specific contexts, other than the site, e.g. chat bots.
- **Question entries** are the FAQ questions with their respective answers. The question and answer texts are saved as draftjs rich text.

For more information about the draftjs rich text editor format, please see: https://draftjs.org/


## Limitations

It is not possible to look up questions by their text (i.e. free text search is not supported).

The API will return up to 100 questions or categories with default pagination.

## Understanding Labels, Categories and Sort Order

### Categories and Labels
Labels and categories are similar, but they have very different use cases.

**Categories** are user-visible in the FAQ section of the site. A site owner can create categories and assign questions to them. 

**Labels** support integration with other apps, and as such are invisible to site owners, and site owners cannot create labels.

Only questions can belong to labels. Labels, unlike categories, cannot exist without a question. No labels are added to a question by default.

A question can only belong to one category, and up to 100 labels.

### Sort Order

Questions, Categories and Labels have a property called `sortOrder`, which works differently in each context:
 - Category: order of categories in the FAQ section on the site.
 - Question: order of questions within a category.
 - Label: order of questions within a label.

## Examples

A user has two categories: `shipping` and `returns`. Those objects look like this:
````
{
  id: "shipping-category-id-uuid",
  title: "shipping",
  sortOrder: 10,
},
{
  id: "returns-category-id-uuid",
  title: "returns",
  sortOrder: 20,
}
````
When listing categories, `shipping` will always be above `returns`. Using increments of 10 allows you to move or add new categories.

Say `shipping` has two questions:
 - "How do you ship?"
 - "How much does shipping cost?"
 
Simplified, they could look like:
````
{
  id: "question-1-id-uuid",
  question: "how do you ship?",
  answer: "< draftjs rich text >",
  sortOrder: 10,
  categoryId: "shipping-category-id-uuid",
  labels: [
    {
      title: "email-question",
      sortOrder: 999
    }
  ]
}
````
The order of this question within the category `shipping` is 10, but in the context of the label `email-question` the order is 999.

In the FAQ section, site visitors will find this question under the category `shipping` and with a `sortOrder` of 10.

However, if a third-party app were to list all questions that have a label `email-question` (from all categories) this FAQ entry would have the order sequence of 999.

To update the `sortOrder` of categories use the Update Category endpoint.

For FAQ entries you can either:
 - Use Update Question if any text fields require updates as well, or
 - Use Update Questions Visibility in Category to move one or several FAQ entries between categories in the site.
 - To change `sortOrder` within labels, use Bulk Update Label Order.

## Integrations

The FAQ is integrated with [Wix Multilingual](https://support.wix.com/en/article/wix-multilingual-an-overview).

### Wix Multilingual
The FAQ comes with out-of-the-box integration with Wix Multilingual.

If the site that contains the FAQ section also contains the Multilingual app - on every create resource (category or question entry) request, resource texts will  be sent to Multilingual, and the site owner can translate FAQ content.

On List requests, FAQ automatically queries data from Multilingual and merges translated content into the requested objects. The language is resolved from Multilingual's language, locale, or the site's defaults (in that order).

If Multilingual is installed to a site later than the FAQ app, all existing FAQ content will be batch sent to Multilingual for localization.

For more information, see [this article on Wix Multilingual](https://support.wix.com/en/article/wix-multilingual-an-overview).
