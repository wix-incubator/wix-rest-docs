SortOrder: 0
# Notes

Notes product is part of the Ascend project. This service exposes CRUD API for Notes. Each Note is related to a specific ContactId and is editable by each site contributor.

## Why are we doing this?
Our users are "one-man shows" that talk with many different customers on a daily basis. As an 'All in one' solution, we want to provide them an easy solution to document each interaction they had with each contact.


By giving users a tool to keep track of the interaction with their customers, we help them to become more organized and give their future conversions more relevant context. This should make our users better at what they do and improve their business.

Having an API for it enables our advanced users to have an efficient 'All in one' solution and enjoy the power of a holistic CRM software

## What do we have?
The Note entity lives inside the Contact Panel and is always assigned on a specific contact. Users can create multiple notes on a specific contact, set their type (General / Call Summary / Meeting Summary) and edit them.

### Examples

* Posting meetings and class summaries, like 'Dan had a good yoga practice today! he becomes more flexible and stable'
* Posting failed calls attempts, like '09/09/19: Tried to call but there was no answer' 