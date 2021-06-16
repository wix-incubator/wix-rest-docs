SortOrder: 0
Wix Data indexing allows defining indexes on collections to accelerate 
filtering and sorting operations when querying data. In addition to accelerating
query, a unique index can be used to enforce unique values in a field across the
collection.

# Working with the API

Index creation and drop procedures are asynchronous. That is successful call does not guarantee that
an index is already usable. 

# How are queries accelerated?

## Filters

It's common to define indexes on queries that commonly occur when using the application. Indexes will
accelerate any equality predicates (*eq*, *hasSome*, *in*) and greater / lesser if 
modeled properly.

While it's common for databases to also accelerate startsWith in Wix Data this is not the case as *startsWith*
is case insensitive.

For an index composed of fields (a, b, c). Queries filtering on a, a & b and a & b & c will be fully
looked up by an index. Filtering on b will not use an index and will cause a full scan. Filtering
on a & c, will accelerate the query by looking up a in an index, but will continue with a partial scan 
for c.

For range filters (such as *gt*, *lt*, *gte* and *lte*) only the last attribute can be looked up
in an index. If there is an index on (a, b, c), then range can be used on a, or equality used on a 
and range on b, or eq used on a & b and range on c.

## Ordering

Sorting operation in a query will make use of an index if filters do not prevent its use and the order
of the fields matches or is exact opposite of how the field order is defined in an index.

If collection has an index (a: asc, b: desc, c: asc) applying no filters and sort in the same direction
will read order from an index. It will also read oder from an index if its in reverse order (sorting
on (a: desc, b: asc, c: desc) will also traverse the index (backwards)).

Ordering and filtering can be combined. In the above case, filtering by a and ordering by b anc c in 
appropriate order will also lookup and traverse by the index.

## Examples

### Example: Paintings

Lets take a painting collection as an example (title: text, author: text, date: datetime). Typical
use case in our example site is to show all paintings, show paintings for an author and allow user
to order paintings by the date (with our without filtering by the author).

What index or indexes should we define?

Since we need to filter by author and sort by date, we can start by defining (author: asc, date: asc). 
This will 
* accelerate filtering just by the author
* filtering by author and ordering by date (in both directions as once we have author index for date can be traversed in both directions)

We can't order just by date as in the index paintings are first ordered by author and then by date. Thus,
we need a second index on just the date.

Having these indexes also allow us to add date range filters and run queries "give me paintings by Rembrant
painted between 1657 and 1963 ordered by date".

# Limitations

A single collection can have up to 

Regular indexes
* 3 indexes per collection
* 3 fields per index

Unique indexes
* 1 index per collection
* 1 field per index

Note that failed indexes take up an index slot and need to be removed to free it.

Indexes value can not be larger than "982 - length of collection name" bytes. For example, in a collection
named "Items" maximum length of indexes values is 977 bytes.

Case insensitive filters, like *startsWith* can not be accelerated by an index.

