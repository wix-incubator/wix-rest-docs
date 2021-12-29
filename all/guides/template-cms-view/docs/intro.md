SortOrder: 0
# Template CMS View API

## About this API
This API is used together with the CMS [Backoffice API](https://bo.wix.com/wix-docs/rest/core-apis#template-cms-backoffice). 
The Backoffice API manages the templates. The View API serves them to users.

## Terminology & concepts
There are 3 hierarchical entities to know: Template, Category & Book.

#### Template
Templates are the leaves of the hierarchy, they contain the actual template data. 
Template data is the template's display text, assets (images, videos), metaSiteId etc.

Templates also have a field called the `slug`, which is a unique url-safe identifier
that can be used to identify the template in an http endpoint.

#### Category
A category is a collection of templates that has a name. 
Categories specify which templates they contain and in which order they should be displayed,
as well as the category display text.

Categories also have a field called the `slug`, which is a unique url-safe identifier
that can be used to identify the category in an http endpoint. 

_Note_ - categories do not specify who their sub-categories are, that is the responsibility of the book.

#### Book
A book is a collection of categories.
Books specify which categories they contain and in which order they should be displayed,
which categories are sub-categories as well as the category label.
The category label is a logical grouping of categories by their function. 
Some labels may mean that the category should not be displayed as is, but rather that 
it carries some metaData.

## API Flow
In order to view the templates, the client must first fetch the currently live book.
This will allow the client to see the category names and structure (their order & sub-categories).
If the client wishes to view the templates inside a category, further API calls
must be performed in order to fetch the category. Categories & templates may
be fetched either by their id or by their [slug](/docs/Slugs)

## API Behavior
When querying the API, a few things happen behind the scenes - 
A/B tests are conducted to determine which books, categories & templates to display and 
display data for the specific language is compiled (all languages inherit their base data 
from English and may override it if they want, this is handled by the Backoffice API).
All of this is hidden behind the API, the API returns data that is ready to be shown to users.

## Slugs
Categories & templates have a field called a `slug`, which is a unique, url-safe identifier
of the entity that can be used to identify the entity from a rest endpoint.
The API exposes a get-by-slug accessor to allow retrieving entities by their slugs.
When participating in A/B tests, the entities under A/B test assume the slug of the `A` variant.
Meaning that when fetching an entity by slug, the result will either be the `A` or the `B` variant
of the A/B test, depending on the result of the experiment draw. 
